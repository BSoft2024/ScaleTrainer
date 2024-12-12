import pyttsx3
import time

def play_intro():
    engine = pyttsx3.init()

    # Set a slower speech rate for the introduction
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 75)  # Adjust rate to slow down the introduction

    # Break the introduction text into paragraphs
    paragraph_1 = "Musical Scale Trainer was developed by Loosey Goosey Media and is released under a Creative Commons Zero license. You may use and distribute it as you wish, without limitation or restriction."
    paragraph_2 = "This program was specifically designed for individuals with low vision or blindness, but anyone is welcome to use it as they please."
    paragraph_3 = "When you use the Trainer in practice mode, notes within the scale will sound properly, while pressing a note that is not part of the scale will result in a distinct error tone. This is not a flaw in the program—it is intended to help you learn the scale more effectively."
    paragraph_4 = "If you have any questions about this program, contact Brant von Goble at: B-R-A-N-T underscore G-O-B-L-E at P-M dot M-E."
    paragraph_5 = "Good luck, and enjoy the program. We will now return to the main menu."

    # Speak each paragraph with pauses in between
    engine.say(paragraph_1)
    engine.runAndWait()
    time.sleep(1)  # Pause for 1 second

    engine.say(paragraph_2)
    engine.runAndWait()
    time.sleep(1)  # Pause for 1 second

    engine.say(paragraph_3)
    engine.runAndWait()
    time.sleep(1)  # Pause for 1 second

    engine.say(paragraph_4)
    engine.runAndWait()
    time.sleep(1)  # Pause for 1 second

    engine.say(paragraph_5)
    engine.runAndWait()

if __name__ == "__main__":
    play_intro()
