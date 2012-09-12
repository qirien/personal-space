# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg stars = "starscape.png"
image him normal = "him.png"

# Declare characters used by this game .
define her = DynamicCharacter("her_name", color="#c8ffc8")
define him = DynamicCharacter("his_name", color="ff0000")


# The game starts here.
label start:

    $ her_name = renpy.input("What is your name?", "Mary", length=20)
    $ his_name = renpy.input("What is your husband's name?", "Jack", length=20)

    scene bg stars
    her "You thought you knew what love was."

    show him normal
    her "After all, that's why you married [his_name]."
    her "There's no way you could have known what the two of you would go through."
    her "This whole journey has been nothing like you could have imagined."

    return
