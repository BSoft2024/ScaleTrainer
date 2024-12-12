#ifndef MIDIHANDLER_H_INCLUDED
#define MIDIHANDLER_H_INCLUDED

#include <juce_audio_devices/juce_audio_devices.h>
#include <juce_audio_basics/juce_audio_basics.h>
#include <juce_audio_utils/juce_audio_utils.h>
#include <vector> // Include for storing scale notes

class MidiHandler : public juce::MidiInputCallback, public juce::AudioSource
{
public:
    MidiHandler();
    ~MidiHandler();

    void startListening();
    void handleIncomingMidiMessage(juce::MidiInput* source, const juce::MidiMessage& message) override;

    // Method to set the scale
    void setScale(const std::vector<int>& scaleNotes);

    // AudioSource required methods
    void prepareToPlay(int samplesPerBlockExpected, double sampleRate) override;
    void releaseResources() override;
    void getNextAudioBlock(const juce::AudioSourceChannelInfo& bufferToFill) override;

private:
    std::unique_ptr<juce::MidiInput> midiInput;
    juce::Synthesiser synth;

    juce::AudioDeviceManager audioDeviceManager;
    juce::AudioSourcePlayer audioSourcePlayer;

    double sampleRate = 44100.0; // Default sample rate
    int bufferSize = 512;        // Default buffer size

    std::vector<int> currentScale; // Holds the valid notes for the current scale

    void initializeSynth();
    void playWarningTone(); // Method to play an error tone for incorrect notes
};

#endif // MIDIHANDLER_H_INCLUDED
