# Afternoon Events
# Technical

# Intro Event and the default
label technical_0:
    "I tuned up some of the farm equipment."
    $ skill_technical += 10

    return

label technical_1:
    "I installed an antenna on the roof so that we can communicate with the town better. It took some trial and error to figure out the exact alignment and height, since this planet's atmosphere and shape are different from Earth's, but it's working with the radios pretty well."
    $ skill_technical += 10
    return

label technical_2:
    "Even though we have a solar panel to run our pad computers, the lights, and a few other things, we do most work the old-fashioned way, without electricity."
    "And did I mention there's no running water? We have a well and a pump, but we're always fetching water with buckets...Well, mostly I fetch water with buckets, since [his_name] has a bunch of pipes and canals setup for watering the farm."
    scene bg farm_interior with fade
    her "Washing dishes by hand is bad enough, but to also have to fetch and heat the water? There's got to be a better way..."
    him "Here, I'll do the dishes tonight."
    her "No, it's my turn, I'll just do it."
    him "No, really. I'll do the dishes, and while I'm washing them, maybe you can think of a better system that would make it easier."
    her "That...is a really good idea."
    "I got out my pad and started sketching some ideas. What could we use for pipes? How could I pump the water out of the well automatically? I did some research on early plumbing systems."
    "[his_name] did the dishes every night for a week while I worked on the plans, and then we spent a day together building it."
    her "OK, so if we turn this crank here, that turns the screw that pulls up the water. Try it!"
    him "Nothing's happening."
    her "Be patient! Keep turning!"
    him "I will...I trust you."
    "The cold trickle was nothing like a faucet of instant hot water like on Earth, but it was much better than running out to the well all the time!"
    
    $ skill_technical += 10

    return

# setup alarm system for solar flares. see http://www.spaceweather.com/glossary/srs.html for information on solar flare radiation storms. Help with technical details appreciated.
label technical_3:
    "We knew that solar flares were probably happening, since our electronics were sometimes unreliable, but we didn't know when they were."
    her "If I adjust this radio to receive AM signals, it can tell me when frequency gets around 20 mHz, which would indicate a solar flare is on its way."
    her "I can attach it to a beeper, so when I hear it I'll have about 13 minutes to assess the size of the flares and take down the solar panels if necessary."
    "I tested my solar flare detector that week. It worked for two of the bigger flares, but the beeper wouldn't stop until the flare was over."
    "There must be some way to make this work."
    menu:
        "Search the local database for a solution":
            "The wireless was down because of the most recent solar flare, but I was able to download a circuitry manual at the library. I learned about a multivibrator, or one-shot circuit that would only make the buzzer beep once."
            "I had to borrow a few more circuits while I was at the library, and while I was there I told Sven about my project."
            Sven "We're working on an intercom system with metal tubes, which wouldn't be affected by the solar flares. When I'm done could we use your flare sensor to tell everyone when to take cover?"
            menu:
                "Of course.":
                    "It's part of my duty as a colonist to help the others. Of course I'll donate my radio."
                    $ community_level += 5
                "I'd like to keep it for myself.":
                    her "I didn't trust Sven's system to reach me out in the fields, so I told him I'd rather keep my radio."
        "Just unplug it during the rest of the flare":
            "I figured that I could keep the buzzer on until a flare occured, and then I could unplug it, checking the radio frequencies before going out again."
            
    $ skill_technical += 10
    return


label technical_4:
    scene bg laundry with fade
    #show her angry at center
    her "These clothes still aren't dry?! It's so humid here, it takes forever..."
    show her normal at center
    her "Perhaps if I could wring out more of the water before hanging them up? Hmmm"
    her "Yes! I'll need a few parts from the storehouse - wait, I should draw out the design first, so I'll know all the parts ahead of time. Some rollers, a crank, several gears..."
    hide her with dissolve
    show her normal with dissolve
    her "Why won't these two parts fit together?! Ohhh, one is imperial and one is metric! Stupid nonstandard parts!"
    "Finally, it was finished. It squeaked and rattled and if I had to do it again I would make some changes to the design, but it works."
    her "The clothes dry about 50 percent faster now."
    him "Huh? Really?"
    her "Yeah, come see what I made!"
    him "You made this?! This is so awesome!\n...\n What is it?"
    her "It's a clothes wringer! What kind of farm boy are you, anyway?"
    him "The kind that always had electricity."
    her "Oh, good idea! I could hook it up to the solar and it could crank itself on sunny days...if we could get enough torque..."
    him "Whatever you want to do, my lovely inventor."
    
    $ skill_technical += 10
    return

label technical_5:
    # put in hot water connected to solar
                                                 
    $ skill_technical += 10
    return

# scavenge electronics, etc from shuttle. Every family gets some seats from the shuttle for a couch!
label technical_6:

    $ skill_technical += 10
    return

# build a water wheel to power a grinding mechanism?
label technical_7:

    $ skill_technical += 10
    return

label technical_8:

    $ skill_technical += 10
    return

label technical_9:

    $ skill_technical += 10
    return

label technical_master:

    $ skill_technical += 10
    return
