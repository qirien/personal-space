# Personal Space
# MAIN
# Declare global variables, images, characters, etc.

define mp = MultiPersistent("cuttlefishgames")

# Declare characters used by this game .
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")

define her = DynamicCharacter("her_name", color="#84b766", image="her", ctc="ctc_blink", ctc_position="nestled") #light mint green
define him = DynamicCharacter("his_name", color="#bc1e0e", image="him", ctc="ctc_blink", ctc_position="nestled") #red 

define naomi = Character("Sister Naomi Grayson", color="#bf98ff", image="naomi", ctc="ctc_blink", ctc_position="nestled")  #light gray
define pavel = Character("Mayor Pavel Grayson", color="#cccccc", image="pavel", ctc="ctc_blink", ctc_position="nestled")   #dark gray
define lily = Character("Dr. Lily Kealoha", color="#6763b5", image="lily", ctc="ctc_blink", ctc_position="nestled")  #purple
define sara = Character("Sara Hill-Andrevski", color="#e25057", image="sara", ctc="ctc_blink", ctc_position="nestled")  # salmon pink
define thuc = Character("Thuc Nguyen", color="#a9ff22", image="thuc", ctc="ctc_blink", ctc_position="nestled")  #lime green
define ilian = Character("Ilian Andrevski", color="#d2d099", image="ilian", ctc="ctc_blink", ctc_position="nestled") #tangerine
define brennan = Character("Brennan Callahan", color="#33b533", image="brennan", ctc="ctc_blink", ctc_position="nestled")  #irish green
define pete = Character("Pete Jennings", color="#ee7755", image="pete", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
define natalia = Character("Natalia Perón", color="#f3ca14", image="natalia", ctc="ctc_blink", ctc_position="nestled")  #yellow
define helen = Character("Helen Jennings", color="#77b8ef", image="helen", ctc="ctc_blink", ctc_position="nestled") #icy gray
define julia = Character("Julia Nguyen", color="#e7b1cb", image="julia", ctc="ctc_blink", ctc_position="nestled") #icy blue
define martin = Character("Martín Perón", color="#9b5b1d", image="martin", ctc="ctc_blink", ctc_position="nestled")  #dark red

define van = Character("Van Nguyen", color="#7788fc", image="van", ctc="ctc_blink", ctc_position="nestled")
define kid = Character("Kid", color="#7788fc", image="kid", ctc="ctc_blink", ctc_position="nestled")


define tutorial = Character("Tutorial", color="#ededed", ctc="ctc_blink", ctc_position="nestled")  #light gray
define note = Character("note", kind=nvl, ctc="ctc_blink", ctc_position="nestled")

# defaults used for debugging purposes
define his_name = "Jack"
define her_name = "Kelly"
define his_nickname = "dear"
define her_nickname = "lover"


# Variables about emotional state.  -100 is minimum, 100 is maximum
define relaxed = 0    # negative = stressed
define loved = 0      # negative = neglected
define made_love = 0  # Counter of lovemaking, used for pregnancy calculation
define community_level = 0 # how successful is the colony?

# This definition needs to happen before our transitions are defined    
init -201 python:
    define.move_transitions('longmove', 1.5)
    define.move_transitions('move', 0.5) # TODO: test this; moves were way too short before, but we don't want them too long.
    

# Variables about skills.  On a scale from 0-100, how skilled is the character?
# These are now defined in dse.rpy

# Variables about our characters and their relationship
# Variables that need to be initialized before anything else
init -200:
    define month = 0
    define local_month = 0
    define year = 1
    define earth_year = 1
    define earth_month = 0
    define save_name = "Intro" #name for the saved game

    define known_each_other = ""
    define profession = ""
    define father_attitude = ""
    define favorite_wedding_gift = ""
    define want_kids = False
    define have_goat = False
    define is_pregnant = False
    define is_pregnant_later = False
    define wearing_dress = False
    define is_nude = False
    define slacked_off = 0  #number of times slacked off at work
    define has_grass = False
    define met_Lily = False
    define times_worked = 1
    define he_hunts = False
    define brennan_relationship = 0
    define trimester = "None"
    define season = "spring"
    define weather = "calm and cool"
    define cheated_on_him = False
    define exposed_brennan = False
    define discovered_qec = False
    define ocean_character = ""
    define wants_to_leave = False
    define hated_food = "turnips"
    define baby_name = "Terra"
    
    define COMMUNITY_LEVEL_OK = 40
    define COMMUNITY_LEVEL_GOOD = 55
    define COMMUNITY_LEVEL_MAX = 70
    define LOVED_GOOD = 40
    define LOVED_MAX = 70
    define SKILL_SAVED_MAX = 60
    define ending = "none"

    #Technical variables used to control how the game displays
    # Custom transitions, positions, etc.
    define fade = Fade(0.2, 0.2, 0.2)
    define midleft = Position(xpos=0.20, xanchor=0)        
    define midright = Position(xpos=0.50, xanchor=0)
    define quarterleft = Position(xpos=0.10, xanchor=0)
    define quarterright = Position(xpos=0.65, xanchor=0)
    define farleft = Position(xpos=-0.30, xanchor=0)
    define farright = Position(xpos=1.0, xanchor=0)    
    define sitting = Position(ypos=0.45, yanchor=0)
    define squatting = Position(ypos=0.25, yanchor=0)
    
    define rightbaby = Position(xpos=830, ypos=430)
    define quarterrightbaby = Position(xpos=750, ypos=430)
    define midrightbaby = Position(xpos=600, ypos=430)    
    define centerbaby = Position(xpos=520, ypos=430)
    define midleftbaby = Position(xpos=400, ypos=430)  
    define quarterleftbaby = Position(xpos=200, ypos=430)
    define leftbaby = Position(xpos=0, ypos=430)
    
    define sans_font = "fonts/Questrial-Regular.otf"
    define serif_font = "fonts/RobotoSlab-Regular.ttf"
    
    define current_song = " "
    define read_messages = False
    
    # TODO: Remove ones we are not using anywhere, fix for credits
    transform rising:
        ypos 1.2 yanchor 1.0
        linear 6.0 ypos 1.0
        
    transform babyrising:
        ypos 1.2 yanchor 1.0 yoffset -160
        linear 6.0 ypos 1.0
        
    transform slowalpha:
        alpha 0
        linear 3.0 alpha 0.9
    
init python:
    # Songs for computer pad
    pop_songs = MusicRoom(fadeout=0)
    pop_songs.add("music/Dandelion.ogg", always_unlocked = True)
    pop_songs.add("music/Shanghai_20_00.ogg", always_unlocked = True)
    pop_songs.add("music/Alpha.ogg", always_unlocked = True)
    pop_songs.add("music/YouUndone.ogg")

    renpy.music.register_channel("bg_sfx", mixer="sfx", loop=False, tight=True)

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

    scene bg stars with fade

    if (persistent.times_beaten):
        menu:
            "New Game+ data found. Do you want to use New Game+ data to start skills at the highest achieved levels?"
            "Yes.":
                "OK, initializing stats to previous levels, to a maximum of [SKILL_SAVED_MAX]."
                $ skill_domestic = persistent.skill_domestic
                $ skill_creative = persistent.skill_creative
                $ skill_technical = persistent.skill_technical
                $ skill_spiritual = persistent.skill_spiritual
                $ skill_social = persistent.skill_social
                $ skill_knowledge = persistent.skill_knowledge
                $ skill_physical = persistent.skill_physical                
                show screen skill_screen()
                "Initialized."
                hide screen skill_screen
            "No.":
                "OK, we will not use New Game+ data."
         
        if not renpy.variant('touch'):
            "To fast-forward through scenes you have already seen, hold down \"Ctrl\" or use the \"Skip\" option in the Config screen."
        else:
            "To fast-forward through scenes you have already seen, use the \"Skip\" option in the Config menu."

    if (config.developer):
        "Do I want to remember how it all began?"
        menu:
            "Do I want to remember how it all began?"
            "Yes.":
                "Of course."
                jump intro
            "No.":
                $ his_name = "Jack"
                $ her_name = "Kelly"
                $ profession = "mechanic"
                $ want_kids = True
                $ known_each_other = "six months"
                jump month01
            "Skip to Debug Point":
                $ his_name = "Jack"
                $ her_name = "Kelly"
                $ profession = "teacher"
                $ community_level = 25
                $ loved = 40
                $ exposed_brennan = True
                $ skill_knowledge = 100
                $ skill_technical = 40
                $ skill_domestic = 100
                $ want_kids = True
                $ is_pregnant = True
                $ known_each_other = "six months"
                #scene bg stars
                #show computer_pad

                #jump monthly_event_25
                #jump test_her_sprites
                #jump test_positions
                jump test_inputter
                #jump show_credits
    
    jump intro

label test_inputter:
    "What is your pet's name?"
    $ input_text = renpy.input("Pet's Name:")
    $ pet_name = input_text or "Fido"
    "You picked the name [pet_name]."
    return

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
    
    