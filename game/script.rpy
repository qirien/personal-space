# Personal Space
# MAIN
# Declare global variables, images, characters, etc.

# Declare images below this line, using the image statement.

# BACKGROUNDS
image bg stars = "bg/starscape.jpg"
image bg earth = "bg/earth.jpg"
image bg farm_exterior = "bg/farm-exterior.jpg"
image bg porch = "bg/farm-porch.jpg"
image bg wedding = "bg/wedding.jpg"
image bg farm_interior = "bg/farm-interior.jpg"
image bg fields = "bg/fields.jpg"
image bg colony_ship_bunk = "bg/colony-ship-bunk.jpg"
image bg talam = "bg/talam.jpg"
image bg pond = "bg/pond.jpg"
image bg path = "bg/path.jpg"
image bg laundry = "bg/laundry.jpg"
image bg library = "bg/library.jpg"
image bg classroom = "bg/classroom.jpg"
image bg clinic = "bg/clinic.jpg"
image bg bedroom = "bg/bedroom.jpg"
image bg sunset = "bg/sunset.jpg"
image bg machine_shop = "bg/machine-shop.jpg"
image bg workshop = "bg/workshop.jpg"
image bg ocean = "bg/ocean.jpg"
image bg storehouse = "bg/storehouse.jpg"
image bg community_center = "bg/community-center.jpg"
image overlay night = "bg/night.png"

# Declare characters used by this game .
define her = DynamicCharacter("her_name", color="#7264d5", image="her")
define him = DynamicCharacter("his_name", color="#c80000", image="him")

define naomi = Character("Sister Naomi", color="#6500ab")
define boss = Character("Mayor Grayson", color="#cccccc")
define lily = Character("Lily", color="#ffe74a")
define sara = Character("Sara", color="#c64e89")
define thuc = Character("Thuc Nguyen", color="a9ff22")
define ilian = Character("Ilian Andrevski", color="ffa922")
define brennan = Character("Brennan Callahan", color="11ee11")
define sven = Character("Sven Engel")
define natalia = Character("Natalia Peron")
define helen = Character("Helen Engel")

# SPRITES

# Him
image him normal = "sprites/him.png"
image him angry = "sprites/him-angry.png"
image him annoyed = "sprites/him-annoyed.png"
image him concerned = "sprites/him-concerned.png"
image him flirt = "sprites/him-flirt.png"
image him happy = "sprites/him-happy.png"
image him laughing = "sprites/him-happy.png"
image him sad = "sprites/him-sad.png"
image him surprised = "sprites/him-surprised.png"

# Her
image her normal = "sprites/her.png"
image her normal flip = im.Flip("sprites/her.png", horizontal = True)
image side her normal = "sprites/her-head.png"
# TODO: Fix angry, annoyed, flirt when they are done.
image her angry = "sprites/her-angry.png"
image her annoyed = "sprites/her-annoyed.png"
image her concerned = "sprites/her-concerned.png"
image side her concerned = "sprites/her-concerned-head.png"
image her flirt = "sprites/her-flirt.png"
image her happy = "sprites/her-happy.png"
image her laughing = "sprites/her-laughing.png"
image her sad = "sprites/her-sad.png"
image her surprised = "sprites/her-surprised.png"


# Other Characters
image female_child = "sprites/female-child.png"
image brennan = "sprites/brennan.png"

define his_name = "???"
define her_name = "Me"
define his_nickname = "dear"
define her_nickname = "lover"

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
define times_worked = 1
define he_hunts = False
define brennan_relationship = 0
define cheated_on_him = False
define exposed_brennan = False
define ocean_character = ""

#Technical variables used to control how the game displays
define fade = Fade(0.2, 0.2, 0.2)

# The game starts here.
label start:
    # Custom transitions, positions, etc.
    $ midleft = Position(xpos=0.30,
        xanchor=0)
    $ midright = Position(xpos=0.50,
        xanchor=0)
    $ quarterleft = Position(xpos=0.20,
        xanchor=0)
    $ quarterright = Position(xpos=0.60,
        xanchor=0)

    $ config.say_attribute_transition = dissolve


    scene bg stars with fade
    show her normal at center with moveinleft

    her normal "Do I want to remember how it all began?"
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

    show him normal at quarterright with moveinright

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
