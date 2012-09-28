# Love in Space

# Declare images below this line, using the image statement.

image bg stars = "starscape.png"
image bg earth = "earth.jpg"
image him normal = "him.png"
image her normal = "her.png"

# Declare characters used by this game .
define her = DynamicCharacter("her_name", color="#8a00ff")
define him = DynamicCharacter("his_name", color="#ed0303")

define his_name = "???"
define her_name = "Me"

# Variables about our characters and their relationship
define profession = ""
define father_attitude = ""
define favorite_wedding_gift = ""
define want_kids = False

# The game starts here.
label start:

    scene bg stars
    play music "void.ogg"
    show her normal at center with moveinleft

    "I thought I knew what love was. After all, that's why I married..."
    $ his_name = renpy.input("What is his name?", "Jack", length=20)
    "After all, that's why I married [his_name]."

    show him normal at right with moveinright

    "There's no way I could have known what the two of us would go through."

    jump choose_career

    return

label choose_career:
    scene bg earth with fade
    play music "Amnesia.ogg" fadeout 1.0
    "It all started back on Earth, when I was working at..."

menu:
    "The craft store":
        jump crafter
        
    "The hospital":
        jump doctor

    "The car repair shop":
        jump mechanic

    "The elementary school":
        jump teacher        
