#include "MidiHandler.h"
#include <iostream>
#include <cmath>
#include <algorithm> // Needed for std::find

// JUCE headers
#include <juce_audio_basics/juce_audio_basics.h>
#include <juce_audio_devices/juce_audio_devices.h>
#include <juce_audio_utils/juce_audio_utils.h>

// Define SimpleSynthSound and SimpleSynthVoice classes here
class SimpleSynthSound : public juce::SynthesiserSound
{
public:
    bool appliesToNote (int /*midiNoteNumber*/) override { return true; }
    bool appliesToChannel (int /*midiChannel*/) override { return true; }
};

class SimpleSynthVoice : public juce::SynthesiserVoice
{
public:
    bool canPlaySound(juce::SynthesiserSound* sound) override
    {
        return dynamic_cast<SimpleSynthSound*>(sound) != nullptr;
    }

    void startNote(int midiNoteNumber, float velocity, juce::SynthesiserSound*, int /*currentPitchWheelPosition*/) override
    {
        frequency = juce::MidiMessage::getMidiNoteInHertz(midiNoteNumber);
        level = velocity;
        currentAngle = 0.0;
        angleDelta = frequency * 2.0 * juce::MathConstants<double>::pi / getSampleRate();
    }

    void stopNote(float /*velocity*/, bool allowTailOff) override
    {
        if (allowTailOff)
        {
            // Tail-off logic could be added here
        }
        else
        {
            clearCurrentNote();
            angleDelta = 0.0;
        }
    }

    void pitchWheelMoved(int) override {}
    void controllerMoved(int, int) override {}

    void renderNextBlock(juce::AudioBuffer<float>& outputBuffer, int startSample, int numSamples) override
    {
        if (angleDelta > 0.0)
        {
            for (int sample = 0; sample < numSamples; ++sample)
            {
                float currentSample = static_cast<float>(std::sin(currentAngle) * level);
                for (int channel = 0; channel < outputBuffer.getNumChannels(); ++channel)
                {
                    outputBuffer.addSample(channel, startSample, currentSample);
                }
                currentAngle += angleDelta;
                ++startSample;
            }
        }
    }

private:
    double currentAngle = 0.0;
    double angleDelta = 0.0;
    double level = 0.0;
    double frequency = 0.0;
};

// Constructor for MidiHandler
MidiHandler::MidiHandler()
{
    // Initialize the synthesizer with custom voice and sound
    synth.clearVoices();
    synth.addVoice(new SimpleSynthVoice());  // Add voices as needed for polyphony
    synth.clearSounds();
    synth.addSound(new SimpleSynthSound());

    // Set up audio device manager and audio output
    audioDeviceManager.initialise(0, 2, nullptr, true);
    audioSourcePlayer.setSource(this); // Set MidiHandler as AudioSource
    audioDeviceManager.addAudioCallback(&audioSourcePlayer);
}

// Destructor for MidiHandler
MidiHandler::~MidiHandler()
{
    audioSourcePlayer.setSource(nullptr);  // Clean up
    audioDeviceManager.removeAudioCallback(&audioSourcePlayer);
}

// Set the current scale for reference
void MidiHandler::setScale(const std::vector<int>& scaleNotes)
{
    currentScale = scaleNotes;
}

// handleIncomingMidiMessage implementation with scale checking
void MidiHandler::handleIncomingMidiMessage(juce::MidiInput* source, const juce::MidiMessage& message)
{
    if (message.isNoteOn())
    {
        int note = message.getNoteNumber();
        float velocity = message.getVelocity();

        // Calculate the pitch class of the incoming note (note % 12)
        int pitchClass = note % 12;

// Debugging output to check the scale contents and played note
        //std::cout << "Played Note: " << note << " (Pitch Class: " << pitchClass << "), Scale: ";
        for (int n : currentScale);
        //std::cout << std::endl;

        // Check if the pitch class is part of the current scale
        if (std::find(currentScale.begin(), currentScale.end(), pitchClass) != currentScale.end())
        {
            // Correct note, play as usual
            synth.noteOn(1, note, velocity);
            //std::cout << "Note On: " << note << ", Velocity: " << velocity << std::endl;
        }
        else
        {
            // Incorrect note, play warning sound
            playWarningTone();
            //std::cout << "Incorrect Note: " << note << " (Warning Tone)" << std::endl;
        }
    }
    else if (message.isNoteOff())
    {
        // Manually stop each active voice without accessing protected members
        for (int i = 0; i < synth.getNumVoices(); ++i)
        {
            if (auto* voice = synth.getVoice(i))
            {
                if (voice->isVoiceActive())
                {
                    voice->stopNote(0.0f, false); // Immediately stop the note without tail-off
                }
            }
        }
        //std::cout << "All active notes stopped" << std::endl;
    }
}

// Play a warning tone if an incorrect note is played
void MidiHandler::playWarningTone()
{
    int highNote = 96; // Set an extremely high note (e.g., C7)
    int minorThirdBelow = highNote - 3; // Minor third below the high note (e.g., A#6)

    float warningVelocity = 0.5f; // Set volume for the warning tone

    // Trigger the high note
    synth.noteOn(1, highNote, warningVelocity);
    // Trigger the minor third below to create dissonance
    synth.noteOn(1, minorThirdBelow, warningVelocity);

    // Hold the tones for a brief duration (e.g., 300 ms)
    juce::Thread::sleep(300);

    // Manually stop both warning tones using stopNote on each active voice
    for (int i = 0; i < synth.getNumVoices(); ++i)
    {
        if (auto* voice = synth.getVoice(i))
        {
            if (voice->isVoiceActive())
            {
                voice->stopNote(0.0f, false); // Stop immediately without tail-off
            }
        }
    }
}


// startListening implementation
void MidiHandler::startListening()
{
    auto midiInputList = juce::MidiInput::getAvailableDevices();

    if (!midiInputList.isEmpty())
    {
        auto midiDevice = midiInputList[0];
        midiInput = juce::MidiInput::openDevice(midiDevice.identifier, this);

        if (midiInput != nullptr)
        {
            midiInput->start();
            std::cout << "MIDI input started. Press 'q' to quit practice mode.\n";

            char input;
            while (true)
            {
                std::cin >> input;
                if (input == 'q' || input == 'Q')
                {
                    std::cout << "Quitting MIDI practice mode...\n";
                    midiInput->stop();
                    break;
                }
            }
        }
        else
        {
            std::cout << "Failed to open MIDI device.\n";
        }
    }
    else
    {
        std::cout << "No MIDI input devices available.\n";
    }
}

// prepareToPlay implementation (from AudioSource)
void MidiHandler::prepareToPlay(int samplesPerBlockExpected, double newSampleRate)
{
    sampleRate = newSampleRate;
    bufferSize = samplesPerBlockExpected;
    synth.setCurrentPlaybackSampleRate(sampleRate);
}

// releaseResources implementation (from AudioSource)
void MidiHandler::releaseResources()
{
    // Any necessary cleanup can be performed here
}

// getNextAudioBlock implementation (from AudioSource)
void MidiHandler::getNextAudioBlock(const juce::AudioSourceChannelInfo& bufferToFill)
{
    // Clear the buffer to avoid noise
    bufferToFill.clearActiveBufferRegion();
    
    // Render the synthesizer’s audio output into the buffer
    juce::MidiBuffer emptyMidiBuffer;
    synth.renderNextBlock(*bufferToFill.buffer, emptyMidiBuffer, 0, bufferToFill.numSamples);
}
