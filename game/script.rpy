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
    "...the hospital. He thought he had broken his wrist, but when we the x-rays came back it turned out it was only sprained. I could feel his eyes on me as I helped him with the sling."
    her "How did you sprain it, anyway?"
    him "You should have seen it; it was heroic. Diving through flames, rescuing small children, wrestling wolves . . ."
    her "Really?"
    him "No, I actually just fell off my horse.  A snake spooked him."
    her "A horse?"
    him "Yes, I live on a farm outside of town."
    "I didn't know what to think about that."
    jump first_date

label mechanic:
    $ profession = "Auto Mechanic"
    "...the car repair shop. His brakes weren't working right, and after I fixed them he wanted me to show him everything I'd done. At first I thought he didn't trust me, but soon I could tell he was a bit of a mechanic himself and interested in fixing things."
    jump first_date

label teacher:
    $ profession = "Teacher"
    "...the elementary school. He had come to tell the kindergartners about life on a farm..."
    jump first_date

label first_date:
    "Afterwards, he asked me if I wanted to come to a barbeque at his house that evening. I thought there was going to be a lot of people, but it ended up being just him and his parents."
    "It wasn't too awkward, though - we all pitched in to make dinner and then sat on the porch swing and talked and watched the stars come out."
    "But it wasn't until he first said my name that I knew I wanted to know more about him."
    $ her_name = renpy.input("What is your name?", "Mary", length=20)
    show him normal at right with moveinright
    him "Thank you for coming, [her_name]..."

    return
