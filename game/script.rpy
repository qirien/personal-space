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
define known_each_other = ""
define profession = ""
define father_attitude = ""
define favorite_wedding_gift = ""
define want_kids = False
define have_goat = False
define is_pregnant = False
define slacked_off = 0  #number of times slacked off at work
define has_grass = False
define met_Lily = False

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
            $ known_each_other = "six months"
            jump month01

    "I thought I knew what love was. After all, that's why I married..."
    $ his_name = renpy.input("What is his name?", "Jack", length=20)
    "After all, that's why I married [his_name]."

    show him normal at right with moveinright

    "We had known each other..."
    menu:
        "How long had we known each other?"
        "Since we were kids":
            "We had known each other since we were kids. He pulled my hair in first grade; I chased him and tried to kiss him. Then in high school we became best friends. It wasn't until recently that we had begun to think about each other romantically."
            $ known_each_other = "since we were kids"
        "For three years":
            "We had known each other for three years. We started out as friends, then pretty soon we were hanging out all the time, and lately we had begun to think about each other as more than friends."
            $ known_each_other = "three years"
        "For just six months":
            "We had known each other for just six months, but we spent almost all our free time together. Though we started out as just friends, lately there was a romantic tension that hadn't been there before."
            $ known_each_other = "six months"
    jump choose_career

    return

label choose_career:

    "One day [his_name] came to my work at..."

menu:
    "Where do I work?"
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
