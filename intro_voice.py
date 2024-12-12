import pyttsx3

def play_intro():
    engine = pyttsx3.init()

    # Set a slower speech rate for the introduction
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 75)  # Adjust rate to slow down the introduction

    # Speak the introduction text
    intro_text = "Welcome to the Musical Scale Trainer."
    engine.say(intro_text)
    engine.runAndWait()

if __name__ == "__main__":
    play_intro()
