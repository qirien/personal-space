# Love in Space

# Declare images below this line, using the image statement.

image bg stars = "bg/starscape.png"
image bg earth = "bg/earth.jpg"
image him normal = "sprites/him.png"
image her normal = "sprites/her.png"

# Declare characters used by this game .
define her = DynamicCharacter("her_name", color="#8a00ff")
define him = DynamicCharacter("his_name", color="#ed0303")

define his_name = "???"
define her_name = "Me"

# Variables about emotional state.  -100 is minimum, 100 is maximum
define relaxed = 0    # negative = stressed
define energized = 0  # negative = exhausted
define loved = 0      # negative = neglected
define inspired = 0   # negative = depressed

# Variables about skills.  On a scale from 0-100, how skilled is the character?  These are now defined in dse.rpy

# Variables about our characters and their relationship
define profession = ""
define father_attitude = ""
define favorite_wedding_gift = ""
define want_kids = False
define have_goat = False

# The game starts here.
label start:

    scene bg stars
    show her normal at center with moveinleft

    # TODO: Stronger beginning    
    menu:
        "Do I want to remember how it all began?"
        "Yes":
            "Of course."
        "No":
            jump month01

    "I thought I knew what love was. After all, that's why I married..."
    $ his_name = renpy.input("What is his name?", "Jack", length=20)
    "After all, that's why I married [his_name]."

    show him normal at right with moveinright

    "There's no way I could have known what the two of us would go through."

    jump choose_career

    return

label choose_career:
    scene bg earth with fade
    "It all started back on Earth, when I was working at..."

menu:
    "The craft store":
        $ skill_creative += 20
        jump crafter
        
    "The hospital":
        $ skill_knowledge += 20
        jump doctor

    "The car repair shop":
        $ skill_technical += 20
        jump mechanic

    "The elementary school":
        $ skill_social += 20
        jump teacher        
