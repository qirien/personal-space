# Love in Space
# MAIN
# Declare global variables, images, characters, etc.

# Declare images below this line, using the image statement.

# BACKGROUNDS
image bg stars = "bg/starscape.png"
image bg earth = "bg/earth.jpg"
image bg farm_exterior = "bg/farm-exterior.png"
image bg farm_interior = "bg/farm-interior.png"
image bg fields = "bg/fields.png"
image bg colony_ship_bunk = "bg/colony-ship-bunk.png"
image bg talam = "bg/talam.png"
image bg pond = "bg/pond.png"
image bg path = "bg/path.png"
image bg laundry = "bg/laundry.png"

# SPRITES
image him normal = "sprites/him.png"
image her normal = "sprites/her.png"

# Declare characters used by this game .
define her = DynamicCharacter("her_name", color="#8a00ff")
define him = DynamicCharacter("his_name", color="#ed0303")

define naomi = Character("Sister Naomi", color="#cccccc")
define boss = Character("Mayor Grayson", color="#0033dd")
define Lily = Character("Lily", color="#dddd00")
define sara = Character("Sara", color="#771199")

define his_name = "???"
define her_name = "Me"

# Variables about emotional state.  -100 is minimum, 100 is maximum
define relaxed = 0    # negative = stressed
define loved = 0      # negative = neglected
define made_love = 0  # Counter of lovemaking, used for pregnancy calculation
define community_level = 0 # how successful is the colony?

# Variables about skills.  On a scale from 0-100, how skilled is the character?  These are now defined in dse.rpy

# Variables about our characters and their relationship
define profession = ""
define father_attitude = ""
define favorite_wedding_gift = ""
define want_kids = False
define have_goat = False
define is_pregnant = False
define slacked_off = 0  #number of times slacked off at work
define has_grass = False

# The game starts here.
label start:

    scene bg stars with fade
    show her normal at center with moveinleft

    # TODO: Stronger beginning    
    menu:
        "Do I want to remember how it all began?"
        "Yes":
            "Of course."
        "No":
            $ his_name = "Jack"
            $ her_name = "Jill"
            $ profession = "doctor"
            $ want_kids = True
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
