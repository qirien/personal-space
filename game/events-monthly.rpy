# Event content for all the important monthly events

# You shouldn't ever see this. This is just a fall through in case something happens
# and there's no event for this month.
# TODO: Make the ending actually happen....
label monthly_event_0:
    "Nothing exciting happened this month."
    return

# MONTH 1 - Chore allocation
label monthly_event_1:
    scene bg farm_interior with fade
    show her normal at center
    show him normal at right
    play music "music/You.ogg" fadeout 2.0
    "Our first month living on our own together, we had to work a lot of things out."
    "Like, do we eat breakfast together, or separately? Who should cook and clean up?"
    menu:
        "What should I do about breakfast today?"
        "Make some for [his_name]":
            her "Here, [his_name], I made you some breakfast."
            him "Oh, thank you. I could just make it myself, you know."
            her "I don't mind making breakfast."
            $ loved += 2
        "Ask if he wants some":
            her "So, I'm making breakfast...do you want some?"
            him "Oh, that'd be great, thanks."
            her "Still just meal rations, until the crops start coming in."
            him "Yeah, it will be a while still."
            $ loved += 2
        "Don't make him any":
            him "Oh, you made breakfast?"
            her "Sorry, I just made some for me."
            him "Okay, I can get my own."
            $ loved -= 2
    
    "That set the pattern for our mornings. Some things weren't as easy to work out, though."
    her "Thanks for making dinner, but you left the dirty dishes on the stove."
    him "I was going to do them later."
    her "You can't save them for later; they'll attract pests!"
    him "Well, I thought since I made dinner, maybe you would do the dishes."
    her "In my house, whoever made the mess cleaned up the mess."
    him "Well, this is {b}our{/b} house, now."
    menu:
        "We'll do it your way":
            her "Fine, we'll do it your way. Whoever cooks, the other person cleans up afterwards."
            him "Great, that will work."
            "But it didn't work..."
            her "When were you going to do those dishes?"
            him "Those? I'm getting around to it."
            her "They're not going to clean themselves! Since I cooked, it's your turn to wash them!"
            him "Okay, but I'm not doing it right now, I'm in the middle of something."
            "When we went to bed they were still there."
            her "Honey? You haven't done the dishes yet."
            him "Oh, I'm too tired, I'll do it in the morning."
            "But the next morning, I found..."
                
        "We'll do it my way":
            her "Let's do it my way. Whoever cooks, cleans up afterwards."
            him "I guess that will work."
            "But it didn't work..."
            her "Are you going to make dinner tonight?"
            him "What? I wasn't planning on it..."
            her "But I made dinner last night."
            him "I'm not that hungry."
            "{b}I{/b} was hungry, so I just made dinner for myself. It felt a little lonely, though, eating by myself while he was poring over his charts for the farm. Still, I cleaned up and settled down to relax."
            her "(If he gets hungry he can make his own dinner.)"
            "I fell asleep early, and awoke the next morning to find..."
                
        "{i}I'll be in charge of dishes{/i}" if (skill_domestic >= 10):
            her "Promptly cleaned dishes are really important to me, so why don't I be in charge of that? We can either take turns cooking, or cook together."
            him "Thanks, I really can't stand doing dishes. I'd rather do almost anything else."
            her "Like getting the water for our breakfast?"
            him "Yeah, I'll do that."
            her "Thank you; I hate going outside first thing in the morning."
            "So that worked out pretty well."
            $loved += 5
            return

        "{i}Let's take turns fairly{/i}" if (skill_knowledge >= 10):
            her "Did you know that men who do more housework are generally happier in their marriages?"
            him "According to who?"
            her "There's also a study correlating amount of housework done with frequency of sex."
            him "What exactly are you trying to say?"
            her "Just thought you might find those studies interesting. In a totally abstract way."
            him "It sounds like splitting household chores is really important to you."
            her "It is. We both work hard all morning in different ways. We don't have to each do half of everything, but I think there will be less chance for arguments if we work out ahead of time what each person will do."
            him "All right, let's make a list, then."
            "We listed all the household chores we could think of, and then marked each one as \"hate\", \"enjoy\" or \"meh\". It turned out that he really hated doing dishes, so I agreed to do them all the time, and since I was not a morning person, he would make breakfast every morning. We worked out the other chores, too."
            "So that worked out pretty well."
            $loved += 5
            return

    scene black with fade
    #if nobody did the dishes, pest problems!
    #show her upset at center
    #show him upset at right
    play music "music/Prelude02.ogg" fadeout 1.0
    her "AAAAAAAAAAAAAAAHHHHHH!!!!"
    him "What is it?! What's wrong?"
    scene bg farm_interior with fade
    "I just pointed to the dirty dishes. Coiled around his mess kit, happily nibbling on bits of leftover food, was a long, flat, segmented creature with innumerable legs and dangerous-looking claws. It was at least as long as my arm."
    him "Whoa!"

    menu:
        "I..."
        "Yelled":
            her "THAT is why you don't leave dirty dishes out overnight!!!"
            him "Okay! How was I supposed to know this planet had giant leftover-eating millipedes?"
            her "It's pretty obvious! Every planet has its scavengers!"
            him "Calm down, [her_name]. I'll take care of it."
            $relaxed -= 5
        "Cried":
            "I started sobbing."
            her "This would have never happened if you hadn't left out those dirty dishes!"
            him "Hey, hey, it's okay, here, I'll take care of it."
            $relaxed -= 5
        "Laughed" if (relaxed >= 5):
            her "Ha ha ha ha ha ha...\nWho invited the millipede to breakfast?"
            him "Sorry about that. He seemed like such a nice fellow last night..."
            her "I'm afraid he's worn out his welcome. Perhaps you could gently escort him off the premises?"
            him "It would be my pleasure."
            
        "{i}Analyzed{/i}" if (skill_knowledge >= 10):
            her "Interesting. It's legs are jointed like an arthropod, but those claws look more crustacean ... of course, arthropods and crustaceans are not that far apart from each other... how did it get inside, anyway?"
            him "I think it crawled under the front door. There's quite a gap there."
            her "Huh. Looks like it's an omnivore; it ate the protein and the vegetables..."
            him "Well, whatever it is, we should put it back outside."
        "{i}Stayed calm{/i}" if (skill_spiritual >= 10):
            her "Oh...my. That is...gigantic."
            him "No kidding. Hold on, I'll get him out of here."
    "He put on his work gloves and picked up the mess kit by the handle. I opened the door so he could take it outside."
    him "C'mon, George, time to take a hike."
    her "George?! You're giving this thing a name?"
    him "Doesn't he look like a George to you? Besides, I accidentally invited him in with my mess, so I guess he's my pet."
    her "As long as he's an outside pet."

    "The dishes were never left undone after that."
    return

# MONTH 2 - The Cellar
label monthly_event_2:
    play music "music/You.ogg" fadeout 2.0
    scene bg farm_exterior with fade
    show him normal at left
    him "It'll sure be nice when we have some fresh food to eat."
    show her normal at center
    her "I know; I'm so tired of MREs!"
    him "It won't take too long until the radishes, spinach, and maybe even carrots are ready."
    #show her worried at center
    her "We don't have a refrigerator..."
    him "No, I was thinking of digging a cellar, but I just haven't had time...preparing the fields has taken longer than I thought."
    menu:
        "The cellar...?"
        "I'll do it!":
            her "Don't worry about the cellar; I'll take care of it!"
            him "Whoa, whoa, that's a big job - why don't we work on it together?"
            her "That does sound better, actually."
            "We dug and hauled out dirt and dug and hauled until finally we had a small cellar to store food in! We were exhausted, but it felt good to get it done together."
            $ loved += 5
            $ skill_physical += 5

        "{i}I'll surprise him...{/i}" if (skill_physical >= 10):
            her "We have time; don't worry about it yet."
            "I started digging after work, thinking I could get a lot dug before he came home, but..."
            him "Nice hole. Are you going to plant something in it?"
            her "No, it's going to be our cellar."
            him "Oh."
            her "..."
            him "Why don't we work on it together?"
            "We dug and hauled out dirt and dug and hauled until finally we had a small cellar to store food in! We were exhausted, but it felt good to get it done together."
            $ loved += 5
            $ skill_physical += 5

        "{i}I'll help with the farm while you dig.{/i}" if (skill_domestic >=10):
            her "Why don't you let me take care of the farm while you dig it?"
            him "Well...That could work. There's a lot of weeds that need pulling; I'll show you how to do the watering with the irrigation ditches I have set up."
            her "I can do that."
            him "You can even...you can take Lettie if you want to."
            #show her laughing at center
            her "Wow, you're trusting me with your favorite horse? I'm touched."
            him "I wouldn't trust anyone else."
            scene bg fields with fade
            "I rode Lettie around, scouting the fields for weeds. I had never noticed how big the farm was before -- [his_name] takes care of a lot of plants!"
            "It took longer than I thought, and I ended up helping him haul out a lot of the dirt, but then we had our very own cellar!"
            $ skill_domestic += 5
            $ loved += 5

        "{i}Maybe I could build something to help.{/i}" if (skill_technical >= 10):
            her "Maybe I could build something to help dig the cellar?"
            him "Really? That would be cool."
            "I researched and designed a simple machine with buckets and pulleys for getting the dirt up out of the hole. I was able to take one of the solar panels from the roof and power it with electricity."
            him "Oh, this will make it a lot faster!"
            "He dug in the hole, and I moved the dirt from where the machine dumped it to go on top of the roof of the cellar, which effectively made it deeper faster."
            "Even though it took a long time, it was kind of fun to work on it together."
            $ loved += 5
            $ skill_technical += 5

        "{i}Maybe the Peron's would help us dig it?{/i}" if (skill_social >= 10):
            her "Maybe the Peron's would help us dig ours, and we could help them dig a cellar, too?"
            him "That would be great; it'll be more efficient with a few more people."
            "I talked to the Peron's and they thought that sounded great, so we were able to help each other have a cellar to store food in. They also gave us some eggs from their chickens, who were acclimatizing to Talam nicely."
            $ skill_social += 5
            $ community_level += 5

        "I don't want to help.":
            her "I'm sure you'll find the time."
            her "(All the farm stuff is his responsibility, anyway)"
            $ loved -= 5
            "It took him two weeks of digging and hauling dirt every second he wasn't caring for the plants. He fell asleep right after dinner, but in the morning he was back digging again, until finally, it was finished."

    "Later in the month, he harvested some radishes, spinach, and carrots, and we were able to store them safely in the cellar."
    return

# MONTH 3 - His Birthday
label monthly_event_3:
    play music "music/Prelude22.ogg" fadeout 2.0
    "Even though we were on a new planet, we still kept track of what day it was on the Earth calendar. The seasons didn't match up or anything, but it helped us feel like we were still a part of things back home."
    scene bg farm_interior with fade
    show her normal at center

    her "It's his birthday this month!"
    menu:
        "Maybe I should do something for him..."
        "{i}Have a party{/i}" if (skill_social >= 20):
            "I invited some friends over and we ate dinner together and played games together until late. We sang Happy Birthday to [his_name]."
            show him normal at right
            him "Thanks, [her_name] - what a great birthday!"
        "{i}Make delicious food{/i}" if (skill_domestic >= 20):
            "I couldn't really copy his bread-cake that he made on the shuttle for my birthday, but I was determined to make him something tasty."
            "I found some berries that I had tried before, and combined them with some biscuits from our rations to make a sort of berry shortcake. We had some candles in our emergency case, so I lit one of those for him, too."
            show him normal at right
            her "Happy birthday, [his_name]"            
            him "Wow! Thank you! This looks great!"
            "It didn't taste anything like strawberry shortcake, but it was still good, and [his_name] seemed to like it."
            
        "{i}Make him a present{/i}" if (skill_creative >= 20):
            "I thought and thought about what I could make him that he would like."
            "I finally decided I would make him a hat."
            "I could only work on it when he wasn't paying attention, so it went pretty slowly. But finally I was able to finish it."
            "I hoped he would actually like it, and not just pretend like he liked it."
            show him normal at right
            her "Happy birthday, [his_name]. This is for you."
            him "A birthday present?! Wow, thanks!"
            him "This hat is perfect! It will keep the sun off my neck and will be warm in the cold wind, too!"
            her "I'm so glad you like it."
        "Make him a card":
            "I made him a nice card and gave it to him on his birthday."
            show him normal at right
            him "What's this for?"
            her "Today's your birthday! On the Earth calendar."
            him "Oh! I hadn't thought about the Earth calendar for a while! I forgot; thank you!"
            her "Sorry I couldn't really get you anything."
            him "It's okay; I have everything I need right here."
            
        "Just tell him happy birthday":
            "I figured it'd be a waste of resources to make him anything special. We had what we needed. But I did tell him happy birthday, and he seemed to like that."
            show him normal at right
            him "Thanks for remembering my birthday."
        "I'm not doing anything":
            "He probably didn't even remember his birthday. Birthdays are dumb, anyway."
            "When his birthday came around, he didn't say anything about it, so I guess I was right."
            $ loved -= 5
            return

    "I was happy I could show him I cared by remembering his birthday."
    $ loved += 5
    return

#helper function for month 4 for a commonly used conversation tree
label unappreciated:
    play music "music/Prelude02.ogg" fadeout 2.0
    her "It's none of your business what I do in my spare time."
    him "Well, it just seems kind of like a waste of time when there's so much real work to be done."
    her "Real work?! You don't think I do real work?!"
    him "Real work provides food, clothing, shelter. The necessities. We don't have extra time for anything else in order for the colony to survive."
    her "If it's just about survival, life isn't worth living."
    him "Well, you don't even get a choice if you don't survive. If something goes wrong, who's going to help us out here? There's no food banks, no Red Cross, no emergency rooms - just us."
    $ relaxed -= 10
    $ loved -= 10
    $ community_level -= 10
    menu:
        "You're freaking me out":
            her "[his_name], you're freaking me out. Are we going to die out here?"
            him "Maybe. But, live or die, it's up to us. Our hard work, or lack of it, will determine our fate."
            her "That's so scary."
            him "At least we are in control. If we die, it's our own damn fault."
        "We can't focus on that all the time":
            her "That's true, but we can't be working on food, clothes, and shelter twenty-four hours a day. If you don't take a break and think about other things once in a while, you'll go insane."
            him "Survival is mostly what I'm thinking about. Every day."
            her "Well, I can't live that way."
            him "Well, hopefully you won't die that way."
        "I can't talk about this anymore":
            her "Stop it, I can't talk about this anymore."
            him "Well, just think about what I said. Are we going to live or die?"
            her "I said stop it!"
            her "I don't want to die..."
            him "Then you need to choose to live."
    return

# MONTH 4 - Are Hobbies a Waste of Time?
label monthly_event_4:
    scene bg farm_interior with fade
    show her normal at center
    show him normal at right

    $ highest_skill = highest_stat()
    if (highest_skill == "Domestic"):
        him "You spend a lot of time around the house; what exactly do you do?"
        menu:
            "What do I do?"
            "You really don't know?":
                her "What do I do?! You really haven't noticed?"
                him "I don't know; I'm sure you're doing something useful, I'm just not sure what."
                her "Well, have you noticed those clean clothes you're wearing?"
                him "Oh, yeah, you washed those, huh?"
                her "And I've planted an herb garden out front to add flavor to our meals, and for herbal teas and things."
                him "Okay, that will be good. Sorry, I didn't meant to accuse, I just really was curious what projects you've been working on."
            "What do {b}you{/b} do?":
                her "What have {b}you{/b} been doing lately? You've been reading a lot."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "Okay, well, that sounds very... necessary."
                her "I've made some curtains and planted an herb garden, in addition to keeping the house pretty spotless."
                him "Oh, is that what those plants are? The house is really clean, too; thank you."
            "It's none of your business.":
                jump unappreciated

    elif (highest_skill == "Creative"):
        him "You spend a lot of time making crafts, don't you?"
        menu:
            "Do I?"
            "It's important.":
                her "I think it's important to know how to make things with what we have on this new planet."
                him "Like what kinds of things?"
                her "I made those placemats that keep our table clean, and I'm learning how to crochet. When our warm clothes from Earth wear out, we'll need to know how to make new ones with the resources we have."
                him "That's true...we can't just go to the store and buy stuff anymore, can we? Sorry, I didn't meant to accuse, I just really was curious what projects you've been working on."
            "{b}You{/b} spend a lot of time reading":
                her "What about you? You've been reading a lot lately."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "That sounds useful."
                her "I've been learning how to make things out of native materials, like these placemats."
                him "Oh, that's good. I want us to be independent from Earth; that's important."
            "You don't appreciate what I do":
                jump unappreciated
    elif (highest_skill == "Technical"):
        him "You spend a lot of time tinkering with things, don't you?"
        menu:
            "Do I?"
            "It's important":
                her "When things break, we can't just take them to a repair shop. I try and keep everything in good condition so it won't break."
                him "Like what?"
                her "Well, I installed the antenna that lets us communicate with the town, and the screw that brings water into the house."
                him "Yeah, I'm really glad to have those. Sorry, I didn't meant to accuse, I just really was curious what projects you've been working on."
            "What do {b}you{/b} do?":
                her "What have {b}you{/b} been doing lately? You've been reading a lot."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "Okay, well, that sounds very... necessary."
                her "I installed the antenna that lets us talk with the village, and the device that brings water into the house."
                him "I love those; thank you."
            "I can't believe you don't appreciate me":
                jump unappreciated

    elif (highest_skill == "Spiritual"):
        him "You spend a lot of time just thinking about stuff, don't you?"
        menu:
            "Do I?"
            "It's important":
                her "So many things have changed, I think it's important to have a reason to work hard and help each other out."
                him "Like what?"
                her "Well, from my studies I've learned how important it is to answer someone with love, even if they are being insensitive or unappreciative."
                him "...You probably have a lot of opportunities to practice that, don't you?"
                her "Well...yes. I think studying this principles helps me to get along better with others and work unselfishly."
                him "That is important. Sorry, I didn't meant to accuse, I just really was curious what you've been learning."
            "What do {b}you{/b} do?":
                her "What have {b}you{/b} been doing lately? You've been reading a lot."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "Okay, well, that sounds very... necessary."
                her "I've been learning about how important it is to answer someone with love, even if they are being insensitive or unappreciative."
                him "That {b}is{/b} important."
                her "I'm not that good at it yet, though."
                him "I could probably use some reminders of that, too. Want to show me what you've been reading?"
                her "Sure, let's read together."
            "I can't believe you don't appreciate me":
                jump unappreciated

    elif (highest_skill == "Social"):
        him "You spend a lot of time just hanging out, don't you?"
        menu:
            "Do I?"
            "It's important":
                her "We need our connections with other people if we're going to survive as a community."
                him "Does that really do any good?"
                her "Well, remember those delicious dried fruits we got from the Peron's? We were \"just hanging out\" when we prepared them."
                him "Yeah, those are good."
                her "We can't survive by ourselves out here - we need the community."
                him "You're right; I don't like to depend on others, but we do need to work together."
            "What do {b}you{/b} do?":
                her "What have {b}you{/b} been doing lately? You've been reading a lot."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "Okay, well, that sounds very... necessary."
                her "I'm not just \"hanging out\", you know. I'm building relationships in the community that we are going to need if we are to survive. We can't make it alone here."
                him "You're right; I wish I didn't need anyone else, but I can't do everything."
            "I can't believe you don't appreciate me":
                jump unappreciated

    elif (highest_skill == "Knowledge"):
        him "You spend a lot of time reading, don't you?"
        menu:
            "Do I?"
            "It's important":
                her "I've been researching native plants that we can use when our reserves from Earth run out."
                him "Like what?"
                her "Well, we are working together on a list of edible plants, and I helped one of the families research how far their outhouse needed to be from the river."
                him "Oh yeah, that is important. Sorry, I didn't mean to accuse, I just was curious about what you're learning."
            "So do you":
                her "You read a lot, too."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "Okay, well, that sounds very... necessary."
                her "I've been researching native plants, and helping the other colonists with their research. One family was going to build their outhouse just 15 meters from the river, but after I did some research I convinced them to build it at least 75 meters away."
                him "That is really important. Thank you for doing that, [her_name]."
            "I can't believe you don't appreciate me":
                jump unappreciated

    elif (highest_skill == "Physical"):
        him "You spend a lot of time exercising, don't you?"
        menu:
            "Do I?"
            "It's important":
                her "I need to keep my body in good condition."
                him "For what?"
                her "Well, did you know that I can run to town in six minutes? And I am getting pretty good at chopping wood, which we'll need when the cold season starts and our solar panels don't work."
                him "Oh yeah, that is important. Sorry, I didn't mean to accuse, I just was curious about what you've been doing."
            "What do {b}you{/b} do?":
                her "What have {b}you{/b} been doing lately? You've been reading a lot."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "Okay, well, that sounds very... necessary."
                her "On that hike I found out about a new water source, and I can run to town in six minutes in case there's an emergency."
                him "Six minutes?! That's pretty fast. You must have been training a lot. I guess I haven't thought about doing that because I usually ride Lettie around."
                her "Well, not all of us have horses, so we have to make do with the legs we have."
                him "And what nice legs they are..."
            "I can't believe you don't appreciate me":
                jump unappreciated

    "We ended up staying up late, talking about all the things we had been doing. I felt like I understood him a little better after that, and he seemed to appreciate what I was doing more, too."
    return

# MONTH 5 - What to do with trash
label monthly_event_5:
    scene bg farm_interior with fade

    "The village council asked us to do a waste assessment to see how much and what kind of materials we needed to permanently dispose of. If the amount of waste was too high, they told us that future colonists would be limited."
    "Our waste pile was fairly small, as we'd already composted any organic material that we didn't eat. Still, there were things like packaging from the MREs, a broken dish, and a pair of worn-out socks."
    her "You threw away a perfectly good pair of socks?"
    him "Well, they have holes in the heels, and the rest of the material is getting thin. I wasn't sure if they were compostable."
    her "We can't just throw things away when they break like on Earth. We need to take care of this planet for future colonists and the life forms that are already here."
    him "Well, what should we do with all this stuff?"
    menu:
        "{i}I could see if any of our neighbors could use the fabric.{/i}" if (skill_social >= 20):
            her "One of my friends is making a quilt, and I think she could cut it up and use it for part of the batting."
            him "Someone will have my skin cells in their quilt! I'm grossed out just thinking about it."
            her "Oh, get over it. We'll wash them real good."
            him "Well, as long as she's okay with it."
        "{i}I could use the broken dish in an artwork.{/i}" if (skill_creative >= 20):
            her "If I crushed the dish pieces even further, I could make a mosaic with it."
            him "Well, mosaics are great and all, but that's not very practical."
            her "Maybe you could use them at the bottom of potted plants to help them drain better."
            him "Okay, okay, maybe there's a way I could use that."
        "{i}I could mend this sock.{/i}" if (skill_domestic >= 20):
            her "I've been practicing some sewing and I could darn these socks."
            him "Can this kind of sock even be darned?"
            her "I want to at least try."
            him "Okay, but we might have to think of another use for them if the darning doesn't work out."
            her "I could keep sock after sock until eventually I can make... a sock quilt!"
            him "..."
            her "Think of how fun it would be to put all the weird sock shapes together in a rectangle!"
            him "Um, well, I hope the darning works out."
        "{i}Let's think of a solution together.{/i}" if (skill_spiritual >= 20):
            her "It might be difficult, but I think if we work together we can think of some way to use these objects."
            him "Hmmm. I might be able to use the packaging from the MREs to separate small rows of crops."
            her "And maybe I could turn these pieces of plate into labels for the crop."
            him "Oh, that would actually be really nice for next year."
        "{i}This stuff is actually compostable.{/i}" if ((skill_knowledge >= 20) or (skill_technical >= 20)):
            her "Actually, we can just compost all these things. They may take a long time to break down, but they will eventually. We can speed the process by breaking them up and spreading them throughout the pile."
            him "OK, I'll cut up the socks."
            her "I'll smash the plate. That sounds satisfying, anyway."
            him "I guess this packaging we can tear into pieces like cave men?"
            her "You mean Paleolithic humans?"
            him "Rawr, rawr."
            her "Wow, you're so paleolithic."
            him "I'll take that as a compliment."
        "{i}I could dig a deep hole for them.{/i}" if (skill_physical >= 30):
            her "If I dig deep enough, we can just get rid of this stuff and no one will know that we couldn't think of a way to reuse them."
            him "It could be our little secret."
            "I dug and dug and dug. After I buried the items, it was nice to not have it cluttering up the house. And I didn't have to feel guilty about preventing other people from starting a new life here."
            "Still, I couldn't help feeling like I might have done better."
            $ relaxed -= 5
            return
        "I'm sick of making all the decisions.":
            her "Why do I have to decide? You're just as much a part of this household."
            him "Well if it's up to me, then let's just throw it all out."
            menu:
                "Fine.":
                    her "Fine. Then it'll be partly your fault if our colony is making too much waste for more colonists to come."
                    him "Good riddance! I came here to get away from them."
                    "It took me several trips to get our trash to the designated area. Someone there said they were trying to recycle as much as possible, but I felt bad for not even trying."
                    $ relaxed -= 10
                    $ loved -= 5
                    $ community_level -= 5
                    return
                "I don't want to throw it all out.":
                    her "I'll think of something on my own if that's how you feel."
                    him "Okay then."
                    "Over the next few days I tried to recycle the items I had, but nothing worked out. I ended up taking most of it to the designated dump. Someone there said they were trying to recycle as much as possible. At least I tried."
                    $ relaxed -= 10
                    $ loved -= 3
                    $ community_level -= 5
                    return
        "Let's compromise.":
            her "We could throw away half of this stuff, and then try to think of uses for what we keep over the next few days."
            him "Okay."
            her "Can you help me sort it?"
            him "Sure."
            "We sorted through our trash and decided to throw most of it away. [his_name] made a box for fresh produce out of some of the old packaging."
            "I was glad we could use some of it, but I felt bad that I didn't come up with anything."
            $relaxed -= 5
            return
            
    "We ended up throwing some of the waste items away, but I felt good about the effort I put it."
    $relaxed += 5

    return

# MONTH 6 - Alien Pests
label monthly_event_6:
    scene bg fields with fade

    "Our crops were starting to give an abundant harvest, but unfortunately, with the rainy season starting, the corn was being attacked by alien insects."
    "A small segmented insect like a sow bug but with thicker legs was our main culprit." 
    him "[her_name], we really have to think of a way to stop these insects from eating our corn."
    her "What have you done so far?"
    him "Well, I've tried picking them off individually and there are just too many now to do that. I wish we could just kill them all at once."
    her "I don't think we have the resources to do that."
    him "Yeah, that's why I was asking you for ideas."
    menu:
        her "Well, we have a few options."
        "{i}Take a sample bug in for research.{/i}" if (skill_knowledge >= 30 or skill_technical >= 30):
            "I collected a few of the insects and brought them to Lily for examination."
            lily "These samples remind me of Tardigrades we have on Earth."
            her "Tardigrades?"
            lily "They're an unusually hardy insect that can survive high and low temperatures as well as radiation. Because their adult forms don't increase in cell number, radiation doesn't damage their DNA like it does in animals whose cells are constantly splitting."
            her "That's... really interesting. Is there any way we could get rid of them?"
            lily "I've been working on an organic pesticide made from fungus. I'm not sure sure if it will work on these insects though. May I keep your sample to test the pesticide on?"
            her "Sure, there's plenty more where that came from."
            "I watched as Lily sprayed the bugs with her mineral oil and fungus concoction."
            her "Um, it looks like they're still alive."
            lily "Yes, if the pesticide works we will know in a few days."
            her "A few days? Our crops will be gone by then."
            lily "It is a rather pressing matter. Do you have any mature garlic cloves?"
            her "I think we do, but why?"
            lily "Garlic is a natural insect repellent. You'll still have to remove all the bugs, but if you can spray your plants with some diluted garlic it might stop them from returning as quickly."
            her "Well, it's worth a shot."
            "For the rest of the week we tried to to remove as many insects by hand as we could. Then we coated the plants with garlic juice. The work was long and hard, and we stunk afterwards."
            if (skill_physical > 20):
                "After a day's work in the field, I fell asleep right away, but in the morning I was ready to keep going."
            else:
                "After the first day I was exhausted. I wasn't able to help as much as I would have liked."
            him "We have baskets and baskets of these insects."
            her "I wonder if we could use them to help us somehow."
            him "Maybe we can. Next time you see Lily, could you ask her about it?"
            her "Sure. Come to think of it, we should know if her pesticide was successful or not by now."
            "Lily's fungus experiment successfully killed a little over half the bugs I gave her. She lent me a sprayer and told me to bring it back as soon as possible, since some other farms had the same insects to spray."
            "When I asked her about how to use the dead insects we had caught, Lily said that we could use them to feed livestock."
            her "I'm not sure if our horse will like how they taste, but I'll try it."
            "We sprayed our crops. Sadly, we couldn't save many of them. Luckily, our underground crops like potatoes and beets weren't attacked by the insects, so we still had something to eat while we planted new crops."
            her "Oh, Lily told me we could use the dead insects for something..."
            him "What is it?"
            her "We could feed them to Lettie!"
            him "Um... no."
            her "I think we should at least try it out! Maybe she'll like them!"
            him "Horses don't eat bugs!"
            her "Well I doubt they eat hay in the wild and it hasn't hurt them."
            him "I'll give her one, but if she gets sick or something, we are just going to crush the rest of the bugs and put them in the compost pile."
            "Lettie didn't seem to hate or like crushed insects, so I used them to extend her food. We still had a lot of leftover insects, so after making sure they were all dead I put them in the compost pile."
            him "I'm glad we could use some of the bugs, but I don't think the crops they ate will last."
            her "Why not?"
            him "They're full of insect eggs. The corn at least. Even if we pick all the infected crops off, I think it's too late to save them."
            her "Well, even if the corn is beyond saving, we could at least keep the greens for Lettie."
            him "And then some!"
            "We cut off and burned all the ears of corn that had eggs in them. We cut and dried all the corn stalks to turn it into hay."
            "[his_name] started plowing the land for a new crop."
        "{i}Use the bugs as food.{/i}" if (skill_domestic >= 30 or skill_creative >= 30):
            her "This is going to sound a little crazy, but I read that it's possible to make flour out of certain kinds of insects."
            him "Okay... will it actually help keep us alive?"
            her "If these insects are anything like Earth insects, they're highly nutritious. You know, low in saturated fats and carbs and high in amino acids."
            him "Well, can you find out if they're okay for us to eat? Because if we can somehow process them, we might not go as hungry this month."
            "I couldn't imagine eating them as they were, so after I boiled them, I ground them up and combined them with flour to make bread."
            "Well... it was more like crackers than bread, since the flour was so heavy. It was a little plain, so I made some beet jam to go with it."
            him "It tastes kind of nutty. Gross! Is this an insect leg?"
            her "Yeah, for the next batch I'm going to try processing the flour a little differently. But for a first try it's not bad, is it?"
            him "It's a whole lot better than nothing, that's for sure."
            "One day I sprinkled them with garlic salt and roasted them. They were crunchy and dry, but edible."
            him "So, eating these insects is great and all, but we should plant something else where that infested corn is right now."
            her "Yeah... how do we get rid of the plants that are already there?"
            him "Well, I could burn them all, and then the ashes can fertilize the next crop."
            her "Sounds better than nothing."
            "We piled all the corn plants into a huge bonfire. It burned into the night and made a big plume of smoke."
            "Our neighbors the Perons came by the see the fire, and we ate roasted insects as we watched the egg-infested crops turn to ash."
        "{i}Ask if anyone else is having the same problem.{/i}" if (skill_spiritual >= 30 or skill_social >= 30):
            her "Let's ask around and see if anyone else has had problems with these pests."
            him "Okay. I'll take Lettie into town; can you ask our neighbors?"
            her "Sure."
            "I found out that the Blairs had the same insect eating their corn. To prevent the insects from laying eggs in the corn, they put mineral oil on the silks."
            "I radioed [his_name] and asked him to bring back some mineral oil from the storehouse. For the rest of the week, we put the oil on our corn silks and picked off the insects by hand."
            "I kept in touch with the Blairs for the rest of the week, and we made a huge pile of dead insects, which we ground up to extend the food we had for our livestock."
            "We were able to preserve some of our corn until it was ready for harvest, although for most of the corn, it was too late."
            "We had a big bonfire with the Perons and burned the infested corn. Their kids danced around the fire as we roasted one of their chickens on the side."
            ## TODO: this section could be expanded by having a dialogue with one of the Blairs?
        "Spray them with pesticide":
            him "We have some pesticide that we used for corn pests on Earth."
            her "Will it work on these bugs?"
            him "I don't know. Usually you apply it before the pests start eating the corn - it works better as a preventative. I hadn't put any on here because I didn't think any of the bugs here would eat an alien plant species."
            her "Seems like these bugs will eat anything."
            him "Yeah, well, let's give it a try."
            "We got some sprayers and face masks and gloves from the storehouse and got to work. Even with the face masks, the stuff smelled awful. It took all day to cover all the fields."
            "We tried to control where we sprayed, but it was windy and it kind of got everywhere."
            "When we were finally done, I had a terrible headache."
            her "Are we really going to eat the corn after we sprayed this poison on it?"
            him "If it works, yes. We don't have enough food to pick and choose."
            "It did seem to get rid of a lot of the pests. Whenever we ate it, I washed it really well, but it always tasted a little funny to me."
            
        "I have no idea.":
            her "I don't have any ideas...I'm sorry."
            him "Well, let's try to salvage what we can."
            "All of the above-ground crops had been partially eaten by the insects. I started trying to cut off the bitten parts, but then I found eggs laid inside some of the corn. We didn't want the insects to keep coming back, so we ended up burning our corn field."
            him "At least our next crop will have some really rich soil to grow on."
            her "Yeah, and at least we have some potatoes, beets and ginger to eat for the next few months."
            him "But what if more insects destroy our existing crops?"
            her "Then we might have a very limited diet. Hopefully someone will find a way to keep them at bay."
            $ community_level -= 5
            return
            
    $ community_level += 5
return

# MONTH 7 - Broken computer - honesty?
label monthly_event_7:
    scene bg farm_interior with fade
    "One day I was doing the dishes at breakfast. [his_name] had already started working in the fields, so I was alone. I noticed he had left his computer pad next to the wash basin."
    her "I'll just move this out of the way so it doesn't get-- AHHH!"
    "It slipped out of my hands right into the soapy dishwater."
    her "Oh no!"
    "I took it out and dried it off, but it wouldn't turn on. Water must have seeped inside."
    $ fixed_computer = False
    menu broken_computer_pad:
        "What should I do?"
        "{i}Try and fix it{/i}" if ((skill_technical >= 40) and (not fixed_computer)):
            "I thought that if it dried out, it would probably work just fine, so I opened the cover and set it on the windowsill in the sun to dry."
            "Sure enough, after a few hours, it turned on just fine."
            $ fixed_computer = True
            "But there was still the question of whether to tell him about it or not..."
            "On the one hand, it works just fine, so he doesn't need to know about it, right?"
            "On the other hand, I don't want to keep secrets from [his_name], even dumb secrets. I want us to be able to trust each other completely."
            jump broken_computer_pad
        "Put it back and pretend not to know what happened":
            "I put it back where I found it. It was just an accident, so he doesn't need to know it was my fault, right?"
            "Even so, I was nervous when he got home."
            him "Hey there, [her_nickname]."
            her "Hi."
            "He washed his hands, and then picked up his computer pad."
            if fixed_computer:
                "I think he was checking his messages; it seemed to work fine. I started to feel a little less nervous."
                "I felt kind of bad for lying to him, but I didn't want him to be mad at me or think I was incompetent...it's not like I was lying about something important, right?"
                $ loved -= 2
                $ relaxed -= 5
            else:
                him "Hey, how come this won't turn on?"
                her "Oh, your computer's not working?"
                him "Yeah, it was working fine this morning..."
                her "Hmmm, I don't know."
                him "Well, I guess I'll take it in to the tech guys tomorrow if it's still not working. Do you mind if I use yours to check my messages?"
                her "Sure, go ahead."
                "Hopefully they would be able to fix it... "
                "I felt kind of bad for lying to him, but I didn't want him to be mad at me or think I was incompetent...it's not like I was lying about something important, right?"
                "The next day at dinner, it looked like his computer was working."
                her "Oh, you got your computer working?"
                him "Yeah...I opened it up, and it was wet inside. Like someone had dropped it in some water."
                menu:
                    "Tell him what happened.":
                        her "I dropped it in the sink the other day...that's why it's wet. It was an accident; I'm sorry."
                        him "So, you lied to me."
                        her "Yes, I'm sorry."
                        him "Wow, I can't believe you didn't just tell me about i."
                        her "What's the big deal? It works now, doesn't it?"
                        him "This isn't about the computer! If you lie about something small like that, who knows what else you might lie about?"
                        her "Hey, I told you about it eventually."
                        him "Only when you got caught in your lie!"
                        her "I said I was sorry, okay?!"
                        him "...Okay."
                        $ loved -= 2
                        $ relaxed -= 2
                    "{i}Apologize sincerely.{/i}" if (skill_spiritual >= 40):
                        her "I'm sorry, [his_name]. I dropped it in the sink, and then I didn't tell you about it because I didn't want you to know how clumsy I was. But I should have told you; I'm so sorry."
                        him "The computer's not a big deal, but we need to always be honest with each other."
                        her "I know; it was stupid of me to lie about it."
                        him "It's okay, [her_name]."
                        "He hugged me and I could tell he had forgiven me."
                    "Pretend you don't know.":
                        her "I wonder how that happened?"
                        him "You really don't know anything about it?"
                        her "No, sorry. Anyway, it works now, so what does it matter?"
                        him "..."
                        "He dropped the subject, but I could tell he didn't believe me. Well, whatever, it's not a big deal."
                        
                        $ loved -= 5
                        $ relaxed -= 5
        "Leave it on the table and tell him when he gets home":
            "I left it on the table so I would remember to tell him about it when he got home."
            him "Hey there, [her_nickname]."
            her "Hi."
            "He washed his hands, and then picked up his computer pad."
            him "Did I leave this here this morning?"
            her "No, actually, you left it by the wash basin...and it fell in while I was washing the dishes."
            if fixed_computer:
                her "But I fixed it, so don't worry. It just needed to air out a little."
                him "Okay, hopefully everything still works fine..."
                "I waited while he logged on and checked a few things."
                him "Seems to be fine. I probably shouldn't leave my computer pad there, huh?"
                her "Probably not. Sorry I dropped it in the water, though."
                him "It's okay; no harm done."

            else:
                him "That explains why it won't turn on..."
                her "I'm really sorry; I feel so clumsy. I was trying to move it, so it wouldn't fall in, but it slipped out of my hands."
                him "..."
                her "I'm sorry..."
                him "It's okay- I shouldn't have left it by the washtub. These things happen."
                her "Maybe they can fix it in town?"
                him "I'll check tomorrow."
                her "In the meantime, do you want to use my computer? It's only fair."
                him "Thanks, yeah."
                "I could tell he was kind of disappointed, but I felt glad I wasn't hiding anything from him."
                "And when he took it in, they were able to fix it so it worked just fine."
            $ loved += 2

    scene black with fade
    "A week later, I was reading my messages when I noticed that they were having a New Year's party."
    her "Has it really been a whole year that we've been here?"
    him "Well, a year on this planet is only seven months, but, yeah. It's good for farming to have a shorter year, especially since the winters are so mild."
    her "Happy New Year, then!"
    him "We should make a toast..."
    menu:
        "What should we toast?"
        "To us!":
            her "To us!"
            if (loved >= 0):
                him "May we have many more years together..."
            else:
                him "To us, then."
        "To the colony!":
            her "To the colony! We made it one year!"
            him "May we all survive many more!"
        "To humanity!":
            her "To humanity! We're still here!"
            him "To humanity!"
        "To partying!":
            her "Here's to any excuse to party!"
            him "To partying!"
    return

# MONTH 8
label monthly_event_8:
    scene bg library with fade
    "The library had a huge collection of Earth media that colonists could check out. They only had enough space for the most popular things, but it was still more media than anyone could experience in a lifetime."
    "One day I noticed they had a movie about space colonists. I was curious to see how people on Earth saw people like us, so I checked it out."
    scene bg farm_interior with fade
    her "What do you want to do tonight? I checked out a movie that looks fun..."
    him "Oh, sorry, I told Thuc I'd help him build a fence tonight. He helped me build ours to keep the animals out of the crops, so I said I'd help with his."
    menu:
        "I was disappointed, but..."

        "Can't you do it another night?":
            her "Can't you help him another night? I was really looking forward to watching this with you."
            him "No, sorry, it has to be tonight."
            her "Okay, see you later."
            him "Bye, [her_nickname]."
            "The house suddenly seemed so quiet. I usually didn't mind being alone, but I had really been looking forward to this. The wind whistled mournfully through the cracks in the walls."
            menu:
                "What should I do?"
                "Watch it without him":
                    her "Forget it, I'm watching it without him!"
                    "It was full of drama, comedy, and funny inaccuracies about space colonies, but I didn't really enjoy it..."
                    $ relaxed -= 5
                "Do something else":
                    "I tried to distract myself with a book, but I wasn't really having fun."
                    $ relaxed -= 5
                "...":
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something fun with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    $ relaxed -= 10
            "Finally, I just went to bed."
            scene black with fade
            "Everything seemed fine the next day, but I still felt insecure."
            $ loved -= 2

        "I'll help, too.":
            her "I'll help too!"
            him "Do you really want to?"
            her "Yes, we all need to work together to succeed. Plus, I'll get to be with you."
            him "All right, let's go!"
            "Thuc had already cut some logs and branches for us to tie up, but we still had to dig holes for posts."
            if (skill_physical >= 20):
                "It was a good thing I came, because there was a lot of hard work to do."
            elif (skill_technical >= 20):
                "It was a good thing I came, because I pointed out a better way we could make the fence that would be really sturdy."
            else:
                "I'm not sure I was much help, but I worked hard and did my best."
            "We worked hard in the gathering darkness, until the moons rose and gave us their wan light. We worked on and on, until finally it was done."
            thuc "Thank you so much, both of you."
            him "Glad we could help. I hope this fence holds up for you."
            thuc "Well, you can count on my help anytime, if you need it."
            her "Thanks, I'm sure we will."
            "We walked home by moonlight.  The two moons cast opposing shadows from the shrubs and trees, making a maze of light for us to follow. [his_name] reached for my hand."
            him "Thanks for coming. Everything's better with you."
            her "Even putting up fences is not too bad when we're together."
            $ loved += 5
            $ skill_physical += 5
            $ community_level += 5
            scene black with fade
  
        "Want to watch it another night?":
            her "No problem, we'll just watch it another night."
            him "Thanks for understanding. I'll see you later, [her_nickname]."
            "It was a little lonely, especially since I was really looking forward to watching the movie with him, but I soon was absorbed in a good book and then went to bed."
            scene black with fade
            "We watched the movie the next night. Even though they got a lot of things wrong about space colonization, we really got into the drama and tension. We both cried a little at the end."
            $ relaxed += 5
            $ loved += 5
  
        "You're never here when I need you!":
            $ loved -= 5
            her "You're never here when I need you!"
            him "What are you talking about? I'm home almost every night."
            her "But you're always on your computer; I wanted to do something together tonight."
            him "Well, I can't. I promised Thuc I'd come tonight."
            her "I'm not really important to you, am I?"
            him "What?! Of course you are!"
            her "Then stay home with me!"
            him "No, I'm not going to break my promise. Now I have to go, we want to get this done before the moons set."
            menu:
                "He's leaving..."
                "Fine, just leave me here.":
                    her "Fine, just leave me here."
                    "He didn't say anything, just shook his head. I watched him leave, feeling hurt and lonely."
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something fun with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    scene black with fade
                    "I forgave him the next day, but I still felt insecure."
                    $ relaxed -= 5
                    "Finally, I just went to bed."
                "...":
                    "I didn't say anything; just watched him leave, feeling hurt and lonely."
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something fun with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    $ relaxed -= 5
                    "Finally, I just went to bed."
                    scene black with fade
                    "I forgave him the next day, but I still felt insecure."
                "Sorry":
                    her "Sorry, [his_name]. I'm being selfish."
                    him "It's all right, [her_nickname]. Let's do something together tomorrow night, okay?"
                    her "Okay, [his_name]."
                    "We watched the movie the next night. Even though they got a lot of things wrong about space colonization, we really got into the drama and tension. We both cried a little at the end."
                    $ relaxed += 2
                    $ loved += 5
    return

# MONTH 9 - how could I do better?
label monthly_event_9:
    scene bg farm_interior with fade
    play music "music/You.ogg" fadeout 2.0
    him "I was just thinking about you. How do you think we're doing?"
    her "Doing what?"
    him "You know, in our marriage. Do you feel loved, is this working for you?"
    menu:
        "Honestly, no" if (loved <= 0):
            her "Honestly, no, it's not."
        "(Lie) It's fine" if (loved <= 0):
            her "Yeah, it's okay, I guess."
        "It's fine":
            her "It's fine; I haven't really had time to think about things like that."
        "It's wonderful" if (loved >= 0):
            her "Of course! It's great!"
    if (loved > 0):
        him "Is there anything I can do to be a be a better husband to you?"
    else:
        him "How can we make it better?"

    menu:
        "Give me stuff":
            her "I'd like if you gave me gifts - nothing big, obviously, but just something little to show you were thinking about me."
            him "Really? You like that sort of thing?"
            her "Yes, it would mean a lot to me."
            $ she_wants = "stuff"
        "Tell me how much you love me":
            her "I'd love it if you told me how much you love me."
            him "Ummm... a lot?"
            her "No! Not like that! Like, what is it you like about me, and tell me things I do that you like, stuff like that."
            him "That's what you like? Words?"
            her "Yeah. You have to mean it, of course."
            $ she_wants = "saynicestuff"
        "Do things together":
            her "I want to do things with you more often."
            him "What kinds of things?"
            her "Anything - go on walks, make dinner together, play games together."
            $ she_wants = "dostuff"
        "Do things for me":
            her "I'd like you to do little things for me sometimes."
            him "Like what?"
            her "Like, washing the dishes when it's my turn, or picking something up from the storehouse, or things like that."
            $ she_wants = "service"
        "Show more affection":
            her "I'd like to hold hands more, hug more, just be close to each other more."
            him "How about rubbing your shoulders? Like this?"
            her "Ohhh yeah, that definitely is good."
            $ she_wants = "affection"
        "Nothing":
            $ she_wants = "nothing"
            her "You don't need to do anything differently; you're doing just fine."

    menu:
        "Thanks for asking":
            her "Thanks for asking; that's really sweet of you."
            $ loved += 2
        "How about you?":
            her "What about you? Is there something you'd like to see more of from me?"
            him "Well..."
            if (made_love < 2):
                him "I'd like it if you showed more physical affection."
                menu:
                    "Typical man":
                        her "Typical. That's all you men ever think about, isn't it?"
                        him "No, sometimes we ask our wives what they would like and try to do it."
                        $ loved -= 5
                    "It's hard":
                        her "That's... hard for me. I'm just so tired all the time; sometimes it feels just like another chore."
                        him "It's a chore?"
                        her "No! It's just... it takes work for me to be in the mood, sometimes."
                        him "Well, you asked what I'd like."
                    "OK, I'll try":
                        her "We should make love more... it's important, even if we're tired or busy."
                        him "Thank you, [her_nickname]."
                        $ loved += 5
            elif (skill_domestic < 10):
                him "I'd like it if you did more things around the house."
                menu:
                   "That's sexist":
                        her "That's sexist. Women belong in the house, is that it?"
                        him "Hey, you asked what I'd like. I'd like to come home to a clean, well-organized house."
                        menu:
                            "If it's that important to you...":
                                her "If it's that important to you, I could work on that."
                                $ loved += 5
                            "No way.":
                                her "Sorry, that's never going to happen."
                                him "..."
                                $ loved -= 5
                   "It's hard":
                       her "That's... hard for me. With work and everything, when I come home I just want to relax."
                       him "Well, you asked what I'd like."
                       menu:
                           "If it's that important to you...":
                               her "If it's that important to you, I could work on that."
                               $ loved += 5
                           "No way.":
                               her "Sorry, that's never going to happen."
                               him "..."
                               $ loved -= 5

                   "OK, I'll try":
                       her "It would be nice if the house was a little neater... OK, I'll try to do that."
                       him "Thank you, [her_nickname]."
                       $ loved += 5
                   "Let's work on it together":
                       her "How about if we take some time one evening and clean up the house together?"
                       him "Yeah, I guess we could do that."
                       $ loved += 2

            elif (loved < 5):
                him "I'd like it if we spent more time together."
                $ loved += 5
                menu:
                    "Me too":
                        her "I'd like that, too."
                        him "Let's go on a walk together."
                        her "Right now?"
                        him "Right after dinner!"
                    "Doing what?":
                        her "Yeah, but what should we do? There's not exactly a lot going on..."
                        him "I could read you Shakespeare."
                        her "Ha ha ha!"
                        him "..."
                        her "You're serious?!"
                        him "Well, I don't know! Doesn't it sound kind of fun to read to each other things that we like?"
                        her "We could try it!"
                    "We don't have time":
                        her "That sounds good, but we don't really have much free time, do we?"
                        him "We have been working pretty hard...but I think it's important to do things together. Even if we're just reading next to each other, that would be nice."
                        her "OK, we can do that."
            else:
                him "Nothing at all. You always make me feel loved."

    "I wondered if he would actually do anything based on what I said I liked. A few days passed and I figured he had forgotten all about it."
    if (loved >= -5):
        "But then..."
        $ loved += 5
        if (she_wants == "stuff"):
            "He brought me some wild fruits he had found. He even checked with Dr. Lily to make sure they were edible first."
            her "Thank you!"
            him "They're just for you."
        if (she_wants == "saynicestuff"):
            him "Your laugh is like a supernova that blasts away my stress and makes the whole world seem like a garden."
            her "Ha ha ha, ha ha, really?"
            him "Yes, and I love how you're such a good [profession]. Not only do you know what you're doing, but you're nice to people about it, too."
            her "Thank you, [his_nickname]."
        if (she_wants == "dostuff"):
            him "Hey, want to go fishing?"
            her "Fishing? I didn't know there were fish here..."
            him "Well, they're not exactly like fish, but there's plants and animals that live near the river that we can eat. Did you see Dr. Lily's email?"
            her "I didn't read it yet... but it sound fun to do something with you!"
            "We found some edible plants, but when we tried to catch the animals there to eat, we ended up falling in the river together. We were laughing so hard we could barely stand up."
        if ((she_wants == "service") or (she_wants == "affection")):
            "After dinner one night, he started rubbing my feet."
            her "Thanks, but I really ought to do the dishes now."
            him "No way. I'm taking over tonight. It's [her_name] night."
            her "I've never heard of that holiday before."
            him "That's because I just made it up."
            "He did the dishes for me and rubbed my feet with a smile."
            her "Thank you, [his_nickname]."
        if (she_wants == "nothing"):
            "I found a poem on my pillow one afternoon:"
            "you are the sweetest thing\n not like honey or sugar"
            "but like the nectar of a bright flower\n you sustain even the clumsy bumblebee."
            her "(That was sweet of him...)"
            
    else:
        "Of course he wasn't serious about it. I shouldn't have gotten my hopes up, I guess."
        $ loved -= 5

    return

# MONTH 10 - Anniversary / Lettie is sick!
label monthly_event_10:
    scene bg farm_interior with fade
    play music "music/Prelude02.ogg" fadeout 2.0
    "It was our anniversary, according to the Earth calendar.  I think we had missed a few while we were on the shuttle? Anyway, it felt like we had been married about a year."
    her "Happy Anniversary!"
    him "Really? Today?"
    her "Yeah! Well, it depends on how you calculate it, but I feel like celebrating it today!"
    him "Great, what do you want to do?"
    her "I'll make us a nice dinner tonight."
    him "Okay, I'll bring home a surprise for you."
    her "Really?"
    him "Yeah! I mean, don't expect too much, but I've got an idea."
    "All day long I looked forward to spending a nice evening together. I got some special ingredients at the storehouse, and made a nice dessert and everything. But [his_name] wasn't home yet."
    her "(He knows we were going to celebrate today! Where could he be?)"
    "I tried calling him on the radio, and messaging him on the computer, but he didn't answer."
    "Finally, just when I was about to give up and eat without him, he stepped in."
    menu:
        "He's so late..."
        "Is everything okay?":
            her "You're home late, [his_nickname]. Is everything okay?"
            him "Yeah."
            $ loved += 1
        "Did you forget about tonight?":
            her "You're home late - did you forget about our anniversary dinner tonight?"
            him "Yeah."
        "Where have you been?!":
            her "Where have you been?! I've been waiting here for an hour!"
            $ loved -= 1
    "He didn't look at me, just washed his hands and sat at the table. He was reading on his computer pad while we ate dinner.  We ate in silence for a few minutes. I thought maybe I'd change the subject."
    her "Something funny happened at work today."
    him "Yeah?"
    her "Little Sasha, you know, the Blair's youngest, came by with his mom, and he said, 'I am an alien that looks like a kid. I really am. I'm not pretending.'"
    him "Yeah?"
    her "Yeah, it was funny, because he's so serious about it..."
    him "Mmmmm."
    menu:
        "What should I say?"
        "Are you listening to me?":
            if (relaxed >= 0):
                her "(Is he even listening to me?!)"
                her "Also, I was thinking after dinner I'd take off all my clothes and parade downtown."
                him "Yeah."
                her "Why don't you come with me?"
                him "Mmm-hmmm."
                her "Great! What song shall we sing?"
                him "Hmmm- what?"
                her "What song are we going to sing as we're dancing around town naked?"
            else:
                "Are you even listening to me?!"
                $ loved -= 5
            "He just looked at me for a minute, then shook his head."
            him "Sorry, [her_name], not right now. I've got to check on something."
            jump follow_him

        "{i}What's bothering you?{/i}" if ((skill_spiritual >= 40) or (skill_knowledge >= 40)):
            her "You seem troubled. What's bothering you, [his_nickname]?"
            "He was quiet for a minute, finishing up his dinner. I was about to ask again, when he said,"
            him "Sorry, [her_name]. I can't talk about it right now. I've got to go check on Lettie."
            her "Is she okay?"
            him "I don't know."
            "He headed out the door."
            jump follow_him

        "(Say nothing)":
            "I figured he would tell me what was bothering him when he was ready."
            jump anniversary_next_day

label anniversary_next_day:
    "He didn't come home that night, just stopped in for a quick breakfast early in the morning and then left again. I didn't have a chance to talk to him again until that evening when I got home."
    him "Hey, [her_nickname]."
    menu:
        "(He's just saying hi like nothing happened!)"
        "Ignore him":
            her "(He ignored me all last night; let's see how he likes it.)"
            her "..."
            him "Hey, are you mad?"
            menu:
                "(Am I mad?!)"
                "Yes!":
                    her "Yes, I'm mad! We were supposed to have a nice dinner for our anniversary, but you just left without saying anything!"
                    him "Lettie was sick! Really sick!"
                    her "And you couldn't have said something like, 'Sorry, Lettie's sick, gotta go.'?"
                    him "I'm sorry; I was too worried."
                    her "Well, is she okay?"
                    him "Yes, she's fine now. Um, here, I got you these."
                    "He handed me a glass bottle with wildflowers in it."
                    her "Oh! Thank you, [his_name]."
                    him "Happy Anniversary."
                    "We kissed perfunctorily. I still felt a little mad, but we'd get over it."
                "No.":
                    her "No, why would I be mad? Where I come from it's totally normal to ignore your wife on your anniversary."
                    him "Lettie was-"
                    her "Lettie?! You were thinking about your HORSE?!"
                    him "Tch, forget it! You are obviously more interested in your own righteous anger than in knowing what actually happened. Here."
                    "He slammed a glass bottle with some wildflowers in it on the table. Water sloshed onto the table and a few of the flowers fell out."
                    him "Happy Anniversary."
                    "Then he stormed out."
                    $ loved -= 5
        "Ask what happened":
            her "What happened? Last night you were really worried about something."
            him "Oh, it was Lettie. I think she ate something poisonous while she was grazing - she was really sick. But she's doing better today; I think she'll be fine."
            her "Oh, I'm glad she's okay."
            him "Yeah, me too."
            him "Sorry about last night - I know we were going to celebrate our anniversary and everything, but I just couldn't celebrate when I was so worried about her. But I did get you something."
            her "What?"
            "He pulled out some wildflowers - he must have picked them earlier today. He had put them in an old glass bottle for a vase."
            him "The little bit of beauty these flowers bring can't compare to the joy you bring to my life. They won't last forever, but my love for you will."
            menu:
                "What should I say?"
                "They're lovely!":
                    her "Oh, they're lovely! Thank you!"
                    him "Sorry it's not much..."
                    her "It's just right. I love you, too."
                "Thank you.":
                    her "Thank you."
                    him "Sorry it's not much."
                    her "It's okay; we don't have much."
                    him "But I'm so glad I have you."
                "At least it's not another cheesy poem.":
                    her "Ha ha, at least it's not a cheesy poem like for my birthday."
                    him "Hey! I worked hard on that poem! I poured out my heart to you!"
                    her "I know, and it was really sweet... but also really cheesy."
                    him "Well, at least I learned my lesson."
                    her "I think there's still a few things you could learn."
                    him "Are you going to teach me?"
            "I didn't even have time to set the flowers down before he wrapped his arms around me. I kissed his chin, then his lips, and we forgot about everything else for a while..."
            $ made_love += 1
            $ loved += 5
    return

label follow_him:
    menu:
        "Go with him.":
            her "I'll help you."
            him "Okay."
            "We walked to the small barn where the animals could sleep at night, and where we could keep hay dry. Lettie was inside, twitching and breathing hard."
        "Follow him quietly.":
            "I waited until he left, then I silently lifted the latch and followed him out."
            "He headed for our small barn. I followed him inside, where I saw his horse Lettie.  She was twitching and breathing hard."
        "Let him go.":
            "He'd tell me what was bothering him when he was ready. I decided to settle down with a book and wait until he came back."
            jump anniversary_next_day

    her "What's wrong with her?"
    him "I think she ate something bad. Usually she's fine grazing on the things here, but maybe it was a strange plant she didn't know was poisonous?"
    her "Oh no! Is there a vet or someone you can call?"
    him "I am the vet, or the closest thing we have, anyway."
    if (profession == "doctor"):
        her "Can you induce vomiting?"
        him "No...horses can't vomit."
        her "I can give her some medicine to help the pain at least..."
        him "Please do; I'm worried she's going to hurt herself."
        "I did a quick search on my computer to see what medicines were safe for horses.  Then I got my bag and gave her an analgesic. She seemed to calm down a little."
    else:
        her "Oh no! What can we do?"
    him "Maybe we can help whatever's bothering her to pass through. Do we have any mineral oil? Or milk of magnesia?"
    if (profession == "crafter" or skill_creative >= 40):
        her "They have some mineral oil in the workshop; I'll get it."
    elif (profession == "doctor"):
        her "There's some laxatives at the clinic; I'll get some."
    else:
        her "Somebody's got to have some! I'll ask Ilian at the storehouse."
        "I got on my computer and sent him a message. I also sent one to the doctor and the Blairs, in case they had any ideas."
        "Ilian got back to me pretty quick and said he could get some and he'd meet me at the storehouse."

    if (skill_physical >= 40):
        "I ran all the way there and back. Good thing I was in shape."
    else:
        "I walked and jogged as fast as I could. I was breathing so hard I thought I was going to throw up when I finally got back."
        $ relaxed -= 5

    "He had me hold Lettie still while he measured it out and administered it to her. I was amazed how much Lettie trusted him."
    "She didn't seem to feel any better right away, but I knew this kind of medicine takes awhile to work."
    him "I'm going to take her for a little walk - why don't you get some rest?"
    menu:
        "Should I get some rest?"
        "I'll stay with you.":
            her "I'll stay with you."
            him "Okay."
            "We walked around with Lettie for a while, and then we let her rest and have plenty of water to drink. She still didn't seem to feel better, but she wasn't getting worse, either."
            "[his_name] sat down in some clean hay. It was a little scratchy, but I sat down next to him."
            "I must have fallen asleep, because I woke up and it was morning. We had spent all night in the barn..."

        "Okay, hope she feels better.":
            her "I think I will. I hope she feels better, soon."
            him "Thanks, [her_name]."
            "I didn't sleep that well that night."
            "The next morning, I decided to check on Lettie and [his_name]."

    "[his_name] was already up, talking to Lettie in a soft voice and petting her nose. She wasn't shaking any more, and her breathing seemed more regular."
    her "She seems better!"
    him "Yeah, I hope so. I'll give her some really good food today and let her take it easy for a while."
    her "Well, I have to get to work, but I'll see you this evening."
    him "Hey, thanks for staying with us, and helping out. It was a lot better not having to wait alone."
    her "You're welcome. I'm glad we could help her."
    "He turned to me and wrapped his arms tight around me. His voice was a little hoarse as he whispered,"
    menu:
        him "Everything's so fragile...\nI love you, [her_name]."
        "I love you, too.":
            her "I love you too..."
        "You owe me big time.":
            "I pulled away enough to poke at his chest sternly."
            her "You owe me, [his_nickname]. Last night was our anniversary dinner - I don't think you even noticed because you were so distracted - but you owe me a fabulous night tonight."
            him "Our anniversary! I'm so sorry - but I will make it up to you tonight."
            her "Shall I make a list for you?"
            him "I think I know what you like."
            $ made_love += 1
    $ loved += 10
    $ relaxed += 2
    return

# MONTH 11
# uses knowledge, physical, creative
#I read about rocket stoves and thought it would be fun to write an event on them http://www.richsoil.com/rocket-stove-mass-heater.jsp   
label monthly_event_11:
    scene bg farm_interior with fade
#do we have a winter? I think there was a winter, but it was a mild one or something?
    "It was another cloudy day, and there wasn't enough solar power to cook and warm our house with."
    him "I'll go get some wood. Can't we just cook inside?."
    her "No, remember how our chimney has a huge crack in it?"
    him "I'll cook outside then."
    her "There's got to be a better way to distribute all this energy."
    "I spent the evening researching low-power heating. Some people found that light bulbs helped heat their houses, but we had LEDs that didn't give off much heat."
    "I found a type of combustion stove called a rocket stove, which burned wood sideways very cleanly. I'd need some metal pipes though." 
    "I knew we were saving a lot of the metal from the shuttle for emergencies. I wasn't sure what I would do."
    her "If we want to advance technologically, we've got to start making our own metal. It's like, the next thing on the tech tree."
    him "Actually, I heard that Lily is gathering ores to see if we can start making our own metal here. But I think gunpowder is next on the tech tree."
    her "Really? Why didn't anyone inform me?"
    him "Well, you're not digging around in the dirt during your working hours. She probably just sent it out to all the farmers."
    "I ran over to the lab the next morning, excited to help."
    her "I heard you've been gathering ore?"
    lily "Yes! Do you have some you'd like to donate?"
    her "I don't, but I'm willing to test the material's melting point!"
    lily "Are you hoping to make something?"
    her "Yes, I want to make a rocket stove to heat our house on cloudy days."
    lily "I don't really have enough to make anything with it yet, but I can help you find more metal."
    lily "I've received samples of three different ores, and I think one could make the kind of metal you're looking for. You'd need to go mining for it though."
    her "Mining, like with a pick?"
    lily "Yes. I think gunpowder would help a lot too."
    her "Blowing up rocks? Is that allowed?"
    lily "Well, we are supposed to survive in a way that doesn't damage the existing ecosystem excessively."
    her "Tell me where you think the metal is and I'll see if I can get it out using our pick. I don't think I want to think about gunpowder quite yet."
    lily "I will tell you where the metal is, but I want your help collecting some samples from a semi-remote location first."
    her "Don't you think metal is more important than documenting organisms?"
    lily "No, I don't. Any you never know, maybe one of these creatures will have  an iron lung or something."
    her "Okay, what do I need to bring?"
    lily "Well, a backpack, food, and another person."
    her "Another person?"
    lily "Yes, it's much safer to travel in a group of three than a group of two. At least, that's what I believe from my observations and the small amount of anecdotal evidence on the behavior of the local carnivores."
    her "When do you need me to be ready?"
    lily "Well, the next low-low tide is in two days. That's when the moons should be in sync long enough to make a tide anyway."
    her "Okay, I'll talk to [his_name]."
    #change scene to home
    her "Hey, [his_name], do you want to come to the ocean with me?"
    him "Wouldn't it take half the day just to get there? Why do you want to go?"
    her "Lily said she would help me find and purify metals if I helped her collect specimens at the ocean."
    him "That sounds fun, but I'm worried that if I take a day off from farming, my plants will die."
    her "Really? They would die if you left them just one day?"
    him "Well, it's more like some of the food might get eaten by something else since it's harvest time again."
    her "Okay. I'll try to find someone else"
    menu:
        "Who should I ask to come?"
        "Sven, the librarian":
                #change scene to library
                her "Hey, Sven."
                sven "Hi, how can I help you?"
                her "Want to come with Lily and me to the seashore?"
                sven "The seashore? The one about six miles away?"      
                her "Yeah, a real beach! Bring a shovel!"
                sven "No thank you. Not after what I've been reading about giant sea creatures and this planet."  
                her "What have you been reading?"  
                sven "Well, I read that the animals in the ocean probably tolerate radiation the best, since the water can diffuse the radiation. The satellite telescope that came with us showed some strange, large shadows in a few of the oceans, and no one knows what they are."
                her "It could be a whale or something?"
                sven "No. These are much bigger. It kind of creeps me out."
                her "Well, we're not going out to the middle of the ocean, just the shore. Wouldn't it be fun to get out of your stuffy library for a day?"
                sven "Now that you mention it, I have been wanting to go for a hike, but I didn't want to go by myself."
                her "Just think of it as a long hike, and if the beach scares you you can stay far away from it."
                sven "Okay, I think I can manage that."
                "There wasn't a road going out to the ocean, so we had to make our way through wild vegetation."     
                "We had some minor run-ins with small insects, but nothing too surprising." 
                "Arriving at the ocean was magnificent. The air was moist, and my eyes could rest on a flat plane of wetness extending to the horizon."
                sven "Wow, this beach reminds me Earth. Lots of rocks and a big blue wet thing." 
                her "I think you mean ocean. It's making me a little homesick too." 
                lily "I'm so glad we made it! Okay, I'd like to take samples of this crusty white stuff and any other organic material you can find."     
                sven "Okay, you guys do the stuff on the shore, and I'll help gather some of this coastal brush." 
                lily "I'm going to take some of the smaller creatures and plants back too."
                her "How much of this white stuff do we need?" 
                lily "The guano? Just get as much as you can. We have an hour or two so don't feel too rushed."
                her "Eww! It's excrement? Well, I guess if it's for science I can do it."
                "We worked hard to get the samples we needed. We found a lot of shells and some bones. As we were getting ready to leave, the tide started to come back in."
                "The incoming waves were purple with one kind of alien sea creature. It had six spiny or hairy arms, and floated like a jellyfish."  
                lily "Oh! I've got to record this."
                sven "Be careful! Those things could be deadly for all we know!"
                "It surprised me how quickly the tide rushed back in. Little spider-crabs rushed to dry rocks, and many got swallowed up by the waves and the purple jellies."
                "A wave splashed under Lily's feet, and one of the purple spiny jellys grabbed at her leg"
                lily "O-oh!"
                "Sven looked on in horror as I jabbed the animal with my shovel. As I contacted it, its arm fell off, still wrapped around Lily."
                if (skill_physical >= 40):
                    "Lily had a strange look on her face, so I carried her further inland so she could sit down."
                    "She wasn't blinking, so I pinched her a few times."
                    lily "Hey, knock it off! What happened? Did I fall asleep?"
                    her "No, one of the purple jellies latched onto you."
                    lily "Weird. I feel like I just woke up from a dream."
                    her "Its tentacle is still on you; we should probably remove it."
                    lily "Oh, I'll take care of that."
                    "She carefully grabbed it with her tweezers and moved it into a specimen bag. Sven and I looked at each other with exasperation. Maybe she was a little TOO dedicated."
                elif (knowledge >= 40):
                    "Lily appeared to be temporarily paralyzed, so I motioned to Sven to help me carry her further inland."
                    "I was trying to think of what I could do to help her when she came out of her trance."
                     lily "W-what happened? Did I fall asleep?"
                    her "No, one of the purple jellies latched onto you."
                    lily "Weird. I feel like I just woke up from a dream."
                    her "Its tentacle is still on you; we should probably remove it."
                    lily "Oh, I'll take care of that."
                    "She carefully grabbed it with her tweezers and moved it into a specimen bag. Sven and I looked at each other with exasperation. Maybe she was a little TOO dedicated."
        "Brennan, my co-worker.":
                #change scene to work
                "I was trying to think of who could come with us at work the next day."    
                brennan "I just wish I could get away from it all, you know? I feel like I'm trapped in this tiny town!"
                her "Did you know what you were getting into when you signed up for this?"
                brennan "Who says I signed up? Besides, I bet you're itching to have an adventure too."   
                her "You should come to the ocean with me." 
                brennan "Seriously?"   
                her "Yes! Lily is coming too, and we need a third person so we can look like a herd and not easy pickings."   
                brennan "Count me in! But why are you going to the ocean? Have you double-handedly reinvented bathing suits?"
                her "No, but we might reinvent biology if we can gather enough specimens." 
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
                her "How much of this excrement stuff do we need?" 
                lily "The guano? Just get as much as you can. We have an hour or two so don't feel too rushed."
                "We worked hard to get the samples we needed. We found a lot of shells and some bones. As we were getting ready to leave, the tide started to come back in."
                "The incoming waves were purple with one kind of alien sea creature. It had six spiny or hairy arms, and floated like a jellyfish."  
                lily "Oh! I've got to record this."
                brennan "Just be careful not to get swept away!" 
                "We stayed up past the tidal edge. It surprised me how quickly the tide rushed back in. Little spider-crabs rushed to dry rocks, and many got swallowed up by the waves and the purple jelly-stars."
                "A wave splashed under Lily's feet, and one of the purple spiny jellys grabbed at her leg"
                lily "O-oh!"
                "Brennan looked on in horror as I jabbed the animal with my shovel. As I contacted it, its arm fell off, still wrapped around Lily."
                if (skill_physical >= 40):
                    "Lily had a strange look on her face, so I carried her further inland so she could sit down."
                    "She wasn't blinking, so I pinched her a few times."
                    lily "Hey, knock it off! What happened? Did I fall asleep?"
                    her "No, one of the purple jellies latched onto you."
                    lily "Weird. I feel like I just woke up from a dream."
                    her "Its tentacle is still on you; we should probably remove it."
                    lily "Oh, I'll take care of that."
                    "She carefully grabbed it with her tweezers and moved it into a specimen bag."
                    brennan "Did that animal make you fall asleep?"
                    lily "I don't have narcolepsy, but it has been an unusually exhausting day. Maybe I overextended myself."
                    brennan "Well, let me know what you find out about that thing."
                elif (knowledge >= 40):
                    "Lily appeared to be temporarily paralyzed, so Brennan helped me carry her further inland."
                    "I was trying to think of what I could do to help her when she came out of her trance."
                     lily "W-what happened? Did I fall asleep?"
                    her "No, one of the purple jellies latched onto you."
                    lily "Weird. I feel like I just woke up from a dream."
                    her "Its tentacle is still on you; we should probably remove it."
                    lily "Oh, I'll take care of that."
                    brennan "Did that animal make you fall asleep?"
                    lily "I don't have narcolepsy, but it has been an unusually exhausting day. Maybe I overextended myself."
                    brennan "Well, let me know what you find out about that thing."
                    #debating about increasing the brennan relationship variable If I increase it here, maybe I should make the threshold in morning 16 higher. You don't really interact with him personally, so I decided not to mess with it.
        "Sara, my friend":
                "At lunch, I asked Sarah if she was interested in going on a field trip to the ocean."
                sara "Oh, I've been wanting to see the ocean ever since I felt so claustrophobic in that shuttle!"
                her "Really? It's kind of a long hike. Are you sure you're up for it?"
                sara "I haven't been just sitting around all day! I'll have you know that I'm in top shape!"
                her "Usually you're so worried about trying anything new, I'm kind of surprised that you're so excited about this."
                sara "Yeah, I guess it could be dangerous. I used to live by an ocean, so I kind of miss it."
                "There wasn't a road going out to the ocean, so we had to make our way through wild vegetation."     
                "We had some minor run-ins with small insects, but nothing too surprising." 
                "Arriving at the ocean was magnificent. The air was moist, and my eyes could rest on a flat plane of wetness extending to the horizon."
                sara "It's not the kind of beach I'd want to swim on, and I'm glad I brought a sweater, but this is such a sight for sore eyes!"
                her "It's an amazing view." 
                lily "I'm so glad we made it! Okay, I'd like to take samples of this crusty white stuff and any other organic material you can find."     
                sara "Okay, I'll take samples of anything that's not moving." 
                lily "I'll focus on some of the smaller creatures then."
                her "How much of this excrement stuff do we need?" 
                lily "The guano? Just get as much as you can. We have an hour or two so don't feel too rushed."
                "We worked hard to get the samples we needed. We found a lot of shells and some bones. As we were getting ready to leave, the tide started to come back in."
                "The incoming waves were purple with one kind of alien sea creature. It had six spiny or hairy arms, and floated like a jellyfish."  
                lily "Oh! I've got to record this."
                sara "Oh, I want a picture too! I can't wait to show everyone how beautiful our planet is."
                "We stayed by the tidal edge. It surprised me how quickly the tide rushed back in. Little spider-crabs rushed to dry rocks, and many got swallowed up by the waves and the purple jelly-stars."
                "A wave splashed under Lily's feet, and one of the purple spiny jellys grabbed at her leg"
                lily "O-oh!"
                "Sara looked on in horror as I jabbed the animal with my shovel. As I contacted it, its arm fell off, still wrapped around Lily."
                if (skill_physical >= 40):
                    "Lily had a strange look on her face, so I carried her further inland so she could sit down."
                    "She wasn't blinking, so I pinched her a few times."
                    lily "Hey, knock it off! What happened? Did I fall asleep?"
                    her "No, one of the purple jellies latched onto you."
                    lily "Weird. I feel like I just woke up from a dream."
                    her "Its tentacle is still on you; we should probably remove it."
                    lily "Oh, I'll take care of that."
                    "She carefully grabbed it with her tweezers and moved it into a specimen bag."
                    sara "Don't worry, I made sure your camera was safe!"
                    lily "Thank you! Maybe I just had a little too much sun today."
                elif (knowledge >= 40):
                    "Lily appeared to be temporarily paralyzed, so Brennan helped me carry her further inland."
                    "I was trying to think of what I could do to help her when she came out of her trance."
                     lily "W-what happened? Did I fall asleep?"
                    her "No, one of the purple jellies latched onto you."
                    lily "Weird. I feel like I just woke up from a dream."
                    her "Its tentacle is still on you; we should probably remove it."
                    lily "Oh, I'll take care of that."
                    sara "Don't worry, I made sure your camera was safe!"
                    lily "Thank you! Maybe I just had a little too much sun today."
    #scene vegetation
    "After Lily was got her bearings, we made the long trip back."
    her "Can you remember anything from your dream?"
    lily "My... dream?"
    "Maybe she wasn't really dreaming."
    #scene lab
    "The next day, Lily told me where to go for the most ore-rich rocks. I followed her directions and gathered nearby rocks. I was pleasantly surprised by how little I needed my pick"
    "I had a lot of help from Lily and Ilian in melting the rocks and using the 3D printers to make the metal can and pipes I needed."
    "I arranged the pipes around the inside of our house and covered them with mud. The rocket stove easily heated our whole home using only a few sticks."
    if (skill_creative >= 40):
        "I made the mud on top of the pipes into a large mud bench. Since it was a little too hot, I made some cushions from dried grasses. It felt luxurious, like having a heated couch."
    # I'm thinking that Lily might make gunpowder on her own. It's such a loaded (heh, sorry) technology that I felt like the implications for introducing it this soon were a little overwhelming to handle in one event.
    # I'm also thinking that some of the sea creatures can kind of communicate with humans by accessing their nervous system or maybe just making them dream. 
    # So the purple jellies are kind of like bees in a collective unconscious sort of way. Maybe that's too far out? It's a seed for something later on anyway.
    return

# MONTH 12
# uses domestic, social
label monthly_event_12:
    scene bg farm_interior with fade
    "Jealous of New Friend"
    return

# MONTH 13 - Jury Duty
# uses spiritual, technical
label monthly_event_13:
    scene bg farm_interior with fade
    "I hadn't thought about it much before, but we didn't have a lot of laws here on Talaam. Some things just didn't apply (like taxes, driving laws, etc), but I remember signing something about agreeing to abide by a set of laws that sounded very reasonable."
    "It had never seemed like something I would have to worry about.  Until I had to be on the jury for Ilian's trial, that is..."
    "We hadn't had any crime our whole first year (though we certainly had our share of arguments, accidents, and disagreements)."
    "After all, who would hurt anyone else in our colony? We needed each other too much."
    "But that peace couldn't last forever..."

    #scene bg community_center with fade
    "We awoke one morning to the tragic news that the Peron's four-year-old girl, Josephina, was missing."
    "Mrs. Peron was alternately furious with herself and those around her."
    natalia "Someone should have been watching her more closely!"
    natalia "I should have been watching her more closely..."
    "Everyone searched together all day long, and finally we found her body washed up downstream of the Peron's farm."
    if (profession == "doctor"):
        "We didn't have a coroner or anything, so I took a look at the girl's body."
        "I could tell she probably died the afternoon before. I found a gash on her head that looked pretty awful, and she had several broken bones. The injuries seemed too severe to have been sustained after she fell in the river..."
    else:
        "We didn't have a coroner or anything, but the doctor took a look at the body."
        "Josephina's body had several broken bones and big gash on her head that didn't seem like they came from falling in the river..."

    "In addition, Mr. Peron found some blood on the road next to his farm that led to the river."
    "We spent a few days being suspicious of each other. [his_name] started barring our door at night."
    "Finally, the mayor called a community meeting."
    boss "I know everyone is worried, and scared, but we can't stop trusting each other. We will find who's responsible for this."
    natalia "Who knows who will be next?! It clearly wasn't an accident!"
    "Finally, Ilian stepped forward."
    ilian "I'm sorry! I'm so sorry!"
    sara "Sorry for what?!"
    ilian "I-- I'm the one that killed Josephina."
    "Nobody said a word. He worked his way up to the front of the room. He brushed his hand in front of his eyes - was he crying?"
    ilian "It was late, I didn't even see her until she was right in front of me. I was driving my tractor, maybe a little fast- she jumped in front of it- I was going too fast- I didn't mean to run over anyone!"
    natalia "But how did her body end up in the river?!"
    ilian "It was obvious she was dead- there was so much blood- I was so horrified- I don't know why I did that- I didn't want anyone to know it was me. So I dropped her body in the river."
    
    "Nobody knew what to say. He was really crying, now, heaving deep sobs that looked pathetic on a man his size. I looked over at his wife, Sara, who looked like she was in shock."
    boss "Ilian, I can tell you're sorry about this, and I'm glad you came forward. We will need to have a trial and decide what to do about this."
    natalia "What do you need a trial for?! He just admitted he killed Josephina!"
    boss "The laws of our community, which you all signed, state that any accused shall receive a trial, administered by myself and with a jury randomly selected from the adults of the colony that are not involved in the crime."
    "The mayor took Ilian to stay at his house until the next day, when the trial started."

    boss "[her_name], you've been randomly selected to be on the jury. Is there any reason you should not do this? Any conflict of interest with either side?"
    her "No, not that I can think of..."
    boss "Very well. We will proceed with the trial at two o'clock."
    
    "Everyone in the town turned out to see the trial. Ilian repeated what happened, and Mrs. Peron repeated what she had found. It sounded like a fairly simple case of involuntary manslaughter; we mainly needed to decide upon a sentence."
    boss "There is no mandatory sentencing in the laws of our colony. I am sure you will find a solution that is fair to all parties involved. In case you don't, I do have the authority to modify sentencing, but I have every confidence in this jury's abilities."
    "He left us jury members to deliberate in private."
    
    lily "He shows great remorse. I doubt he will be so careless as to repeat his mistakes."
    sven "It could have been any of us..."
    thuc "But would one of us have dumped her body in the river and covered it up? That behavior is suspicious. He says it was an accident, but who can tell for certain?"
    her "But why would anyone kill Josephina?"
    thuc "Why does any criminal do what they do? They want to, and they don't care about other people."
    lily "Ilian has not shown any other behavior that would be cause for concern."
    thuc "But it's possible that it was not an accident. We cannot show too much mercy, or people will think they can get away with anything."
    sven "We don't have a jail; you're not thinking of execting him, are you?!"
    thuc "Of course not. I propose temporary banishment. He should have to live on his own, off the land, for a year. That will show how important our community is, both to him and any would-be criminals."
    lily "There are no would-be criminals here, Thuc. What you are proposing is a death sentence. I think he should simply provide a certain amount of free labor to the Peron family every week. Perhaps that way they can eventually forgive him."
    sven "I don't like either of those options, but I can't think of anything better."

    menu:
        "What will you argue for?"
        "Work for Perons":
            her "I agree with Lily; he should have to work for the Peron's. It can't make up for the loss of a child, but it will require some sacrifice and will help him show his remorse."
            thuc "He should be their slave for a year!"
            her "Well, we don't want his farm going to waste..."
            sven "Maybe he could be required to work a certain number of hours? Like community service?"
            her "Yes, but instead of the community it will be for the Perons. Let's say eight hours a week for a year."

            "The jury agreed to that, and the Mayor, Ilian, and the Perons all accepted our proposal. Sara didn't seem to happy about it, though. She'd probably have to do extra work on their farm to make up for his absence."

        "Banishment":
            her "I agree with Thuc; we need to show that our community won't allow such behavior."
            lily "You might as well just shoot him in the head; he can't survive for a year out there!"
            her "I agree. Also, he is a healthy worker, which we can't afford to lose for that long. So I propose that he live outside the community boundaries, but close enough that we can trade with him. He can hunt or gather useful things and trade them for food or other community resources."
            thuc "That's too soft!"
            lily "I think a year is still too long."
            her "How about two months?"
            thuc "Three."
            lily "I suppose that would work...as long as the resources he gathers go to help the Peron family."
            "Finally, we had come to an agreement."
            "Ilian and the Perons accepted it, but Sara and the Mayor frowned. Poor Sara... I guess in a way we were sentencing her, too."
            
        "{i}Compromise{/i}" if (skill_spiritual >= 40):
            her "Those both sound like good ideas. Perhaps some of both might be appropriate?"
            sven "What do you propose?"
            her "Having him work for the Perons is a good idea, but it is too soon. They would feel angry, and then he would feel like his apology was not accepted."
            her "But a year is too long to send anyone to live outside the community. I propose Ilian leave the community for two weeks. When he returns, he will have to work for the Perons one day of every week for the next half year."
            lily "That sounds fair for all involved."
            thuc "I think two weeks is too short, but I will agree to this plan also."
            "Everyone agreed to my proposal. The mayor seemed happy with it, too, and both Ilian and the Perons accepted it without argument."
        "{i}He's innocent{/i}" if ((skill_technical >= 40) or (skill_knowledge >= 40)):
            her "He should provide some reparations, but I know he didn't kill her on purpose."
            thuc "How do you know that?"
            her "Her injuries are consistent with being hit by a car and then floating down the river. She doesn't have any injuries that would come from being physically assaulted."
            sven "Yes, that's right!"
            thuc "That's true... I guess he is still innocent unless proven guilty..."
            her "He still should provide some reparations, though. I think he should work for the Perons one day a week for a year."
            lily "I agree."
            sven "That sounds fair."
            "We all agreed, and the Mayor, Ilian, and the Perons seemed satisfied with our verdict also."

    "I was just glad it was over."
    "Being on a jury was so stressful; I hope I never have to do that again."

    return

# MONTH 14 - Pregnancy or not?
label monthly_event_14:
    scene bg farm_interior with fade
    if (want_kids and (made_love >= 3)):
        her "I wonder if I'm getting sick; I've felt so tired lately."
        him "I haven't heard of anything going around. That's one of the good things about being so far from Earth - we don't get as many of their germs."
        her "Well, I've got something. It's not like I'd make it up!"
        him "What? No, of course not."
        her "Do you think I'd make that sort of thing up?!"
        him "No, not at all!"
        "I felt like crying. One part of my brain knew it was not a big deal, but the other part just felt so lonely and afraid all of a sudden."
        if (loved >= 0):
            "He came over and held me close"
            him "It'll be okay, [her_nickname]. Why don't you get some rest?"
            her "Maybe I will..."
            "I fell asleep immediately..."
        else:
            him "You should get some rest."
            her "Oh, suddenly you know exactly what I should do? You think I don't know how to take care of myself?!"
            him "Hey, I'm not telling you what to do, you just seem a little tired, that's all."
            her "Tired?! I just said I'm sick!"
            "I went to lay down and fell asleep immediately..."

        "The next morning I felt less tired, but still a little off. I went to work anyway, and had been standing up all day when I started to feel dizzy and sick to my stomach."
        her "Excuse me, please."
        brennan "Are you alright? You don't look so good."
        her "I just need... to rest for a bit..."
        menu:
            "I sat down and put my head on my desk. Slowly, the dizziness subsided, but I didn't feel like eating."
            "Go home":
                her "Brennan, I'm feeling sick. Can you take care of things here for a bit; I'm going to go home."
                brennan "Are you sure you're up to walking? Want me to call [his_name]?"
                her "I'll be fine, thanks."
                "The fresh air and walking seemed to help some, but I was still glad to finally get home."
            "Try and get some work done":
                "I went back out and was able to finish up the day's work, taking two more breaks when I started to feel too light-headed."
        "It felt good to get home. I still wasn't feeling well so I decided to lie down."
        him "Are you feeling any better?"
        her "Not really."
        him "Sorry to hear that, [her_nickname]. Do you want to stop by the clinic in the morning?"
        menu:
            her "I'm not feeling {b}that{/b} bad, but..."
            "Go to the Clinic":
                her "It can't hurt to check it out."
                him "I'll come with you tomorrow."
                "We walked to the clinic holding hands, not saying anything, just watching the sun rise and feeling together."
                if (profession == "doctor"):
                    "I reviewed my own symptoms in my head and decided to take a urine sample first."
                else:
                    "The doctor at the clinic listened to my symptoms and had me give a urine sample."
                "The results said..."
                him "You're pregnant?!"
                her "Oh! I've been so busy I haven't even been thinking about that lately. But...yes, I guess I am."
                        
            "Don't go":
                her "I'll be fine. If I don't feel better in a few days, I'll have it checked out."
                him "Alright."
                "I didn't feel better, but I didn't feel much worse, either. My chest ached, sometimes, though, and I got headaches when I never used to."
                "Finally it dawned on me..."
                her "Maybe I'm pregnant?"
                "Sure enough, I went to the clinic and tested positive for pregnancy."
                
            "Run some tests" if (profession == "doctor"):
                her "I'll just run some tests at work today, no big deal."
                if (loved >= 0):
                    him "I'll come with you."
                    "We walked to the clinic holding hands. It felt so good not to be alone right now."
                else:
                    him "Okay, let me know what happens."
                her "Brennan, will you please help me get a blood sample?"
                brennan "From who?"
                her "From me."
                brennan "Well, sure. That's a bit hard to do yourself, isn't it?"
                "I started laughing, but it wasn't that funny. Somehow that just made it funnier. Brennan wasn't laughing, just looking at me quizzically."
                "He took the blood sample and we ran the standard tests on it."
                "Everything was normal except--"
                brennan "You're pregnant?"
                her "I guess...I am!"
                "That explained everything."
                
        him "[her_name], that's great!"
        menu:
            "How do I feel about it?"
            "It's awesome!":
                her "Yeah! We're gonna be parents!"
            "It's strange.":
                her "I guess it is. At least I know now what was wrong with me."
            "It's awful.":
                her "I hope I don't feel this bad the whole time. I don't know if I can take nine months of feeling this sick."
        him "I wish it didn't have to be so hard for you, but our little baby is worth it!"
        her "Our little baby..."
        "This was going to take some getting used to."
        $ is_pregnant = True

    # They want kids but didn't make love enough
    elif (want_kids):
        her "[his_name]... it's been over a year since we've been trying to have a baby."
        him "Yeah, I guess sometimes it takes a while."
        her "We haven't made love very often, have we?"
        him "Well, we have both been busy, and tired..."
        menu:
            "Should we change things?"
            "No rush":
                her "I guess there's no need to rush, right? In fact, it's probably good that I'm not pregnant, so we can have things setup better when it happens."
                if (loved >= 0):
                    him "Yeah, that's true. Come here, [her_nickname] - we have plenty of time. Plenty of time for you, and me, and whoever else might join us in the future..."
                    "He held me close for a long time, stroking my hair."
                    $ made_love += 1
                    $ loved += 5
                else:
                    him "Is that why you haven't wanted sex lately?"
                    her "No! That's not it at all! I'm just trying to see the bright side of things."
                    him "The only bright side is that there's no kids to be hurt by our unstable relationship."
                    her "Unstable?!"
                    him "People who are married don't act this way. We never do things together; we never make love. And when I try and do things for you, it's like I can never do anything right."
                    her "Is that really how you see us?"
                    him "It's true, isn't it? We have to turn things around if we want this to work, and especially if we want to bring kids into this family."
                    "We talked about it some more, and we both agreed to try and put the other person as more of a priority in our own life. But I wonder if we can actually do it... or if our marriage is already doomed."

                    # Reset loved a little closer to zero to give the relationship another chance
                    if (loved < -10):
                        $ loved = -10
                    else:
                        $ loved = 0

            "Let's make a baby!":
                her "Come on over here, [his_nickname], and make me a baby!"
                him "You want me to turn you into a baby?"
                her "Ohhh, you!"
                him "Sorry, I mean, 'Yes ma'am'!"
                $ made_love += 2
                $ loved += 5

    else:
        her "[his_name], there's something we need to discuss."
        him "Oh? What's that?"
        her "When I went to try to get more birth control, they informed me that they only had enough for six more months. 'We need everyone to help populate the colony,' they said."
        menu:
            him "Six months, huh? Do you think we'll be ready by then?"
            "No way":
                her "No way! We can barely take care of our farm and a horse; how can we take care of a baby?!"
                him "I think we're doing pretty good."
                her "It just feels like one more thing to worry about; I'm already stressed out about food, work, and this whole crazy planet."
                him "Don't worry; we'll figure something out. We can always... get creative."
                her "I like it when you get creative."
            "Maybe":
                her "I guess we could be, but...I just don't feel ready yet. Maybe things will be different in six months... or we could always use other methods."
                him "Yeah, I feel ready, but you're the one that will be carrying the baby, so we can do whatever you think is best."
                her "Let's not worry about it now. We'll see in six months."
                if (loved >= 0):
                    him "Okay, [her_name]. I love you."
                    her "I love you, too."
                else:
                    him "Okay."
                    her "Yeah."
                    "And that was that."
 
            "I'm ready now":
                her "You know, I think I'm ready now."
                him "Yeah? You've changed your mind from last year?"
                her "Yeah...let's stop the birth control now, and just see what happens."
                him "Yes, momma."
                her "Oh, ick, don't call me momma!"
                him "You better get used to it! Someday a bunch of kids are going to call you that all the time!"
                her "That's so... weird! But at least they'll be calling you 'daddy', so I won't be alone."
                him "You'll never be alone."
                $want_kids = True
                $made_love += 1   
            
    return

# MONTH 15 Fertility and Food and Community
label monthly_event_15:
    scene bg farm_interior with fade
    if (is_pregnant):
        him "I made you breakfast, so eat up, [her_name]! You're eating for two!"
        her "Yeah, but one of us is the size of a pea..."
        her "Eggs? Bacon?! Where did you get this stuff?!"
        him "Well, when Mrs. Peron heard about your 'condition', she insisted that you needed to eat eggs to have a healthy baby. And when I told Ilian the good news, he pulled this out of some stash in the storehouse."
        her "Wait, you told them I'm pregnant?"
        him "Yeah, why not?"
        her "I don't know if I'm ready for people to know, yet."
        him "Oh... well, when I told Mrs. Peron, she posted a message about it on the colony message board..."
        her "So everyone knows?"
        him "Yeah, pretty much."
        her "I haven't even told my parents yet!"
        him "What's stopping you?"
        her "I guess... I wanted to tell them in person, but that's just not possible, is it?"
        him "No... but we can send them a message."
        her "But what if something goes wrong, like a miscarriage?"
        him "Don't say that!"
        her "Well, it's a possibility, isn't it?!"
        him "Yeah, but... Whatever happens, I want to face it with friends and family knowing everything."
        menu:
            "How do I feel?"
            "I'd rather keep it to myself":
                her "I disagree. I'd rather face our problems on our own, if we can."
            "I guess you're right":
                her "Yeah, that makes sense. Hopefully nothing bad will happen."
            "I can't believe you did that":
                her "I can't believe you told other people without talking to me first!"
                him "What, so you want to decide what I can and can't tell people?"
                her "No, but it's something important enough that we should have decided on it together!"
                $ loved -= 3
        if (loved >= 5):
            him "I'm sorry; I probably should have talked to you about it first."
            her "It's okay. At least I got a delicious breakfast out of it."
        else:
            him "Sorry, love, but at least you got a good breakfast out of it, right?"
            her "Yeah..."

    elif (want_kids):
        him "I made you breakfast, so eat up! Soon you might be eating for two."
        her "Ha ha, we'll see..."
        her "Yum, is this berries and cream?! Where did you get it?"
        him "Well, when Mrs. Nguyen heard we were trying to have kids, she insisted that you needed to eat cream to have a healthy baby. So she gave me some from her goats."
        her "Wait, how does she know we are trying to have a baby?"
        him "Well, I might have mentioned it to Thuc...and I guess he told his wife?"
        her "So basically the whole colony knows."
        menu:
            him "Is that a problem?"
            "Not really":
                her "I guess not. It's just kind of weird. As long as they don't start serenading us with fertility songs or anything it doesn't really matter."
                him "Okay, I'll post that to the message board. 'Thanks for the well-wishes, but no fertility rites, please.'"
                her "Shut up and try some of this."
            "It's annoying":
                her "That's really annoying. I don't want people to be asking me all the time if I'm pregnant yet, or giving well-meaning but idiotic advice, or looking at me like I'm a time bomb or something."
                him "I'm not sure you can prevent that, anyway. I mean, they're going to know sooner or later, right?"
                if (loved >= 0):
                    her "Yes, but I wanted it to be on my terms."
                    him "I see.  I'm sorry, [her_name], I didn't even think about it."
                    her "It's all right; we'll deal with it. Come on and eat breakfast with me, okay?"
                    him "No problem."
                else:
                    her "Yes, but I wanted to decide that! It's my body, you know!"
                    him "It's *our* child."
                    her "It doesn't even exist yet! What if I change my mind, or something goes wrong?"
                    him "I thought we had already decided."
                    her "Well, we didn't decide to tell people about it, that's for sure."
                    him "Look, I'm sorry. I just wanted to tell somebody, and Thuc's probably the best friend I have here, except for you."
                    her "Oh, it's all right. Just come eat some breakfast."
                $ loved -= 2
                $ relaxed -= 2
            "I'm mortified":
                her "I'm mortified! I don't want people thinking about us conceiving a baby!"
                him "Don't you think it's pretty obvious? I mean, healthy, newly-married couple on a colony, that's kind of why we're here?"
                her "Yeah, but... it should be more private than that."
                him "I guess I don't see it that way."
                her "So you're totally okay with people looking at us thinking, 'I wonder if they got it on last night?'"
                him "I don't think anyone's thinking that. And if they are, you can't stop them."
                her "Ugh, whatever, let's just eat breakfast."
                $ loved -= 5
                $ relaxed -= 5
    else:
        him "I made you breakfast."
        her "Oh! Thank you!"
        her "Wow, berries and cream, what a treat!"
        him "Yeah, Thuc's wife gave them to me. She said they might help if you were having, uh, female problems."
        her "What?!"
        him "I think she was trying to help us have a baby."
        her "Ha ha, it'll take more than berries and cream..."
        him "Well, we can enjoy it anyway, right?"
        her "We? She sent this for me!"
        him "Oh, so you want me to tell her that we're not trying to have a baby?"
        her "Don't say that! Then she won't send any more!"
        him "Better share, then!"
        menu:
            "Should I share it?"
            "Share":
                her "Here, have some."
                him "Mmmm, thank you."
                $ loved += 2
            "Don't share":
                her "Hands off, this is mine!"
                him "Alright, alright! Sheesh!"
                $ loved -= 2
    return

# MONTH 16 - Morning sickness/Illness
label monthly_event_16:
    scene bg farm_interior with fade
    if (is_pregnant):
        "Being pregnant wasn't as much of a change as I thought it would be; mostly I was just more tired (and maybe a little cranky). Sometimes I even forgot about the tiny baby growing inside me; it didn't seem real."
    else:
        "Once nice thing about living on the colony was that we didn't usually get sick. Most of the microorganisms here seemed to ignore our strange biochemistry, and they worked hard to keep germs from Earth off the shuttle."
    "But today I just felt awful."
    "I tried to eat breakfast, but I didn't really feel like eating. [his_name] had already cooked it, though, so I didn't want to waste it..."
    menu:
        "What should I do?"
        "Throw it away":
            "I tossed it onto the garbage heap. Some animals would probably eat it."
            $ community_level -= 2
        "{i}Trick yourself{/i}" if (skill_creative >= 50):
            "I decided to pretend I was a starving waif who had just been taken in by a rich kind stranger and this was my first real meal in months. It sort of worked; I was able to get most of it down."
        "{i}Use acupressure{/i}" if ((skill_knowledge >= 50) and (is_pregnant)):
            "I looked up on my computer pad and found that acupressure sometimes can help morning sickness."
            "I rigged up some acupressure bracelets with some old buttons and elastic. I'm not sure if they helped, or if the morning sickness wore off, but soon I felt well enough to eat some."
        "Give it to the goat." if (have_goat):
            "I carried my leftovers over to the goat, who seemed to really enjoy them. Watching the goat eat, though, I felt like throwing up..."
        "Give it to [his_name]" if (loved >= 0):
            her "Do you want this? I'm not hungry..."
            him "What? Sure, OK"
            $ loved += 2

    "I felt better at work, and lunchtime was no problem, but as I was walking home, I felt sick again. I ended up throwing up by the side of the road, which wouldn't have been too bad except some of it got on my clothes. Now I had to do laundry, and it was my turn to make dinner..."
    menu:
        "What should I do?"
        "Cook something simple":
            "I went to the cellar to look at what we had for dinner. Nothing looked good."
            if (is_pregnant):
                "I wanted fried chicken or ice cream or french fries or fresh rolls, but all we had was turnips and carrots and beans."
            else:
                "We had been eating a lot of turnips and carrots and beans lately, and I was starting to get used to them, but what I really wanted was a can of good ol' chicken noodle soup. All the foods we had took so much work..."
            "I knew it was so silly, but I felt like crying. I remembered when if I craved a food, I'd just stop by the store on my way home from work and buy it, without thinking anything of it. I didn't even realize how decadent that was!"
            "That's how [his_name] found me, crying in the cellar over the food he worked so hard to grow."
        "Lie down and take a nap":
            "I wasn't hungry; why should I make dinner? What I really needed was a nap..."
            "I took off my dirty clothes and dozed for a while, and woke up to the sound of [his_name] opening the door."
        "Ask [his_name] for help":
            "I decided to ask [his_name] for help. After all, that's why we have each other, isn't it?"
            "Finally, he came home."

    menu:
        him "Hey, [her_name], what's for dinner?"
        "I'm sick":
            her "I don't feel good..."
            if (loved >= 0):
                him "You don't look good. You go lie down; I'll make my own dinner."
            else:
                him "I thought it was your turn."
                her "It is, but..."
                him "OK, I'll trade you nights, since you're not feeling good."
            $ loved += 2
        "Make your own dinner" if (relaxed <= 0):
            her "Make your own damn dinner, I'm not hungry!"
            him "Hey, hey! Calm down!"
            her "Calm down?! I don't have time to calm down! I need to wash out this vomit and make dinner out of vegetables I hate and try not to die while doing it, because everything on this planet is trying to kill us!!"
            if (loved >= 0):
                him "Okay, it seems like you could use a little break, so why don't you go lie down?"
                her "I don't have time to--"
                him "Laundry can wait, I'll make dinner, and nothing's trying to kill us at the moment, so go rest, okay?"
            else:
                him "Quit overreacting. You're just making excuses."
                her "I hate this place! I hate this food! I hate not having anything when we need it! I hate the animals, I hate the plants, I hate the moons that can't make up their mind whose turn it is to be in the sky!"
                him "Anything else?"
                menu hate_stuff:
                    "I hate the sun":
                        her "I hate the stupid sun and its temperamental solar flares."
                        him "Yeah, I hate that, too."
                        $ loved += 2
                    "I hate you":
                        her "Sometimes, I hate you."
                        him "..."
                        her "..."
                        him "I was about to say, 'At least we'll always have each other.'  Now I don't know what to say."
                        $ loved -= 10
                    "I hate my job":
                        her "I hate my job here."
                        him "It seems pretty easy compared to mine."
                        her "Well, not all of us are tough farmers like you!"
                        him "Maybe you should be."
                        $ loved -= 2
                    "I'm sorry":
                        her "I'm sorry; I'm sounding pretty hysterical, aren't I?"
                        him "Yeah, but I love you anyway."
                        $ loved += 5
                
        "Just a minute" if (relaxed >= 0):
            her "I'm working on it, just a minute."
            him "Hey, are you crying?"
            her "Just a little."
            him "What's wrong?"
            menu:
                "It's morning sickness" if (is_pregnant):
                    her "It's morning sickness, I think."
                    him "Aw, I hear that can be rough."
                    her "It's not that bad, but..."
                    him "You want me to cook tonight?"
                    her "Yeah, thank you. I'm not even hungry."
                    $ loved += 2
                "I'm sick" if (not is_pregnant):
                    her "I'm sick."
                    him "Really? We haven't had much illness here..."
                    her "Well, I sure didn't throw up all over myself just for fun."
                    him "Ohh, is that what that smell is?"
                    her "Yeah..."
                    him "Well, you should take it easy, then, I'll make myself something."
                    $ loved += 2
                "It's this place":
                    her "It's this place... I'm so sick of everything here."
                    him "Like what?"
                    her "I hate not having foods that I like, and feeling like there's dangerous things around every corner, and being so far away from everyone."
                    him "Anything else?"
                    jump hate_stuff

    "I went to lie down, and he made dinner for himself."
    $ relaxed += 2
    if (is_pregnant):
        "I felt better after a little rest. I felt a little sick the every morning for a few weeks, but that was the worst day."
    else:
        "I had to visit the outhouse several more times before my stomach finally calmed down."
        if (loved >= 0):
            "He made me some tea and sat by me and held my hand."
        else:
            "[his_name] left me alone until I was feeling better."
                             
    return

# MONTH 17
# uses knowledge, technical
label monthly_event_17:
    scene bg farm_interior with fade
    return

# MONTH 18 - something bad happens where you need help (related to pests?); he doesn't want to ask for help but you think you need it.
# uses spiritual, social, physical
label monthly_event_18:
    scene bg farm_interior with fade
    return

# MONTH 19 - Clothing wearing out, stiff, doesn't fit anymore if pregnant.
# clothes don't fit anymore (bras, etc); air drying makes they stiff and uncomfy, what to do?
# use domestic, social, creative
label monthly_event_19:
    scene bg farm_interior with fade
    "Fashion was one thing we never had to worry about."
    "We mainly had our colony-issue shirts and pants, made of special durable, breathable, material, and whatever extra clothes we managed to fit in our one allotted suitcase."
    "I did get a little tired of wearing the same thing all the time, but everyone else on the colony was in the same situation, so it wasn't something I worried about."
    if (is_pregnant):
        "But now that my belly was growing, the pants were starting to get uncomfortable. They weren't made to stretch this much. The shirt was getting tight, too"
        "I had to do something about it, but what?"
        menu maternity_clothing:
            "What should I do?"
            "Check the storehouse":
                #scene bg storehouse
                her "Hey, Ilian, do we have any extra clothes here?"
                ilian "A few..."
                "I found a large men's shirt that wasn't very flattering, but would fit."
                "They had a pair of larger pants, but they were also too long. Well, I'd just have to roll them or hem them or something."
            "{i}Modify your pants{/i}" if ((skill_domestic >= 60) or (skill_creative >= 60)):
                "I decided to turn one of the pairs of Earth pants I had into maternity pants."
                "After all, I wasn't going to be pregnant forever, so I didn't want to ruin my nice space uniform."
                "So I took a pair of low-rise jeans and added a strip of stretchy material."
                "The shirt"
                "It was kind of tedious sewing by hand, but I got it done."

            "Ask [his_name]":
                her "Hey, [his_name], could I borrow some of your clothes?"
                him "Only if you let me borrow some of yours."
                her "No way! You'd stretch them out!"
                him "I'm just kidding. I don't have a lot of clothes, but there's one pair you could have."
                her "Thanks!"
                "He handed me an old pair of jeans and a t-shirt. They fit okay right now, but I could tell they wouldn't fit the whole pregnancy."
                "Well, I'd figure something else out later."
            "Try nudity":
                "I guess I didn't need to wear clothes around the house - it felt so good not to have that waistband constricting my growing belly!"
                him "Hey, is it no pants day? How come I didn't get the memo?"
                her "It just feels so much more comfortable this way..."
                him "Good idea."
                "Pretty soon [his_name] was walking around free as a bird, too."
                "But I was pretty sure I had to wear clothes to work, so I needed to try something else, too"
                jump maternity_clothing
            "Ask around" if (skill_social >= 60):
                "I knew Helen was also expecting, so I decided to send her a message and see what she had done."
                her "Hey, Helen, what are you doing for maternity clothes?"
                helen "Oh, I just made a big tent dress out of a hospital gown. It doesn't look very good, but it's very comfortable."
                her "Do you think you could show me how?"
                helen "Well, I'm sort of stuck in bed because of this pregnancy... but send me your measurements and I'll make you one!"
                her "Really?!"
                helen "Sure, I've got nothing else to do all day, and I'm sick of crocheting baby clothes..."
                "Sure enough, it looked kind of terrible. But it fit, and was comfy, so I wore it a lot."

    else:
        "But for some reason this month it really bothered me. I was sick of the uniform's fabric, its unisex cut, and the sameness of it all."
        "But what could I do about it?"
        menu:
            "Make a new accessory" if (skill_creative >= 60):
                "I knew how to crochet, so I decided to make myself some long fingerless gloves. Luckily, someone had made some yarn from shearing their sheep and donated it to the storehouse."
                "They color was pretty plain, but they definitely stood out and looked unique."
            "Host a clothing swap party" if (skill_social >= 60):
                "I figured I wasn't the only one getting tired of the same clothes every day, so I posted a message on the colony message board and invited everyone to bring one outfit to the community center, and we could all trade."
                "Not everyone was the same size, but we also didn't have much to choose from, so we weren't picky."
                "For some reason, it felt so good to sift through the clothes - I didn't think I'd miss shopping, but it felt so luxurious to have several different things to choose from and make my own."
            "Decorate old clothes" if (skill_domestic >= 60):
                "I thought I'd just decorate some of the clothes I already had to look different."
                "I printed out a design I liked from the internet, printed it out on paper, and cut out parts of it to make a stencil. Then I sprayed bleach over the stencil until the part with the cut-outs faded. Then I dunked it in water to wash the bleach out."
                "It was like having a whole new shirt!"
            "Nothing. Who cares?":
                "It was too much work. We had more important things to worry about than clothes, anyway."

    return

label monthly_event_20:
    scene bg farm_interior with fade
    return

label monthly_event_21:
    scene bg farm_interior with fade
    return


label monthly_event_22:
    scene bg farm_interior with fade
    return

# Climax - epic conflict leading to either "We'll always be together" or "I just want to get away from you!"
label monthly_event_23:

    return

label monthly_event_24:
    "birth if pregnant, pregnant if made_love is high enough (ran out of birth control), else what to do if no more BC and still don't want kids"
    return
