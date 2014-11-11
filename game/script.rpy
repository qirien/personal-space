# Personal Space
# MAIN
# Declare global variables, images, characters, etc.

define mp = MultiPersistent("cuttlefishgames")

# Declare characters used by this game .
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
define her = DynamicCharacter("her_name", color="#8864d5", image="her", ctc="ctc_blink", ctc_position="nestled") #periwinkle
define him = DynamicCharacter("his_name", color="#c80000", image="him", ctc="ctc_blink", ctc_position="nestled") #red 

define naomi = Character("Sister Naomi", color="#ededed", image="naomi", ctc="ctc_blink", ctc_position="nestled")  #light gray
define pavel = Character("Mayor Grayson", color="#cccccc", image="pavel", ctc="ctc_blink", ctc_position="nestled")   #dark gray
define lily = Character("Lily", color="#8655bd", image="lily", ctc="ctc_blink", ctc_position="nestled")  #purple
define sara = Character("Sara", color="#c64e89", image="sara", ctc="ctc_blink", ctc_position="nestled")  # dark pink
define thuc = Character("Thuc Nguyen", color="a9ff22", image="thuc", ctc="ctc_blink", ctc_position="nestled")  #lime green
define ilian = Character("Ilian Andrevski", color="ffa922", image="ilian", ctc="ctc_blink", ctc_position="nestled") #tangerine
define brennan = Character("Brennan Callahan", color="33b533", image="brennan", ctc="ctc_blink", ctc_position="nestled")  #irish green
define jed = Character("Jed Engel", color="cb5500", image="jed", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
define natalia = Character("Natalia Perón", color="ffe74a", image="natalia", ctc="ctc_blink", ctc_position="nestled")  #yellow
define helen = Character("Helen Engel", color="cdcfb2", image="helen", ctc="ctc_blink", ctc_position="nestled") #tan
define julia = Character("Julia Nguyen", color="#4b54cd", image="julia", ctc="ctc_blink", ctc_position="nestled") #icy blue
define martin = Character("Martín Perón", color="#990011", image="martin", ctc="ctc_blink", ctc_position="nestled")  #dark red


define tutorial = Character("Tutorial", color="#ededed", ctc="ctc_blink", ctc_position="nestled")  #light gray
define note = Character("note", kind=nvl)

# defaults used for debugging purposes
define his_name = "Jack"
define her_name = "Kelly"
define his_nickname = "dear"
define her_nickname = "lover"


# Variables about emotional state.  -100 is minimum, 100 is maximum
# TODO: might need to normalize these, set as stats, so we can use bars for them.  Maybe 0 to 100?
define relaxed = 0    # negative = stressed
define loved = 0      # negative = neglected
define made_love = 0  # Counter of lovemaking, used for pregnancy calculation
define community_level = 0 # how successful is the colony?

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
    define save_name = "Intro"

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
    
    define COMMUNITY_LEVEL_OK = 30
    define COMMUNITY_LEVEL_GOOD = 50
    define COMMUNITY_LEVEL_MAX = 60    
    define LOVED_GOOD = 40
    define LOVED_MAX = 60
    define SKILL_SAVED_MAX = 60

    #Technical variables used to control how the game displays
    # Custom transitions, positions, etc.
    define fade = Fade(0.2, 0.2, 0.2)
    define midleft = Position(xpos=0.20, xanchor=0)        
    define midright = Position(xpos=0.50, xanchor=0)
    define quarterleft = Position(xpos=0.10, xanchor=0)
    define quarterright = Position(xpos=0.65, xanchor=0)
    define farleft = Position(xpos=-0.30, xanchor = 0)
    define farright = Position(xpos=1.0, xanchor = 0)    
    define sitting = Position(ypos=0.5, yanchor=0)
    define squatting = Position(ypos=0.2, yanchor=0)
    

    define sans_font = "fonts/Questrial-Regular.otf"
    define serif_font = "fonts/RobotoSlab-Regular.ttf"
    
    define current_song = " "
    
init python:
    # Songs for computer pad
    pop_songs = MusicRoom(fadeout=0.5)
    pop_songs.add("music/Dandelion.ogg", always_unlocked = True)
    pop_songs.add("music/Shanghai_20_00.ogg", always_unlocked = True)
    pop_songs.add("music/Alpha.ogg", always_unlocked = True)
    pop_songs.add("music/YouUndone.ogg")

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
    # add a default dissolve transition between each say if no other transition is speficied
    $ config.say_attribute_transition = dissolve
  

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
                
            "No.":
                "OK, we will not use New Game+ data."
         
        # TODO: Make a skip and menu button to go on the dialogue box. Change this for Android?
        "To fast-forward through scenes you have already seen, hold down \"Ctrl\" or use the \"Skip\" button."

    "Do I want to remember how it all began?"
    # TODO: Remove this, or change it somehow?
    menu:
        "Do I want to remember how it all began?"
        "Yes.":
            "Of course."
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
            #show overlay computer_pad

            #jump monthly_event_25
            jump settling_in
            #jump test_positions
            #jump test_inputter
            #jump show_credits

    "I thought I knew what love was."
    "Smiling ridiculously whenever I thought of him."
    "Counting down the minutes until we could meet again."
    "My heart beating faster when we kissed."
    "That feeling of contentment when he held me in his arms."
    "That's what I thought love was...{p}I was so wrong."
    "But that's why I married him..."
    show her normal at center with moveinleft

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
    
    "I thought we were in love. That's why I married [his_name]."

    "We had known each other..."
    menu:
        "How long had we known each other?"
        "Since we were kids.":
            "We had known each other since we were kids. He pulled my hair in first grade; I chased him and tried to kiss him. Then in high school we became best friends. It wasn't until recently that we had begun to think about each other romantically."
            $ known_each_other = "since we were kids"
        "For three years.":
            "We had known each other for three years. We started out as friends, then pretty soon we were hanging out all the time, and lately we had begun to think about each other as more than friends."
            $ known_each_other = "three years"
        "For just six months.":
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
    show her normal
    "I loved how he put his whole soul into everything he did." 
    "And when he said my name... it was as if he knew everything about me and loved every bit of it."
    
    # Get the main character's ame
    if not renpy.variant('touch'):
        $ her_name = renpy.input("What is your name?", "Kelly", length=20)
    else:
        "What is your name?"
        $ text_group = 1
        $ input_text = ''
        $ input_header = 'First Name:'
        call inputter
        $ her_name = input_text or "Kelly"
        
    show him at midleft with move
    him normal "[her_name]... you're incredible. Being here with you is almost perfect."
    her flirting "Almost?"
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
    
    him serious "It's because it's grown with love."
    her flirting "Oh, you \"love\" your asparagus, do you?"
    him flirting "Of course I do. How else would I know what it needs?"
    her annoyed "And does your asparagus love you back?"
    him happy "It sure does; can't you taste it in every bite? Mmmm..."
    her flirting "That's the taste of love, huh? Asparagus?"
    him serious "That's one kind."
    her happy "There's much better kinds, you know."
    him normal "Of course. But some of those are dangerous."
    her surprised "Dangerous?"
    him concerned "You know, like blackberries and their thorns."
    her normal "Blackberries are so delicious, they're worth the thorns."
    him serious "You're right. They're so sweet, and soft...they just melt in your mouth..."
    show him normal at center with move
    "He came closer - for a kiss? I couldn't help blurting out a response."
    her flirting "Don't forget plump, sour, and just a little bit lumpy."
    show him surprised at midleft with move
    him surprised "Lumpy! I would never insult a blackberry like that. I love them just the way they are. And--"
    her surprised "And?"
    him serious "And I love you, just the way you are."
    show him normal at center with move
    "His face neared mine, and I decided this wasn't the time for more jokes."
    her happy "I love you, [his_name]. You and your silly asparagus and blackberries and everything."
    
    scene black with fade
    
    "That night we stayed up until four in the morning, mostly talking... we didn't even realize how late it was!  He stayed to watch the sunrise with me, and then headed straight to work. I felt kind of guilty that I had the day off and could sleep in."

    jump choose_career

    return

label choose_career:

    "A few days later, [his_name] came to my work at..."

menu:
    "Where do I work?"
    "The hardware store":
        jump carpenter
        
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
