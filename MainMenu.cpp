#include "MainMenu.h"
#include <iostream>
#include <cstdlib> // For system calls
#include <limits>  // For std::numeric_limits
#include "config.h"  // Corrected include

MainMenu::MainMenu()
{
    // Constructor code if needed
}

void MainMenu::displayMenu()
{
    std::cout << "Welcome to MIDI Scale Trainer!" << std::endl;
    std::cout << "Select a scale to practice:" << std::endl;
    std::cout << "1. Start MIDI Program" << std::endl;
    std::cout << "2. C Major" << std::endl;
    std::cout << "3. G Major" << std::endl;
    std::cout << "4. D Major" << std::endl;
    std::cout << "5. A Major" << std::endl;
    std::cout << "6. E Major" << std::endl;
    std::cout << "7. F Major" << std::endl;
    std::cout << "8. B♭ Major" << std::endl;
    std::cout << "9. E♭ Major" << std::endl;
    std::cout << "10. A♭ Major" << std::endl;
    std::cout << "11. D♭ Major" << std::endl;
    std::cout << "12. G♭ Major" << std::endl;
    std::cout << "13. B Major" << std::endl;
    std::cout << "14. F♯ Major" << std::endl;
    std::cout << "15. A Minor" << std::endl;
    std::cout << "16. E Minor" << std::endl;
    std::cout << "17. B Minor" << std::endl;
    std::cout << "18. F# Minor" << std::endl;
    std::cout << "19. C# Minor" << std::endl;
    std::cout << "20. G# Minor" << std::endl;
    std::cout << "21. D# Minor" << std::endl;
    std::cout << "22. A# Minor" << std::endl;
    std::cout << "23. D Minor" << std::endl;
    std::cout << "24. G Minor" << std::endl;
    std::cout << "25. C Minor" << std::endl;
    std::cout << "26. F Minor" << std::endl;
    std::cout << "27. Bb Minor" << std::endl;
    std::cout << "28. Eb Minor" << std::endl;
    std::cout << "29. Ab Minor" << std::endl;
    std::cout << "Enter your choice (1-29): ";

    // Use system command to call Python script for text-to-speech menu announcement
    int result = system((pythonPath + " recite_scale.py \"Welcome to MIDI Scale Trainer. Please choose a scale or start the MIDI program.\"").c_str());
    if (result != 0)
    {
        std::cout << "Failed to execute Python script. Please ensure that Python is installed and accessible." << std::endl;
    }
}

std::string MainMenu::getSelectedScale()
{
    int choice;
    while (true)
    {
        std::cin >> choice;

        if (std::cin.fail() || choice < 1 || choice > 29)
        {
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            std::cout << "Invalid choice. Please enter a number between 1 and 29: ";
        }
        else
        {
            break; // Exit loop if input is valid
        }
    }

    switch (choice)
    {
        case 1:
            std::cout << "Starting MIDI Program..." << std::endl;
            midiHandler.startListening();  // Ensure midiHandler is properly defined elsewhere
            return "MIDI Program Started";
        case 2:
            announceSelection("C Major");
            return "C Major";
        case 3:
            announceSelection("G Major");
            return "G Major";
        case 4:
            announceSelection("D Major");
            return "D Major";
        case 5:
            announceSelection("A Major");
            return "A Major";
        case 6:
            announceSelection("E Major");
            return "E Major";
        case 7:
            announceSelection("F Major");
            return "F Major";
        case 8:
            announceSelection("B♭ Major");
            return "B♭ Major";
        case 9:
            announceSelection("E♭ Major");
            return "E♭ Major";
        case 10:
            announceSelection("A♭ Major");
            return "A♭ Major";
        case 11:
            announceSelection("D♭ Major");
            return "D♭ Major";
        case 12:
            announceSelection("G♭ Major");
            return "G♭ Major";
        case 13:
            announceSelection("B Major");
            return "B Major";
        case 14:
            announceSelection("F♯ Major");
            return "F♯ Major";
        case 15:
            announceSelection("A Minor");
            return "A Minor";
        case 16:
            announceSelection("E Minor");
            return "E Minor";
        case 17:
            announceSelection("B Minor");
            return "B Minor";
        case 18:
            announceSelection("F# Minor");
            return "F# Minor";
        case 19:
            announceSelection("C# Minor");
            return "C# Minor";
        case 20:
            announceSelection("G# Minor");
            return "G# Minor";
        case 21:
            announceSelection("D# Minor");
            return "D# Minor";
        case 22:
            announceSelection("A# Minor");
            return "A# Minor";
        case 23:
            announceSelection("D Minor");
            return "D Minor";
        case 24:
            announceSelection("G Minor");
            return "G Minor";
        case 25:
            announceSelection("C Minor");
            return "C Minor";
        case 26:
            announceSelection("F Minor");
            return "F Minor";
        case 27:
            announceSelection("Bb Minor");
            return "Bb Minor";
        case 28:
            announceSelection("Eb Minor");
            return "Eb Minor";
        case 29:
            announceSelection("Ab Minor");
            return "Ab Minor";
        default:
            return ""; // This line should never be reached, but added as a safety
    }
}

void MainMenu::announceSelection(const std::string& scale)
{
    std::cout << "You selected: " << scale << std::endl;

    // Use text-to-speech to announce the selected scale
    std::string command = pythonPath + " recite_scale.py \"" + scale + "\"";
    int result = system(command.c_str());
    if (result != 0)
    {
        std::cout << "Failed to execute Python script for scale announcement." << std::endl;
    }
}
