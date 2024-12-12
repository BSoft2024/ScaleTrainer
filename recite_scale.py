import pyttsx3
import sys
import time

def recite_scale(notes, right_hand_fingering, left_hand_fingering):
    # Replace flat and sharp symbols with proper names for pronunciation
    readable_notes = [note.replace("b", " flat").replace("#", " sharp") for note in notes]

    engine = pyttsx3.init()

    # Set a normal speech rate for note recitation
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)

    # Announce the introductory phrase
    engine.say("Here are the notes of the scale.")
    engine.runAndWait()

    # Announce each note with a slight pause in between
    for note in readable_notes:
        engine.say(note)
        engine.runAndWait()
        time.sleep(0.5)  # Pause between notes

    # Announce the right-hand fingering instructions
    engine.say("Now, let's go over the right-hand fingering.")
    engine.runAndWait()
    engine.say(right_hand_fingering)
    engine.runAndWait()

    # Pause between right-hand and left-hand instructions
    time.sleep(1)

    # Announce the left-hand fingering instructions
    engine.say("And now, the left-hand fingering.")
    engine.runAndWait()
    engine.say(left_hand_fingering)
    engine.runAndWait()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python recite_scale.py <scale>")
        sys.exit(1)

    scale = sys.argv[1].lower()

    # Dictionary of all scales with their notes
    scales = {
        "c_major": ["C", "D", "E", "F", "G", "A", "B", "C"],
        "g_major": ["G", "A", "B", "C", "D", "E", "F#", "G"],
        "d_major": ["D", "E", "F#", "G", "A", "B", "C#", "D"],
        "a_major": ["A", "B", "C#", "D", "E", "F#", "G#", "A"],
        "e_major": ["E", "F#", "G#", "A", "B", "C#", "D#", "E"],
        "b_major": ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"],
        "f_sharp_major": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"],  # E# -> F
        "c_sharp_major": ["C#", "D#", "E#", "F#", "G#", "A#", "B#", "C#"],  # E# -> F, B# -> C
        "f_major": ["F", "G", "A", "Bb", "C", "D", "E", "F"],
        "bb_major": ["Bb", "C", "D", "Eb", "F", "G", "A", "Bb"],
        "eb_major": ["Eb", "F", "G", "Ab", "Bb", "C", "D", "Eb"],
        "ab_major": ["Ab", "Bb", "C", "Db", "Eb", "F", "G", "Ab"],
        "db_major": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C", "Db"],
        "gb_major": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"],  # Cb -> B
        "a_minor": ["A", "B", "C", "D", "E", "F", "G", "A"],
        "e_minor": ["E", "F#", "G", "A", "B", "C", "D", "E"],
        "b_minor": ["B", "C#", "D", "E", "F#", "G", "A", "B"],
        "f_sharp_minor": ["F#", "G#", "A", "B", "C#", "D", "E", "F#"],
        "c_sharp_minor": ["C#", "D#", "E", "F#", "G#", "A", "B", "C#"],
        "g_sharp_minor": ["G#", "A#", "B", "C#", "D#", "E", "F#", "G#"],
        "d_sharp_minor": ["D#", "E#", "F#", "G#", "A#", "B", "C#", "D#"],  # E# -> F
        "a_sharp_minor": ["A#", "B#", "C#", "D#", "E#", "F#", "G#", "A#"],  # B# -> C, E# -> F
        "d_minor": ["D", "E", "F", "G", "A", "Bb", "C", "D"],
        "g_minor": ["G", "A", "Bb", "C", "D", "Eb", "F", "G"],
        "c_minor": ["C", "D", "Eb", "F", "G", "Ab", "Bb", "C"],
        "f_minor": ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"],
        "bb_minor": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
        "eb_minor": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db", "Eb"],  # Cb -> B
        "ab_minor": ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb", "Ab"]   # Cb -> B, Fb -> E
    }

    # Fingering instructions for right and left hands for each scale
fingerings = {
    "c_major": {
        "right_hand": "Right hand fingering for C Major: Start with your thumb (finger 1) on C, index finger (finger 2) on D, middle finger (finger 3) on E. Cross your thumb (finger 1) on F, index finger (finger 2) on G, middle finger (finger 3) on A, ring finger (finger 4) on B, and pinky (finger 5) on C.",  
 	"left_hand": "Left hand fingering for C Major: Start with your pinky (finger 5) on C, ring finger (finger 4) on D, middle finger (finger 3) on E, index finger (finger 2) on F, and thumb (finger 1) on G. Cross your middle finger (finger 3) to A, index finger (finger 2) on B, and thumb (finger 1) on C."
    },
    "g_major": {
        "right_hand": "Right hand fingering for G Major: Start with your thumb (finger 1) on G, index finger (finger 2) on A, middle finger (finger 3) on B. Cross your thumb (finger 1) on C, index finger (finger 2) on D, middle finger (finger 3) on E, ring finger (finger 4) on F sharp, and pinky (finger 5) on G.",
        "left_hand":  "Left hand fingering for G Major: Start with your pinky (finger 5) on G, ring finger (finger 4) on A, middle finger (finger 3) on B, index finger (finger 2) on C, thumb (finger 1) on D. Cross your middle finger (finger 3) on E, index finger (finger 2) on F sharp, and thumb (finger 1) on G."
    },
    "d_major": {
        "right_hand": "Right hand fingering for D Major: Start with your thumb (finger 1) on D, index finger (finger 2) on E, middle finger (finger 3) on F sharp. Cross your thumb (finger 1) on G, index finger (finger 2) on A, middle finger (finger 3) on B, ring finger (finger 4) on C sharp, and pinky (finger 5) on D.",
        "left_hand": "Left hand fingering for D Major: Start with your pinky (finger 5) on D, ring finger (finger 4) on E, middle finger (finger 3) on F sharp, index finger (finger 2) on G, and thumb (finger 1) on A. Cross your middle finger (finger 3) on B, index finger (finger 2) on C sharp, and thumb (finger 1) on D."
    },
    "a_major": {
        "right_hand": "Right hand fingering for A Major: Start with your thumb (finger 1) on A, index finger (finger 2) on B, middle finger (finger 3) on C sharp. Cross your thumb (finger 1) to D, index finger (finger 2) on E, middle finger (finger 3) on F sharp, ring finger (finger 4) on G sharp, and pinky (finger 5) on A.",
        "left_hand": "Left hand fingering for A Major: Start with your pinky (finger 5) on A, ring finger (finger 4) on B, middle finger (finger 3) on C sharp, index finger (finger 2) on D, and thumb (finger 1) on E. Cross your middle finger (finger 3) on F sharp, index finger (finger 2) on G sharp, and thumb (finger 1) on A."
    },
    "e_major": {	
        "right_hand": "Right hand fingering for E Major: Start with your thumb (finger 1) on E, index finger (finger 2) on F sharp, middle finger (finger 3) on G sharp. Cross your thumb (finger 1) under to A, index finger (finger 2) on B, middle finger (finger 3) on C sharp, ring finger (finger 4) on D sharp, and pinky (finger 5) on E.",
        "left_hand": "Left hand fingering for E Major: Start with your pinky (finger 5) on E, ring finger (finger 4) on F sharp, middle finger (finger 3) on G sharp, index finger (finger 2) on A, and thumb (finger 1) on B. Cross your middle finger (finger 3) on sharp, index finger (finger 2) on D sharp, and thumb (finger 1) on E."
    },
    "b_major": {
        "right_hand": "Right hand fingering for B Major: Start with your thumb (finger 1) on B, index finger (finger 2) on C sharp, middle finger (finger 3) on D sharp. Cross your thumb (finger 1) on E, index finger (finger 2) on F sharp, middle finger (finger 3) on G sharp, ring finger (finger 4) on A sharp, and pinky (finger 5) on B.", 
        "left_hand": "Left hand fingering for B Major: Start with your ring finger (finger 4) on B, middle finger (finger 3) on C sharp, index finger (finger 2) on D sharp, and thumb (finger 1) on E. Cross your ring finger (finger 4) on F sharp, middle finger (finger 3) on G sharp, index finger (finger 2) on A sharp, and thumb (finger 1) on B."
    },
    "f_sharp_major": {
        "right_hand": "Right hand fingering for F Sharp Major: Start with your index finger (finger 2) on F sharp, middle finger (finger 3) on G sharp, ring finger (finger 4) on A sharp. Cross your thumb (finger 1) on B, index finger (finger 2) on C sharp, middle finger (finger 3) on D sharp. Cross your thumb (finger 1) on E sharp, and index finger (finger 2)  on F sharp.",
        "left_hand": "Left hand fingering for F Sharp Major: Start with your ring finger (finger 4) on F sharp, middle finger (finger 3) on G sharp, index finger (finger 2) on A sharp, thumb (finger 1) on B. Cross your middle finger (finger 3) over to C sharp, index finger (finger 2) and use your thumb (finger 1) on E sharp. Cross your ring finger (finger 4) on F sharp."
    },
    "c_sharp_major": {
        "right_hand": "Right hand fingering for C Sharp Major: Start with your index finger (finger 2) on C sharp, middle finger (finger 3) on D sharp. Cross your thumb (finger 1) on E sharp, index finger (finger 2) to F sharp, middle finger (finger 3) on G sharp, ring finger (finger 4) on A sharp. Cross your thumb (finger 1) on B sharp, and index finger (finger 2) on C sharp.",
        "left_hand": "Left hand fingering for C Sharp Major: Start with your middle finger (finger 3) on C sharp, index finger (finger 2) on D sharp, thumb (finger 1) on E sharp. Cross your ring finger (finger 4) on F sharp, middle finger (finger 3) on G sharp, index finger (finger 2) on A sharp, and thumb (finger 1) on B sharp. Cross your ring finger (finger 3) on C sharp."
    },
    "f_major": {
        "right_hand": "Right hand fingering for F Major: Start with your thumb (finger 1) on F, index finger (finger 2) on G, middle finger (finger 3) on A, ring finger (finger 4) on B flat. Cross your thumb (finger 1) on C, index finger (finger 2) on D, middle finger (finger 3) on E, and ring finger (finger 4) on F",
        "left_hand": "Left hand fingering for F Major: Start with your pinky (finger 5) on F, ring finger (finger 4) on G, middle finger (finger 3) on A, index finger (finger 2) on B flat, and thumb (finger 1) on C. Cross your middle finger (finger 3) over to D, index finger (finger 2) on E, and thumb (finger 1) on F."
    },
    "bb_major": {
        "right_hand": "Right hand fingering for B Flat Major: Start with your ring finger (finger 4) on B flat, Cross your thumb (finger 1) on C, index finger (finger 2) on D, middle finger (finger 3) on E flat. Cross your thumb (finger 1) on F, index finger (finger 2) on G, middle finger (finger 3) on A, and ring finger (finger 4) B flat.",
        "left_hand": "Left hand fingering for B Flat Major: Start with your middle finger (finger 3) on B flat, index finger (finger 2) on C, thumb (finger 1) on D. Cross your ring finger (finger 4) on E flat, middle finger (finger 3) on F, index finger (finger 2) over to G, thumb (finger 1) on A. Cross your middle finger (finger 3) on B flat."
    },
    "eb_major": {
        "right_hand": "Right hand fingering for E Flat Major: Start with your middle finger (finger 3) on E flat. Cross your thumb (finger 1) on F, index finger (finger 2) on G, middle finger (finger 3) on A flat, ring finger (finger 4) on B flat. Cross your thumb (finger 1) on C, index finger (finger 2) on D, and your middle finger (finger 3) on E flat.",
        "left_hand": "Left hand fingering for E Flat Major: Start with your middle finger (finger 3) on E flat, index finger (finger 2) on F, thumb (finger 1) on G. Cross your ring finger (finger 4) on A flat, middle finger (finger 3) on B flat, index finger (finger 2) over to C, thumb (finger 1) on D. Cross your middle finger (finger 3) on E flat."
    },
    "ab_major": {
        "right_hand": "Right hand fingering for A Flat Major: Start with your middle finger (finger 3) on A flat, ring finger (finger 4) on B flat. Cross your thumb (finger 1) on C, index finger (finger 2) under to D flat, middle finger (finger 3) on E flat. Cross your thumb (finger 1) on F, index finger (finger 2) on G, and middle finger (finger 3) on A flat.",
        "left_hand": "Left hand fingering for A Flat Major: Start with your middle finger (finger 3) on A flat, index finger (finger 2) on B flat, thumb (finger 1) on C. Cross your ring finger (finger 4) on D flat, middle finger (finger 3) on E flat, index finger (finger 2) on F, thumb (finger 1) on G. Cross your middle finger (finger 3) on A flat."
    },
    "db_major": {
        "right_hand": "Right hand fingering for D Flat Major: Start with your index finger (finger 2) on D flat, middle finger (finger 3) on E flat. Cross your thumb (finger 1) on F, index finger (finger 2) on G flat, middle finger (finger 3) on A flat, ring finger (finger 4) on B flat. Cross your thumb (finger 1) on C, and index finger (finger 2) on D flat. ",
        "left_hand": "Left hand fingering for D Flat Major: Start with your middle finger (finger 3) on D flat, index finger (finger 2) on E flat, thumb (finger 1) on F. Cross your ring finger (finger 4) on G flat, middle finger (finger 3) on A flat, index finger (finger 2) on B flat, and thumb (finger 1) on C. Cross your middle finger (finger 3) on D flat."
    },
    "gb_major": {
        "right_hand": "Right hand fingering for G Flat Major: Start with your index finger (finger 2) on G flat, middle finger (finger 3) on A flat, ring finger (finger 4) on B flat. Cross your thumb (finger 1) on B, index finger (finger 2) on D flat, middle finger (finger 3) on E flat. Cross your thumb (finger 1) on F, and your index finger (finger 2) on G flat",
        "left_hand": "Left hand fingering for G Flat Major: Start with your ring finger (finger 4) on G flat, middle finger (finger 3) on A flat, index finger (finger 2) on B flat, thumb (finger 1) on B. Cross your middle finger (finger 3) on D flat, index finger (finger 2) on E flat, and thumb (finger 1) on F. Cross your ring finger (finger 4) on G flat."
    },
    "a_minor": {
        "right_hand": "Right hand fingering for A Minor: Start with your thumb (finger 1) on A, index finger (finger 2) on B, middle finger (finger 3) on C, cross your thumb (finger 1) on D, index finger (finger 2) on E, middle finger (finger 3) on F, ring finger (finger 4) on G, and pinky (finger 5) on A.",
        "left_hand": "Left hand fingering for A Minor: Start with your pinky (finger 5) on A, ring finger (finger 4) on B, middle finger (finger 3) on C, index finger (finger 2) on D, thumb (finger 1) on E. Cross your middle finger (finger 3) on F, index finger (finger 2) on G, and thumb (finger 1) on A."
    },
    "e_minor": {
        "right_hand": "Right hand fingering for E Minor: Start with your thumb (finger 1) on E, index finger (finger 2) on F sharp, middle finger (finger 3) on G, cross your thumb (finger 1) on A, index finger (finger 2) on B, middle finger (finger 3) on C, ring finger (finger 4) on D, and pinky (finger 5) on E.",
        "left_hand": "Left hand fingering for E Minor: Start with your pinky (finger 5) on E, ring finger (finger 4) on F sharp, middle finger (finger 3) on G, index finger (finger 2) on A, thumb (finger 1) on B. Cross your middle finger (finger 3) on C, index finger (finger 2) on D, and thumb (finger 1) on E."
    },
    "b_minor": {
        "right_hand": "Right hand fingering for B Minor: Start with your thumb (finger 1) on B, index finger (finger 2) on C sharp, middle finger (finger 3) on D. Cross your thumb (finger 1) on E, index finger (finger 2) on F sharp, middle finger (finger 3) on G, ring finger (finger 4) on A, and pinky (finger 5) on B.",
        "left_hand": "Left hand fingering for B Minor: Start with your ring finger (finger 4) on B, middle finger (finger 3) on C sharp, index finger (finger 2) on D, thumb (finger 1) on E. Cross your ring finger (finger 4) on F sharp, middle finger (finger 3) over to G, index finger (finger 2) on A, and your thumb (finger 1) on B."
    },
    "f_sharp_minor": {
        "right_hand": "Right hand fingering for F Sharp Minor: Start with your index finger (finger 2) on F sharp, middle finger (finger 3) on G sharp. Cross your thumb (finger 1) on A, index finger (finger 2) on B, middle finger (finger 3) on C sharp. Cross your thumb (finger 1) on D, index finger (finger 2) on E, and middle finger (finger 3) on F sharp.",
        "left_hand": "Left hand fingering for F Sharp Minor: Start with your ring finger (finger 4) on F sharp, middle finger (finger 3) on G sharp, index finger (finger 2) on A, thumb (finger 1) on B. Cross your middle finger (finger 3) on C sharp, index finger (finger 2) on D, and your thumb (finger 1) on E. Cross your ring finger (finger 4) on F sharp."
    },
    "c_sharp_minor": {
        "right_hand": "Right hand fingering for C Sharp Minor: Start with your middle finger (finger 3) on C sharp, ring finger (finger 4) on D sharp. Cross your thumb (finger 1) on E, index finger (finger 2) on F sharp, middle finger (finger 3) on G sharp. Cross your thumb (finger 1) on A, index finger (finger 2) on B, and middle finger (finger 3) on C sharp.",
        "left_hand": "Left hand fingering for C Sharp Minor: Start with your middle finger (finger 3) on C sharp, index finger (finger 2) on D sharp, thumb (finger 1) on E. Cross your ring finger (finger 4) on F sharp, middle finger (finger 3) on G sharp, index finger (finger 2) on A, and thumb (finger 1) on B. Cross your middle finger (finger 3) on C sharp."
    },
    "g_sharp_minor": {
        "right_hand": "Right hand fingering for G Sharp Minor: Start with your middle finger (finger 3) on G sharp, ring finger (finger 4) on A sharp. Cross your thumb (finger 1) on B, your index finger (finger 2) on C sharp, middle finger (finger 3) on D sharp. Cross your thumb (finger 1) on E, index finger (finger 2) on F sharp, and middle finger (finger 3) on G sharp.",
        "left_hand": "Left hand fingering for G Sharp Minor: Start with your middle finger (finger 3) on G sharp, index finger (finger 2) on A sharp, thumb (finger 1) on B. Cross your middle finger (finger 3) on C sharp, index finger (finger 2) on D sharp, thumb (finger 1) E. Cross your middle finger (finger 3) on F sharp and middle index (finger 2) on G sharp."
    },
    "d_sharp_minor": {
        "right_hand": "Right hand fingering for D Sharp Minor: Start with your middle finger (finger 3) on D sharp. Cross your thumb (finger 1) on E sharp, index finger (finger 2) on F sharp, middle finger (finger 3) on G sharp, ring finger (finger 4) on A sharp. Cross your thumb (finger 1) on B, index finger (finger 2) on C sharp, and middle finger (finger 3) on D sharp.",
        "left_hand": "Left hand fingering for D Sharp Minor: Start with your index finger (finger 2) on D sharp, thumb (finger 1) on E sharp. Cross your ring finger (finger 4) on F sharp, middle finger (finger 3) on G sharp, index (finger 2) on A sharp, thumb (finger 1) on B. Cross your middle finger (finger 3) on C sharp and index finger (finger 2) D sharp."
    },
    "a_sharp_minor": {
        "right_hand": "Right hand fingering for A Sharp Minor: Start with your index finger (finger 2) on A sharp. Cross your thumb (finger 1) on B sharp, index finger (finger 2) on C sharp, middle finger (finger 3) on D sharp. Cross your thumb (finger 1) on E sharp, index finger (finger 2) on F sharp, middle finger (finger 3) on G sharp, and ring finger (finger 4) on A sharp.",
        "left_hand": "Left hand fingering for A Sharp Minor: Start with index finger (finger 2) on A sharp, thumb (finger 1) on B sharp. Cross your middle finger (finger 3) on C sharp, index finger (finger 2) on D sharp, thumb (finger 1) on E sharp. Cross your ring finger (finger 4) on F sharp, middle finger (finger 3) on G sharp, and index finger (finger 2) on A sharp"
    },
    "d_minor": {
        "right_hand": "Right hand fingering for D Minor: Start with your thumb (finger 1) on D, index finger (finger 2) on E, middle finger (finger 3) on F. Cross your thumb (finger 1) on G, index finger (finger 2) on A, middle finger (finger 3) on B flat, ring finger (finger 4) on C, and pinky (finger 5) on D.",
        "left_hand": "Left hand fingering for D Minor: Start with your pinky (finger 5) on D, ring finger (finger 4) on E, finger (finger 3) on F, index finger (finger 2) on G, thumb (finger 1) on A. Cross your middle finger (finger 3) over to B flat, index finger (finger 2) on C, and thumb (finger 1) on D."
    },
    "g_minor": {
        "right_hand": "Right hand fingering for G Minor: Start with thumb (finger 1) on G, index finger (finger 2) on A, middle finger (finger 3) on B flat. Cross your thumb (finger 1) on C, index finger (finger 2) on D, middle finger (finger 3) on E flat. ring finger (finger 4) on F, and pinky (finger 5) on G.",
        "left_hand": "Left hand fingering for G Minor: Start with your pinky (finger 5) on G, ring finger (finger 4) on A, middle finger (finger 3) on B flat, index finger (finger 2) on C, thumb (finger 1) on D. Cross your middle finger (finger 3) over to E flat, index finger (finger 2) on F, and thumb (finger 1) on G."
    },
    "c_minor": {
        "right_hand": "Right hand fingering for C Minor: Start with your thumb (finger 1) on C, index finger (finger 2) on D, middle finger (finger 3) on E flat. Cross your thumb (finger 1) on F, index finger (finger 2) on G, middle finger (finger 3) on A flat, ring finger (finger 4) on B flat, and pinky (finger 5) on C.",
        "left_hand": "Left hand fingering for C Minor: Start with your pinky (finger 5) on C, ring finger (finger 4) on D, middle finger (finger 3) on E flat, index finger (finger 2) on F, thumb (finger 1) on G. Cross your middle finger (finger 3) on A flat, index finger (finger 2) on B flat, and thumb (finger 1) on C."
    },
    "f_minor": {
        "right_hand": "Right hand fingering for F Minor: Start with your thumb (finger 1) on F, index finger (finger 2) on G, middle finger (finger 3) on A flat, ring finger (finger 4) on B flat. Cross your thumb (finger 1) on C, index finger (finger 2) on D, middle finger (finger 3) on E flat, and ring finger (finger 4) on F.",
        "left_hand": "Left hand fingering for F Minor: Start with your pinky (finger 5) on F, ring finger (finger 4) on G, middle finger (finger 3) on A flat, index finger (finger 2) on B flat, thumb (finger 1) on C. Cross your middle finger (finger 3) on D, index finger (finger 2) on E flat, and thumb (finger 1) on F."
    },
    "bb_minor": {
        "right_hand": "Right hand fingering for B Flat Minor: Start with your index finger (finger 2) on B flat. Cross your thumb (finger 1) on C, index finger (finger 2) on D flat, middle finger (finger 3) on E flat. Cross your thumb (finger 1) on F, index finger (finger 2) on G flat, middle finger (finger 3) on A flat, and ring finger (finger 4) on B flat.",
        "left_hand": "Left hand fingering for B Flat Minor: Start with your index (finger 2) on B flat, thumb (finger 1) on C. Cross your middle finger (finger 3) on D flat, index finger (finger 2) on E flat, thumb (finger 1) on F. Cross your ring finger (finger 4) on G flat, middle finger (finger 3) on A flat, and index finger (finger 2) on B flat."
    },
    "eb_minor": {
        "right_hand": "Right hand fingering for E Flat Minor: Start with your middle finger (finger 3) on E flat. Cross your thumb (finger 1) on F, index finger (finger 2) on G flat, middle finger (finger 3) on A flat, ring finger (finger 4) on B flat. Cross your thumb (finger 1) on B, index finger (finger 2) on D flat, and middle finger (finger 3) on E flat.",
        "left_hand": "Left hand fingering for E Flat Minor: Start with your index finger (finger 2) on E flat, thumb (finger 1) on F. Cross your ring finger (finger 4) on G flat, middle finger (finger 3) on A flat, index finger (finger 2) on B flat, thumb (finger 1) over to B. Cross your middle finger (finger 3) on D flat and your index finger (finger 2) E flat."
    },
    "ab_minor": {
        "right_hand": "Right hand fingering for A Flat Minor: Start with your middle finger (finger 3) on A flat, ring finger (finger 4) on B flat. Cross your thumb (finger 1) on B, index finger (finger 2) on D flat, middle finger (finger 3) on E flat. Cross your thumb (finger 1) on E, index finger (finger 2) on G flat, and middle finger (finger 3) on A flat.",
        "left_hand": "Left hand fingering for A Flat Minor: Start with your middle ring (finger 3) on A flat, index finger (finger 2) on B flat, thumb (finger 1) on B. Cross your middle finger (finger 3) on D flat, index finger (finger 2) on E flat, thumb (finger 1) on E. Cross your middle finger (finger 3) on G flat and index finger (finger 2) on A flat."
    }
}

# Replace enharmonic equivalents
for key in scales:
    scales[key] = [note.replace("E#", "F").replace("B#", "C").replace("Cb", "B").replace("Fb", "E") for note in scales[key]]

if scale in scales:
    # Retrieve the right and left hand fingerings
    right_hand_fingering = fingerings.get(scale, {}).get("right_hand", "Right-hand fingering information not available.")
    left_hand_fingering = fingerings.get(scale, {}).get("left_hand", "Left-hand fingering information not available.")
    
    # Recite the scale, followed by the fingering information
    recite_scale(scales[scale], right_hand_fingering, left_hand_fingering)
else:
    print("Unknown scale. Please enter a valid scale name.")
    sys.exit(1)

