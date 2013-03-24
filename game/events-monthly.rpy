# Event content for all the important monthly events

# You shouldn't ever see this. This is just a fall through in case something happens
# and there's no event for this month.
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
    menu:
        "It's breakfast time."
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

    #TODO: But who actually ended up doing the dishes?!
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
    her "I can't believe you don't appreciate me and what I do."
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
                her "Well, I made the curtains over there."
                him "Oh, yeah, those are nice. Very insulating."
                her "And I've planted an herb garden out front to add flavor to our meals, and for herbal teas and things."
                him "Okay, that will be good. Sorry, I didn't meant to accuse, I just really was curious what projects you've been working on."
            "What do {b}you{/b} do?":
                her "What have {b}you{/b} been doing lately? You've been reading a lot."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "Okay, well, that sounds very... necessary."
                her "I've made some curtains and planted an herb garden, in addition to keeping the house pretty spotless."
                him "Oh, is that what those plants are? The house is really clean, too; thank you."
            "I can't believe you don't appreciate me":
                jump unappreciated

    #TODO fill these in when we have more skill events written.
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
            "I can't believe you don't appreciate me":
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
                her "Well, did you know that I can run to town in five minutes? And I am getting pretty good at chopping wood, which we'll need when the cold season starts and our solar panels don't work."
                him "Oh yeah, that is important. Sorry, I didn't mean to accuse, I just was curious about what you've been doing."
            "What do {b}you{/b} do?":
                her "What have {b}you{/b} been doing lately? You've been reading a lot."
                him "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field. I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her "Okay, well, that sounds very... necessary."
                her "On that hike I found out about a new water source, and I can run to town in five minutes in case there's an emergency."
                him "Five minutes?! That's pretty fast. You must have been training a lot. I guess I haven't thought about doing that because I usually ride Lettie around."
                her "Well, not all of us have horses, so we have to make do with the legs we have."
                him "And what nice legs they are..."
            "I can't believe you don't appreciate me":
                jump unappreciated

    "We ended up staying up late, talking about all the things we had been doing. I felt like I understood him a little better after that, and he seemed to appreciate what I was doing more, too."
    return

# MONTH 5 - What to do with trash
label monthly_event_5:
    "The village council asked us to do a waste assessment to see how much and what kind of materials we needed to permanently dispose of. If the amount of waste was too high, they told us that future colonists would be limited."
    "Our waste pile was fairly small, as we'd already composted any organic material that we didn't eat. Still, there was things like packaging from the MREs, a broken dish, and a pair of worn-out socks."
    her "You threw away a perfectly good pair of socks?"
    him "Well, they have holes in the heels, and the rest of the material is getting thin. I wasn't sure if they were compostable."
    her "We can't just throw things away when they break like on Earth. We need to take care of this planet for future colonists and the life forms that are already here."
    him "Well, what should we do with them then?"
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
        "{i}This stuff is actually compostable.{/i}" if ((skill_knowledge >= 30) or (skill_technical >= 30)):
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
            
    "We ended up throwing some of waste items away, but I felt good about the effort I put it."
    $relaxed += 5

    return

# MONTH 6 - Alien Pests
label monthly_event_6:
    #biological pesticide--fungus
    "Our crops were starting to give and abundant harvest, but unfortunately, with the rainy season starting, the corn was being attacked by alien insects."
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
            "Lily's fungus experiment sucessfully killed a little over half the bugs I gave her. She lent me a sprayer and told me to bring it back as soon as possible, since some other farms had the same insects to spray."
            "When I asked her about how to use the dead insects we had caught, Lily said that we could use them to feed livestock."
            her "I'm not sure if our horse will like how they taste, but I'll try it."
            "We sprayed our crops. Sadly, we couldn't save much of them. Luckily, our underground crops like potatoes and beets weren't attacked by the insects, so we still had something to eat while we planted new crops."
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
            him "They're full of their eggs. The corn at least. Even if we pick all the infected crops off, I think it's too late to save them."
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
            him "It tastes kind of nutty. And... gross, is this an insect leg?"
            her "Yeah, for the next batch I'm going to try processing the flour a little differently. But for a first try it's not bad, is it?"
            him "It's a whole lot better than nothing, that's for sure."
            "One day I roasted them seasoned with garlic salt. They were crunchy and dry, but edible."
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
            "We were able to preserve some of our corn until it was ready for harvest, although for most of the corn it was too late."
            "We had a big bonfire with the Perons and burned the infested corn. Their kids danced around the fire as we roasted one of their chickens on the side."
            ## this section could be expanded by having a dialogue with one of the Blairs.
        "I have no idea.":
            her "I don't have any ideas...I'm sorry."
            him "Well, let's try to salvage what we can."
            "All of the above-ground crops had been partially eaten by the insects. I started trying to cut off the bitten parts, but then I found eggs laid inside some of the corn. We didn't want the insects to keep coming back, so we ended up burning our corn field."
            him "At least our next crop will have some really rich soil to grow on."
            her "Yeah, and at least we have some potatoes, beets and ginger to eat for the next few months."
            him "But what if more insects destroy our crops?"
            her "Then we might have a very limited diet. Hopefully someone will find a way to keep them at bay."
            $ community_level -= 5
            return
            
    $ community_level += 5
return

# MONTH 7 - Broken computer - honesty?
label monthly_event_7:
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
                        $ relaxed -= 5
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
                        $ relaxed -= 10
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
    return

label monthly_event_8:
    "Conflict of Interest: Community vs. Spouse"
    return

label monthly_event_9:
    "Different Date Ideas"
    return

label monthly_event_10:
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
    her "Hi, are you okay?"
    him "Huh? Yeah, everything's fine now."
    her "What happened? Last night you were really worried about something."
    him "Oh, it was Lettie. I think she ate something poisonous while she was grazing - she was really sick. But she's doing better today; I think she'll be fine."
    her "Oh, I'm glad she's okay."
    him "Yeah, me too.\n Sorry about last night - I know we were going to celebrate our anniversary and everything, but I just couldn't celebrate when I was so worried about her. But I did get you something."
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
        "I ran all the way there, no problem. Good thing I was in shape."
    else:
        "I walked and jogged as fast as I could."
        $ relaxed -= 5
    "I got the laxative and returned to [his_name] and Lettie."
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


label monthly_event_11:
    "Jealous of New Friend"
    return

label monthly_event_12:
    "Frustration with Work"
    return

label monthly_event_13:
    "On the Jury for a Crime"
    return

# MONTH 14 - Pregnancy or not?
label monthly_event_14:
    scene bg farm_interior with fade
    if (want_kids and (made_love >= 5)):
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
                
            "Ask the doctor" if (profession != "doctor"):
                "I went over to the clinic and explained my symptoms. The first thing they had me do was give them a urine sample."
                "It turned out I was pregnant."

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
                her "That's so weird! But at least they'll be calling you 'daddy', so I won't be alone."
                him "You'll never be alone."
                $want_kids = True
                $made_love += 1   
            
    return

label monthly_event_15:
    "if pregnant, renewed concern about quality of food and its impact on fetus... but spouse might not agree that the more expensive food is better or whatever.  if not pregnant... maybe spouse gets tired of your cooking or something"
    return

label monthly_event_16:
    "if pregnant, morning sickness and getting behind on chores; if not pregnant, get sick and get behind on chores. Either way, do you ask your spouse for help or silently take care of it later?"
    return

label monthly_event_17:
    return

label monthly_event_18:
    return

label monthly_event_19:
    return

label monthly_event_20:
    return

label monthly_event_21:
    return

label monthly_event_22:
    return

label monthly_event_23:
    "birth if pregnant, pregnant if made_love is high enough (ran out of birth control), else what to do if no more BC and still don't want kids"
    return
