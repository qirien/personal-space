# Afternoon Events
# Technical

# Default Event
label technical_def:
    scene bg tractor with fade
    "I tuned up some of the farm equipment."
    $ skill_technical += 10

# Intro Event
label technical_0:
    scene bg tractor with fade
    "I decided to familiarize myself with all the farm equipment so that if something broke, I would be able to understand the problem quicker."
    "The tractors were an interesting biofuel/solar hybrid and were built in a very modular way so that pieces could easily be taken out and replaced, and it had a hitch on the back for attachments like plows, cutters, loaders, etc."
    "I downloaded the schematics and spent some time studying them."
    
    scene bg farm_exterior with fade
    "I also installed an antenna on the roof so that we can communicate with the town better."
    play bg_sfx "sfx/radio.mp3"
    "It took some trial and error to figure out the exact alignment and height, since this planet's atmosphere and shape are different from Earth's, but it's working with the radios pretty well."
    "Maybe this way we wouldn't be completely cut off during a solar flare, but could still have some communication with town."
    $ skill_technical += 10
    return

# Build a water pump
label technical_1:
    scene bg farm_exterior with fade
    "Even though we have a solar panel to run our pad computers, the lights, and a few other things, we do most work the old-fashioned way, without electricity."
    "And did I mention there's no running water? We have a well and a pump, but we're always fetching water with buckets...Well, mostly I fetch water with buckets, since [his_name] has a bunch of pipes and canals setup for watering the farm."
    scene bg farm_interior with fade
    show her annoyed at midright
    show him serious at midleft
    with dissolve
    her annoyed "Washing dishes by hand is bad enough, but to also have to fetch and heat the water? There's got to be a better way..."
    him normal "Here, I'll do the dishes tonight."
    her serious "No, it's my turn, I'll just do it."
    him serious "No, really. I'll do the dishes, and while I'm washing them, maybe you can think of a better system that would make it easier."
    her surprised "That...is a really good idea."
    scene black with fade
    "I got out my pad and started sketching some ideas. What could we use for pipes? How could I pump the water out of the well automatically? I did some research on early plumbing systems."
    "[his_name] did the dishes every night for a week while I worked on the plans, and then we spent a day together building it."
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    her normal "OK, so if we turn this crank here, that turns the screw that pulls up the water. Try it!"
    him serious "Nothing's happening."
    her happy "Be patient! Keep turning!"
    him flirting "I will...I trust you."
    play bg_sfx "sfx/trickle.mp3"
    "The cold trickle was nothing like a faucet of instant hot water like on Earth, but it was much better than running out to the well all the time!"
    
    $ skill_technical += 10
    stop bg_sfx fadeout 1.0
    return

# Improve alarm system for solar flares.
label technical_2:
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    play bg_sfx "sfx/radio.mp3" loop
    show him serious with dissolve
    her serious "Did you hear there's probably going to be another flare today? Guess we're stuck at home..."
    him angry "There goes all my chance to get anything done this morning! If I had known there was going to be a flare today, I would have worked harder yesterday and slept in this morning!"
    her surprised "I wonder if there's a way to get more advanced notice of the flares?"
    him happy "If there is, I bet you'll find it!"
    scene black with fade
    "Since I couldn't go to work, either, I decided to spend the time working on a better solar flare detector."
    "The current detector could detect flares as they started and give about an hour's notice to everyone."
    "But I thought we could do better. I researched solar flares and detection and prediction methods, and discovered a method for predicting solar flares based on the rate of decay of radioactive materials."
    stop bg_sfx fadeout 1.0
    "I didn't have any of those lying around, so when the flare was over, I decided to ask Dr. Lily."
    scene bg lab with fade
    show lily at midright with dissolve
    show her normal at midleft with moveinleft
    her concerned "Do you have any radioactive materials I could use?"
    lily "Yes, we have a small stockpile for use with--"
    her surprised "What?"
    lily upset "Why do you want it?"
    her normal "I want to build a solar flare predictor instead of just a detector."
    lily normal "Ah, yes, because gamma-radiation rates change slightly when exposed to solar neutrinos. Winston, one of the scientists who used to work with me was working on a similar project."
    her surprised "Oh, I've never met him. Where is he now?"
    lily upset "He died."
    her sad "Oh, I'm sorry..."
    lily "He failed to adequately shield himself from solar and radioactive radiation. It eventually caught up with him."
    her serious "I won't make the same mistake. Can you show me what he was working on?"
    lily normal "Yes, here is the device. It has a small amount of manganese 54 inside, and a gamma-radiation detector here. That's as far as he got."
    her normal "This is a great start! All I need to do is hook it up to the network so it can send me the data."
    lily upset "Yes. I probably should have finished this project, but... it reminded me too much of Winston."
    her concerned "Oh...were you close?"
    lily normal "He was my husband."
    her surprised "Oh! I didn't know you were married!"
    her sad "I'm so sorry..."
    lily "It's not your fault. But it has considerably slowed down the research here."
    her happy "Well, that part, at least, I can help with."

    hide lily with moveoutright
    show her normal with dissolve    
    "I hooked up the radiation detector to the network and had it send the data to one of the servers in the lab. Then I wrote a program to analyze the data and detect changes."
    "I would need to collect more data to make sure the system was really working properly, so I didn't publish the data to the colony just yet."
    "But during the next flares, I would see how the radiation rates changed beforehand and use that data to write prediction software."
            
    $ skill_technical += 10
    return

# Make laundry wringer
label technical_3:
    scene bg laundry with fade
    show her annoyed at center
    her "These clothes still aren't dry?! It's so humid here, it takes forever..."
    her surprised "Perhaps if I could wring out more of the water before hanging them up? Hmmm..."
    her happy "Yes! I'll need a few parts from the storehouse - wait, I should draw out the design first, so I'll know all the parts ahead of time. Some rollers, a crank, several gears..."
    hide her with moveoutright
    show her normal with moveinleft
    her annoyed "Why won't these two parts fit together?!"
    her surprised "Ohhh, one is imperial and one is metric! Stupid nonstandard parts!"
    play bg_sfx "sfx/gears.mp3" loop
    "Finally, it was finished. It squeaked and rattled and if I had to do it again I would make some changes to the design, but it works."
    stop bg_sfx fadeout 1.0
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    her happy "The clothes dry about 50 percent faster now."
    him surprised "Huh? Really?"
    her "Yeah, come see what I made!"
    scene bg laundry with fade
    show her normal at midright
    show him normal at midleft
    with moveinleft
    play bg_sfx "sfx/gears.mp3" loop
    him happy "You made this?! This is so awesome!\n...\n What is it?"
    her flirt "It's a clothes wringer! What kind of farm boy are you, anyway?"
    him serious "The kind that always had electricity."
    her surprised "Oh, good idea! I could hook it up to the solar and it could crank itself on sunny days...if we could get enough torque..."
    him normal "Whatever you want to do, my lovely inventor."
    stop bg_sfx fadeout 1.0
    $ skill_technical += 10
    return

# Hot water heater
# put in hot water connected to solar
label technical_4:
    scene bg farm_interior with fade
    "One of the things I missed from Earth life was having hot water available whenever I wanted it. Of the few luxuries we enjoyed, hot water seemed like one I could improve on."
    show her normal at midright
    show him normal at midleft
    with dissolve
    her surprised "I wonder if we could make our own hot water heater."
    him serious "Well, we don't exactly have a ton of gas or electricity to spare. But you might be able to use the sun to heat it up and then store it somewhere insulated so it doesn't take as long to heat up."
    her normal "I'll look into it."
    "Most water-heating designs assumed I would have access to more solar panels. I didn't, but I felt like I could at least stick a container of water in the sun to heat it. If I could make something out of metal or another material that transferred heat easily, I could get something to work."
    "I took a trip to the storeroom to see what they had."
    scene bg storehouse with fade
    show ilian at midright with dissolve
    show her normal at midleft with moveinleft
    her normal "Hi Ilian. How are you today?"
    "He didn't look happy to see me."
    ilian "I have the feeling you need more materials from me."
    her serious "Well, yes, I was going to see if you had any pipes or sheets of metal or something."
    ilian "We don't have much left. If it's an emergency or something vital to our survival you can use it, but I'm afraid that otherwise I have to say no."
    menu:
        "It's not vital to my survival.":
            her serious "I just wanted to build a hot water heater for my house. Do you have any ideas about what kind of material I could use that would conduct heat easily?"
            ilian "Hmm. Well, I know we're always finding new uses for these animal skeleton things."
            her flirt "And by \"always finding\" you mean no one has thought of anything to do with them?"
            ilian happy "They're looking pretty good in my junk pile, if I do say so myself."
            her serious "I'll take a few. There has to be some way I could use them."
            "The exoskeletons varied in texture. Some parts were brittle while others were as hard as a seashell. I felt like there was no way I could make anything useful out of them."
            "I put them aside and wondered if I could make a tank out of wood."
            scene bg farm_exterior with fade
            show him normal at midright with dissolve
            show her normal at midleft with moveinleft
            her normal "[his_name], could you cut down a tree for me so I can make a water tank for our house?"
            him "Well, I'm not sure, but I can try. How about you come with me to help pick out a tree?"
            "We found a tree that was about the width I needed. [his_name] cut it down, and we brought it home on our wagon in pieces."
            "After the wood dried out, I hollowed it out using tools at the storehouse."
            "In the end, it just ended up being lukewarm storage for more water."
        "I'll die if I don't get what I need.":
            her concerned "It's for something really important. Can I please get two sheets of metal and some pipes?"
            ilian "What exactly is it for?"
            her angry "I don't have time for your questions! This is a matter of life and death!"
            ilian "Alright, alright, here you go."
            "After some careful welding, I made a tank for water with many metal arms sticking out of it to help passively heat the water."
            "I was able to put a pipe from the tank to our house, complete with a stopper that kind of leaked."
            play bg_sfx "sfx/trickle.mp3"
            scene bg farm_interior with fade
            show her normal with dissolve
            her happy "Ahhh, warm water!"
            stop bg_sfx fadeout 1.0
            $ community_level -= 5
                                                 
    $ skill_technical += 10
    return

# scavenge electronics, etc from shuttle to make blender
label technical_5:
    scene bg farm_interior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    "[his_name] grew a lot of vegetables; I guess part of their farming strategy was to grow many kinds of things, so if one thing got wiped out, you still had food."
    "But I didn't always like them."
    "My least favorite was:"
    menu:
        "What was my least favorite food?"
        "Kale.":
            $ hated_food = "kale"
        "Beets.":
            $ hated_food = "beets"
        "Turnips.":
            $ hated_food = "turnips"
        "Brussels sprouts.":
            $ hated_food = "brussels sprouts"
    her concerned "I just don't like [hated_food]."
    him serious "Sorry, it's nutritious and it grows really well here, so we have a lot of it."
    "I had to find some way to eat it that I wouldn't hate quite so much. Something to cover up the taste?"
    "Back on Earth I would sometimes make smoothies, but we didn't have any blenders here."
    "I figured I would try to make one. At the very least, thinking about the plans would distract me while I was choking down [hated_food]."
    "I would need a lot of parts, so I headed over to the storehouse."
    scene bg storehouse with fade
    show ilian at midright with dissolve
    show her normal at midleft with moveinleft
    ilian "I don't have any extras of these things, but if you help us dismantle some of the shuttle's electronics, you could keep some for your project."
    her surprised "(Hmmm... Do I want a blender that badly?)"
    menu:
        "What should I say?"
        "Yes, I'll help.":
            her normal "Sure, I'll help you out."
            "We took out whole circuit boards, disconnected all the wires, and took some of the components off the boards. Soon we had a nice pile of resistors, capacitors, LEDs, motors, wires, and microchips."
        "No, thanks.":
            her concerned "No, thanks, I don't really need a blender, I guess."
            ilian "You want to make a blender?"
            her serious "Yeah..."
            ilian "We could use one here at the storehouse; Pete wanted to make peanut butter."
            her normal "Well, maybe he could help you dismantle parts, and I will see if there's enough to make two blenders."

    scene black with fade
    "I found a fan and thought I could use that for the blades of the blender. In the fuel intake there were plenty of gaskets, though it was tough to find them in the right size."
    "I even added a dial connected to some resistors that let you control the speed of the blender. The container wasn't transparent (I wasn't sure if the metal we used was even technically food-safe), but it fit on the blades okay."
    play bg_sfx "sfx/blender.mp3"
    "When I tried it out, it leaked -- a lot. I sealed the leaks up and played around with the speeds to get a speed that would mix and blend without foaming or stalling."
    "Finally, I had a blender. It used so much electricity that it wouldn't run at the same time as anything else, so we had to turn off the lights when we needed to use it."
    "I didn't mind, though. I just sat back and enjoyed my smoothie full of [hated_food]."
    stop bg_sfx
    $ skill_technical += 10
    return

# build a water wheel to augment power grid
label technical_6:
    scene bg farm_exterior with fade
    "Our solar panels worked well most of the time, but sometimes it was cloudy for days and our batteries ran out. Then we had to use candles and burn wood for cooking, which made a big mess and felt wasteful."
    "I wondered if we could use the nearby river to augment our electricity sources."
    "I looked up some diagrams other people had made, and drew up some plans for a water wheel that would work with our river."

    scene bg storehouse with fade
    show ilian at midright with dissolve
    show her normal at midleft with moveinleft
    her surprised "Do you mind if I get some more parts from the shuttle?"
    ilian "What are you making now?"
    her normal "A water wheel, for electricity."
    ilian happy "That sounds great. Can you hook it up to the storehouse?"
    her concerned "No, it's just for our house..."
    ilian normal "Maybe we should all be on the same power grid..."
    her serious "Maybe so, but we're not right now. Besides, if we were, we'd have the same problems we do now on cloudy days, just everyone will blame their neighbors for using all the electricity."
    ilian "True. Well, if you find something you can use, go ahead - you're the only one who's shown much of an interest so far."
    her normal "Thanks, I will."
    
    scene black with fade
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

# 8 - programmable substance mixer, farming app
label technical_7:
    scene bg farm_interior with fade
    show him normal at midright
    show her normal at midleft with dissolve
    her happy "Hey, is there anything you need around the farm?"
    him surprised "Like what?"
    her normal "Like an invention or something to help automate some of the tasks you do all the time."
    him serious "I'm sure there is, but I can't think of anything right now."
    her normal "Okay, let me know when you think of something."
    scene black with fade
    scene bg farm_interior with fade
    show her normal at midright with dissolve
    show him normal at midleft with moveinleft
    him surprised "Hey, [her_name], I thought of something you could make for me."
    her surprised "What is it?"
    him serious "Well, I'm always mixing different amounts of different kinds of fertilizer and other substances for different fields."
    her concerned "Okay..."
    him normal "I was wondering if you could set something up where I just enter in the proportions I need and it would measure and mix it for me?"
    her serious "Or you could keep track of what you've planted, and it could cross-reference it with the Ag database and make suggestions for you?"
    him happy "Yeah, even better! But there should be a manual option, too, in case I need something out of the ordinary."
    her happy "Alright, I'll do it!"
    scene bg tractor with fade
    "The more I thought about it, the bigger this project seemed."
    "Not only would I have to make a mechanical device to measure out the right amount of each substance, and a mixer to mix them all up, but I'd also have to make it so [his_name] could program and control it with a nice interface."
    "And I'd need a lot of parts, too..."
    scene bg storehouse with fade
    show ilian at midright with dissolve
    show her normal at midleft with moveinleft
    her happy "Hey, Ilian, how are you doing?"
    ilian normal "What do you want?"
    her annoyed "...you don't care for small talk, do you?"
    ilian "No."
    her serious "Fine, I need some electronic ratio control valves and connecting pipe."
    ilian "Let me check..."
    ilian "We don't have any extras of those."
    her surprised "What, really?"
    ilian "All the control valves we have are mechanical."
    her annoyed "Hmmm, okay..."
    scene black with fade
    "I would have to do something else."
    "I ended up focusing more on the farming app [his_name] wanted; it couldn't measure the amounts of chemicals for him, but he said it would be useful even if it just reminded him of the right proportions for the plants he was working on."
    "I put in a map interface, where he could quickly tell the app what plants he planted where, and when, and it would remind him when it was time to fertilize or harvest."
    "It also listed the recommended nutrient proportions for each plant and calculated what soil amendments would be necessary given the chemical makeup of Talaam's soil."
    scene bg farm_interior with fade
    show him normal at midright with dissolve
    show her normal at midleft with moveinleft
    her normal "Here, will you give this a try?"
    him surprised "You finished it already?"
    her serious "Well, it's pretty rough, but I wanted your input before I finalized the design."
    him serious "Okay, let me try it."
    him happy "Wow, this is really cool!"
    her surprised "Don't you already keep track of all this stuff somewhere?"
    him normal "Yeah, but it'll be better to have it all in one place. Thank you, [her_name]."
    her happy "You're welcome."
    "I wasn't a farmer, but I felt satisfied that I could help out in my own way."
    
    $ skill_technical += 10
    return


# 9 - Help Ilian with the inventory software - build good queries, or streamline interface, etc.
label technical_8:
    scene bg storehouse with fade
    show ilian at midright with dissolve
    show her normal at midleft with moveinleft
    her normal "Hey, Ilian, I was wondering if we have any--"
    ilian "No."
    her surprised "What?"
    ilian "I'm not giving you anything else until you help me with something. I'm always giving you materials; now it's time for you to pay up."
    her annoyed "I help out! I'm a [profession]; what do you think I do all day?!"
    ilian "Here's what I need. We have this database software to manage our inventory, but it takes forever to find out how much we have of something, and to change how much we have."
    her surprised "Oh, so you want an easier interface?"
    ilian "Yes, I do. Then I will be able to help distribute things more fairly and not rely on memory."
    her normal "That sounds fun! Let me take a look at what you currently have..."
    "The current inventory management system had all sorts of buttons that would be useful in a store, but had no meaning on our colony."
    her serious "I could delete those buttons, and make it quicker to look up the things you need all the time. Will you make me a list of things that need to be easier?"
    ilian happy "Yes, I will."
    scene bg farm_interior with fade
    show her normal at center
    "I worked on the inventory system every evening for a few weeks, asking Ilian for feedback after major changes."
    her happy "That should do it!"
    her concerned "Although, hmmm, it might be convenient to have access to this database from my computer..."
    menu:
        "What should I do?"
        "Keep access private for just authorized people.":
            "I didn't think anyone needed access except Ilian and Mayor, so I just kept that part the same."
        "Ask Ilian about putting in a public interface.":
            "I sent Ilian an e-mail about adding a public interface."
            her_c "If we had a way for everyone to access the database, they wouldn't have to come ask you about every little thing; they could just look it up themselves."
            ilian_c "I don't know if that's a good idea..."
            nvl clear
            her_c "Why not? Haven't you been distributing things fairly?"
            ilian_c "For the most part... although {b}some{/b} people always seem to need more things than others."
            her_c "Well, some of us make more things than others."
            ilian_c "I don't think the inventory system should be public."
            her_c "Okay, I guess I understand."
            nvl clear
        "Add in a back door for yourself.":
            "I put in a back door so that I could access the database if I needed to. I mean, no need to bug Ilian about something when I could just look it up, right?"
            $ community_level -= 5
    "Finally, it had everything he needed."
    scene bg storehouse with fade
    show ilian at midright with dissolve
    show her normal at midleft with moveinleft
    her happy "It's done!"
    ilian "Good, let me see."
    ilian "...add item, quantity, expiration, good... move item, good... What about the current status?"
    her serious "You can use this screen here. It shows current levels of everything, sorted by type: food, tools, electronics, etc."
    ilian "I see..."
    her normal "And you can also just type in the name of something here and it will search for all the items with that name and tell you where they are."
    ilian happy "This is... much better. Thank you."
    her "So, now that you have a perfect inventory system, can I have some more flour, please?"
    ilian "That's all you wanted? Sure, here you go."
    her annoyed "...You didn't even look it up!"
    ilian normal "I don't have to; these barrels here are all full of flour. It's not something we're running out of."
    her laughing "Well, how about variable-rate resistors?"
    ilian "...Let me see... Sorry, we're out of those."
    her normal "Okay, well, at least now we have a quick way to find out."
    ilian "Yes, I believe I already said thank you."
    
    $ skill_technical += 10
    return



# Setup webcams around the farm to monitor fields/(goat)
label technical_master:
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    "Sometimes, I felt like we had time-traveled to the 1800s. We were so dependent on our plants and animals, and so removed from Earth."
    "Luckily, though, we had a few things they didn't."
    "We had a few hundred year's worth of science and engineering progress, reference materials, computers, and other electronic resources."
    "Other people wanted to do things the old-fashioned way. But I felt it would be a waste of all this technology if we didn't put it to good use!"
    him concerned "Guess I'll check on the north fields again. Something keeps breaking through the fence there and messing everything up."
    her surprised "You're going to ride out there and look at it?"
    him surprised "Well, yeah, how else am I going to know if something's out there?"
    her normal "Go ahead and check on it, but I have a better idea for next time."
    hide him with moveoutleft
    scene bg storehouse with fade
    show ilian at midright with dissolve
    show her normal at midleft with moveinleft
    "I rummaged through the broken parts bin at the storehouse until I found what I was looking for."
    her "Aha! A broken computer pad! Let's see if there's any more..."
    ilian "What are you going to use that for?"
    her "A surveillance system."
    ilian "What?! I don't think anyone's going to break into your house..."
    her "Not for the house! For the fields!"
    ilian "Yeah, okay, whatever."
    "I found a bunch of security cameras from the shuttle, and some extra wires, too."
    "I took them all home with me and started building."

    scene bg farm_interior with fade
    "I hooked up the security cameras to point at different parts of the farm. One for the barn, one for the north fields, and one for the south fields."
    "I used mini solar chargers for power, which meant they wouldn't work at night or on very cloudy days, but they were still better than manually checking everything."
    "I was excited to show [his_name]."
    show her happy at midright
    show him normal at midleft
    her happy "Hey, [his_name], want to check on the farm?"
    him concerned "Maybe after dinner..."
    her normal "No, do it right now... from your computer!"
    him surprised "What? How does that work?"
    her laughing "Take a look!"
    "I showed him the view from the cameras."
    him happy "Wow, this is really cool! Hey, look, there's Lettie! Hi, girl!"
    her happy "You like it?"
    him concerned "Yeah, but... I still kind of want to check on things."
    her annoyed "Why? You can see right here everything's fine!"
    him annoyed "This is good, but sometimes I still want to see it with my own eyes."
    her concerned "Yeah, okay."
    him happy "Want to come with me?"
    menu:
        "What should I say?"
        "Sure.":
            her happy "Sure, I could use a walk anyway."
            scene bg fields with fade
            show her normal at midright
            show him normal at midleft with dissolve
            "We walked around the farm, and I showed him all the cameras and how I had anchored them in place."
            him serious "You're amazing, you know that? I could never have built something like that."
            her flirt "Well, I'm hopeless at growing food, so it all works out."
            $ loved += 2
        "No, thanks.":
            her annoyed "No, thanks. That's why I made this whole thing, so we wouldn't have to walk around the whole farm every night."
            him annoyed "Well, you don't have to come."
            her serious "Okay, bye."
            him serious "Bye."
            "He did still use my security cameras sometimes, but I guess he actually enjoyed his nightly patrol, because he still walked around the farm almost every night."
        "I'll just watch you from here.":
            her flirt "I'll just watch you from here."
            him flirting "All right, I'll try and make watching me worth your time."
            hide him with moveoutleft
            her happy "(Hee hee, he's visiting Lettie...)"
            her annoyed "(Did he just give her a kiss?! Gross!)"
            her happy "(Now he's making silly faces at me. Will he ever grow up?!)"
            her normal "(Nice close-up of your teeth...or... what {b}is{/b} that?!)"
            show him normal with moveinleft
            him happy "I'm back!"
            her happy "Welcome home."
            $ loved += 1

    "The surveillance equipment made it easier to see the farm at a glance. I decided to put instructions for them online in case anyone else wanted to make some."
    call set_work_bg
    show her normal at midright with dissolve
    "The next day at work, the mayor came to see me."
    show pavel at midleft, behind her with moveinleft
    pavel "I hear you have a great camera system setup at your farm, [her_name]."
    her happy "Yeah, here, take a look! You can see the fields in every direction."
    pavel "Would you mind setting up something similar at a few locations around town?"
    her surprised "Sure, I could do that."
    "I setup some cameras; one at the river, one at the community center, and one overlooking the whole town, and made an interface so anyone in our community could see them and collect data from them."
    "A couple people even asked me for more instructions like the one I had posted, so I added how-tos for the water screw, laundry wringer, and everything else I had made."
    "Life on the colony was still hard, but some of my inventions made it easier for everyone."

    $ skill_technical += 10
    $ community_level += 10
    return

