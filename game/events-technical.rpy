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
    "It was nothing like a faucet of instant hot water like on Earth, but it was much better than running out to the well all the time!"
    
    $ skill_technical += 10

    return

label technical_3:

    $ skill_technical += 10
    return


label technical_4:

    #show her angry at center
    her "These clothes still aren't dry?! It's so humid here, it takes forever..."
    show her normal at center
    her "Perhaps if I could wring out more of the water before hanging them up? Hmmm"
    her "Yes! I'll need a few parts from the storehouse - wait, I should draw out the design first, so I'll know all the parts ahead of time. Some rollers, a crank, several gears..."
    hide her with dissolve
    show her normal with dissolve
    her "Why won't these two parts fit together?! Ohhh, one is imperial and one is metric! Stupid nonstandard parts!"
    "Finally, it was finished. It squeaked and rattled and if I had to do it again I would make some changes to the design, but it works."
    her "The clothes dry about 50% faster now."
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

label technical_6:

    $ skill_technical += 10
    return

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
