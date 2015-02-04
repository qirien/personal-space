# Script for the trailer for Our Personal Space
#

image title = "bg/title-screen.png"

label trailer:
    play music "music/Rain.ogg" fadein 1.0
    scene black with fade
    $ renpy.pause(3.0)
    scene cuttlefish with fade
    $ renpy.pause(3.0)
    scene title with fade
    $ renpy.pause(3.0)
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}a sci-fi relationship simulation\nvisual novel{/font}{/size}"
    $ renpy.pause(2.0)
    
#    scene bg city_street with fade
#    "I thought I knew what love was."    
#    show her happy at midleft 
#    with moveinleft
#    "Smiling ridiculously whenever I thought of him."
#    show him happy at midright
#    with moveinright        
#    "Counting down the minutes until we could meet again."
#    show him sleeping at center with move
#    show her sleeping with dissolve    
#    "My heart beating faster when we kissed."
    
    scene bg porch with fade
    show her surprised at midleft
    show him serious at midright
    with dissolve
    him serious "I want you to come with me to the new colony. As my wife."
    her concerned "On a new planet? So many things could go wrong..."
    him normal "And when they do, I want you by my side."
#    her happy "We'll create a new life together, on a new world..."
    
#    scene talaam_approach:
#        crop (0,0,1024,600)
#        easein 4.0 crop (884, 272, 1024, 600)
#    $ renpy.pause(4.0)
#    "And so we arrived on Talaam."
        
    scene bg talam with fade
    show her normal at midright
    show him normal at midleft
    with moveinright
    her annoyed "Why is our house so far from everyone else?"
    him happy "Look at all this space! Space to grow! Space to breathe! Space to do whatever we want!"
    her flirt "Our own personal space..."
#    scene bg farm_exterior with fade
#    show her normal at midright
#    show him normal at midleft
#    with moveinright
#    him normal "Here it is! Home, sweet home!"
#    her happy "This might actually work!"
    
    scene black with fade
    scene bg farm_interior with fade
    show him serious at midleft
    show her serious at midright    
    with dissolve
    her annoyed "It's none of your business what I do in my spare time."
    him angry "We need to think about food, clothing, shelter. We don't have time for anything else in order for the colony to survive."
#    her angry "If it's just about survival, life isn't worth living."
#    him annoyed "Well, you don't even get a choice if you don't survive. If something goes wrong, who's going to help us out here? There's no food banks, no Red Cross, no emergency rooms."
    her sad "I can't live that way..."
    show him concerned with dissolve
    
    scene black with fade
    $ is_nude = True
    scene bg bedroom with fade
    show him nude serious at midright, squatting
    show her serious at midleft, squatting
    show bedroom_covers
    show night
    with dissolve
    
    him nude concerned "I want this to work. How can I be a better husband to you?"
    menu:
        "What should I say?"
        "Tell me how much you love me.":
            her concerned "Maybe you could tell me how much you love me."
            him nude surprised "Ummm... a lot?"
            her annoyed "No! Not like that!"
            him nude normal "Hmmm, okay, let me think..."
            show her surprised with dissolve
            him nude happy "Your laugh is like a supernova that blasts away my stress and makes the whole world seem like a cosmic garden of possibilities."
        "Let's do more things together.":
            her normal "I want to do things with you more often."
            him nude surprised "What kinds of things?"
            her happy "Anything - go on walks, make dinner together, play games together."
            him nude happy "Okay, let's go fishing!"
            her surprised "Are there even any fish here?"
            him nude normal "They're more like crayfish, but let's go together, tomorrow!"
            her happy "It's a date!"
            $ she_wants = "dostuff"
        "I want you to know what I want.":
            her normal "I don't want to have to tell you what I want; you should figure it out on your own."
            him nude annoyed "With what, telepathy? I thought that's what communication was for."
            her annoyed "Well, it's not romantic if I have to tell you 'Hey, don't forget to say 'I love you'."
            him nude surprised "Okay, so you want me to say 'I love you' more often?"
            her concerned "No! I mean, that's fine, but I want you to do romantic things because you feel romantic, not because you feel like you're supposed to."
            him nude annoyed "Oooookay. I guess I'll try that, then."
            her flirt "It's not that hard; you can do it."
        
    show her happy at center, squatting with move
#    "And then he pulled me close and whispered into my hair."
#    him nude serious "I love you so much... I need to make this work. I'll do what it takes."
#    show her concerned with dissolve

    scene black with fade
    $ is_nude = False
    show text "{size=60}{font=fonts/Exo2.otf}{size=60}{font=fonts/Exo2.otf}Solve Problems at Work{/font}{/size}"
    $ renpy.pause(2.0)    
    
    scene bg machine_shop with fade
    show her normal at midright with dissolve
    show brennan at midleft with dissolve
    her annoyed "This is the third one of these radios that has broken so far! It's probably the variable resistor again..."
#    brennan mad "I know; you'd think it might have occurred to them that we can't order new parts on a whim."
#    her serious "Well, there's nothing we can do, unless..."
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Strengthen the Community{/font}{/size}"
    $ renpy.pause(2.0)   
    
    scene bg community_center with fade
    show lily at quarterleft
    show ilian at midleft
    show thuc sad at right
    show her serious at midright
    with dissolve

    lily normal "He shows great remorse over the girl's death."
    thuc "But he dumped her body in the river!"
    ilian "What do you think?"
    show her concerned with dissolve
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Explore Different Skills{/font}{/size}"
    $ renpy.pause(2.0)
    
#    scene bg hotspring with fade
#    show him normal at midleft
#    show her normal at center    
#    with moveinleft    
#    "We followed the stream up the mountain until we found a hot spring!"
    
    scene bg sunset with fade
    "I hadn't done any photography in a long time, but the way the light drifted across the empty plain really inspired me."
    
    scene bg laundry with fade
    show her serious at center with dissolve
    her concerned "It looks like it'll take at least a month to make soap from scratch..."
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Decide the Future of their Family{/font}{/size}"
    $ renpy.pause(2.0)
    
    scene bg colony_ship_bunk with fade
    show him normal at midright
    show her surprised at midleft
    with dissolve
    him surprised "So, what do you think about having kids?"
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Choose Your Own Fate{/font}{/size}"
    $ renpy.pause(2.0)
    
    scene screenshot with fade
    "Time to decide what to do this month..."
    
    scene black with fade
    show text "{size=60}{font=fonts/Exo2.otf}Will their trials break their love...{/font}{/size}"
    $ renpy.pause(2.0)
    
    $ wearing_dress = True
    scene bg farm_interior with fade
    show her annoyed at midleft
    show him annoyed at midright
    with dissolve
    him angry "You can't just let the food go to waste. I worked hard growing those tomatoes!"
    her angry "Well, I don't have time to pick them!"
    
    scene black with fade
    $ wearing_dress = False
    show text "{size=60}{font=fonts/Exo2.otf}...or refine it into something stronger?{/font}{/size}"
    $ renpy.pause(2.0)
    
    scene bg sunset with fade
    show her concerned at midright
    show him serious at midleft 
    him normal "I'm glad you came with me to build this fence; everything's better with you."
    her flirt "Tough manual labor is not so bad when we're together."
    him concerned "We will stay together, won't we? Forever?"
    show her surprised with dissolve
    $ renpy.pause(1.0)
            
#    scene bg bedroom with fade
#    $ is_nude = True
#    show him nude sleeping at midright, squatting
#    show her serious at midleft, squatting
#    show baby girl at quarterleftbaby
#    show bedroom_covers
#    show night
#    with dissolve
    
#    him nude concerned "Thank you for taking a chance on me. And for loving me even when I'm grouchy or make mistakes."
##    her concerned "You have kept loving me this whole time - through pests and fires and sicknesses and everything."
#    him nude serious "Stay with me, [her_name]..."
#    show her concerned with dissolve
##    show him nude serious at center, squatting with move
##    "We didn't say anything else. He caressed my cheek with his hand until I brought my own hand up to hold on to his."
#    show him nude sleeping at center, squatting with move
#    show her sleeping with dissolve
    
    scene title with fade
    $ is_nude = False
    $ renpy.pause(10.0)