# Love in Space

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg stars = "starscape.png"
image bg earth = "earth.jpg"
image him normal = "him.png"
image her normal = "her.png"

# Declare characters used by this game .
define her = DynamicCharacter("her_name", color="#c8ffc8")
define him = DynamicCharacter("his_name", color="990000")

define his_name = "???"
define her_name = "Me"
define profession = "Layabout"

# The game starts here.
label start:

    scene bg stars
    play music "void.ogg"
    show her normal at center with moveinleft

    "I thought I knew what love was."

    "After all, that's why I married..."
    $ his_name = renpy.input("What is his name?", "Jack", length=20)
    "After all, that's why I married [his_name]."

    show him normal at right with moveinright

    "There's no way I could have known what the two of us would go through."

    jump choose_career

    stop music

    return

label choose_career:
    scene bg earth with fade
    "It all started back on Earth, when I was working at..."

menu:
    "The hospital":
        jump doctor

    "The car repair shop":
        jump mechanic

    "The elementary school":
        jump teacher
