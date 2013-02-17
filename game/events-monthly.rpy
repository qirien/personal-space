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

# Alien Pests
label monthly_event_6:
    #biological pesticide--fungus
    "Our crops were starting to give and abundant harvest, but unfortunately, with the rainy season starting, they were being attacked by alien insects."
    "A small segmented insect like a sow bug but with thicker legs was our main culprit." 
    him "[her_name], we really have to think of a way to stop these insects from eating our crops."
    her "What have you done so far?"
    him "Well, I've tried picking them off individually and there are just too many now to do that. I wish we could just kill them all at once."
    her "I don't think we have the resources to do that."
    him "Yeah, that's why I was asking you for ideas."
    her "Well, we have a few options."
    menu:
        "{i}Take a sample bug in for research.{/i}" if (skill_knowledge >= 30 or skill_technical >= 30):
            "I collected a few of the insects and brought them to Lily for examination."
            Lily "These samples remind me of Tardigrades we have on Earth."
            her "Tardigrades?"
            Lily "They're an unusually hardy insect that can survive high and low temperatures as well as radiation. Because their adult forms don't increase in cell number, radiation doesn't mess their DNA like it does in animals whose cells are constantly splitting."
            her "That's... really interesting. Is there any way we could get rid of them?"
            Lily "I've been working on an organic pesticide made from fungus. I'm not sure sure if it will work on these insects though. May I keep your sample to test the pesticide on?"
            her "Sure, there's plenty more where that came from."
            "I watched as Lily sprayed the bugs with her mineral oil and fungus concoction."
            her "Um, it looks like they're still alive."
            Lily "Yes, if the pesticide works we will know in a few days."
            her "A few days? Our crops will be gone by then."
            Lily "It is a rather pressing matter. Do you have any mature garlic cloves?"
            her "I think we do, but why?"
            Lily "Garlic is a natural insect repellent. You'll still have to remove all the bugs, but if you can spray your plants with some diluted garlic it might stop them from returning as quickly."
            her "Well, it's worth a shot."
            "For the rest of the week we tried to to remove as many insects by hand as we could. Then we coated the plants with garlic juice. The work was long and hard, and we stunk afterwards."
            if (skill_physical > 20):
                "After a day's work in the field, I fell asleep right away, but in the morning I was ready to keep going."
            else:
                "After the first day I was exhausted. I wasn't able to help as much as I would have liked."
            him "We have baskets and baskets of these insects."
            her "I wonder if we could use them to help us somehow."
            him "That might work. Next time you see Lily, could you ask her about it?"
            her "Sure. Come to think of it, we should know if her pesticide was successful or not by now."
            "Lily's fungus experiment sucessfully killed a little over half the bugs I gave her. She lent me a sprayer and told me to bring it back as soon as possible."
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
        "{i}Use the bugs as food.{/i}" if (skill_domestic >= 30 or skill_creative >= 30):
            her "This is going to sound a little crazy, but I read that it's possible to make flour out of certain kinds of insects."
            him "Okay... will it actually help keep us alive?"
            her "If these insects are anything like Earth insects, they're highly nutritious. You know, low in saturated fats and carbs and high in amino acids."
            him "Well, can you find out if they're okay for us to eat? Because if we can somehow process them, we might not go as hungry this month."
            "I couldn't imagine eating them as they were, so I decided to grind them up and combine them with flour to make bread."
            ## to be continued
        "{i}Ask if anyone else is having the same problem.{/i}" if (skill_spiritual >= 30 or skill_social >= 30):
            her "Let's ask around and see if anyone else has had problems with these pests."
            
    return

label monthly_event_7:
    "How Honest Should You Be?"
    return

label monthly_event_8:
    "Conflict of Interest: Community vs. Spouse"
    return

label monthly_event_9:
    "Different Date Ideas"
    return

label monthly_event_10:
    "Something Bothering Him - What To Do?"
    return

label monthly_event_11:
    "Jealous of New Friend"
    return

label monthly_event_12:
    "Frustration with Work"
    return

label monthly_event_13:
    "Monthly 13"
    return

label monthly_event_14:
    "Pregnancy/ Tired And Emotional"
    return

label monthly_event_15:
    return

label monthly_event_16:
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
    return
