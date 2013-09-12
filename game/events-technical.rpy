# Afternoon Events
# Technical

# Intro Event and the default
label technical_0:
    if (skill_technical <= 0):
        "I decided to familiarize myself with all the farm equipment so that if something broke, I would be able to understand the problem quicker. The tractors were an interesting biofuel/solar hybrid and were built in a very modular way so that pieces could easily be taken out and replaced, and it had a hitch on the back for attachments like plows, cutters, loaders, etc."
        "I downloaded the schematics and spent some time studying them."
    else:
        "I tuned up some of the farm equipment."
    $ skill_technical += 10

    return

# Better Radio Communication
label technical_1:
    "I installed an antenna on the roof so that we can communicate with the town better. It took some trial and error to figure out the exact alignment and height, since this planet's atmosphere and shape are different from Earth's, but it's working with the radios pretty well."
    $ skill_technical += 10
    return

# Build a water pump
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
            ilian "Hmm. Well, I know we're always finding new uses for these animal skelton things."
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
    "[his_name] grew a lot of vegetables; I guess part of their farming strategy was to grow many kinds of things, so if one thing got wiped out, you still had food."
    "But I didn't always like them."
    $ hated_food = "kale"
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
    "Our solar panels worked well most of the time, but sometimes it was cloudy for days and our batteries ran out. Then we had to use candles and burn wood for cooking, which made a big mess and felt wasteful."
    "I wondered if we could use the nearby river to augment our electricity sources."
    "I studied some diagrams on the internet and drew up some plans for a water wheel that would work with our river."

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

# make dehydrator out of scavenged parts?
#I read about rocket stoves and thought it would be fun to write a technical event on them http://www.richsoil.com/rocket-stove-mass-heater.jsp   
label technical_8:
    #do we have a winter? I think there was a winter, but it was a mild one or something?
    "It was another cloudy day, and there wasn't enough solar power to cook and warm our house with."
    him "I'll go get some wood. Maybe I can cook the food outside in the fire pit."
    her "But then cooking won't warm our house up."
    him "Well, if I cook inside we have to open all the windows anyway since we don't have much of a chimney."
    #or maybe they do have a chimney?
    her "There's got to be a better way to distribute all this energy."
    "I spent the evening researching low-power heating. Some people found that light bulbs helped heat their houses, but we had LEDs that didn't give off much heat."
    "I found a type of combustion stove called a rocket stove, which burned wood sideways very cleanly. Once again though, I'd need some metal pipes." 
    "I knew we were saving a lot of the metal from the shuttle for emergencies. I wasn't sure what I would do."
    her "If we want to advance technologically, we've got to start making our own metal. It's like, the next thing on the tech tree."
    him "Actually, I heard that Lily is gathering ores to see if we can start making our own metal here. But I think gunpowder is next on the tech tree."
    her "Really? Why didn't anyone inform me?"
    him "Well, you're not exactly digging around in the dirt during your working hours. She probably just sent it out to all the farmers."
    "I ran over to the lab the next morning, excited to help."
    her "I heard you've been gathering ore?"
    lily "Yes! Do you have some you'd like to donate?"
    her "I don't, but I'm willing to test the material's melting point!"
    lily "Are you hoping to make something?"
    her "Yes, I want to make a rocket stove to heat our house on cloudy days."
    lily "I don't have enough to really make anything with yet, but I can help you find it."
    lily "I've received samples of three different ores, and I think one could make the kind of metal you're looking for. You'd need to go mining for it though."
    her "Mining, like with a pick?"
    lily "Yes. I think gunpowder would help a lot too."
    her "Blowing up rocks? Is that allowed?"
    lily "Well, we are supposed to survive in a way that doesn't damage the existing ecosystem excessively."
    menu: 
        "Should I try to mine using gunpowder?"
        "Yes.":
            "I'm part of this planet's ecosystem too. Besides, I won't blow up too much since Lily knows where to look."
            her "Okay, let's do this. Do we have any gunpowder?"
            lily "We don't. But you can easily make some from the nitrogen in the crab-spider's guano."
            her "Spider crabs? I think you mean land-lobsters."
            lily "No, crab-spiders are a different animal. They live on the sea shore. It should be pretty easy to gather the material at low-low tide."
            her "Isn't that pretty far away?"
            lily "Well, do you want gunpowder or not?"
            her "I want gunpowder!"
            lily "If we can get Sven to come, we should be a large enough group to defend ourselves from any wandering carnivores"
            her "Okay, when's the next low-low tide?"
            lily "Well, we have to wait for both the moons to be together in the daytime, so it'll be in two days."
            her "Okay, I'll talk to Sven."
            #change scene here
            her "Hey, Sven."
            sven "Hi, how can I help you?"
            her "Want to come with Lily and me to the seashore?"
            sven "The seashore? The one about six miles away?"
            her "Yeah, a real beach! Bring a shovel!"
            sven "No thank you. Not after what I've been reading about giant sea creatures and this planet."
            her "Fine. I'll find someone else."
            #scene change to work
            "I was trying to think of who could come with us at work the next day."
            brennan "I just wish I could get away from it all, you know? I feel like I'm trapped in this tiny town!"
            her "Did you know what you were getting into when you signed up for this?"
            brennan "Who says I signed up? Besides, I bet you're itching to have an adventure too."
            her "You should come to the ocean with me."
            brennan "Seriously?"
            her "Yes! Lily is coming too, and we need a third person so we can look like a herd and not easy pickings."
            brennan "Count me in! But why are you going to the ocean? Have you double-handedly reinvented bathing suits?"
            her "Well, we're going to be gathering some materials for a reinvention, yes."
            brennan "I don't really care what we do, as long as it's something exciting."
            her "Oh, it'll be exciting."
            #scene vegetation
            "There wasn't a road going out to the ocean, so we had to make our way through wild vegetation.."
            "We had some minor run-ins with small insects, but nothing too surprising."
            #scene ocean
            "Arriving at the ocean was magnificent. The air was moist, and my eyes could rest on a flat plane of wetness extending to the horizon."
            brennan "I didn't think there would be so many rocks at the seashore. There's barely any beach!"
            her "Well, we're not here to swim anyway."
            lily "I'm so glad we made it! This crusty white stuff is what you want. "
            her "Okay, so I can just kind of scrape it off?"
            lily "Yeah. We'll be treating it later, so it's not necessary to preserve the form of the guano."
            brennan "Gross. Is it okay if I touch the water?"
            lily "I would advise against it until we know what's in it. I would like to take a sample of it though, if you wouldn't mind. I'm going to take some of the smaller creatures and plants back too."
            her "How much of this do I need?"
            lily "Just get as much as you can. We have an hour or two so don't feel too rushed."
            "We worked hard to get the materials and samples we needed. We found a lot of shells and some bones. As we were getting ready to leave, the tide started to come back in."
            "The incoming waves were purple with one kind of alien sea creature. It had six spiny or hairy arms, and floated like a jellyfish."
            lily "Oh! I've got to record this."
            brennan "Just be careful not to get swept away!"
            "We stayed up past the tidal edge. It surprised me how quickly the tide rushed back in. Little spider-crabs rushed to dry rocks, and many got swallowed up by the waves and the purple jelly-stars."
            #scene vegetation
            "After Lily was satisfied, we made the long trip back."
            #scene lab
            "The next day, I followed Lily's directions to purify the nitrates from the guano. I had to pour water over it and collect the debris, which I poured over ashes. I boiled the remaining liquidy material, skimmed off the scum, and waited for crystals to form."
            "Luckily, we had the other ingredients we needed, so Lily was able to explain how the gunpowder would work. I had to keep the ingredients separate until I was ready to make an explosion."
            #this could be expanded into a second event?
            "Lily told me where to go for the most ore-rich rocks. I followed her directions and successfully created an explosion."
            "It wasn't very big, but it gave me a lot of rocks to take back and start melting into metals."
            "I had a lot of help from Lily and Ilian in making the metal can and pipes I needed."
            "I arranged the pipes around the inside of our house and covered them with mud. The rocket stove easily heated our whole home using only a few sticks."
            
            #maybe they can find some cephalopod shells like http://en.wikipedia.org/wiki/Baculite or a crinoid http://en.wikipedia.org/wiki/Uintacrinus
           
        "No.":
            "We don't know enough about this planet to start blowing things up. Plus, if we already have gunpowder, it's going to be that much easier to make guns, and I think we're better off without them."
            her "Tell me where you think the metal is and I'll see if I can get it out using our pick."
            lily "I will tell you where the metal is, but I want your help collecting some samples from a semi-remote location first."
            her "Don't you think metal is more important than documenting organisms?"
            lily "No, I don't. Any you never know, maybe one of these creatures will have  an iron lung or something."
            her "Okay, what do I need to bring?"
            lily "Well, a backpack, food, and another person."
            her "Another person?"
            lily "Yes, it's much safer to travel in a group of three than a group of two. At least, that's what I believe from my observations and the small amount of anecdotal evidence on the behavior of the local carnivores."
            her "When do you need me to be ready?"
            lily "Well, the next low-low tide is in two days. That's when the moons should be in sync long enough to make a tide anyway."
            her "Okay, I'll talk to Sven."
            #change scene here
            her "Hey, Sven."
            sven "Hi, how can I help you?"
            her "Want to come with Lily and me to the seashore?"
            sven "The seashore? The one about six miles away?"
            her "Yeah, a real beach! Bring a shovel!"
            sven "No thank you. Not after what I've been reading about giant sea creatures and this planet."
            her "Fine. I'll find someone else."
            #scene change to work
            "I was trying to think of who could come with us at work the next day."
            brennan "I just wish I could get away from it all, you know? I feel like I'm trapped in this tiny town!"
            her "Did you know what you were getting into when you signed up for this?"
            brennan "Who says I signed up? Besides, I bet you're itching to have an adventure too."
            her "You should come to the ocean with me."
            brennan "Seriously?"
            her "Yes! Lily is coming too, and we need a third person so we can look like a herd and not easy pickings."
            brennan "Count me in! But why are you going to the ocean? Have you double-handedly reinvented bathing suits?"
            her "Well, we're going to be gathering some materials for a reinvention, yes."
            brennan "I don't really care what we do, as long as it's something exciting."
            her "Oh, it'll be exciting."
            "There wasn't a road going out to the ocean, so we had to make our way through wild vegetation."
            "We had some minor run-ins with small insects, but nothing too surprising."
            "Arriving at the ocean was magnificent. The air was moist, and my eyes could rest on a flat plane of wetness extending to the horizon."
            brennan "I didn't think there would be so many rocks at the seashore. There's barely any beach!"
            her "Well, we're not here to swim anyway."
            lily "I'm so glad we made it! Okay, I'd like to take samples of this crusty white stuff and any other organic material you can find."
            brennan "Gross. Is it okay if I touch the water?"
            lily "I would advise against it until we know what's in it. I would like to take a sample of it though, if you wouldn't mind. I'm going to take some of the smaller creatures and plants back too."
            her "How much of this do I need?"
            lily "Just get as much as you can. We have an hour or two so don't feel too rushed."
            "We worked hard to get the samples we needed. We found a lot of shells and some bones. As we were getting ready to leave, the tide started to come back in."
            "The incoming waves were purple with one kind of alien sea creature. It had six spiny or hairy arms, and floated like a jellyfish."
            lily "Oh! I've got to record this."
            brennan "Just be careful not to get swept away!"
            "We stayed up past the tidal edge. It surprised me how quickly the tide rushed back in. Little spider-crabs rushed to dry rocks, and many got swallowed up by the waves and the purple jelly-stars."
            #scene vegetation
            "After Lily was satisfied, we made the long trip back."
            #scene lab
            "The next day, Lily told me where to go for the most ore-rich rocks. I followed her directions and gathered nearby mineral-rich rocks."
            "I had a lot of help from Lily and Ilian in melting the rocks and making the metal can and pipes I needed."
            "I arranged the pipes around the inside of our house and covered them with mud. The rocket stove easily heated our whole home using only a few sticks."
    
    $ skill_technical += 10
    return

# Make a tractor attachment that places seeds and fertilizer at the same time
label technical_9:

    $ skill_technical += 10
    return

# Make app that connects to solar flare sensor and alerts everyone on their
# tablet computer, and also sends out radio message
label technical_master:

    $ skill_technical += 10
    return
