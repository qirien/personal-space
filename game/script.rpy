# Personal Space
# MAIN
# Declare global variables, images, characters, etc.

init:
    define mp = MultiPersistent("MetasepiaGames")
    
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

    # TODO: Add this once we know what it is
    define config.steam_appid = 1703600
    
    # defaults used for debugging purposes
    default his_name = "Jack"
    default her_name = "Kelly"
    default his_nickname = "dear"
    default her_nickname = "lover"
    
    
    # Variables about emotional state.  -100 is minimum, 100 is maximum
    default relaxed = 0    # negative = stressed
    default loved = 0      # negative = neglected
    default made_love = 0  # Counter of lovemaking, used for pregnancy calculation
    default community_level = 0 # how successful is the colony?

# This definition needs to happen before our transitions are defined    
init -201 python:
    define.move_transitions('longmove', 1.5)
    define.move_transitions('move', 0.5)
    
# Variables about skills.  On a scale from 0-100, how skilled is the character?
# These are now defined in dse.rpy

# Constant variables
init -200:
    define COMMUNITY_LEVEL_OK = 40
    define COMMUNITY_LEVEL_GOOD = 60
    define COMMUNITY_LEVEL_MAX = 75
    define LOVED_GOOD = 35
    define LOVED_MAX = 75
    define SKILL_SAVED_MAX = 60
    define ending = "none"

    #Technical variables used to control how the game displays
    # Custom transitions, positions, etc.
    define fade = Fade(0.2, 0.2, 0.2)
    define midleft = Position(xpos=0.35, xanchor=0.5)        
    define midright = Position(xpos=0.65, xanchor=0.5)
    define quarterleft = Position(xpos=0.22, xanchor=0.5)
    define quarterright = Position(xpos=0.78, xanchor=0.5)
    define farleft = Position(xpos=-0.30, xanchor=0)
    define farright = Position(xpos=1.0, xanchor=0)    
    define sitting = Position(ypos=0.45, yanchor=0)
    define squatting = Position(ypos=0.25, yanchor=0)
    define standing = Position(ypos= 1.0, yanchor = 1.0)
    
    define rightbaby = Position(xpos=1.0, xanchor=1.0, ypos=430)
    define quarterrightbaby = Position(xpos=0.78, xanchor=0.5, ypos=430)
    define midrightbaby = Position(xpos=0.65, xanchor=0.5, ypos=430)    
    define centerbaby = Position(xpos=0.5, xanchor=0.5, ypos=430)
    define midleftbaby = Position(xpos=0.35, xanchor=0.5, ypos=430)  
    define quarterleftbaby = Position(xpos=0.22, xanchor=0.5, ypos=430)
    define leftbaby = Position(xpos=0, xanchor=0.0, ypos=430)
    
    define sans_font = "fonts/Questrial-Regular.otf"
    define serif_font = "fonts/RobotoSlab-Regular.ttf"
    
    define current_song = " "
    define song_to_play = None
    define read_messages = False
    
    transform rising:
        ypos 1.2 yanchor 1.0
        linear 6.0 ypos 1.0
        
    transform babyrising:
        ypos 1.2 yanchor 1.0 yoffset -160
        linear 6.0 ypos 1.0
        
    define SKILL_MUSIC = "music/OceansApart.ogg"
    define WORK_MUSIC = "music/Isaiah.ogg"
    define RELAX_ALONE_MUSIC = "music/Will.ogg"
    define RELAX_TOGETHER_MUSIC = "music/Reflections.ogg"
    define EVENT_MUSIC = "music/RainSea.ogg"
    
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
    with Pause(0.5)

    show cuttlefish with dissolve
    with Pause(1)
    
    scene black
    with Pause(0.5)

    return
    

#    
# START
#
label start:  
    # Initializing Variables
    # Variables about our characters and their relationship
    default month = 0
    default local_month = 0
    default year = 1
    default earth_year = 1
    default earth_month = 0
    default save_name = "Intro" #name for the saved game

    default known_each_other = ""
    default profession = ""
    default father_attitude = ""
    default favorite_wedding_gift = ""
    default want_kids = False
    default have_goat = False
    default is_pregnant = False
    default is_pregnant_later = False
    default wearing_dress = False
    default is_nude = False
    default slacked_off = 0  #number of times slacked off at work
    default has_grass = False
    default times_worked = 1
    default he_hunts = False
    default brennan_relationship = 0
    default trimester = "None"
    default season = "spring"
    default weather = "calm and cool"
    default cheated_on_him = False
    default exposed_brennan = False
    default discovered_qec = False
    default ocean_character = ""
    default wants_to_leave = False
    default hated_food = "turnips"
    default baby_name = "Terra"
    default notified_stat_max = False    

    default skill_domestic = 0
    default skill_creative = 0
    default skill_technical = 0
    default skill_spiritual = 0
    default skill_social = 0
    default skill_knowledge = 0
    default skill_physical = 0

    $ achievement.register("Separation")
    $ achievement.register("Making it Work")
    $ achievement.register("Love Grows")    
    $ achievement.register("Oh Baby")
    $ achievement.sync()
    
    
    scene bg stars with fade

    if (persistent.times_beaten):
        # Check for achievements someone should have received previously and grant them.
        if (persistent.got_bad_ending):
            $ achievement.grant("Separation")
        if (persistent.got_mediocre_ending):
            $ achievement.grant("Making it Work")
        if (persistent.got_good_ending):
            $ achievement.grant("Love Grows")
        $ achievement.sync()
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
            "To fast-forward through scenes you have already seen, hold down \"Ctrl\" or use the new \"Skip\" button on the far right."
        else:
            "To fast-forward through scenes you have already seen, use the new \"Skip\" button to the right."
    
    jump intro

label test_inputter:
    "What is your pet's name?"
    $ input_text = renpy.input("Pet's Name:")
    $ pet_name = input_text or "Fido"
    "You picked the name [pet_name]."
    return

label test_positions:
    scene bg farm_interior
    with fade
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
    show brennan at quarterright
    "right"
    show natalia at right
    "end test positions 1"
    
    scene bg farm_exterior
    with fade
    show him normal at quarterright
    show her normal at quarterleft
    with dissolve
    her surprised "Why am I in the center of the screen?"
    him flirting "You probably just want to be near me."
    "end test positions 2"
    "OK? Test positions forever!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    "Takes forever"
    return
    
    