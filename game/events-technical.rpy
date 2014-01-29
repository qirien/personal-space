# Afternoon Events
# Technical

# Default Event
label technical_def:
    scene bg farm_exterior with fade
    "I tuned up some of the farm equipment."
    $ skill_technical += 5

# Intro Event
label technical_0:
    scene bg farm_exterior with fade
    "I decided to familiarize myself with all the farm equipment so that if something broke, I would be able to understand the problem quicker."
    "The tractors were an interesting biofuel/solar hybrid and were built in a very modular way so that pieces could easily be taken out and replaced, and it had a hitch on the back for attachments like plows, cutters, loaders, etc."
    "I downloaded the schematics and spent some time studying them."
    $ skill_technical += 10

    return

# Better Radio Communication
label technical_1:
    scene bg farm_exterior with fade
    "I installed an antenna on the roof so that we can communicate with the town better. It took some trial and error to figure out the exact alignment and height, since this planet's atmosphere and shape are different from Earth's, but it's working with the radios pretty well."
    $ skill_technical += 10
    return

# Build a water pump
label technical_2:
    scene bg farm_exterior with fade
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
# TODO: they would have to already have this or else everyone would be dying from radiation. Perhaps she is making a local one in case Lily's doesn't work?
label technical_3:
    scene bg farm_interior with fade
    "We knew that solar flares were probably happening, since our electronics were sometimes unreliable, but we didn't know when they were."
    her "If I adjust this radio to receive AM signals, it can tell me when the frequency indicates a solar flare is on its way."
    her "I can attach it to a beeper, so when I hear it I'll have about 13 minutes to assess the size of the flares and take down the solar panels if necessary."
    "I tested my solar flare detector that week. It worked for two of the bigger flares, but the beeper wouldn't stop until the flare was over."
    "There must be some way to make this work."
    menu:
        "Search the local database for a solution":
            "The network at our house was down because of the most recent solar flare, but I was able to download a circuitry manual at the library. I learned about a one-shot circuit that would only make the buzzer beep once."
            "I had to borrow a few more circuits while I was at the library, and while I was there I told Sven about my project."
            sven "We're working on an intercom system with metal tubes, which wouldn't be affected by the solar flares. When I'm done could we use your flare sensor to tell everyone when to take cover?"
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

# Make laundry wringer
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

# Hot water heater
label technical_5:
    scene bg farm_interior with fade
    # put in hot water connected to solar
    "One of the things I missed from Earth life was having hot water available whenever I wanted it. Of the few luxuries we enjoyed, hot water seemed like one I could improve on."
    her "I wonder if we could make our own hot water heater."
    him "Well, we don't exactly have a ton of gas or electricity to spare. But you might be able to use the sun to heat it up and then store it somewhere insulated so it doesn't take as long to heat up."
    her "I'll look into it."
    "Most water-heating designs assumed I would have access to more solar panels. I didn't, but I felt like I could at least stick a container of water in the sun to heat it. If I could make something out of metal or another material that transferred heat easily, I could get something to work."
    "I took a trip to the storeroom to see what they had."
    her "Hi Ilian. How are you today?"
    "He didn't look happy to see me."
    ilian "I have the feeling you need more materials from me."
    her "Well, yes, I was going to see if you had any pipes or sheets of metal or something."
    ilian "We don't have much left. If it's an emergency or something vital to our survival you can use it, but I'm afraid that otherwise I have to say no."
    menu:
        "It's not vital to my survival":
            her "I just wanted to build a hot water heater for my house. Do you have any ideas about what kind of material I could use that would conduct heat easily?"
            ilian "Hmm. Well, I know we're always finding new uses for these animal skeleton things."
            her "And by always finding you mean no one has thought of anything to do with them?"
            ilian "They're looking pretty good in my junk pile, if I do say so myself."
            her "I'll take a few. There has to be some way I could use them."
            "The exoskeletons varied in texture. Some parts were brittle while others were as hard as a seashell. I felt like there was no way I could make anything useful out of them."
            # do we have trees?
            "I put them aside and wondered if I could make a tank out of wood."
            her "[his_name], could you cut down a tree for me so I can make a water tank for our house?"
            him "Well, I'm not sure, but I can try. How about you come with me to help pick out a tree?"
            "We found a tree that was about the width I needed. [his_name] cut it down, and we brought it home on our wagon in pieces."
            "After the wood dried out, I hollowed it out using tools at the storehouse."
            "In the end, it just ended up being lukewarm storage for more water."
        "I'll die if I don't get what I need":
            her "It's for something really important. Can I please get two sheets of metal and some pipes?"
            ilian "What exactly is it for?"
            her "I don't have time for your questions! This is a matter of life and death!"
            ilian "Alright, alright, here you go."
            "After some careful welding, I made a tank for water with many metal arms sticking out of it to help passively heat the water."
            "I was able to put a pipe from the tank to our house, complete with a stopper that kind of leaked."
            $ community_level -= 5
    
                                                 
    $ skill_technical += 10
    return

# scavenge electronics, etc from shuttle to make blender
label technical_6:
    scene bg farm_interior with fade
    "[his_name] grew a lot of vegetables; I guess part of their farming strategy was to grow many kinds of things, so if one thing got wiped out, you still had food."
    "But I didn't always like them."
    menu:
        her "I don't care how 'super' of a food it is, I just don't like:"
        "Kale":
            $ hated_food = "kale"
        "Beets":
            $ hated_food = "beets"
        "Carrots":
            $ hated_food = "carrots"
        "Brussels sprouts":
            $ hated_food = "brussels sprouts"
    her "I just don't like [hated_food]."
    him "Sorry, it grows really well here, so we have a lot of it."
    "I had to find some way to eat it that I wouldn't hate quite so much. Something to cover up the taste?"
    "Back on Earth I would sometimes make smoothies, but we didn't have any blenders here."
    "I figured I would try to make one. At the very least, thinking about the plans would distract me while I was choking down [hated_food]."
    "I would need a lot of parts, so I headed over to the storehouse."
    ilian "I don't have any extras of these things, but if you help us dismantle some of the shuttle's electronics, you could keep some for your project."
    menu:
        "Do I want a blender that badly?"
        "Yes, I'll help him":
            her "Sure, I'll help you out."
            "We took out whole circuit boards, disconnected all the wires, and took some of the components off the boards. Soon we had a nice pile of resistors, capacitors, LEDs, motors, wires, and microchips."
        "No, thanks":
            her "No, thanks, I don't really need a blender, I guess."
            ilian "You want to make a blender?"
            her "Yeah..."
            ilian "We could use one here at the storehouse; Sven wanted to make peanut butter."
            her "Well, maybe he could help you dismantle parts, and I will see if there's enough to make two blenders."

    "I found a fan and thought I could use that for the blades of the blender. In the fuel intake there were plenty of gaskets, though it was tough to find them in the right size."
    "I even added a dial connected to some resistors that let you control the speed of the blender. The container wasn't transparent (I wasn't sure if the metal we used was even technically food-safe), but it fit on the blades okay."
    "When I tried it out, it leaked -- a lot. I sealed the leaks up and played around with the speeds to get a speed that would mix and blend without foaming or stalling."
    "Finally, I had a blender. It used so much electricity that it wouldn't run at the same time as anything else, so we had to turn off the lights when we needed to use it."
    "I didn't mind, though. I just sat back and enjoyed my [hated_food] smoothie."
    $ skill_technical += 10
    return

# build a water wheel to augment power grid
label technical_7:
    scene bg farm_exterior with fade
    "Our solar panels worked well most of the time, but sometimes it was cloudy for days and our batteries ran out. Then we had to use candles and burn wood for cooking, which made a big mess and felt wasteful."
    "I wondered if we could use the nearby river to augment our electricity sources."
    "I studied some diagrams on the internet and drew up some plans for a water wheel that would work with our river."

    scene bg storehouse with fade
    her "Do you mind if I get some more parts from the shuttle?"
    ilian "What are you making now?"
    her "A water wheel, for electricity."
    ilian "That sounds great. Can you hook it up to the storehouse?"
    her "No, it's just for our house..."
    ilian "Maybe we should all be on the same power grid..."
    her "Maybe so, but we're not right now. Besides, if we were, we'd have the same problems we do now on cloudy days, just everyone will blame their neighbors for using all the electricity."
    ilian "True. Well, if you find something you can use, go ahead - you're the only one who's shown much of an interest so far."
    her "Thanks, I will."
    
    "I rummaged around, but I couldn't find all the parts I needed. I probably could make some of them, but it would be a huge project..."
    menu:
        "What should I do?"
        "Try and build it anyway.":
            "I knew it was a lot of work, but I decided to build it anyway."
            "I scavenged what I could, and shaped the rest of the pieces out of wood."
            "Magnets were also in short supply, so I had to 'borrow' some from the store house."
            "Finally, the water turned the wheel that turned a generator. It didn't generate a ton of current, but it was steady, which is more than I could say for the solar panels."
            "It wouldn't charge the battery fast enough to keep up with the stove, but it would let it run a little longer."
            $ community_level -= 1

        "Publish the plans and let someone else build it":
            "I didn't have time to waste on that. But I put my plans on the colony website, in case anyone ever did want to build one."
            $ community_level += 1

        "{i}Spearhead a community effort to build it{/i}" if (skill_social >= 30):
            "With some help, it wouldn't be too hard to build the water wheel. I asked around, and found several people willing to help make a community water wheel that fed into the community power grid."
            "It didn't help me personally that much, but I guess if it helped the store house and clinic have more reliable electricity, that would help us all."
            $ community_level += 5
    
    $ skill_technical += 10
    return

# Help Ilian with the inventory software - build good queries, or streamline interface, etc.
label technical_8:

    $ skill_technical += 10
    return

# Setup webcams around the farm to monitor fields/(goat)
label technical_9:

    $ skill_technical += 10
    return

# 10 - write an app that uses weather data and frost prediction and knowledge of various plants to remind you when to plant/harvest crops. Also keeps track of your fields, what's been on them, and helps you rotate them efficiently.
label technical_master:

    $ skill_technical += 10
    return
