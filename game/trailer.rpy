# Ren'Py script for the trailer for Our Personal Space
#
# by Andrea Landaker
# Licensed under the GNU GPLv3


# Sprite images (such as "her" "him") are defined elsewhere 
# Backgrounds used in the game (such as "porch" and "talam") are also defined elsewhere
image title = "bg/title-screen.png"

label trailer:
    play music "music/LinesBuildWalls.ogg" fadein 1.0
    scene black with fade
    $ renpy.pause(1.0)
    scene title with fade
    $ renpy.pause(2.5)
    scene cuttlefish with fade
    $ renpy.pause(2.0)    
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}a sci-fi relationship simulation\nvisual novel{/font}{/size}"
    $ renpy.pause(2.0)
    
    scene bg porch with fade
    show her surprised at midleft
    show him serious at midright
    with dissolve
    him serious "I want you to come with me to the new colony. As my wife."
    her concerned "On a new planet? So many things could go wrong..."
        
    scene bg talam with fade
    show her normal at midright
    show him normal at midleft
    with moveinright
    him happy "Look at all this space! Space to grow! Space to breathe! Space to do whatever we want!"
    her flirt "Our own \"personal space\"...?"
    
    scene black with fade
    scene bg farm_interior with fade
    show him angry at midleft
    show her annoyed at midright    
    with dissolve
    him angry "We need to think about food, clothing, shelter. We don't have time for anything else in order for the colony to survive."

    scene black with fade
    $ is_nude = True
    scene bg bedroom with fade
    show him nude serious at midright, squatting
    show her serious at midleft, squatting
    show bedroom_covers
    show night
    with dissolve
    
    him nude concerned "I want this to work. How can I be a better husband to you?"   
    $ time = 2
    $ timer_range = 2
    $ timer_jump = "after_trailer_menu"        
    show screen countdown
    menu:
        "What should I say?"
        "Tell me how much you love me.":
           pass
        "Let's do more things together.":
           pass
        "I want you to know what I want.":
           pass
        

label after_trailer_menu:
    hide screen countdown
    scene black with fade
    $ is_nude = False
    show text "{size=60}{font=fonts/Exo2.otf}{size=60}{font=fonts/Exo2.otf}Solve Problems at Work{/font}{/size}"
    $ renpy.pause(1.0)    
    
    scene bg clinic with fade
    show her serious at midright
    show brennan mad at midleft
    show kid frown at quarterright
    with dissolve
    her concerned "We need to quarantine the clinic until we can get this infection under control."
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Strengthen the Community{/font}{/size}"
    $ renpy.pause(1.0)   
    
    scene bg community_center with fade
    show underwater   
    show ilian happy at quarterleft
    show sara at midleft
    show lily happy at left
    show martin at quarterright
    show natalia at right
    show her happy at center
    show raul at midright
    with dissolve

    "As people started to arrive at the party, their faces brightened and their shoulders lifted."
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Explore Different Skills{/font}{/size}"
    $ renpy.pause(1.0)
    
    scene bg sunset with fade
    "The way the light drifted across the barren plain inspired me to take a series of photographs."
    
    scene bg laundry with fade
    show her serious at center with dissolve
    her concerned "It looks like it'll take at least a month to make soap from scratch..."
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Decide the Future of their Family{/font}{/size}"
    $ renpy.pause(1.0)
    
    scene bg colony_ship_bunk with fade
    show him normal at midright
    show her surprised at midleft
    with dissolve
    him surprised "So, what do you think about having kids?"
    $ time = 2
    $ timer_range = 2
    $ timer_jump = "after_kids_menu"         
    show screen countdown
    menu:
        "What should I say?"

        # Want to have kids
        "I think we're ready.":
            her happy "I think we're ready."
        # Not sure about kids
        "I don't know.":
            her concerned "I don't know..."
        # Definitely no kids
        "That's really crazy.":
            her annoyed "That's really crazy."
            
label after_kids_menu:   
    hide screen countdown
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Choose Your Own Fate{/font}{/size}"
    $ renpy.pause(1.0)
    
    scene screenshot with fade
    "Time to decide what to do this month..."
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Will their trials break their love...{/font}{/size}"
    $ renpy.pause(1.0)
    
    $ wearing_dress = True
    scene bg farm_interior with fade
    show her annoyed at midleft
    show him angry at midright
    with dissolve
    him angry "You can't just let the food go to waste. I worked hard growing those tomatoes!"
    her yelling "Well, I don't have time to pick them!"
    
    scene black with fade
    $ wearing_dress = False
    show text "{size=60}{font=fonts/Exo2.otf}...or refine it into something stronger?{/font}{/size}"
    $ renpy.pause(1.5)
    
    scene bg farm_interior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    her happy "You've brought me love, joy, and laughter. You've even brought me to new worlds, literally!"
    show him happy with dissolve
    $ renpy.pause(1.0)
            
    scene title with fade
    $ is_nude = False
    $ renpy.pause(10.0)
    
    scene black with fade
    $ renpy.pause(1.0)
    return

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.02), false=[Hide('countdown'), Jump(timer_jump)])
      