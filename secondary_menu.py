import pyttsx3

def read_menu():
    engine = pyttsx3.init()

    # Set a normal speech rate for reading the menu
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)

    menu_text = [
        "Press R to repeat the scale. Press P to begin practice. Press Q to quit. Press M to return to the main menu. Remember that you can stop practice at any time by hitting Q and enter."
    ]

    # Read each line of the menu
    for line in menu_text:
        engine.say(line)
        engine.runAndWait()

if __name__ == "__main__":
    read_menu()
