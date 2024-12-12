#ifndef MAINMENU_H_INCLUDED
#define MAINMENU_H_INCLUDED

#include <string>
#include "MidiHandler.h" // Include MidiHandler

class MainMenu
{
public:
    MainMenu();
    void displayMenu();
    std::string getSelectedScale();

private:
    void announceSelection(const std::string& scale);
    MidiHandler midiHandler;  // Declare MidiHandler instance
};

#endif // MAINMENU_H_INCLUDED
