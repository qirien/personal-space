# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg stars = "starscape.png"
image bg earth = "earth.jpg"
image him normal = "him.png"
image her normal = "her.png"

# Declare characters used by this game .
define her = DynamicCharacter("her_name", color="#c8ffc8")
define him = DynamicCharacter("his_name", color="990000")

define his_name = "Jack"
define her_name = "Mary"
define profession = "Layabout"

# The game starts here.
label start:

    scene bg stars
    play music "void.ogg"

    "I thought I knew what love was."

    show her normal at center with moveinleft

    "After all, that's why I married..."
    $ his_name = renpy.input("What is your husband's name?", "Jack", length=20)
    "After all, that's why I married [his_name]."

    show him normal at right with moveinright

    "There's no way I could have known what the two of us would go through."
    "This whole journey has been nothing like I could have imagined."

    jump choose_career

    stop music

    return

label choose_career:
    scene bg earth
    "It all started back on Earth, when I was working at..."

menu:
    "The hospital":
        jump doctor

    "The car repair shop":
        jump mechanic

    "The high school":
        jump teacher

label doctor:
    $ profession = "Doctor"
    "He had broken his arm..."
    jump first_date

label mechanic:
    $ profession = "Auto Mechanic"
    "He only needed an oil change..."
    jump first_date

label teacher:
    $ profession = "Teacher"
    "He had come to tell the kindergartners about life on a farm..."
    jump first_date

label first_date:
    "But it wasn't until he first said my name that I knew I wanted to know more about him."
    $ her_name = renpy.input("What is your name?", "Mary", length=20)
    show him normal at right with moveinright
    him "[her_name]..."

    "For our first date, we..."

    return
