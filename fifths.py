import pyttsx3
import time

def play_intro():
    engine = pyttsx3.init()

    # Set a slower speech rate for the introduction
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Adjust rate to slow down the introduction

    # Text content for the introduction, broken into paragraphs
    paragraphs = [
        "Hello! Today, I’d like to introduce you to a tool called the circle of fifths and explain why it can be helpful when learning major and minor scales.",
        
        "The circle of fifths is a visual representation that shows the relationship between different musical keys. It’s called the 'circle of fifths' because each key on the circle is a perfect fifth apart from the next. For example, starting from C major and moving clockwise, the next key is G major, then D major, A major, and so on.",
        
        "Now, you might be wondering, how does this help with learning scales? Well, practicing scales in the order of the circle of fifths has several benefits:",
        
        "Gradual Introduction of Sharps and Flats: As you move around the circle, you’ll notice that each key adds just one sharp or flat at a time. This progression helps you internalize the changes in key signatures gradually, making it easier to understand which notes belong to each scale.",
        
        "Harmonic Relationships: The circle of fifths isn’t just a tool for scales; it also shows how keys are harmonically related. This is especially useful when learning chord progressions and understanding how different keys connect in music composition.",
        
        "Muscle Memory and Finger Patterns: Practicing scales in the circle’s order helps build muscle memory. Your fingers will become familiar with common patterns that appear in music, making it easier to play pieces that change key or incorporate modulation.",
        
        "To sum up, while you may practice scales alphabetically for organization, using the circle of fifths helps deepen your understanding of music theory and enhances your playing skills. It’s a great way to get comfortable with scales and see how they interrelate, preparing you for more complex music in the future.",
        
        "To give you a clearer picture of how the circle of fifths is structured, here is a spoken list of the major and minor scales in order:"
    ]
    
    # List of scales with pauses between each
    scales = [
        "C major and its relative minor, A minor – no sharps or flats.",
        "G major and its relative minor, E minor – one sharp.",
        "D major and its relative minor, B minor – two sharps.",
        "A major and its relative minor, F-sharp minor – three sharps.",
        "E major and its relative minor, C-sharp minor – four sharps.",
        "B major and its relative minor, G-sharp minor – five sharps.",
        "F-sharp major and its relative minor, D-sharp minor – six sharps.",
        "D-flat major and its relative minor, B-flat minor – five flats (also enharmonic to C-sharp major).",
        "A-flat major and its relative minor, F minor – four flats.",
        "E-flat major and its relative minor, C minor – three flats.",
        "B-flat major and its relative minor, G minor – two flats.",
        "F major and its relative minor, D minor – one flat.",
        "And then we return to C major and A minor, completing the circle."
    ]
    
    # Recommended training order with pauses between each step
    training_order = [
        "Start with C major and A minor – no sharps or flats.",
        "Move to G major and E minor – one sharp.",
        "Progress to D major and B minor – two sharps.",
        "Continue to A major and F-sharp minor – three sharps.",
        "Practice E major and C-sharp minor – four sharps.",
        "Work on B major and G-sharp minor – five sharps.",
        "Explore F-sharp major and D-sharp minor – six sharps.",
        "Shift to D-flat major and B-flat minor – five flats.",
        "Follow with A-flat major and F minor – four flats.",
        "Move to E-flat major and C minor – three flats.",
        "Continue with B-flat major and G minor – two flats.",
        "Finally, practice F major and D minor – one flat.",
        "Repeat this order multiple times to strengthen your understanding of key signatures and the relationships between scales."
    ]

    # Speak each paragraph with pauses in between
    for paragraph in paragraphs:
        engine.say(paragraph)
        engine.runAndWait()
        time.sleep(1)  # Pause for 1 second between paragraphs

    # Speak each scale with a pause in between
    for scale in scales:
        engine.say(scale)
        engine.runAndWait()
        time.sleep(0.75)  # Pause for 0.75 seconds between scales

    # Speak the training order with pauses in between
    engine.say("Recommended Training Order: To build confidence and skill, it’s beneficial to practice in this order.")
    engine.runAndWait()
    time.sleep(1)

    for step in training_order:
        engine.say(step)
        engine.runAndWait()
        time.sleep(0.75)  # Pause for 0.75 seconds between recommendations

    # End message
    engine.say("Thank you for listening, and I hope this helps as you practice your scales! We will now return to the main menu.")
    engine.runAndWait()

if __name__ == "__main__":
    play_intro()
