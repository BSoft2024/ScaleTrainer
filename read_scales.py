import pyttsx3

def read_menu():
    engine = pyttsx3.init()

    # Set a normal speech rate for reading the menu
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)

    menu_text = [
        "Select a scale to practice. Type your selection and press ENTER after the menu has been read",
        "1. A Flat Major",
     	"2. A Major",
     	"3. B Flat Major",
     	"4. B Major",
     	"5. C Major",
     	"6. D Flat Major",
     	"7. D Major",
     	"8. E Flat Major",
     	"9. E Major",
     	"10. F Major",
     	"11. F Sharp Major",
     	"12. G Major",
     	"13. A Minor",
     	"14. B Flat Minor",
     	"15. B Minor",
     	"16. C Minor",
     	"17. C Sharp Minor",
     	"18. D Minor",
     	"19. D Sharp Minor",
     	"20. E Minor",
     	"21. F Minor",
     	"22. F Sharp Minor",
     	"23. G Minor",
     	"24. G Sharp Minor",
	"25. To quit the program",
	"26. To hear about the program",
	"27. To hear about the circle of fifths",
    ]

    # Read each line of the menu
    for line in menu_text:
        engine.say(line)
        engine.runAndWait()

if __name__ == "__main__":
    read_menu()
