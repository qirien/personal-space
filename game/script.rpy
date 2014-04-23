# Personal Space
# MAIN
# Declare global variables, images, characters, etc.

# Declare images below this line, using the image statement.

# BACKGROUNDS
image cuttlefish = "bg/cuttlefish-logo.png"
image bg stars = "bg/starscape.jpg"
image bg earth = "bg/earth.jpg"
image bg farm_exterior = "bg/farm-exterior.jpg"
image bg farm_exterior flip = im.Flip("bg/farm-exterior.jpg", horizontal = True)
image bg farm_exterior flip burned = "bg/farm-exterior-burned.jpg"
image bg porch = "bg/farm-porch.jpg"
image bg wedding = "bg/wedding.jpg"
image bg farm_interior = "bg/farm-interior.jpg"
image bg farm_interior flip = im.Flip("bg/farm-interior.jpg", horizontal = True)
image bg fields = "bg/fields.jpg"
image bg fields flip = im.Flip("bg/fields.jpg", horizontal = True)
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
image bg lab = "bg/lab.jpg"
image bg barn = "bg/barn.jpg"
image bg mountains = "bg/mountains.jpg"
image bg stream = "bg/stream.jpg"
image bg hotspring = "bg/hot-spring.jpg"
image bg tractor = "bg/tractor.jpg"
image bg church = "bg/church.jpg"
image bg city_street = "bg/city-street.jpg"
image bg bathhouse = "bg/bathhouse.jpg"
image overlay night = "bg/night.png"
image overlay bathhouse = "bg/bathhouse-overlay.png"

# Declare characters used by this game .
define her = DynamicCharacter("her_name", color="#7264d5", image="her") #periwinkle
define him = DynamicCharacter("his_name", color="#c80000", image="him") #red 

define naomi = Character("Sister Naomi Grayson", color="#ededed", image="naomi")  #light gray
define boss = Character("Mayor Grayson", color="#cccccc", image="pavel")   #dark gray
define lily = Character("Lily", color="#8655bd", image="lily")  #purple
define sara = Character("Sara", color="#c64e89", image="sara")  # dark pink
define thuc = Character("Thuc Nguyen", color="a9ff22", image="thuc")  #lime green
define ilian = Character("Ilian Andrevski", color="ffa922", image="ilian") #tangerine
define brennan = Character("Brennan Callahan", color="33b533", image="brennan")  #irish green
define sven = Character("Sven Engel", color="522f19", image="sven")  #brown
define natalia = Character("Natalia Peron", color="ffe74a", image="natalia")  #yellow
define helen = Character("Helen Engel", color="cdcfb2", image="helen") #tan
define julia = Character("Julia Nguyen", color="#4b54cd", image="julia") #icy blue
define martin = Character("Martin Peron", color="#990011", image="martin")  #dark red
# TODO: add accent on Martin (also Peron?)

define note = Character("", kind=nvl)
define computer = Character("", kind=nvl)

# SPRITES

# Him
image him normal = "sprites/him.png"
image him angry = "sprites/him-angry.png"
image him annoyed = "sprites/him-annoyed.png"
image him concerned = "sprites/him-concerned.png"
image him flirting = "sprites/him-flirt.png"
image him happy = "sprites/him-happy.png"
image him laughing = "sprites/him-happy.png"
image him sad = "sprites/him-sad.png"
image him surprised = "sprites/him-surprised.png"
image him serious = "sprites/him-serious.png"
image him sleeping = "sprites/him-sleeping.png"

# Her
image her normal = "sprites/her.png"
image her normal flip = im.Flip("sprites/her.png", horizontal = True)
#image side her normal = "sprites/her-head.png"
# TODO: Fix angry, annoyed, flirting, serious,sleeping when they are done.
image her angry = "sprites/her-angry.png"
image her annoyed = "sprites/her-annoyed.png"
image her concerned = "sprites/her-concerned.png"
#image side her concerned = "sprites/her-concerned-head.png"
image her flirting = "sprites/her-flirt.png"
image her happy = "sprites/her-happy.png"
image her laughing = "sprites/her-laughing.png"
image her sad = "sprites/her-sad.png"
image her surprised = "sprites/her-surprised.png"
image her serious = "sprites/her-serious.png"
image her sleeping = "sprites/her-sleeping.png"

# Other Characters
image female_child = "sprites/female-child.png"
image sara = "sprites/sara.png"
image pavel = "sprites/pavel.png"
image thuc = "sprites/thuc.png"
image natalia = "sprites/natalia.png"
image julia = "sprites/julia.png"
image brennan = "sprites/brennan.png"
image lily = "sprites/lily.png"
image naomi = "sprites/naomi.png"
image sven = "sprites/sven.png"
image helen = "sprites/helen.png"
image ilian = "sprites/ilian.png"
image martin = "sprites/martin.png"
image kid = "sprites/kid.png"

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

# Variables that need to be initialized before anything else
init -200:
    define month = 0

    define known_each_other = ""
    define profession = ""
    define father_attitude = ""
    define favorite_wedding_gift = ""
    define want_kids = False
    define have_goat = False
    define is_pregnant = False
    define is_pregnant_later = False
    define slacked_off = 0  #number of times slacked off at work
    define has_grass = False
    define met_Lily = False
    define times_worked = 1
    define he_hunts = False
    define brennan_relationship = 0
    define cheated_on_him = False
    define exposed_brennan = False
    define discovered_qec = False
    define ocean_character = ""
    define wants_to_leave = False
    define hated_food = "turnips"
    define baby_name = "Terra"
    
    define COMMUNITY_LEVEL_OK = 30
    define COMMUNITY_LEVEL_GOOD = 50
    define LOVED_GOOD = 30

#Technical variables used to control how the game displays
    define fade = Fade(0.2, 0.2, 0.2)

# Splashscreen before the main menu
label splashscreen:
    scene black
    with Pause(1)

    show cuttlefish with dissolve
    with Pause(2)

    scene black
    with Pause(1)

    return
    

# The game starts here.
label start:
    # Custom transitions, positions, etc.
    $ midleft = Position(xpos=0.20,
        xanchor=0)
    $ midright = Position(xpos=0.50,
        xanchor=0)
    $ quarterleft = Position(xpos=0.10,
        xanchor=0)
    $ quarterright = Position(xpos=0.65,
        xanchor=0)
    $ sitting = Position(ypos=0.5, yanchor=0)
    $ squatting = Position(ypos=0.2, yanchor=0)

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
            $ profession = "mechanic"
            $ want_kids = True
            $ known_each_other = "six months"
            jump month01
        "Skip to Debug Point":
            $ his_name = "Jack"
            $ her_name = "Jill"
            $ profession = "teacher"
            $ community_level = 25
            $ loved = 60
            $ exposed_brennan = True
            $ skill_knowledge = 100
            $ skill_domestic = 100
            $ want_kids = True
            $ is_pregnant = True
            $ known_each_other = "six months"

            #jump test_positions
            jump test_inputter
            #call screen computer_pad

    "I thought I knew what love was. After all, that's why I married..."
    show him normal at quarterright with moveinright
    
    # Get his name
    if not renpy.variant('touch'):
        $ his_name = renpy.input("What is his name?", "Jack", length=20)
    else:
        "What is his name?"
        $ text_group = 1
        $ input_text = ''
        $ input_header = 'First Name:'
        call inputter
        $ his_name = input_text or "Jack"
    
    "After all, that's why I married [his_name]."

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

    scene bg city_street with fade
    
    show her normal at midright with dissolve
    show him normal at quarterleft with moveinleft
    "After working hard on his parents' farm all day, he'd take a shower and meet me at the cafe near my work. We'd get something to drink, and I'd tell him about work, or the latest book I was reading, or a video game he might like."
    "He would tell me about what was going on on the farm - it was cute how serious he got about everything."
    him concerned "I can tell Mathilda's in a lot of pain - she's been hobbling around, and she doesn't want to eat anything. But she still walks over and says hello to me whenever she sees me."
    her surprised "Is Mathilda your aunt?"
    him laughing "No, she's one of the horses!"
    show her laughing
    "I loved the way he said my name... as if he knew everything about me and loved every bit of it."
    
    # Get the main character's ame
    if not renpy.variant('touch'):
        $ her_name = renpy.input("What is your name?", "Mary", length=20)
    else:
        "What is your name?"
        $ text_group = 1
        $ input_text = ''
        $ input_header = 'First Name:'
        call inputter
        $ her_name = input_text or "Mary"
        
    show him at midleft with move
    him normal "[her_name], you're incredible. But..."
    her concerned "But?"
    him annoyed "This little town is driving me insane! I've lived here my whole life!"
    her surprised "You want to move?"
    him serious "Someday. Think about how much of the world there is out there."
    him happy "Forget the world, there's so much of the {b}universe{/b} out there!"
    her normal "Yeah, I'd love to see it..."
    show him concerned
    her concerned "Someday."
    "Neither of us had enough money to seriously consider moving. I was still paying off my school debts, and he said his family was lucky to have enough income from the farm to repair their equipment every year."
    "But we made sure to see each other, even if we didn't have the money to do anything big and exciting yet."
    scene bg porch with fade
    show him normal at midleft with dissolve
    show her normal at midright with moveinright
    "Sometimes he'd invite me over for dinner and cook up some fresh vegetables from the farm."
    her surprised "You grew these?"
    him happy "Yeah! Well, my family and I did, anyway."
    him concerned "Do you like them?"
    her happy "Of course! I didn't even know asparagus could taste this good!"
    him flirting "Well, part of that's my secret ingredient."
    her flirting "What is it? Butter? Paprika? MSG?"
    him normal "Nope. It's lots and lots of love."
    her laughing "Ha ha ha..."
    him serious "..."
    her surprised "... Are you serious?"
    him flirting "Maybe..."

    "That night we stayed up until three in the morning, just talking... we didn't even realize how late it was!  He stayed to watch the sunrise with me, and then headed straight to work. I felt kind of guilty that I had the day off and could sleep in."

    jump choose_career

    return

label choose_career:

    "One day [his_name] came to my work at..."

menu:
    "Where do I work?"
    "The craft store":
        jump crafter
        
    "The hospital":
        jump doctor

    "The car repair shop":
        jump mechanic

    "The elementary school":
        jump teacher        

label test_inputter:
    "What is your pet's name?"
    $ style.button_text.size = "+4"
    $ style.button_text.font = "Times New Roman.ttf"
    $ text_group = 1
    $ input_text = ''
    $ input_header = 'Pet\'s Name:'
    call inputter
    $ pet_name = input_text or "Fido"
    "You picked the name [pet_name]."

label test_positions:
    "left"
    show her normal at left
    "quarterleft"
    show him normal at quarterleft
    "midleft"
    show pavel at midleft, behind sara
    "center"
    show sara at center
    "midright"
    show lily at midright
    "quarterright"
    show him at quarterright
    "right"
    show her at right
    "end test positions"
    return
    
    
########################################################
#   Android keyboard input stuff, adapted from: http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=14985
init python:
    text_list1=["Q","W","E","R","T","Y","U","I","O","P","0",
                      "A","S","D","F","G","H","J","K","L","0",
                      "Z","X","C","V","B","N","M","0"]
    text_list2=["q","w","e","r","t","y","u","i","o","p","0",
                      "a","s","d","f","g","h","j","k","l","0",
                      "z","x","c","v","b","n","m","0"]
    input_text = ''
    input_header = 'NAME:'
    text_limit = 16
    text_list=text_list1
    text_group=1
    initial_caps=True
   
########################################################
#   More android keyboard input stuff, adapted from: http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=14985

label inputter:
    if initial_caps:
        $ text_group = 1
        $ initial_caps = False
    if text_group==1:
        $text_list=text_list1
    elif text_group==2:
        $text_list=text_list2
         
    $ ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0, xminimum=450)
    $ ui.vbox()
    $ ui.text(input_header+" "+input_text)
    $ ui.null(height=30)

    $ ui.hbox()
    $ ui.textbutton("Done", clicked=ui.returns("Done"))
    $ ui.textbutton("Backspace", clicked=ui.returns("Backspace"))
    $ ui.textbutton("Delete all", clicked=ui.returns("Deleteall"))
    if text_group==1:
        $ ui.textbutton("Caps (On)", clicked=ui.returns("lowercase"))
    elif text_group==2:
        $ ui.textbutton("Caps (Off)", clicked=ui.returns("uppercase"))
    $ ui.close()

    $ ui.null(height=10)

    $ ui.hbox(xalign= 0.5)
    python:
        for text_code in text_list:
            if text_code=="0":
                ui.close()
                ui.hbox(xalign= 0.5)
            elif  len(input_text)<=text_limit-1:
                ui.textbutton(text_code, clicked=ui.returns(text_code))
    $ ui.close()
    $ ui.close()
    $ button_selection=ui.interact()
               
    if button_selection=="Backspace":
        $ input_text=input_text[:-1]
        jump inputter
    elif button_selection=="Deleteall":
        $ input_text=''
        $ initial_caps = True
        $ ui.returns("uppercase")
        jump inputter
    elif button_selection=="uppercase":
        $text_group=1
        jump inputter
    elif button_selection=="lowercase":
        $text_group=2
        jump inputter
    elif button_selection=="Done":
        return
    $ select_text=button_selection

    python:
        initial_caps = False
        text_group = 2
        for text_code in text_list:
            if select_text==text_code:
                input_text += text_code
    jump inputter    
