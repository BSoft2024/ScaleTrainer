#include <cstdlib>
#include <string>
#include <iostream>
#include <vector>  // Include for vector
#include "MidiHandler.h"
#include "MainMenu.h"
#include <conio.h> // For _kbhit() on Windows

#ifdef _WIN32
    const std::string pythonPath = "myenv\\Scripts\\python.exe";  // For Windows
#else
    const std::string pythonPath = "./myenv/bin/python";  // For macOS/Linux
#endif

// Function to execute Python script
void executePythonScript(const std::string& scriptName, const std::string& argument = "")
{
    std::string command = pythonPath + " " + scriptName;

    if (!argument.empty())
    {
        command += " " + argument;
    }
    int result = system(command.c_str());

    if (result != 0)
    {
        std::cout << "Failed to execute Python script. Please ensure that Python is installed and accessible.\n";
    }
}

// Function to execute Python script to read scales
void executePythonScriptReadScales()
{
    std::string command = pythonPath + " read_scales.py";  // Use the Python executable from the virtual environment
    int result = system(command.c_str());

    if (result != 0)
    {
        std::cout << "Failed to execute Python script 'read_scales.py'. Please ensure that Python is installed and accessible.\n";
    }
}
// Function to get the MIDI notes for a selected scale
std::vector<int> getMidiNotesForScale(const std::string& scaleName)
{
    std::vector<int> scalePattern;

    // Major scales
    if (scaleName == "c_major")
    {
        scalePattern = {0, 2, 4, 5, 7, 9, 11}; // C, D, E, F, G, A, B
    }
    else if (scaleName == "g_major")
    {
        scalePattern = {2, 4, 6, 7, 9, 11, 0}; // G, A, B, C, D, E, F# //Edited
    }
    else if (scaleName == "d_major")
    {
        scalePattern = {2, 4, 6, 7, 9, 11, 1}; // D, E, F#, G, A, B, C#
    }
    else if (scaleName == "a_major")
    {
        scalePattern = {9, 11, 1, 2, 4, 6, 8}; // A, B, C#, D, E, F#, G#
    }
    else if (scaleName == "e_major")
    {
        scalePattern = {4, 6, 8, 9, 11, 1, 3}; // E, F#, G#, A, B, C#, D#
    }
    else if (scaleName == "b_major")
    {
        scalePattern = {11, 1, 3, 4, 6, 8, 10}; // B, C#, D#, E, F#, G#, A#
    }
    else if (scaleName == "f_sharp_major")
    {
        scalePattern = {6, 8, 10, 11, 1, 3, 5}; // F#, G#, A#, B, C#, D#, E#
    }
    else if (scaleName == "c_sharp_major")
    {
        scalePattern = {1, 3, 5, 6, 8, 10, 0}; // C#, D#, E#, F#, G#, A#, B#
    }
    else if (scaleName == "f_major")
    {
        scalePattern = {5, 7, 9, 10, 0, 2, 4}; // F, G, A, Bb, C, D, E
    }
    else if (scaleName == "bb_major")
    {
        scalePattern = {10, 0, 2, 3, 5, 7, 9}; // Bb, C, D, Eb, F, G, A
    }
    else if (scaleName == "eb_major")
    {
        scalePattern = {3, 5, 7, 8, 10, 0, 2}; // Eb, F, G, Ab, Bb, C, D
    }
    else if (scaleName == "ab_major")
    {
        scalePattern = {8, 10, 0, 1, 3, 5, 7}; // Ab, Bb, C, Db, Eb, F, G
    }
    else if (scaleName == "db_major")
    {
        scalePattern = {1, 3, 5, 6, 8, 10, 0}; // Db, Eb, F, Gb, Ab, Bb, C
    }
    else if (scaleName == "gb_major")
    {
        scalePattern = {6, 8, 10, 11, 1, 3, 5}; // Gb, Ab, Bb, Cb, Db, Eb, F
    }
    // Minor scales
    else if (scaleName == "a_minor")
    {
        scalePattern = {9, 11, 0, 2, 4, 5, 7}; // A, B, C, D, E, F, G
    }
    else if (scaleName == "e_minor")
    {
        scalePattern = {4, 6, 7, 9, 11, 0, 2}; // E, F#, G, A, B, C, D
    }
    else if (scaleName == "b_minor")
    {
        scalePattern = {11, 1, 2, 4, 6, 7, 9}; // B, C#, D, E, F#, G, A
    }
    else if (scaleName == "f_sharp_minor")
    {
        scalePattern = {6, 8, 9, 11, 1, 2, 4}; // F#, G#, A, B, C#, D, E
    }
    else if (scaleName == "c_sharp_minor")
    {
        scalePattern = {1, 3, 4, 6, 8, 9, 11}; // C#, D#, E, F#, G#, A, B
    }
    else if (scaleName == "g_sharp_minor")
    {
        scalePattern = {8, 10, 11, 1, 3, 4, 6}; // G#, A#, B, C#, D#, E, F#
    }
    else if (scaleName == "d_sharp_minor")
    {
        scalePattern = {3, 5, 6, 8, 10, 11, 1}; // D#, E#, F#, G#, A#, B, C#
    }
    else if (scaleName == "a_sharp_minor")
    {
        scalePattern = {10, 0, 1, 3, 5, 6, 8}; // A#, B#, C#, D#, E#, F#, G#
    }
    else if (scaleName == "d_minor")
    {
        scalePattern = {2, 4, 5, 7, 9, 10, 0}; // D, E, F, G, A, Bb, C
    }
    else if (scaleName == "g_minor")
    {
        scalePattern = {7, 9, 10, 0, 2, 3, 5}; // G, A, Bb, C, D, Eb, F
    }
    else if (scaleName == "c_minor")
    {
        scalePattern = {0, 2, 3, 5, 7, 8, 10}; // C, D, Eb, F, G, Ab, Bb
    }
    else if (scaleName == "f_minor")
    {
        scalePattern = {5, 7, 8, 10, 0, 1, 3}; // F, G, Ab, Bb, C, Db, Eb
    }
    else if (scaleName == "bb_minor")
    {
        scalePattern = {10, 0, 1, 3, 5, 6, 8}; // Bb, C, Db, Eb, F, Gb, Ab
    }
    else if (scaleName == "eb_minor")
    {
        scalePattern = {3, 5, 6, 8, 10, 11, 1}; // Eb, F, Gb, Ab, Bb, Cb, Db
    }
    else if (scaleName == "ab_minor")
    {
        scalePattern = {8, 10, 11, 1, 3, 4, 6}; // Ab, Bb, Cb, Db, Eb, Fb, Gb
    }

    // Generate MIDI note numbers for all octaves (from MIDI note 0 to 127)
    std::vector<int> scaleNotes;
    for (int octave = 0; octave < 11; ++octave) // MIDI has 11 octaves
    {
        int baseNote = octave * 12; // Each octave starts at a multiple of 12
        for (int note : scalePattern)
        {
            int midiNote = baseNote + note;
            // Ensure the MIDI note is within the valid range (0-127)
            if (midiNote >= 0 && midiNote <= 127)
            {
                scaleNotes.push_back(midiNote);
            }
        }
    }

    return scaleNotes; // Return the MIDI note numbers for the specified scale
}

int main()
{
    // Create instances of MainMenu and MidiHandler
    MainMenu mainMenu;
    MidiHandler midiHandler;

    // Execute the script to read the menu aloud
    executePythonScript("intro_voice.py");

    while (true) {
        // Show the main menu
        executePythonScriptReadScales();

        // Display the expanded menu to list all major and minor scales
        std::cout << "Select a scale to practice:" << std::endl;
        std::cout << "1. Ab Major" << std::endl;
        std::cout << "2. A Major" << std::endl;
        std::cout << "3. Bb Major" << std::endl;
        std::cout << "4. B Major" << std::endl;
        std::cout << "5. C Major" << std::endl;
        std::cout << "6. Db Major" << std::endl;
        std::cout << "7. D Major" << std::endl;
        std::cout << "8. Eb Major" << std::endl;
        std::cout << "9. E Major" << std::endl;
        std::cout << "10. F Major" << std::endl;
        std::cout << "11. F# Major" << std::endl;
        std::cout << "12. G Major" << std::endl;
        std::cout << "13. A Minor" << std::endl;
        std::cout << "14. Bb Minor" << std::endl;
        std::cout << "15. B Minor" << std::endl;
        std::cout << "16. C Minor" << std::endl;
        std::cout << "17. C# Minor" << std::endl;
        std::cout << "18. D Minor" << std::endl;
        std::cout << "19. D# Minor" << std::endl;
        std::cout << "20. E Minor" << std::endl;
        std::cout << "21. F Minor" << std::endl;
        std::cout << "22. F# Minor" << std::endl;
        std::cout << "23. G Minor" << std::endl;
        std::cout << "24. G# Minor" << std::endl;
        std::cout << "25. Quit" << std::endl;  // Option to quit from the main menu
        std::cout << "26. About the Program" << std::endl;  // Added "about" option
        std::cout << "27. About the Circle of Fifths" << std::endl;

        std::cout << "Enter your choice: ";

        int choice;
        std::cin >> choice;

        if (choice == 25) {
            std::cout << "Quitting the program..." << std::endl;
            break;
        } else if (choice == 26) {
            // Execute the 'about' Python script to hear about the program
            executePythonScript("about.py");
            continue;  // Return to the main menu after executing the "about" script
        } else if (choice == 27) {
            // Execute the 'about' Python script to hear about the program
            executePythonScript("fifths.py");
            continue;  // Return to the main menu after executing the "about" script
        }

        // Determine the selected scale
        std::string selectedScale;
        switch (choice) {
            case 1: selectedScale = "ab_major"; break;
            case 2: selectedScale = "a_major"; break;
            case 3: selectedScale = "bb_major"; break;
            case 4: selectedScale = "b_major"; break;
            case 5: selectedScale = "c_major"; break;
            case 6: selectedScale = "db_major"; break;
            case 7: selectedScale = "d_major"; break;
            case 8: selectedScale = "eb_major"; break;
            case 9: selectedScale = "e_major"; break;
            case 10: selectedScale = "f_major"; break;
            case 11: selectedScale = "f_sharp_major"; break;
            case 12: selectedScale = "g_major"; break;
            case 13: selectedScale = "a_minor"; break;
            case 14: selectedScale = "bb_minor"; break;
            case 15: selectedScale = "b_minor"; break;
            case 16: selectedScale = "c_minor"; break;
            case 17: selectedScale = "c_sharp_minor"; break;
            case 18: selectedScale = "d_minor"; break;
            case 19: selectedScale = "d_sharp_minor"; break;
            case 20: selectedScale = "e_minor"; break;
            case 21: selectedScale = "f_minor"; break;
            case 22: selectedScale = "f_sharp_minor"; break;
            case 23: selectedScale = "g_minor"; break;
            case 24: selectedScale = "g_sharp_minor"; break;
            default:
                std::cout << "Unknown scale. Please enter a valid scale number." << std::endl;
                continue;  // Go back to the start of the loop to re-prompt the user
        }

        // Execute the script to recite the selected scale
        executePythonScript("recite_scale.py", selectedScale);

        // Get the MIDI notes for the selected scale
        std::vector<int> selectedScaleNotes = getMidiNotesForScale(selectedScale);
        
        // Set the scale in the MIDI handler
        midiHandler.setScale(selectedScaleNotes);

        // Provide options for the user
        while (true) {
            executePythonScript("secondary_menu.py");
            std::cout << "Press 'r' to repeat the scale, 'p' to begin practice, 'm' to return to the main menu, or 'q' to quit." << std::endl;
            // Check for immediate quit input
            if (_kbhit()) {
                char ch = _getch();
                if (ch == 'q' || ch == 'Q') {
                    std::cout << "Quitting the program..." << std::endl;
                    return 0;
                }
            }

            char userChoice;
            std::cin >> userChoice;

            if (userChoice == 'r' || userChoice == 'R') {
                // Repeat the scale
                executePythonScript("recite_scale.py", selectedScale);
            } else if (userChoice == 'p' || userChoice == 'P') {
                std::cout << "Starting MIDI practice... (handled by a separate MIDI handler program)" << std::endl;
                midiHandler.startListening();  // Start the MIDI handling part
            } else if (userChoice == 'm' || userChoice == 'M') {
                // Return to main menu
                break;  // Exit the inner while loop, go back to the main menu
            } else if (userChoice == 'q' || userChoice == 'Q') {
                std::cout << "Quitting the program..." << std::endl;
                return 0;  // Exit the program
            } else {
                std::cout << "Invalid option. Please enter 'r' to repeat the scale, 'p' to begin practice, 'm' to return to the main menu, or 'q' to quit." << std::endl;
            }
        }
    }

    std::cout << "Practice session ended." << std::endl;
    return 0;
}
