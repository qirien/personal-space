# Event content for all the important monthly events

# You shouldn't ever see this. This is just a fall through in case something happens
# and there's no event for this month.
label monthly_event_0:
    "Nothing exciting happened this month."
    return

# MONTH 1 - Chore allocation
label monthly_event_1:
    scene bg farm_interior with fade
    show her normal at midleft
    show him normal at midright
    play music "music/You.ogg" fadeout 2.0
    "Our first month living on our own together, we had to work a lot of things out."
    "Like, do we eat breakfast together, or separately? Who should cook and clean up?"
    menu:
        "What should I do about breakfast today?"
        "Make some for [his_name]":
            her normal "Here, [his_name], I made you some breakfast."
            him happy "Oh, thank you. I could just make it myself, you know."
            her happy "I don't mind making breakfast."
            $ loved += 2
        "Ask if he wants some":
            her normal "So, I'm making breakfast...do you want some?"
            him normal "Oh, that'd be great, thanks."
            her "Still just meal rations, until the crops start coming in."
            him "Yeah, it will be a while still."
            $ loved += 2
        "Don't make him any":
            him surprised "Oh, you made breakfast?"
            her "Sorry, I just made some for me."
            him annoyed "Okay, I can get my own."
            $ loved -= 2
    
    "That set the pattern for our mornings. Dishes weren't as easy to work out, though."
    her concerned "Thanks for making dinner, but you left the dirty dishes on the stove."
    him annoyed "I was going to do them later."
    her annoyed "You can't save them for later; they'll attract pests!"
    him "Well, I thought that since I made dinner, maybe you would do the dishes."
    her "In my house, whoever made the mess cleaned up the mess."
    him "Well, this is {b}our{/b} house, now."
    menu:
        "We'll do it your way":
            her normal "Okay, we'll do it your way. Whoever cooks, the other person cleans up afterwards."
            him normal "Great, that will work."
            "But it didn't work..."
            her annoyed "When were you going to do those dishes?"
            him annoyed "Those? I'm getting around to it."
            her angry "They're not going to clean themselves! Since I cooked, it's your turn to wash them!"
            him angry "Okay, but I'm not doing it right now, I'm in the middle of something!"
            "When we went to bed they were still there."
            her annoyed "Hey, [his_nickname]? You haven't done the dishes yet."
            him concerned "Oh, I'm too tired, I'll do it in the morning."
            "But the next morning, I found..."
                
        "We'll do it my way":
            her normal "Let's do it my way. Whoever cooks, cleans up afterwards."
            him annoyed "I guess that will work."
            "But it didn't work..."
            her surprised "Aren't you going to make dinner tonight?"
            him surprised "What? I wasn't planning on it..."
            her annoyed "But I made dinner last night."
            him annoyed "I'm not that hungry."
            "{b}I{/b} was hungry, so I just made dinner for myself. It felt a little lonely, though, eating by myself while he was poring over his charts for the farm. Still, I cleaned up and settled down to relax."
            her "(If he gets hungry he can make his own dinner.)"
            hide her with moveoutright
            "I fell asleep early, and awoke the next morning to find..."
                
        "{i}I'll be in charge of dishes{/i}" if (skill_domestic >= 10):
            her normal "Promptly cleaned dishes are really important to me, so why don't I be in charge of that? We can either take turns cooking, or cook together."
            him happy "Thanks, I really can't stand doing dishes. I'd rather do almost anything else."
            her surprised "Like getting the water for our breakfast?"
            him normal "Yeah, I'll do that."
            her normal "Thank you; I hate going outside first thing in the morning."
            "So that worked out pretty well."
            $loved += 5
            return

        "{i}Let's take turns fairly{/i}" if (skill_knowledge >= 10):
            her surprised "Did you know that men who do more housework are generally happier in their marriages?"
            him surprised "According to who?"
            her flirting "There's also a study correlating amount of housework done with frequency of sex."
            him annoyed "What exactly are you trying to say?"
            her normal "Just thought you might find those studies interesting. In a totally abstract way."
            him normal "It sounds like splitting household chores is really important to you."
            her "It is. We both work hard all day in different ways. We don't have to each do half of everything, but I think there will be less chance for arguments if we decide ahead of time what each person will do."
            him "All right, let's make a list, then."
            "We listed all the household chores we could think of, and then marked each one as \"hate\", \"enjoy\" or \"neutral\". It turned out that he really hated doing dishes, so I agreed to do them all the time, and since I was not a morning person, he would make breakfast every morning. We worked out the other chores, too."
            "So that worked out pretty well."
            $loved += 5
            return

    scene black with fade
    #if nobody did the dishes, pest problems!
    play music "music/Prelude02.ogg" fadeout 1.0
    her "AAAAAAAAAAAAAAAHHHHHH!!!!"
    scene bg farm_interior with fade
    show her surprised at midleft
    show him surprised at midright with moveinright
    him "What is it?! What's wrong?"
    "I just pointed to the dirty dishes. Coiled around his mess kit, happily nibbling on bits of leftover food, was a long, flat, segmented creature with innumerable legs and dangerous-looking claws. It was at least as long as my arm."
    him "Whoa!"

    menu:
        "I..."
        "Yelled":
            her angry "THAT is why you don't leave dirty dishes out overnight!!!"
            him angry "Okay! How was I supposed to know this planet had giant leftover-eating millipedes?"
            her "It's pretty obvious! Every planet has its scavengers!"
            him annoyed "Calm down, [her_name]. I'll take care of it."
            $relaxed -= 5
        "Cried":
            "I started sobbing."
            her sad "This would have never happened if you hadn't left out those dirty dishes!"
            him concerned "Hey, hey, it's okay, here, I'll take care of it."
            $relaxed -= 5
        "Laughed" if (relaxed >= 5):
            her laughing "Ha ha ha ha ha ha...\nWho invited the millipede to breakfast?"
            him happy "Sorry about that. He seemed like such a nice fellow last night..."
            her happy "I'm afraid he's worn out his welcome. Perhaps you could gently escort him off the premises?"
            him normal "It would be my pleasure."
            
        "{i}Analyzed{/i}" if (skill_knowledge >= 10):
            her surprised "Interesting. It's legs are jointed like an arthropod, but those claws look more crustacean ... of course, arthropods and crustaceans are not that far apart from each other... how did it get inside, anyway?"
            him normal "I think it crawled under the front door. There's quite a gap there."
            her "Huh. Looks like it's an omnivore; it ate the protein and the vegetables..."
            him "Well, whatever it is, we should put it back outside."
        "{i}Stayed calm{/i}" if (skill_spiritual >= 10):
            her surprised "Oh...my. That is...gigantic."
            him concerned "No kidding. Hold on, I'll get him out of here."
    "He put on his work gloves and picked up the mess kit by the handle. I opened the door so he could take it outside."
    him "C'mon, George, time to take a hike."
    her surprised "George?! You're giving this thing a name?"
    him happy "Doesn't he look like a George to you? Besides, I accidentally invited him in with my mess, so I guess he's my pet."
    her annoyed "As long as he's an outside pet."

    "The dishes were never left undone after that."
    return

# MONTH 2 - The Cellar
label monthly_event_2:
    play music "music/You.ogg" fadeout 2.0
    scene bg farm_exterior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve

    him "It'll sure be nice when we have some fresh food to eat."
    her annoyed "I know; I'm so tired of MREs!"
    him "It won't take too long until the radishes, spinach, and maybe even carrots are ready."
    her concerned "We don't have a refrigerator..."
    him "No, I was thinking of digging a cellar, but I just haven't had time...preparing the fields has taken longer than I thought."
    menu:
        "The cellar...?"
        "I'll do it!":
            her happy "Don't worry about the cellar; I'll take care of it!"
            him happy "Whoa, whoa, that's a big job - why don't we work on it together?"
            her normal "That does sound better, actually."
            play sound "sfx/shovel.mp3"
            "We dug and hauled out dirt and dug and hauled until finally we had a small cellar to store food in! We were exhausted, but it felt good to get it done together."
            stop sound fadeout 2.0
            $ loved += 5
            $ skill_physical += 5

        "{i}I'll surprise him...{/i}" if (skill_physical >= 10):
            her normal "We have time; don't worry about it yet."
            play sound "sfx/shovel.mp3"
            "I started digging after work, thinking I could get a lot dug before he came home, but..."
            him happy "Nice hole. Are you going to plant something in it?"
            her annoyed "No, it's going to be our cellar."
            him surprised "Oh."
            her "..."
            him normal "Why don't we work on it together?"
            "We dug and hauled out dirt and dug and hauled until finally we had a small cellar to store food in! We were exhausted, but it felt good to get it done together."
            stop sound fadeout 2.0
            $ loved += 5
            $ skill_physical += 5

        "{i}I'll help with the farm while you dig.{/i}" if (skill_domestic >=10):
            her surprised "Why don't you let me take care of the farm while you dig it?"
            him normal "Well...That could work. There's a lot of weeds that need pulling; I'll show you how to do the watering with the irrigation ditches I have set up."
            her normal "I can do that."
            him concerned "You can even...you can take Lettie if you want to."
            her laughing "Wow, you're trusting me with your favorite horse? I'm touched."
            him annoyed "I wouldn't trust anyone else."
            scene bg fields with fade
            "I rode Lettie around, scouting the fields for weeds. I had never noticed how big the farm was before -- [his_name] takes care of a lot of plants!"
            "It took longer than I thought, and I ended up helping him haul out a lot of the dirt he dug, but then we had our very own cellar!"
            $ skill_domestic += 5
            $ loved += 5

        "{i}Maybe I could build something to help.{/i}" if (skill_technical >= 10):
            her "Maybe I could build something to help dig the cellar?"
            him surprised "Really? That would be cool."
            "I researched and designed a simple machine with buckets and pulleys for getting the dirt up out of the hole. I was able to take one of the solar panels from the roof and power it with electricity."
            him happy "Oh, this will make it a lot faster!"
            play sound "sfx/shovel.mp3"
            "He dug in the hole, and I moved the dirt from where the machine dumped it to go on top of the roof of the cellar, which effectively made it deeper faster."
            stop sound fadeout 2.0
            "Even though it took a long time, it was kind of fun to work on it together."
            $ loved += 5
            $ skill_technical += 5

        "{i}Maybe the Peron's would help us dig it?{/i}" if (skill_social >= 10):
            her surprised "Maybe the Peron's would help us dig ours, and we could help them dig a cellar, too?"
            him happy "That would be great; it'll be more efficient with a few more people."
            "I talked to the Peron's and they thought that sounded great, so we were able to help each other have a cellar to store food in. They also gave us some eggs from their chickens, who were acclimatizing to Talam nicely."
            $ skill_social += 5
            $ community_level += 5

        "I don't want to help.":
            her "I'm sure you'll find the time."
            her "(All the farm stuff is his responsibility, anyway)"
            $ loved -= 5
            "It took him two weeks of digging and hauling dirt every second he wasn't caring for the plants. He fell asleep right after dinner, but in the morning he was back to digging again. Finally, it was finished."

    "Later in the month, he harvested some radishes, spinach, and carrots, and we were able to store them safely in the cellar."
    return

# MONTH 3 - His Birthday
label monthly_event_3:
    play music "music/Prelude22.ogg" fadeout 2.0
    "Even though we were on a new planet, we still kept track of what day it was on the Earth calendar. The seasons didn't match up or anything, but it helped us feel like we were still a part of things back home."
    scene bg farm_interior with fade
    show her normal at midleft with dissolve

    her "It's his birthday this month!"
    menu:
        "Maybe I should do something for him..."
        "{i}Have a party{/i}" if (skill_social >= 20):
            show sara at right
            show ilian at quarterright
            show thuc at quarterleft
            show julia at left
            show him normal at midright
            show her normal at midleft
            with dissolve
            "I invited some friends over and we ate dinner together and played games together until late. We sang Happy Birthday to [his_name]."
            him happy "Thanks, [her_name] - what a great birthday!"
        "{i}Make delicious food{/i}" if (skill_domestic >= 20):
            "I couldn't really copy his bread-cake that he made on the shuttle for my birthday, but I was determined to make him something tasty."
            "I found some berries that I had eaten before, and combined them with some biscuits from our rations to make a sort of berry shortcake. We had some candles in our emergency case, so I lit one of those for him, too."
            show him normal at midright
            her happy "Happy birthday, [his_name]"            
            him happy "Wow! Thank you! This looks great!"
            "It didn't taste anything like strawberry shortcake, but it was still good, and [his_name] seemed to like it."
            
        "{i}Make him a present{/i}" if (skill_creative >= 20):
            "I thought and thought about what I could make him that he would like."
            "I finally decided I would make him a hat."
            "I could only work on it when he wasn't paying attention, so it went pretty slowly. Finally, I was able to finish it."
            "I hoped he would actually like it, and not just pretend that he liked it."
            show him normal at midright
            her normal "Happy birthday, [his_name]. This is for you."
            him surprised "A birthday present?! Wow, thanks!"
            him happy "This hat is perfect! It'll keep the sun off my neck and it'll be warm in the cold wind, too!"
            her happy "I'm so glad you like it."
        "Make him a card":
            "I made him a nice card and gave it to him on his birthday."
            show him normal at midright
            him surprised "What's this for?"
            her happy "Today's your birthday! On the Earth calendar."
            him happy "Oh! I hadn't thought about the Earth calendar for a while! I forgot; thank you!"
            her sad "Sorry I couldn't really get you anything."
            him flirting "It's okay; I have everything I need right here."
        "Just tell him happy birthday":
            "I figured it'd be a waste of resources to make him anything special. We had what we needed. But I did tell him happy birthday, and he seemed to like that."
            show him normal at midright
            him normal "Thanks for remembering my birthday."
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
    her annoyed "It's none of your business what I do in my spare time."
    him annoyed "Well, it just seems kind of like a waste of time when there's so much real work to be done."
    her angry "Real work?! You don't think I do real work?!"
    him angry "Real work provides food, clothing, shelter. The necessities. We don't have extra time for anything else in order for the colony to survive."
    her "If it's just about survival, life isn't worth living."
    him "Well, you don't even get a choice if you don't survive. If something goes wrong, who's going to help us out here? There's no food banks, no Red Cross, no emergency rooms - just us."
    $ relaxed -= 10
    $ loved -= 10
    $ community_level -= 10
    menu:
        "You're freaking me out":
            her sad "[his_name], you're freaking me out. Are we going to die out here?"
            him annoyed "Maybe. But, live or die, it's up to us. Our hard work, or lack of it, will determine our fate."
            her concerned "That's so scary."
            him "At least we are in control. If we die, it's our own damn fault."
        "We can't focus on that all the time":
            her concerned "That's true, but we can't be working on food, clothes, and shelter twenty-four hours a day. If you don't take a break and think about other things once in a while, you'll go insane."
            him annoyed "Survival is mostly what I'm thinking about. Every day."
            her annoyed "Well, I can't live that way."
            him "Well, hopefully you won't die that way."
        "I can't talk about this anymore":
            her sad "Stop it, I can't talk about this anymore."
            him annoyed "Well, just think about what I said. Are we going to live or die?"
            her angry "I said stop it!"
            her sad "I don't want to die..."
            him annoyed "Then you need to choose to live."
    return

# MONTH 4 - Are Hobbies a Waste of Time?
label monthly_event_4:
    scene bg farm_interior with fade
    show her serious at midleft
    show him serious at midright
    with dissolve

    $ highest_skill = highest_stat()
    if (highest_skill == "Domestic"):
        him surprised "You spend a lot of time around the house; what exactly do you do?"
        menu:
            "What do I do?"
            "You really don't know?":
                her annoyed "What do I do?! You really haven't noticed?"
                him annoyed "I don't know; I'm sure you're doing something useful, I'm just not sure what."
                her annoyed "Well, have you noticed those clean clothes you're wearing?"
                him surprised "Oh, yeah, you washed those, huh?"
                her normal "And I've planted an herb garden out front to add flavor to our meals, and for herbal teas and things."
                him normal "Okay, that sounds good. Sorry, I didn't meant to accuse, I just really was curious what projects you've been working on."
            "What do {b}you{/b} do?":
                her surprised "What have {b}you{/b} been doing lately? You've been reading a lot."
                him normal "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field."
                him "I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they will grow."
                her concerned "Okay, well, that sounds very... necessary."
                her normal "I've made some curtains and planted an herb garden, in addition to keeping the house pretty spotless."
                him "Oh, is that what those plants are? The house is really clean, too; thank you."
            "It's none of your business.":
                jump unappreciated

    elif (highest_skill == "Creative"):
        him surprised "You spend a lot of time making crafts, don't you?"
        menu:
            "Do I?"
            "It's important.":
                her normal "I think it's important to know how to make things with what we have on this new planet."
                him "Like what kinds of things?"
                her "I made those placemats that keep our table clean, and I'm learning how to crochet. When our warm clothes from Earth wear out, we'll need to know how to make new ones with the resources we have."
                him normal "That's true...we can't just go to the store and buy stuff anymore, can we? Sorry, I didn't meant to accuse, I just really was curious what projects you've been working on."
            "{b}You{/b} spend a lot of time reading":
                her surprised "What about you? You've been reading a lot lately."
                him normal "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field."
                him "I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they'll grow."
                her normal "That sounds useful."
                her happy "I've been learning how to make things out of native materials, like these placemats."
                him "Oh, good. It's important for us to be independent from Earth."
            "You don't appreciate what I do":
                jump unappreciated
    elif (highest_skill == "Technical"):
        him surprised "You spend a lot of time tinkering with things, don't you?"
        menu:
            "Do I?"
            "It's important":
                her annoyed "When things break, we can't just take them to a repair shop. I try and keep everything in good condition so it won't break."
                him surprised "Like what?"
                her normal "Well, I installed the antenna that lets us communicate with the town, and the screw that brings water into the house."
                him normal "Yeah, I'm really glad to have those. Sorry, I didn't meant to accuse, I just really was curious what projects you've been working on."
            "What do {b}you{/b} do?":
                her annoyed "What have {b}you{/b} been doing lately? You've been reading a lot."
                him normal "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field."
                him "I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they'll grow."
                her concerned "Okay, well, that sounds very... necessary."
                her normal "I installed the antenna that lets us talk with the village, and the device that brings water into the house."
                him happy "I love those; thank you."
            "I can't believe you don't appreciate me":
                jump unappreciated

    elif (highest_skill == "Spiritual"):
        him surprised "You spend a lot of time just thinking about stuff, don't you?"
        menu:
            "Do I?"
            "It's important":
                her normal "So many things have changed, I think it's important to have a reason to work hard and help each other out."
                him surprised "Like what?"
                her flirting "Well, from my studies I've learned how important it is to answer someone with love, even if they are being insensitive or unappreciative."
                him flirting "...You probably have a lot of opportunities to practice that, don't you?"
                her happy "Well...yes. I think studying these principles helps me to get along better with others and work unselfishly."
                him normal "That is important. Sorry, I didn't meant to accuse, I just really was curious what you've been learning."
            "What do {b}you{/b} do?":
                her surprised "What have {b}you{/b} been doing lately? You've been reading a lot."
                him normal "Yeah, I've been reading up on all the plants we're growing and scheduling out what needs to be done each week for preparing, planting, tending, and harvesting each field."
                him "I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they'll grow."
                her concerned "Okay, well, that sounds very... necessary."
                her flirting "I've been learning about how important it is to answer someone with love, even if they are being insensitive or unappreciative."
                him flirting "That {b}is{/b} important."
                her sad "I'm not that good at it yet, though."
                him normal "I could probably use some reminders of that, too. Want to show me what you've been reading?"
                her happy "Sure, let's read together."
            "I can't believe you don't appreciate me":
                jump unappreciated

    elif (highest_skill == "Social"):
        him surprised "You spend a lot of time just hanging out with friends, don't you?"
        menu:
            "Do I?"
            "It's important":
                her annoyed "We need our connections with other people if we're going to survive as a community."
                him surprised "Does that really do any good?"
                her concerned "Well, remember those delicious dried fruits we got from the Peron's? We were \"just hanging out\" when we prepared them."
                him normal "Yeah, those are good."
                her normal "We can't survive by ourselves out here - we need the community."
                him normal "You're right; I don't like to depend on others, but we do need to work together."
            "What do {b}you{/b} do?":
                her annoyed "What have {b}you{/b} been doing lately? You've been reading a lot."
                him normal "Yeah, I've been reading up on all the plants we're growing, and I've scheduled out what needs to be done each week for preparing, planting, tending, and harvesting each field."
                him "I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they'll grow."
                her concerned "Okay, well, that sounds very... necessary."
                her normal "I'm not just \"hanging out\", you know. I'm building relationships in the community that we're going to need if we're going to survive. We can't make it alone here."
                him normal "You're right; I wish I didn't need anyone else, but I can't do everything."
            "I can't believe you don't appreciate me":
                jump unappreciated

    elif (highest_skill == "Knowledge"):
        him surprised "You spend a lot of time reading, don't you?"
        menu:
            "Do I?"
            "It's important":
                her normal "I've been researching native plants that we can use when our reserves from Earth run out."
                him surprised "Like what?"
                her normal "Well, we are working together on a list of edible plants, and I helped one of the families research how far their outhouse needed to be from the river."
                him normal "Oh yeah, that is important. Sorry, I didn't mean to accuse, I just was curious about what you're learning."
            "So do you":
                her annoyed "You read a lot, too."
                him normal "Yeah, I've been reading up on all the plants we're growing, and I've scheduled out what needs to be done each week for preparing, planting, tending, and harvesting each field."
                him "I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they'll grow."
                her concerned "Okay, well, that sounds very... necessary."
                her "I've been researching native plants, and helping the other colonists with their research. One family was going to build their outhouse just 15 meters from the river, but after I did some research I convinced them to build it at least 75 meters away."
                him normal "That's really important. Thank you for doing that, [her_name]."
                show her normal
            "I can't believe you don't appreciate me":
                jump unappreciated

    elif (highest_skill == "Physical"):
        him surprised "You spend a lot of time exercising, don't you?"
        menu:
            "Do I?"
            "It's important":
                her normal "I need to keep my body in good condition."
                him surprised "For what?"
                her happy "Well, did you know that I can run to town in six minutes? And I am getting pretty good at chopping wood, which we'll need when the cold season starts and our solar panels don't work."
                him normal "Oh yeah, that is important. Sorry, I didn't mean to accuse, I just was curious about what you've been doing."
            "What do {b}you{/b} do?":
                her annoyed "What have {b}you{/b} been doing lately? You've been reading a lot."
                him normal "Yeah, I've been reading up on all the plants we're growing, and I've scheduled out what needs to be done each week for preparing, planting, tending, and harvesting each field."
                him "I've also been researching ideal conditions for the strains of plants they gave us, so hopefully they'll grow."
                her concerned "Okay, well, that sounds very... necessary."
                her normal "On that hike, I found out about a new water source, and I can run to town in six minutes in case there's an emergency."
                him surprised "Six minutes?! That's pretty fast. You must have been training a lot. I guess I haven't thought about doing that because I usually ride Lettie around."
                her flirting "Well, not all of us have horses, so we have to make do with the legs we have."
                him flirting "And what nice legs they are..."
            "I can't believe you don't appreciate me":
                jump unappreciated

    "We ended up staying up late, talking about all the things we had been doing. I felt like I understood him a little better after that, and he seemed to appreciate what I was doing more, too."
    return

# MONTH 5 - What to do with trash
label monthly_event_5:
    scene bg farm_interior with fade

    "The village council asked us to do a waste assessment to see how much and what kind of materials we needed to permanently dispose of. If the amount of waste was too high, they told us that future colonists would be limited."
    "Our waste pile was fairly small, as we'd already composted any organic material that we didn't eat. Still, there were things like packaging from the MREs, a broken dish, and a pair of worn-out socks."
    show her normal at midleft
    show him normal at midright
    with dissolve

    her surprised "You threw away a perfectly good pair of socks?"
    him "Well, they have holes in the heels, and the rest of the material is getting thin. I wasn't sure if they were compostable."
    her concerned "We can't just throw things away when they break like on Earth. We need to take care of this planet for future colonists and the life forms that are already here."
    him annoyed "Well, what should we do with all this junk?"
    menu:
        "{i}I could see if any of our neighbors could use the fabric.{/i}" if (skill_social >= 20):
            her normal "One of my friends is making a quilt, and I think she could cut it up and use it for part of the batting."
            him surprised "Someone will have my skin cells in their quilt! I'm grossed out just thinking about it."
            her annoyed "Oh, get over it. We'll wash them real good."
            him normal "Well, as long as she's okay with it."
        "{i}I could use the broken dish in an artwork.{/i}" if (skill_creative >= 20):
            her normal "If I crushed the dish pieces even further, I could make a mosaic with it."
            him annoyed "Well, mosaics are great and all, but that's not very practical."
            her normal "Maybe you could use them at the bottom of potted plants to help them drain better."
            him happy "Okay, okay, maybe there's a way I could use that."
        "{i}I could mend this sock.{/i}" if (skill_domestic >= 20):
            her normal "I've been practicing some sewing and I could darn these socks."
            him surprised "Can this kind of sock even be darned?"
            her normal "I want to at least try."
            him normal "Okay, but we might have to think of another use for them if the darning doesn't work out."
            her happy "I could keep sock after sock until eventually I can make... a sock quilt!"
            him annoyed "..."
            her laughing "Think of how fun it would be to put all the weird sock shapes together in a rectangle!"
            him concerned "Um, well, I hope the darning works out."
        "{i}Let's think of a solution together.{/i}" if (skill_spiritual >= 20):
            her normal "It might be difficult, but I think if we work together we can think of some unusual ways to use these objects."
            him surprised "Hmmm. I might be able to use the packaging from the MREs to separate small rows of crops."
            her happy "And maybe I could turn these pieces of plate into labels for the crops."
            him normal "Oh, that would actually be really nice for next year."
        "{i}This stuff is actually compostable.{/i}" if ((skill_knowledge >= 20) or (skill_technical >= 20)):
            her normal "Actually, we can just compost all these things. They may take a long time to break down, but they will eventually. We can speed the process by breaking them up and spreading them throughout the pile."
            him normal "OK, I'll cut up the socks."
            her "I'll smash the plate. That sounds satisfying, anyway."
            him surprised "I guess this packaging we can tear into pieces like cave men?"
            her flirting "You mean Paleolithic humans?"
            him angry "Rawr, rawr."
            her flirting "Wow, you're so paleolithic."
            him flirting "I'll take that as a compliment."
        "{i}I could dig a deep hole for them.{/i}" if (skill_physical >= 30):
            her normal "If I dig deep enough, we can just get rid of this stuff and no one will know that we couldn't think of a way to reuse them."
            him happy "It could be our little secret."
            "I dug and dug and dug. After I buried the items, it was nice to not have it cluttering up the house. And I didn't have to feel guilty about preventing other people from starting a new life here."
            "Still, I couldn't help feeling like I might have done better."
            $ relaxed -= 5
            return
        "I'm sick of making all the decisions.":
            her annoyed "Why do I have to decide? You're just as much a part of this household."
            him annoyed "Well if it's up to me, then let's just throw it all out."
            menu:
                "Fine.":
                    her angry "Fine. Then it'll be partly your fault if our colony is making too much waste for more colonists to come."
                    him angry "Good riddance! I came here to get away from them."
                    "It took me several trips to get our trash to the designated area. Someone there said they were trying to recycle as much as possible, but I felt bad for not even trying."
                    $ relaxed -= 10
                    $ loved -= 5
                    $ community_level -= 5
                    return
                "I don't want to throw it all out.":
                    her concerned "I'll think of something on my own if that's how you feel."
                    him annoyed "Okay then."
                    "Over the next few days I tried to recycle the items I had, but nothing worked out. I ended up taking most of it to the designated dump. Someone there said they were trying to recycle as much as possible. At least I tried."
                    $ relaxed -= 10
                    $ loved -= 3
                    $ community_level -= 5
                    return
        "Let's compromise.":
            her surprised "We could throw away half of this stuff, and then try to think of uses for what we keep over the next few days."
            him annoyed "Okay."
            her surprised "Can you help me sort it?"
            him normal "Sure."
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
    show her normal at midleft
    show him normal at midright

    him annoyed "[her_name], we really have to think of a way to stop these insects from eating our corn."
    her surprised "What have you done so far?"
    him normal "Well, I've tried picking them off individually and there are just too many now to do that. I wish we could just kill them all at once."
    her surprised "I don't think we have the resources to do that."
    him annoyed "Yeah, that's why I was asking you for ideas."
    menu:
        her "Well, we have a few options."
        "{i}Take a sample bug in for research.{/i}" if (skill_knowledge >= 30 or skill_technical >= 30):
            "I collected a few of the insects and brought them to Lily for examination."
            scene bg lab with fade
            show her normal at midleft
            show lily at midright
            lily "These samples remind me of Tardigrades we have on Earth."
            her surprised "Tardigrades?"
            lily "They're an unusually hardy insect that can survive high and low temperatures as well as radiation. Because their adult forms don't increase in cell number, radiation doesn't damage their DNA like it does in animals whose cells are constantly splitting."
            her normal "That's... really interesting. Is there any way we could get rid of them?"
            lily "I've been working on an organic pesticide made from fungus. I'm not sure sure if it will work on these insects though. May I keep your sample to test the pesticide on?"
            her "Sure, there's plenty more where that came from."
            "I watched as Lily sprayed the bugs with her mineral oil and fungus concoction."
            her annoyed "Um, it looks like they're still alive."
            lily "Yes, if the pesticide works we will know in a few days."
            her angry "A few days? Our crops will be gone by then."
            lily "It is a rather pressing matter. Do you have any mature garlic cloves?"
            her surprised "I think we do, but why?"
            lily "Garlic is a natural insect repellent. You'll still have to remove all the bugs, but if you can spray your plants with some diluted garlic it might stop them from returning as quickly."
            her normal "Well, it's worth a shot."
            scene bg fields with fade
            "For the rest of the week we tried to to remove as many insects by hand as we could. Then we coated the plants with garlic juice. The work was long and hard, and we stunk afterwards."
            if (skill_physical > 20):
                "After a day's work in the field, I fell asleep right away, but in the morning I was ready to keep going."
            else:
                "After the first day I was exhausted. I wasn't able to help as much as I would have liked."
            show him serious at midright
            show her serious at midleft
            with dissolve
            him annoyed "We have baskets and baskets of these insects."
            her surprised "I wonder if we could use them to help us somehow."
            him surprised "Maybe we can. Next time you see Lily, could you ask her about it?"
            her normal "Sure. Come to think of it, we should know if her pesticide was successful or not by now."
            hide him
            "Lily's fungus experiment successfully killed a little over half the bugs I gave her. She lent me a sprayer and told me to bring it back as soon as possible, since some other farms had the same insects to spray."
            "When I asked her about how to use the dead insects we had caught, Lily said that we could use them to feed livestock."
            her "I'm not sure if our horse will like how they taste, but I'll try it."
            "We sprayed our crops. Sadly, we couldn't save many of them. Luckily, our underground crops like potatoes and beets weren't attacked by the insects, so we still had something to eat while we planted new crops."
            her normal "Oh, Lily told me we could use the dead insects for something..."
            him surprised "What is it?"
            her happy "We could feed them to Lettie!"
            him annoyed "Um... no."
            her normal "I think we should at least try it out! Maybe she'll like them!"
            him angry "Horses don't eat bugs!"
            her annoyed "Well I doubt they eat hay in the wild and it hasn't hurt them."
            him annoyed "I'll give her one, but if she gets sick or something, we are just going to crush the rest of the bugs and put them in the compost pile."
            "Lettie didn't seem to hate or like crushed insects, so I used them to extend her food. We still had a lot of leftover insects, so after making sure they were all dead I put them in the compost pile."
            him concerned "I'm glad we could use some of the bugs, but I don't think the crops they ate will last."
            her surprised "Why not?"
            him sad "They're full of insect eggs. The corn at least. Even if we pick all the infected crops off, I think it's too late to save them."
            her normal "Well, even if the corn is beyond saving, we could at least keep the greens for Lettie."
            him normal "And then some!"
            "We cut off and burned all the ears of corn that had eggs in them. We cut and dried all the corn stalks to turn it into hay."
            "[his_name] started plowing the land for a new crop."
        "{i}Use the bugs as food.{/i}" if (skill_domestic >= 30 or skill_creative >= 30):
            her surprised "This is going to sound a little crazy, but I read that it's possible to make flour out of certain kinds of insects."
            him surprised "Okay... will it actually help keep us alive?"
            her normal "If these insects are anything like Earth insects, they're highly nutritious. You know, low in saturated fats and carbs and high in amino acids."
            him normal "Well, can you find out if they're okay for us to eat? Because if we can somehow process them, we might not go as hungry this month."
            scene bg farm_interior with fade
            "I couldn't imagine eating them as they were, so after I boiled them, I ground them up and combined them with flour to make bread."
            "Well... it was more like crackers than bread, since the flour was so heavy. It was a little plain, so I made some beet jam to go with it."
            him normal "It tastes kind of nutty."
            him surprised "Gross! Is this an insect leg?"
            her normal "Yeah, for the next batch I'm going to try processing the flour a little differently. But for a first try it's not bad, is it?"
            him annnoyed "It's a whole lot better than nothing, that's for sure."
            "One day I sprinkled them with garlic salt and roasted them. They were crunchy and dry, but edible."
            him normal "So, eating these insects is great and all, but we should plant something else where that infested corn is right now."
            her surprised "Yeah... how do we get rid of the plants that are already there?"
            him normal "Well, I could burn them all, and then the ashes can fertilize the next crop."
            her concerned "Sounds better than nothing."
            "We piled all the corn plants into a huge bonfire. It burned into the night and made a big plume of smoke."
            "Our neighbors the Perons came by the see the fire, and we ate roasted insects as we watched the egg-infested crops turn to ash."
        "{i}Ask if anyone else is having the same problem.{/i}" if (skill_spiritual >= 30 or skill_social >= 30):
            her normal "Let's ask around and see if anyone else has had problems with these pests."
            him normal "Okay. I'll take Lettie into town; can you ask our neighbors?"
            her "Sure."
            "I found out that the Perons had the same insect eating their corn. To prevent the insects from laying eggs in the corn, they put mineral oil on the silks."
            "I radioed [his_name] and asked him to bring back some mineral oil from the storehouse. For the rest of the week, we put the oil on our corn silks and picked off the insects by hand."
            "I kept in touch with the Perons, and we made a huge pile of dead insects, which we ground up to extend the food we had for our livestock."
            "We were able to preserve some of our corn until it was ready for harvest, although for most of the corn, it was too late."
            scene bg fields with fade
            show overlay night
            show her normal at quarterright
            show him normal at center
            "We had a big bonfire with the Perons and burned the infested corn. Their kids danced around the fire, and they brought a chicken for us to roast."
            natalia "All that work..."
            him sad "I know."
            her sad "..."
        "Spray them with pesticide":
            him normal "We have some pesticide that we used for corn pests on Earth."
            her surprised "Will it work on these bugs?"
            him concerned "I don't know. Usually you apply it before the pests start eating the corn - it works better as a preventative. I hadn't put any on here because I didn't think any of the bugs here would eat an alien plant species."
            her normal "Seems like these bugs will eat anything."
            him normal "Yeah, well, let's give it a try."
            "We got some sprayers and face masks and gloves from the storehouse and got to work. Even with the face masks, the stuff smelled awful. It took all day to cover all the fields."
            "We tried to control where we sprayed, but it was windy and it kind of got everywhere."
            "When we were finally done, I had a terrible headache."
            her "Are we really going to eat the corn after we sprayed this poison on it?"
            him "If it works, yes. We don't have enough food to pick and choose."
            "It did seem to get rid of a lot of the pests. Whenever we ate it, I washed it really well, but it always tasted a little funny to me."
            $ relaxed -= 5
        "I have no idea.":
            her sad "I don't have any ideas...I'm sorry."
            him concerned "Well, let's try to salvage what we can."
            "All of the above-ground crops had been partially eaten by the insects. I started trying to cut off the bitten parts, but then I found eggs laid inside some of the corn. We didn't want the insects to keep coming back, so we ended up burning our corn field."
            him concerned "At least our next crop will have some really rich soil to grow on."
            her concerned "Yeah, and at least we have some potatoes, beets and ginger to eat for the next few months."
            him annoyed "But what if more insects destroy our existing crops?"
            her normal "Then we might have a very limited diet. Hopefully someone will find a way to keep them at bay."
            $ community_level -= 5
            return
            
    $ community_level += 5
return

# MONTH 7 - Broken computer - honesty?
label monthly_event_7:
    scene bg farm_interior with fade
    show her normal at center
    "One day I was doing the dishes at breakfast. [his_name] had already started working in the fields, so I was alone. I noticed he had left his computer pad next to the wash basin."
    her normal "I'll just move this out of the way so it doesn't get-- AHHH!"
    show her surprised
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
            call broken_computer_pad
        "Put it back and pretend not to know what happened":
            "I put it back where I found it. It was just an accident, so he doesn't need to know it was my fault, right?"
            "Even so, I was nervous when he got home."
            show her serious at quarterright
            show him normal at quarterleft with moveinleft
            him happy "Hey there, [her_nickname]."
            her concerned "Hi."
            "He washed his hands, and then picked up his computer pad."
            if fixed_computer:
                "I think he was checking his messages; it seemed to work fine. I started to feel a little less nervous."
                "I felt kind of bad for lying to him, but I didn't want him to be mad at me or think I was incompetent...it's not like I was lying about something important, right?"
                $ loved -= 2
                $ relaxed -= 5
            else:
                him annoyed "Hey, how come this won't turn on?"
                her surprised "Oh, your computer's not working?"
                him "Yeah, it was working fine this morning..."
                her concerned "Hmmm, I don't know."
                him normal "Well, I guess I'll take it in to the tech guys tomorrow if it's still not working. Do you mind if I use yours to check my messages?"
                her normal "Sure, go ahead."
                "Hopefully they would be able to fix it... "
                "I felt kind of bad for lying to him, but I didn't want him to be mad at me or think I was incompetent...it's not like I was lying about something important, right?"
                "The next day at dinner, it looked like his computer was working."
                her surprised "Oh, you got your computer working?"
                him annoyed "Yeah...I opened it up, and it was wet inside. Like someone had dropped it in some water."
                menu:
                    "Tell him what happened.":
                        her concerned "I dropped it in the sink the other day...that's why it's wet. It was an accident; I'm sorry."
                        him annoyed "So, you lied to me."
                        her concerned "Yes, I'm sorry."
                        him annoyed "Wow, I can't believe you didn't just tell me about i."
                        her annoyed "What's the big deal? It works now, doesn't it?"
                        him angry "This isn't about the computer! If you lie about something small like that, who knows what else you might lie about?"
                        her angry "Hey, I told you about it eventually."
                        him "Only when you got caught in your lie!"
                        her "I said I was sorry, okay?!"
                        him annoyed "...Okay."
                        $ loved -= 2
                        $ relaxed -= 2
                    "{i}Apologize sincerely.{/i}" if (skill_spiritual >= 40):
                        her concerned "I'm sorry, [his_name]. I dropped it in the sink, and then I didn't tell you about it because I didn't want you to know how clumsy I was. But I should have told you; I'm so sorry."
                        him annoyed "The computer's not a big deal, but we need to always be honest with each other."
                        her sad "I know; it was stupid of me to lie about it."
                        him normal "It's okay, [her_name]."
                        "He hugged me and I could tell he had forgiven me."
                    "Pretend you don't know.":
                        her surprised "I wonder how that happened?"
                        him annoyed "You really don't know anything about it?"
                        her normal "No, sorry. Anyway, it works now, so what does it matter?"
                        him concerned "..."
                        "He dropped the subject, but I could tell he didn't believe me. Well, whatever, it's not a big deal."
                        
                        $ loved -= 5
                        $ relaxed -= 5
        "Leave it on the table and tell him when he gets home":
            "I left it on the table so I would remember to tell him about it when he got home."
            show her at quarterright
            show him normal at quarterleft with moveinleft
            him happy "Hey there, [her_nickname]."
            her concerned "Hi."
            "He washed his hands, and then picked up his computer pad."
            him surprised "Did I leave this here this morning?"
            her "No, actually, you left it by the wash basin...and it fell in while I was washing the dishes."
            if fixed_computer:
                her happy "But I fixed it, so don't worry. It just needed to air out a little."
                him annoyed "Okay, hopefully everything still works fine..."
                "I waited while he logged on and checked a few things."
                him normal "Seems to be fine. I probably shouldn't leave my computer pad there, huh?"
                her normal "Probably not. Sorry I dropped it in the water, though."
                him "It's okay; no harm done."

            else:
                him annoyed "That explains why it won't turn on..."
                her sad "I'm really sorry; I feel so clumsy. I was trying to move it, so it wouldn't fall in, but it slipped out of my hands."
                him concerned "..."
                her concerned "I'm sorry..."
                him  "It's okay- I shouldn't have left it by the washtub. These things happen."
                her normal "Maybe they can fix it in town?"
                him "I'll check tomorrow."
                her concerned "In the meantime, do you want to use my computer? It's only fair."
                him concerned "Thanks, yeah."
                "I could tell he was kind of disappointed, but I felt glad I wasn't hiding anything from him."
                "And when he took it in, they were able to fix it so it worked just fine."
            $ loved += 2

    scene black with fade
    "A week later, I was reading my messages when I noticed that they were having a New Year's party."
    scene bg farm_interior with fade
    show her normal at midleft
    show him normal at midright
    with dissolve
    her surprised "Has it really been a whole year that we've been here?"
    him normal "Well, a year on this planet is only seven months, but, yeah. It's good for farming to have a shorter year, especially since the winters are so mild."
    her happy "Happy New Year, then!"
    scene black with fade
    "We all took a week off from working. People celebrated their winter holidays, worked on things at home, and visited each other. We ended the festivities with a all-night party at the community center."
    scene bg community_center with fade
    show him happy at midright
    show her happy at midleft 
    with dissolve
    him happy "We should make a toast..."
    menu:
        "What should we toast?"
        "To us!":
            her happy "To us!"
            if (loved >= 0):
                him happy "May we have many more years together..." #I got here while playing and it looped back to the beginning of the event. Does the if need a return after it?
            else:
                him normal "To us, then."
            $ loved += 2
        "To the colony!":
            her happy "To the colony! We made it one year!"
            him happy "May we all survive many more!"
            $ community_level += 2
        "To humanity!":
            her happy "To humanity! We're still here!"
            him happy "To humanity!"
            $ relaxed += 2
        "To partying!":
            her laughing "Here's to any excuse to party!"
            him laughing "To partying!"

    return

# MONTH 8 Want to watch a movie, he is busy helping neighbor
label monthly_event_8:
    scene bg library with fade
    "The library had a huge collection of Earth media that colonists could check out. They only had enough space for the most popular things, but it was still more media than anyone could experience in a lifetime."
    "One day I noticed they had a movie about space colonists. I was curious to see how people on Earth saw people like us, so I checked it out."
    scene bg farm_interior with fade
    show her normal at midleft
    show him normal at midright
    her happy "Hey, [his_nickname], I got a movie for us to watch tonight."
    him concerned "Oh, sorry, I told Thuc I'd help him build a fence tonight. He helped me build ours to keep the animals out of the crops, so I said I'd help with his."
    menu:
        "I was disappointed, but..."

        "Can't you do it another night?":
            her annoyed "Can't you help him another night? I was really looking forward to watching this with you."
            him serious "No, sorry, it has to be tonight."
            her normal "Okay, see you later."
            him normal "Bye, [her_nickname]."
            show her concerned
            hide him with moveoutright
            "The house suddenly seemed so quiet. I usually didn't mind being alone, but I had really been looking forward to this. The wind whistled mournfully through the cracks in the walls."
            menu:
                "What should I do?"
                "Watch it without him":
                    her annoyed "Forget it, I'm watching it without him!"
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
            "Things seemed better in the morning, but I still felt uneasy."
            $ loved -= 2

        "{i}I'll help, too.{/i}" if (relaxed>=0):
            her happy "I'll help too!"
            him surprised "Do you really want to?"
            her normal "Yes, we all need to work together to succeed. Plus, I'll get to be with you."
            him happy "All right, let's go!"
            scene bg sunset with fade
            show overlay night
            show her normal at midright
            show him normal at center
            show thuc at quarterleft
            "Thuc had already cut some logs and branches for us to tie up, but we still had to dig holes for posts."
            play sound "sfx/shovel.mp3"
            if (skill_physical >= 20):
                "It was a good thing I came, because there was a lot of hard work to do."
            elif (skill_technical >= 20):
                "It was a good thing I came, because I pointed out a better way we could make the fence that would be really sturdy."
            else:
                "I'm not sure I was much help, but I worked hard and did my best."
            "We worked hard in the gathering darkness, until the moons rose and gave us their wan light. We worked on and on, until finally it was done."
            stop sound
            thuc "Thank you so much, both of you."
            him "Glad we could help. I hope this fence holds up for you."
            thuc "Well, you can count on my help anytime, if you need it."
            her happy "Thanks, I'm sure we will."
            hide thuc with moveoutleft
            show him normal at midleft with move
            "We walked home by moonlight.  The two moons cast opposing shadows from the shrubs and trees, making a maze of light for us to follow. [his_name] reached for my hand."
            show him at center with move
            him normal "Thanks for coming. Everything's better with you."
            her flirting "Even putting up fences is not too bad when we're together."
            $ loved += 5
            $ skill_physical += 5
            $ community_level += 5
            scene black with fade
  
        "Want to watch it another night?":
            her normal "No problem, we'll just watch it another night."
            him normal "Thanks for understanding. I'll see you later, [her_nickname]."
            "It was a little lonely, especially since I was really looking forward to watching the movie with him, but I soon was absorbed in a good book and then went to bed."
            scene black with fade
            "We watched the movie the next night. Even though they got a lot of things wrong about space colonization, we really got into the drama and tension. We both cried a little at the end."
            $ relaxed += 5
            $ loved += 5
  
        "You're never here when I need you!":
            $ loved -= 5
            her sad "You're never here when I need you!"
            him annoyed "What are you talking about? I'm home almost every night."
            her "But you're always reading; I wanted to do something together tonight."
            him "Well, I can't. I promised Thuc I'd come tonight."
            her annoyed "I'm not really important to you, am I?"
            him annoyed "What?! Of course you are!"
            her angry "Then stay home with me!"
            him angry "No, I'm not going to break my promise. Now I have to go, we want to get this done before the moons set."
            menu:
                "He's leaving..."
                "Fine, just leave me here.":
                    her angry "Fine, just leave me here."
                    "He didn't say anything, just shook his head. I watched him leave, feeling hurt and lonely."
                    hide him with moveoutright
                    show her sad at center
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    scene black with fade
                    "I forgave him the next day, but I still felt insecure."
                    $ relaxed -= 5
                    "Finally, I just went to bed."
                "...":
                    "I didn't say anything; just watched him leave, feeling hurt and lonely."
                    hide him with moveoutright
                    show her sad at center
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something fun with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    $ relaxed -= 5
                    "Finally, I just went to bed."
                    scene black with fade
                    "I forgave him the next day, but I still felt insecure."
                "Sorry":
                    her sad "Sorry, [his_name]. I'm being selfish."
                    him concerned "It's all right, [her_nickname]. Let's do something together tomorrow night, okay?"
                    her concerned "Okay, [his_name]."
                    scene black with fade
                    "We watched the movie the next night. Even though they got a lot of things wrong about space colonization, we really got into the drama and tension. We both cried a little at the end."
                    $ relaxed += 2
                    $ loved += 5
    return

# Helper function for Month 9 where he tells her what he'd like her to do
label she_can_do_better:
    if (made_love < 2):
        him concerned "I'd like it if you showed more physical affection."
        menu:
            "What should I say?"
            "Typical man":
                her annoyed "Typical. That's all you men ever think about, isn't it?"
                him annoyed "No, sometimes we ask our wives what they would like and try to do it."
                $ loved -= 5
            "It's hard":
                her concerned "That's... hard for me. I'm just so tired all the time; sometimes it feels just like another chore."
                him surprised "It's a chore?"
                her annoyed "No! It's just... it takes work for me to be in the mood, sometimes."
                him annoyed "Well, you asked what I'd like."
            "OK, I'll try":
                her normal "We should make love more... it's important, even if we're tired or busy."
                him happy "Thank you, [her_nickname]."
                $ loved += 5
    elif (loved < 5):
        him normal "I'd like it if we spent more time together."

        menu:
            "Me too":
                her normal "I'd like that, too."
                him normal "Let's go on a walk together."
                her surprised "Right now?"
                him normal "Right after dinner!"
                if (loved < -5):
                    $ loved = 0
                else:
                    $ loved += 5
            "Doing what?":
                her concerned "Yeah, but what should we do? There's not exactly a lot going on..."
                him happy "I could read you Shakespeare."
                her laughing "Ha ha ha!"
                him sad "..."
                her surprised "You're serious?!"
                him annoyed "Well, I don't know! Doesn't it sound kind of fun to read to each other things that we like?"
                her happy "We could try it!"
            "We don't have time":
                her concerned "That sounds good, but we don't really have much free time, do we?"
                him concerned "We have been working pretty hard...but I think it's important to do things together. Even if we're just reading next to each other, that would be nice."
                her normal "OK, we can do that."
    elif (skill_domestic < 10):
        him "I'd like it if you did more things around the house."
        menu:
            "That's sexist":
                her annoyed "That's sexist. Women belong in the house, is that it?"
                him annoyed "Hey, you asked what I'd like. I'd like to come home to a clean, well-organized house."
                menu:
                    "If it's that important to you...":
                        her concerned "If it's that important to you, I could work on that."
                        $ loved += 5
                    "No way.":
                        her annoyed "Sorry, that's never going to happen."
                        him annoyed "..."
                        $ loved -= 5
                    "It's hard":
                       her concerned "That's... hard for me. With work and everything, when I come home I just want to relax."
                       him annoyed "Well, you asked what I'd like."
                       menu:
                           "I can try.":
                               her concerned "If it's that important to you, I could work on that."
                               $ loved += 5
                           "It's not going to happen.":
                               her annoyed "Sorry, that's never going to happen."
                               him annoyed "..."
                               $ loved -= 5

            "OK, I'll try":
                her normal "It would be nice if the house was a little neater... OK, I'll try to do that."
                him happy "Thank you, [her_nickname]."
                $ loved += 5
            "Let's work on it together":
                her normal "How about if we take some time one evening and clean up the house together?"
                him normal "Yeah, I guess we could do that."
                $ loved += 2 
    else:
        him happy "Nothing at all. You always make me feel loved, and everything around the house is always so clean and organized, and we spend lots of time together."
    return


# MONTH 9 - how could I do better?
label monthly_event_9:
    scene bg farm_interior with fade
    show him normal at midright
    with dissolve
    show her normal at midleft
    with moveinleft
    play music "music/You.ogg" fadeout 2.0
    him "I was just thinking about you. How do you think we're doing?"
    her surprised "At what?"
    him concerned "You know, in our marriage. Do you feel loved, is this working for you?"
    menu:
        "Honestly, no" if (loved <= 0):
            her concerned "Honestly, no, it's not."
        "(Lie) It's fine" if (loved <= 0):
            her concerned "Yeah, it's okay, I guess."
        "It's fine" if (loved >= 0):
            her normal "It's fine; I haven't really had time to think about things like that."
        "It's wonderful" if (loved >= 0):
            her happy "Of course! It's great!"
    if (loved > 0):
        him normal "Is there anything I can do to be a be a better husband to you?"
    else:
        him concerned "How can we make it better?"

    menu:
        "Give me stuff":
            her normal "I'd like if you gave me gifts - nothing big, obviously, but just something little to show you were thinking about me."
            him "Really? You like that sort of thing?"
            her "Yes, it would mean a lot to me."
            $ she_wants = "stuff"
        "Tell me how much you love me":
            her normal "I'd love it if you told me how much you love me."
            him surprised "Ummm... a lot?"
            her annoyed "No! Not like that! Like, what is it you like about me, and tell me things I do that you like, stuff like that."
            him surprised "That's what you like? Words?"
            her normal "Yeah. You have to mean it, of course."
            $ she_wants = "saynicestuff"
        "Do things together":
            her normal "I want to do things with you more often."
            him surprised "What kinds of things?"
            her "Anything - go on walks, make dinner together, play games together."
            $ she_wants = "dostuff"
        "Do things for me":
            her normal "I'd like you to do little things for me sometimes."
            him surprised "Like what?"
            her "Like, washing the dishes when it's my turn, or picking something up from the storehouse, or things like that."
            $ she_wants = "service"
        "Show more affection":
            her normal "I'd like to hold hands more, hug more, just be close to each other more."
            him normal "How about rubbing your shoulders? Like this?"
            her happy "Ohhh yeah, that definitely is good."
            $ she_wants = "affection"
        "I want you to know what I want":
            her normal "I don't want to have to tell you what I want; you should figure it out on your own."
            him annoyed "With what, telepathy? I thought that's what communication was for."
            her annoyed "Well, it's not romantic if I have to tell you 'Hey, don't forget to say 'I love you'."
            him "Okay, so you want me to say 'I love you' more often?"
            her "No! I mean, that's fine, but I want you to do romantic things because you feel romantic, not because you feel like you're supposed to."
            him angry "Tch, I give up. You obviously don't want to tell me what you want, and I'm not going to waste time guessing."
            $ she_wants = "nothing"
            $ loved -= 5
            hide him
            her angry "(He is not romantic at all!)"
            return
        "Nothing":
            $ she_wants = "nothing"
            her normal "You don't need to do anything differently; you're doing just fine."

    menu:
        "Thanks for asking":
            her happy "Thanks for asking; that's really sweet of you."
            $ loved += 2
        "I'm sorry":
            her sad "I'm sorry, I'm not a very good wife to you."
            if (loved <=0):
                him concerned "..."
                her surprised "What could I do better?"
                call she_can_do_better
            elif ((loved >= 5) and (skill_domestic >= 10) and (made_love >= 2)):
                him surprised "What are you talking about?! You are the perfect wife!"
                her surprised "Really?"
                him happy "Yeah! You always spend time with me, and show me lots of lovin', and you even take care of the house and everything."
                her flirting "There must be something I'm doing wrong."
                him serious "I can't think of a single thing."
            else:
                him normal "I think you do a pretty good job."
                her flirting "I'm sure there's something you'd like me to do differently. What is it?"
                call she_can_do_better
        "How about you?":
            her concerned "What about you? Is there something you'd like to see more of from me?"
            him concerned "Well..."
            call she_can_do_better

    scene black with fade
    "I wondered if he would actually do anything based on what I said I liked. A few days passed and I figured he had forgotten all about it."
    if (loved >= -5):
        "But then..."
        scene bg farm_interior with fade
        show her normal at midleft
        show him normal at midright with moveinright
        $ loved += 5
        if (she_wants == "stuff"):
            "He brought me some wild fruits he had found. He even checked with Dr. Lily to make sure they were edible first."
            her happy "Thank you!"
            him happy "They're just for you."
        if (she_wants == "saynicestuff"):
            him normal "Your laugh is like a supernova that blasts away my stress and makes the whole world seem like a garden."
            her laughing "Ha ha ha, ha ha, really?"
            him happy "Yes, and I love how you're such a good [profession]. Not only do you know what you're doing, but you're nice to people about it, too."
            her happy "Thank you, [his_nickname]."
        if (she_wants == "dostuff"):
            him surprised "Hey, want to go fishing?"
            her surprised "Fishing? I didn't know there were fish here..."
            him normal "Well, they're not exactly like fish, but there's plants and animals that live near the river that we can eat. Did you see Dr. Lily's email?"
            her normal "I didn't read it yet... but it sounds fun to do something with you!"
            "We found some edible plants, but when we tried to catch the animals there to eat, we ended up falling in the river together. We were laughing so hard we could barely stand up."
        if ((she_wants == "service") or (she_wants == "affection")):
            "After dinner one night, he started rubbing my feet."
            her concerned "Thanks, but I really ought to do the dishes now."
            him normal "No way. I'm taking over tonight. It's [her_name] night."
            her happy "I've never heard of that holiday before."
            him happy "That's because I just made it up."
            "He did the dishes for me and rubbed my feet with a smile."
            her flirting "Thank you, [his_nickname]."
        if (she_wants == "nothing"):
            "I found a poem on my pillow one afternoon:"
            "you are the sweetest thing\n not like honey or sugar"
            "but like the nectar of a bright flower\n you sustain even the clumsy bumblebee."
            her happy "(That was sweet of him...)"
            
    else:
        "Of course he wasn't serious about it. I shouldn't have gotten my hopes up, I guess."
        $ loved -= 5

    return

# MONTH 10 - Anniversary / Lettie is sick!
label monthly_event_10:
    scene bg farm_interior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    play music "music/Prelude02.ogg" fadeout 2.0
    "It was our anniversary, according to the Earth calendar.  I think we had missed a few while we were on the shuttle? Anyway, it felt like we had been married about a year."
    her happy "Happy Anniversary!"
    him surprised "Really? Today?"
    her normal "Yeah! Well, it depends on how you calculate it, but I feel like celebrating it today!"
    him happy "Great, what do you want to do?"
    her happy "I'll make us a nice dinner tonight."
    him normal "Okay, I'll bring home a surprise for you."
    her surprised "Really?"
    him normal "Yeah! I mean, don't expect too much, but I've got an idea."
    call set_work_bg
    "All day long I looked forward to spending a nice evening together."
    scene bg farm_interior with fade
    show her normal at center
    "I got some special ingredients at the storehouse, and made a nice dessert and everything. But [his_name] wasn't home yet."
    her annoyed "(He knows we were going to celebrate today! Where could he be?)"
    "I tried calling him on the radio, and messaging him on the computer, but he didn't answer."
    "Finally, just when I was about to give up and eat without him, he stepped in."
    show him serious at midleft with moveinleft
    show her at midright with move
    menu:
        "He's so late..."
        "Is everything okay?":
            her concerned "You're home late, [his_nickname]. Is everything okay?"
            him concerned "Yeah."
            $ loved += 1
        "Did you forget about tonight?":
            her annoyed "You're home late - did you forget about our anniversary dinner tonight?"
            him concerned "Yeah."
        "Where have you been?!":
            her angry "Where have you been?! I've been waiting here for an hour!"
            him concerned "Sorry."
            $ loved -= 1
    "He didn't look at me, just washed his hands and sat at the table. He was reading on his computer pad while we ate dinner.  We ate in silence for a few minutes. I thought maybe I'd change the subject."
    her normal "Something funny happened at work today."
    him concerned "Yeah?"
    her happy "Little Van, you know, the Nguyen's youngest, came by with his mom, and he said, 'I am an alien that looks like a kid. I really am. I'm not pretending.'"
    him concerned "Yeah?"
    her normal "Yeah, it was funny, because he's so serious about it..."
    him "Mmmmm."
    menu:
        "What should I say?"
        "Are you listening to me?":
            if (relaxed >= 0):
                her annoyed "(Is he even listening to me?!)"
                her happy "Also, I was thinking after dinner I'd take off all my clothes and parade downtown."
                him "Yeah."
                her laughing "Why don't you come with me?"
                him "Mmm-hmmm."
                her happy "Great! What song shall we sing?"
                him surprised "Hmmm- what?"
                her normal "What song are we going to sing as we're dancing around town naked?"
            else:
                her annoyed "Are you even listening to me?!"
                $ loved -= 5
            "He just looked at me for a minute, then shook his head."
            him concerned "Sorry, [her_name], not right now. I've got to check on something."
            jump follow_him

        "{i}What's bothering you?{/i}" if ((skill_spiritual >= 40) or (skill_knowledge >= 40)):
            her concerned "You seem troubled. What's bothering you, [his_nickname]?"
            "He was quiet for a minute, finishing up his dinner. I was about to ask again, when he said,"
            him serious "Sorry, [her_name]. I can't talk about it right now. I've got to go check on Lettie."
            her surprised "Is she okay?"
            him concerned "I don't know."
            "He headed out the door."
            jump follow_him

        "(Say nothing)":
            "I figured he would tell me what was bothering him when he was ready."
            jump anniversary_next_day

label anniversary_next_day:
    scene black with fade
    "He didn't come home that night, just stopped in for a quick breakfast early in the morning and then left again. I didn't have a chance to talk to him again until that evening when I got home."
    scene bg farm_interior with fade
    him normal "Hey, [her_nickname]."
    menu:
        "(He's just saying hi like nothing happened!)"
        "Ignore him":
            her annoyed "(He ignored me all last night; let's see how he likes it.)"
            her angry "..."
            him surprised "Hey, are you mad?"
            menu:
                "(Am I mad?!)"
                "Yes!":
                    her angry "Yes, I'm mad! We were supposed to have a nice dinner for our anniversary, but you just left without saying anything!"
                    him angry "Lettie was sick! Really sick!"
                    her "And you couldn't have said something like, 'Sorry, Lettie's sick, gotta go.'?"
                    him annoyed "I'm sorry; I was too worried."
                    her annoyed "Well, is she okay?"
                    him serious "Yes, she's fine now."
                    him concerned "Um, here, I got you these."
                    "He handed me a glass bottle with wildflowers in it."
                    her surprised "Oh! Thank you, [his_name]."
                    him normal "Happy Anniversary."
                    show her normal
                    "We kissed perfunctorily. I still felt a little mad, but we'd get over it."
                "No.":
                    her annoyed "No, why would I be mad? Where I come from it's totally normal to ignore your wife on your anniversary."
                    him normal "Lettie was-"
                    her angry "Lettie?! You were thinking about your HORSE?!"
                    him angry "Tch, forget it! You are obviously more interested in your own righteous anger than in knowing what actually happened. Here."
                    "He slammed a glass bottle with some wildflowers in it on the table. Water sloshed onto the table and a few of the flowers fell out."
                    him "Happy Anniversary."
                    "Then he stormed out."
                    $ loved -= 5
        "Ask what happened":
            her concerned "What happened? Last night you were really worried about something."
            him serious "Oh, it was Lettie. I think she ate something poisonous while she was grazing - she was really sick."
            him happy "But she's doing better today; I think she'll be fine."
            her happy "Oh, I'm glad she's okay."
            him normal "Yeah, me too."
            him concerned "Sorry about last night - I know we were going to celebrate our anniversary and everything, but I just couldn't celebrate when I was so worried about her. But I did get you something."
            her surprised "What?"
            "He pulled out some wildflowers - he must have picked them earlier today. He had put them in an old glass bottle for a vase."
            show her normal
            him serious "The little bit of beauty these flowers bring can't compare to the joy you bring to my life. They won't last forever, but my love for you will."
            menu:
                "What should I say?"
                "They're lovely!":
                    her happy "Oh, they're lovely! Thank you!"
                    him concerned "Sorry it's not much..."
                    her normal "It's just right. I love you, too."
                "Thank you.":
                    her normal "Thank you."
                    him concerned "Sorry it's not much."
                    her happy "It's okay; we don't have much."
                    him happy "But I'm so glad I have you."
                "At least it's not another cheesy poem.":
                    her laughing "Ha ha, at least it's not a cheesy poem like for my birthday."
                    him annoyed "Hey! I worked hard on that poem! I poured out my heart to you!"
                    her happy "I know, and it was really sweet... but also really cheesy."
                    him serious "Well, at least I learned my lesson."
                    her flirting "I think there's still a few things you could learn."
                    him flirting "Are you going to teach me?"
            "I didn't even have time to set the flowers down before he wrapped his arms around me. I kissed his chin, then his lips, and we forgot about everything else for a while..."
            $ made_love += 1
            $ loved += 5
    return

label follow_him:
    menu:
        "Go with him.":
            her serious "I'll help you."
            him concerned "Okay."
            scene bg farm_exterior with fade
            show overlay night
            "We walked to the small barn where the animals could sleep at night, and where we could keep hay dry."
        "Follow him quietly.":
            "I waited until he left, then I silently lifted the latch and followed him out."
            scene bg farm_exterior with fade
            show overlay night
            "He headed for our small barn, and I followed him."
        "Let him go.":
            "He'd tell me what was bothering him when he was ready. I decided to settle down with a book and wait until he came back."
            jump anniversary_next_day

    scene bg barn with fade
    show him serious at midright
    show her serious at midleft
    with moveinleft
    "Lettie was inside, twitching and breathing hard."
    her surprised "What's wrong with her?"
    him serious "I think she ate something bad. Usually she's fine grazing on the things here, but maybe it was a strange plant she didn't know was poisonous?"
    her concerned "Oh no! Is there a vet or someone you can call?"
    him concerned "I'm the closest thing we have..."
    if (profession == "doctor"):
        him normal "...aside from you, of course."
        her serious "Can you induce vomiting?"
        him serious "No...horses can't vomit."
        her normal "I can give her some medicine to help the pain at least..."
        him serious "Please do; I'm worried she's going to hurt herself."
        "I did a quick search on my computer to see what medicines were safe for horses.  Then I got my bag and gave her an analgesic. She seemed to calm down a little."
    else:
        her surprised "Oh no! What can we do?"
    him serious "Maybe we can help whatever's bothering her to pass through. Do we have any mineral oil? Or milk of magnesia?"
    if (profession == "doctor"):
        her normal "There's some laxatives at the clinic; I'll get some."
        hide her with moveoutleft
        scene bg clinic with fade
    elif (profession == "crafter" or skill_creative >= 40):
        her normal "They have some mineral oil in the workshop; I'll get it."
        hide her with moveoutleft
        scene bg workshop with fade
    else:
        her normal "Somebody's got to have some! I'll ask Ilian at the storehouse."       
        "I got on my computer and sent him a message. I also sent one to the doctor and the Nguyens, in case they had any ideas."
        "Ilian got back to me pretty quick and said he could get some and he'd meet me at the storehouse."
        hide her with moveoutleft
        scene bg storehouse with fade

    if (skill_physical >= 40):
        "I ran all the way there and back. Good thing I was in shape."
    else:
        "I walked and jogged as fast as I could. I was breathing so hard I thought I was going to throw up when I finally got back."
        $ relaxed -= 5

    scene bg barn with fade
    show him serious at quarterright
    show her serious at midleft with moveinleft
    "He had me hold Lettie still while he measured it out and administered it to her. I was amazed how much Lettie trusted him."
    "She didn't seem to feel any better right away, but I knew this kind of medicine takes awhile to work."
    him serious "I'm going to take her for a little walk - why don't you get some rest?"
    menu:
        "Should I get some rest?"
        "I'll stay with you.":
            her normal "I'll stay with you."
            him normal "Okay."
            "We walked around with Lettie for a while, and then we let her rest and have plenty of water to drink. She still didn't seem to feel better, but she wasn't getting worse, either."
            "[his_name] sat down in some clean hay. It was a little scratchy, but I sat down next to him."
            show him sleeping
            show her sleeping
            with dissolve
            "I must have fallen asleep, because I woke up and it was morning. We had spent all night in the barn..."
            $ loved += 2

        "Okay, hope she feels better.":
            her normal "I think I will. I hope she feels better, soon."
            him serious "Thanks, [her_name]."
            scene black with fade
            "I didn't sleep that well that night."
            "The next morning, I decided to check on Lettie and [his_name]."

    scene bg barn with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    "[his_name] was already up, talking to Lettie in a soft voice and petting her nose. She wasn't shaking any more, and her breathing seemed more regular."
    her happy "She seems better!"
    him normal "Yeah, I hope so. I'll give her some really good food today and let her take it easy for a while."
    her normal "Well, I have to get to work, but I'll see you this evening."
    him serious "Hey, thanks for staying with us, and helping out. It was a lot better not having to wait alone."
    her normal "You're welcome. I'm glad we could help her."
    "He turned to me and wrapped his arms tight around me. His voice was a little hoarse as he whispered,"
    him serious "Everything's so fragile...\nI love you, [her_name]."
    show her concerned
    menu:
        "What should I say?"
        "I love you, too.":
            her serious "I love you too..."
        "You owe me big time.":
            "I pulled away enough to poke at his chest sternly."
            her angry "You owe me, [his_nickname]. Last night was our anniversary dinner - I don't think you even noticed because you were so distracted - but you owe me a fabulous night tonight."
            him surprised "Our anniversary! I'm so sorry - but I will make it up to you tonight."
            her flirting "Shall I make a list for you?"
            him flirting "I think I know what you like."
            $ made_love += 1
    $ loved += 10
    $ relaxed += 2
    return

# Helper function for month 11
label goto_ocean:
    scene bg talam with fade
    "There wasn't a road going out to the ocean, so we had to make our way through wild vegetation."     
    "We had some minor run-ins with small insects, but nothing too surprising." 
    scene bg ocean with fade
    "Arriving at the ocean was magnificent. The air was moist, and my eyes could rest on a flat plane of wetness extending to the horizon."
    show lily at left
    show her normal at midright
    with dissolve
    if (ocean_character == "Sven"):
        show sven at right with dissolve
        sven "Whoa, this beach reminds me Earth. Lots of rocks and a big blue wet thing." 
        her normal "I think you mean ocean. It's making me a little homesick too." 
    if (ocean_character == "Brennan"):
        show brennan at right with dissolve
        brennan "I didn't think there would be so many rocks at the seashore. There's barely any beach!" 
        her serious "Well, we're not here to swim anyway."
        brennan "More's the pity."
    if (ocean_character == "Sara"):
        show sara at right with dissolve
        sara "It's not the kind of beach I'd want to swim on, and I'm glad I brought a sweater, but this is such a sight for sore eyes!"
        her happy "It's an amazing view." 

    lily "I'm so glad we made it! Okay, I'd like to take samples of this crusty white stuff and any other organic material you can find."     

    if (ocean_character == "Sven"):
        sven "Okay, you guys do the stuff on the shore, and I'll get some of this coastal brush." 
        lily "I'm going to take some of the smaller creatures and plants back too."
    elif (ocean_character == "Brennan"):
        brennan "Lovely. Is it all right if I touch the water?" 
        lily "I would advise against it until we know what's in it. I would like to take a sample of it though, if you wouldn't mind. I'm going to take some of the smaller creatures and plants back too."
    elif (ocean_character == "Sara"):
        sara "Okay, I'll take samples of anything that's not moving." 
        lily "I'll focus on some of the smaller creatures then."

    her surprised "How much of this white stuff do we need?" 
    lily "The guano? Just get as much as you can. We have an hour or two so don't feel too rushed."
    her annoyed "Eww! It's excrement? Well, I guess if it's for science I can do it."
    "We worked hard to get the samples we needed. We found a lot of shells and some bones. As we were getting ready to leave, the tide started to come back in."
    "The incoming waves were purple with one kind of alien sea creature. It had six spiny or hairy arms, and floated like a jellyfish."  
    lily "Oh! I've got to record this."
    if (ocean_character == "Sven"):
        sven "Be careful! Those critters might be deadly!"
    elif (ocean_character == "Brennan"):
        brennan "Just be careful not to get swept away!" 
    elif (ocean_character == "Sara"):
        sara "Oh, I want a picture too! I can't wait to show everyone how beautiful our planet is."

    "It surprised me how quickly the tide rushed back in. Little spider-crabs rushed to dry rocks, and many got swallowed up by the waves and the purple jellies."
    "A wave splashed under Lily's feet, and one of the purple spiny jellys grabbed at her leg."
    show lily at midleft with move
    lily "O-oh!"
    "[ocean_character] looked on in horror as I jabbed the animal with my shovel. As I contacted it, its arm fell off, still wrapped around Lily."
    if (skill_physical >= 40):
        "Lily had a strange look on her face, so I carried her further inland so she could sit down."
        "She wasn't blinking, so I pinched her a few times."
        lily "Hey, knock it off! What happened? Did I fall asleep?"
    elif (skill_knowledge >= 40):
        "Lily appeared to be temporarily paralyzed, so I motioned to [ocean_character] to help me carry her further inland."
        "I was trying to think of what I could do to help her when she came out of her trance."
        lily "W-what happened? Did I fall asleep?"
    else:
        "I had no idea what to do next. I just stood there, scared."
        if (ocean_character == "Sven"):
            sven "Don't just sit there, do something!"
            "Lily started to collapse, but luckily she fell onto me and I could support her." 
        elif (ocean_character == "Brennan"):
            show her at right with move
            show brennan at midright with move
            "[ocean_character] rushed over to catch Lily as she collapsed."
        else:
            show her at right with move
            show sara at midright with move
            "[ocean_character] rushed over to catch Lily as she collapsed."
            
        her surprised "Umm..."
        lily "W-what happened? Did I fall asleep?"

    her normal "No, one of the purple jellies latched onto you."
    lily "Weird. I feel like I just woke up from a dream."
    her serious "Its tentacle is still on you; we should probably remove it."
    lily "Oh, I'll take care of that."
    if (ocean_character == "Brennan"):
        brennan "Did that animal make you fall asleep?"
        lily "I don't have narcolepsy, but it has been an unusually exhausting day. Maybe I overextended myself."
        brennan "Well, let me know what you find out about that thing."
    elif (ocean_character == "Sven"):
        "She carefully grabbed it with her tweezers and moved it into a specimen bag. Sven and I looked at each other with exasperation. Maybe she was a little TOO dedicated."
    else:
        sara "Don't worry, I made sure your camera was safe!"
        lily "Thank you! Maybe I just had a little too much sun today."

    return

# MONTH 11
# uses knowledge, physical, creative
#I read about rocket stoves and thought it would be fun to write an event on them http://www.richsoil.com/rocket-stove-mass-heater.jsp   
label monthly_event_11:
    scene bg farm_interior with fade
    show him normal at midleft
    show her normal at midright
    with dissolve
#do we have a winter? I think there was a winter, but it was a mild one or something?
    "It was another cloudy day, and there wasn't enough solar power to cook and warm our house with."
    him serious "I'll go get some wood. Can't we just cook inside?."
    her annoyed "No, remember how our chimney has a huge crack in it?"
    him annoyed "I'll cook outside then."
    hide him with moveoutleft
    her serious "There's got to be a better way to distribute all this energy."
    "I spent the evening researching low-power heating. Some people found that light bulbs helped heat their houses, but we had LEDs that didn't give off much heat."
    "I found a type of combustion stove called a rocket stove, which burned wood sideways very cleanly. I'd need some metal pipes though." 
    "I knew we were saving a lot of the metal from the shuttle for emergencies. I wasn't sure what I would do."
    show him normal at midleft with moveinleft
    her normal "If we want to advance technologically, we've got to start making our own metal. It's like, the next thing on the tech tree."
    him normal "I heard that Lily is gathering ores to see if we can start making our own metal here. But I think gunpowder is next on the tech tree."
    her surprised "Really? Why didn't anyone inform me?"
    him annoyed "Well, you're not digging around in the dirt during your working hours. She probably just sent it out to all the farmers."
    scene black with fade
    "I ran over to the lab the next morning, excited to help."
    scene bg lab with fade
    show lily at quarterright with dissolve
    show her normal at midleft with moveinleft
    her surprised "I heard you've been gathering ore?"
    lily "Yes! Do you have some you'd like to donate?"
    her happy "I don't, but I'm willing to test the material's melting point!"
    lily "Are you hoping to make something?"
    her normal "Yes, I want to make a rocket stove to heat our house on cloudy days."
    lily "I don't really have enough to make anything with it yet, but I can help you find more metal."
    lily "I've received samples of three different ores, and I think one could make the kind of metal you're looking for. You'd need to go mining for it though."
    her surprised "Mining, like with a pick?"
    lily "Yes. I think gunpowder would help a lot too."
    her "Blowing up rocks? Is that allowed?"
    lily "Well, we are supposed to survive in a way that doesn't damage the existing ecosystem excessively."
    her normal "Tell me where you think the metal is and I'll see if I can get it out using our pick. I don't think I want to think about gunpowder quite yet."
    lily "I will tell you where the metal is, but I want your help collecting some samples from a semi-remote location first."
    her annoyed "Don't you think metal is more important than documenting organisms?"
    lily "No, I don't. And you never know, maybe one of these creatures will have an iron lung or something."
    her normal "Okay, what do I need to bring?"
    lily "Well, a backpack, food, and another person."
    her surprised "Another person?"
    lily "Yes, it's much safer to travel in a group of three than a group of two. At least, that's what I believe from my observations and the small amount of anecdotal evidence on the behavior of the local carnivores."
    her serious "When do you need me to be ready?"
    lily "Well, the next low-low tide is in two days. That's when the moons should be in sync long enough to make a tide anyway."
    her normal "Okay, I'll talk to [his_name]."
    scene bg farm_interior with fade
    show him normal at midleft
    show her normal at midright
    with dissolve
    her happy "Hey, [his_name], do you want to come to the ocean with me?"
    him surprised "Wouldn't it take half the day just to get there? Why do you want to go?"
    her normal "Lily said she would help me find and purify metals if I helped her collect specimens at the ocean."
    him concerned "That sounds fun, but I'm worried that if I take a day off from farming, my plants will die."
    her annoyed "Really? They would die if you left them just one day?"
    him annoyed "Well, it's more like some of the food might get eaten by something else since it's harvest time again."
    her normal "Okay. I'll try to find someone else."
    scene black with fade
    menu:
        "Who should I ask to come?"
        "Sven, the librarian":
            $ ocean_character = "Sven"
            scene bg library
            show sven at quarterright with dissolve
            show her normal at midleft with moveinleft
            her normal "Hey, Sven."
            sven "Hi, how can I help you?"
            her "Want to come with Lily and me to the seashore?"
            sven "The seashore? The one a few kilometers away?"      
            her happy "Yeah, a real beach! Bring a shovel!"
            sven "No way. Not after what I've been reading about giant sea creatures and this planet."  
            her surprised "What have you been reading?"  
            sven "Well, I read that the animals in the ocean probably tolerate radiation the best, since the water can diffuse the radiation. The satellite telescope that came with us showed some strange, large shadows in a few of the oceans, and no one knows what they are."
            her serious "It could be a whale or something?"
            sven "No. These are much bigger. Pretty darn creepy, if you ask me."
            her normal "Well, we're not going out to the middle of the ocean, just the shore. Wouldn't it be fun to get out of your stuffy library for a day?"
            sven "Now that you mention it, I have been wanting to go for a hike."
            her happy "Just think of it as a long hike, and if the beach scares you you can stay far away from it."
            sven "Okay, can do."
            call goto_ocean
                    
        "Brennan, my co-worker":
            $ ocean_character = "Brennan"

            call set_work_bg
            show brennan at midright
            show her normal at midleft
            with dissolve
            "I was trying to think of who could come with us at work the next day."    
            brennan "I just wish I could get away from it all! I feel like I'm trapped in this tiny town."
            her normal "Didn't you know what you were getting into when you signed up for this?"
            brennan "Who says I signed up? Besides, I bet you're itching to have an adventure too."   
            her serious "You should come to the ocean with me." 
            brennan "Really?"   
            her happy "Yes! Lily is coming too, and we need a third person so we can look like a herd and not easy pickings."   
            brennan "Count me in! But why are you going to the ocean? Thinking of going for a swim?"
            her normal "No, Lily wants to gather specimens."
            brennan "I don't really care what we do, as long as it's something exciting."  
            her happy "Oh, it'll be exciting."

            call goto_ocean

        "Sara, my friend":
            $ ocean_character = "Sara"
            scene bg community_center with fade
            show sara at midright
            show her normal at midleft
            with dissolve
            "At lunch, I asked Sara if she was interested in going on a field trip to the ocean."
            sara "Oh, I've been wanting to see the ocean ever since I felt so claustrophobic in that shuttle!"
            her surprised "Really? It's kind of a long hike. Are you sure you're up for it?"
            sara "I haven't been just sitting around all day! I'll have you know that I'm in top shape!"
            her concerned "Usually you're so worried about trying anything new, I'm kind of surprised that you're so excited about this."
            sara "Yeah, I guess it could be dangerous. But I used to live by an ocean, so I kind of miss it."

            call goto_ocean

    scene bg talam with fade
    "After Lily got her bearings, we made the long trip back."
    her surprised "Can you remember anything from your dream?"
    lily "My... dream?"
    show her serious
    "Maybe she hadn't been dreaming."
    scene bg lab with fade
    "The next day, Lily told me where to go for the most ore-rich rocks. I followed her directions and gathered nearby rocks. I was pleasantly surprised by how little I needed my pick."
    "I had a lot of help from Lily and Ilian in melting the rocks and using the 3D printers to make the metal can and pipes I needed."
    "I arranged the pipes around the inside of our house and covered them with mud. The rocket stove easily heated our whole home using only a few sticks."
    if (skill_creative >= 40):
        "I made the mud on top of the pipes into a large mud bench. Since it was a little too hot, I made some cushions from dried grasses. It felt luxurious, like having a heated bed."
    # I'm thinking that Lily might make gunpowder on her own. It's such a loaded (heh, sorry) technology that I felt like the implications for introducing it this soon were a little overwhelming to handle in one event.
    # I'm also thinking that some of the sea creatures can kind of communicate with humans by accessing their nervous system or maybe just making them dream. 
    # So the purple jellies are kind of like bees in a collective unconscious sort of way. Maybe that's too far out? It's a seed for something later on anyway.
    return

# MONTH 12
# Jealous of time spent with friend
# uses domestic, social, spiritual
# TODO: Revisit this; is he too whiny?
label monthly_event_12:
    scene bg farm_interior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    him annoyed "So, how was your little vacation with [ocean_character]?"
    her surprised "Vacation? Not really; Dr. Lily got stung by some weird jellyfish creature, and we scraped guano off the rocks for her."
    him concerned "I don't know; it just sounds fun to get away from everything here for a change..."
    her annoyed "Well, you should have come with us!"
    him annoyed "I didn't have time then, but I could have done it if you waited a few weeks until that harvest was over."
    her serious "Well, we can go again if you really want to. Dr. Lily could always use more guano."
    him concerned "No, I really shouldn't leave the farm."
    her annoyed "Well, then what's the big deal? It's not like it was a big fun vacation; I had to go to fix the stove."
    him sad "I never see you anymore. Whenever I want to talk to you, you're off somewhere else."
    her annoyed "What?! I'm home all the time! And when I am home, half the time you're doing farm stuff anyway, so I never get to talk to {b}you{/b}!"
    if (ocean_character == "Brennan"):
        him concerned "You seem to have plenty of time to see Brennan."
        her annoyed "That's because we work at the same place!"
        him annoyed "And go on trips together..."
        her surprised "What are you trying to say? This isn't really about Brennan, is it?"
    elif (ocean_character == "Sara"):
        him concerned "You have plenty of time for Sara."
        her annoyed "Well, she's my best friend."
        him annoyed "{b}She's{/b} your best friend?"
        her surprised "What is going on with you? This isn't really about Sara, is it?"
    else:
        him concerned "You're always hanging out in town, like at the storehouse or the library."
        her annoyed "The library?! I only go there if I'm doing research!"
        him angry "Well, it seems like you do a lot of research."
        her surprised "What are you trying to say? This isn't really about the library, is it?"

    if (loved >= 0):
        him concerned "No, it's... I missed you when you were gone."
        her annoyed "Well, why don't you just say so, instead of turning it into an argument?"
        him sad "..."
        her sad "..."
    else:
        him sad "We're falling apart, [her_name]. I want to stop it."
        her annoyed "Well, yelling at me isn't the way to go about it!"
        him angry "Yeah? What should I do, then? I can't bring you flowers, or take you to a concert, or even take you out for coffee!"
        her angry "What are you so mad about?!"

    him concerned "I'm sorry, [her_name]..."
    menu:
        "What should I say?"
        "{i}Let's forget about it and do some work together{/i}" if (skill_domestic >= 40):
            her serious "It's okay..."
            her normal "Hey, let's do something together! Let's clean the kitchen!"
            him surprised "Wha- you want to clean the kitchen right now?"
            her happy "Yeah, together! It needs to get done; we need to spend time together; we can do both at the same time!"
            if (loved >= -5):
                him serious "Okay, where should we start?"
                her serious "There's some grease on the walls; let's scrub that off."
                "We put on some energetic music and scrubbed together. It was still hard work, but soon we weren't mad at each other anymore."
                $ loved += 5
                
                her serious "Now, do you want to talk about what's really bothering you?"

            else:
                him annoyed "I don't want to clean the kitchen. I have too much other work to do."
                her annoyed "Fine, whatever."
                "I cleaned it myself, while he did whatever it was that was so important he couldn't spend time with me."
                "I got the kitchen clean, but I didn't know what I could do about [his_name]..."
                $ loved -= 5
                return
        "{i}Let's forgive each other{/i}" if (skill_spiritual >= 40):
            her normal "It's okay, [his_name]. I'm sorry for arguing, too."
            him concerned "We're both pretty stressed out, aren't we?"
            if (relaxed < 0):
                her concerned "Yeah, I know I am. There's so much to do, and so much going wrong..."
                her serious "But we need to help each other! How can I help you?"
            else:
                her flirting "Well, the only thing I'm stressed out about right now is the fact that you seem stressed out! How can I help?"
                
            him concerned "Oh, [her_name], I don't know. But I need you by my side, on my side."
            
        "{i}You need another friend{/i}" if (skill_social >= 40):
            her surprised "Don't you have any other friends you can hang out with, if I'm not around?"
            him concerned "Not really... well, Thuc and I help each other a lot, but we don't really talk..."
            her concerned "Maybe he could help you? What's wrong, anyway?"

        "I'm sorry, too":
            her concerned "I'm sorry, too."
            him sad "..."
            her sad "..."
            
        "I can't talk to you right now" if (relaxed <= 0):
            her annoyed "I can't deal with this now."
            him annoyed "Fine, do what you need to."
            "We both dealt with our problems separately. At bedtime, we kissed goodnight, but I could tell we were both engrossed in our own worries."
            $ loved -= 2    
            return

    him concerned "It's just...a lot of things went wrong today..."
    her surprised "Like what?"
    him serious "The tractor broke down today, and it took me a few hours to figure out what was wrong and fix it."
    him serious "That meant I didn't have time to get to clearing out the old radish and spinach field, which means I'm behind on planting the next things..."
    him annoyed "Then the mayor wants a report on how all the crops are coming, and it's going to take a while to prepare it, when I really should be working on actually growing food!"
    him sad "The fences keep breaking and there's a new pest I've found evidence of but haven't identified yet..."
    her surprised "You do have a lot going on. Is there someone who can help you?"
    him serious "I can do it all, I just need--"
    her surprised "What do you need?"
    him serious "I just need you."
    if (loved >= 0):
        her serious "Here I am...here for you and loving you, [his_nickname]."
        "We held each other for a long time. I felt there was so much I wanted to say, I tried to put it all into my hug and strengthen him and help him."
    else:
        her serious "Yeah, I'm here for you."
        "That's what I said, but inside I just felt annoyed. I had enough problems of my own without worrying about his."
        him concerned "Okay, thanks."
    $ loved += 5
    
    return

# MONTH 13 - Jury Duty
# uses spiritual, technical
label monthly_event_13:
    scene black with fade
    "I hadn't thought about it much before, but we didn't have a lot of laws here on Talaam. Some things just didn't apply (like taxes, driving laws, etc), but I remember signing something about agreeing to abide by a set of laws that sounded very reasonable."
    "It had never seemed like something I would have to worry about.  Until I had to be on the jury for Ilian's trial, that is..."
    "We hadn't had any crime our whole first year (though we certainly had our share of arguments, accidents, and disagreements)."
    "After all, who would hurt anyone else in our colony? We needed each other too much."
    "But that peace couldn't last forever..."

    scene bg community_center with fade
    "We awoke one morning to the tragic news that the Peron's four-year-old girl, Josephina, was missing."
    show her serious at midleft
    show natalia at midright
    "Mrs. Peron was alternately furious with herself and those around her."
    natalia "Someone should have been watching her more closely!"
    natalia "I should have been watching her more closely..."
    scene bg talam with fade
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
    scene bg community_center with fade
    show pavel at center with dissolve
    boss "I know everyone is worried, and scared, but we can't stop trusting each other. We will find who's responsible for this."
    show natalia at right with moveinright
    natalia "Who knows who will be next?! It clearly wasn't an accident!"
    show ilian at midleft with moveinleft
    "Finally, Ilian stepped forward."
    ilian "I'm sorry! I'm so sorry!"
    show sara at left with dissolve
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
    scene black with fade
    "The mayor took Ilian to stay at his house until the next day, when the trial started."

    call set_work_bg
    show pavel at midleft
    show her serious at midright
    with dissolve
    boss "[her_name], you've been randomly selected to be on the jury. Is there any reason you should not do this? Any conflict of interest with either side?"
    her "I'm friends with Sara and Ilian, but, I guess everyone knows each other here."
    boss "That's fine. We will proceed with the trial at two o'clock."
    
    scene bg community_center with fade
    "Everyone in the town turned out to see the trial. Ilian repeated what happened, and Mrs. Peron repeated what she had found. It sounded like a fairly simple case of involuntary manslaughter; we mainly needed to decide upon a sentence."
    show pavel at midleft
    show ilian at midright
    with dissolve
    boss "There is no mandatory sentencing in the laws of our colony. I am sure you will find a solution that is fair to all parties involved. In case you don't, I do have the authority to modify sentencing, but I have every confidence in this jury's abilities."
    "He left us jury members to deliberate in private."
    hide pavel
    hide ilian
    with moveoutleft
    
    show lily at midright
    show sven at midleft
    show thuc at right
    show her serious at left
    with dissolve

    lily "He shows great remorse. I doubt he will be so careless as to repeat his mistakes."
    sven "It coulda been any of us..."
    thuc "But would one of us have dumped her body in the river and covered it up? That behavior is suspicious. He says it was an accident, but who can tell for certain?"
    her surprised "But why would anyone kill Josephina?"
    thuc "Why does any criminal do what they do? They want to, and they don't care about other people."
    show her serious
    lily "Ilian has not shown any other behavior that would be cause for concern."
    thuc "But it's possible that it was not an accident. We cannot show too much mercy, or people will think they can get away with anything."
    sven "You're not thinking of killing him, are you?!"
    thuc "Of course not. I propose temporary banishment. He should have to live on his own, off the land, for a year. That will show how important our community is, both to him and any would-be criminals."
    lily "There are no would-be criminals here, Thuc. What you are proposing is a death sentence. I think he should simply provide a certain amount of free labor to the Peron family every week. Perhaps that way they can eventually forgive him."
    sven "I don't much like either of those options, but I can't think of anything better."

    # TODO: Make all these options work with being able to see Ilian around town still.
    menu:
        "What will you argue for?"
        "Work for Perons":
            her serious "I agree with Lily; he should have to work for the Perons. It can't make up for the loss of a child, but it will require some sacrifice and will help him show his remorse."
            thuc "He should be their slave for a year!"
            her concerned "Well, we don't want his farm going to waste..."
            sven "We could make him work a certain number of hours? Like community service?"
            her serious "Yes, but instead of the community it will be for the Perons. Let's say eight hours a week for a year."

            "The jury agreed to that, and the Mayor, Ilian, and the Perons all accepted our proposal. Sara didn't seem to happy about it, though. She'd probably have to do extra work on their farm to make up for his absence."

        "Banishment":
            her serious "I agree with Thuc; we need to show that our community won't allow such behavior."
            lily "It would be more humane to simply shoot him in the head; it would be impossible to survive for a year alone out there."
            her "I agree. Also, he is a healthy worker, which we can't afford to lose for that long. So I propose that he live outside the community boundaries, but close enough that we can trade with him. He can hunt or gather useful things and trade them for food or other community resources."
            thuc "That's too soft!"
            lily "I think a year is still too long."
            her "How about two months?"
            thuc "Three."
            lily "I suppose that would work...as long as the resources he gathers go to help the Peron family."
            "Finally, we had come to an agreement."
            "Ilian and the Perons accepted it, but Sara and the Mayor frowned. Poor Sara... I guess in a way we were sentencing her, too."
            
        "{i}Compromise{/i}" if (skill_spiritual >= 40):
            her normal "Those both sound like good ideas. Perhaps some of both might be appropriate?"
            sven "What's your idea?"
            her concerned "Having him work for the Perons is a good idea, but it is too soon. They would feel angry, and then he would feel like his apology was not accepted."
            her serious "But a year is too long to send anyone to live outside the community. I propose Ilian leave the community for two weeks. When he returns, he will have to work for the Perons one day of every week for the next half year."
            lily "That sounds fair for all involved."
            thuc "I think two weeks is too short, but I will agree to this plan also."
            "Everyone agreed to my proposal. The mayor seemed happy with it, too, and both Ilian and the Perons accepted it without argument."
        "{i}He's innocent{/i}" if ((skill_technical >= 40) or (skill_knowledge >= 40)):
            her serious "He should provide some reparations, but I know he didn't kill her on purpose."
            thuc "How do you know that?"
            her "Her injuries are consistent with being hit by a car and then floating down the river. She doesn't have any injuries that would come from being physically assaulted."
            sven "Yes, that's right!"
            thuc "That's true... I guess he is still innocent unless proven guilty..."
            her "He still should provide some reparations, though. I think he should work for the Perons one day a week for a year."
            lily "I agree."
            sven "That's fair."
            "We all agreed, and the Mayor, Ilian, and the Perons seemed satisfied with our verdict also."

    scene black with fade
    "I was just glad it was over."
    "Being on a jury was so stressful; I hope I never have to do that again."
    $ relaxed -= 2
    return

# MONTH 14 - Pregnancy or not?
label monthly_event_14:
    scene bg farm_interior with fade
    show her normal at midleft
    show him normal at midright
    with dissolve
    if (want_kids and (made_love >= 3)):
        her concerned "I wonder if I'm getting sick; I've felt so tired lately."
        him serious "I haven't heard of anything going around. That's one of the good things about being so far from Earth - we don't get as many of their germs."
        her annoyed "Well, I've got something. It's not like I'd make it up!"
        him surprised "What? No, of course not."
        her angry "Do you think I'd make that sort of thing up?!"
        him annoyed "No, not at all!"
        "I felt like crying. One part of my brain knew it was not a big deal, but the other part just felt so lonely and afraid all of a sudden."
        if (loved >= 0):
            "He came over and wrapped his arms around me in a hug."
            him serious "It'll be okay, [her_nickname]. Why don't you get some rest?"
            her sad "Maybe I will..."
            scene bg bedroom with fade
            show her sleeping at center
            "I fell asleep immediately..."
            
        else:
            him serious "You should get some rest."
            her annoyed "Oh, suddenly you know exactly what I should do? You think I don't know how to take care of myself?!"
            him annoyed "Hey, I'm not telling you what to do, you just seem a little tired, that's all."
            her angry "Tired?! I just said I'm sick!"
            him angry "Fine, do whatever you want!"
            "I went to lay down and fell asleep immediately..."
            scene bg bedroom with fade
            show her sleeping at center
            "I fell asleep immediately..."

        scene black with fade
        "The next morning I felt less tired, but still a little off. I went to work anyway, and had been standing up all day when I started to feel dizzy and sick to my stomach."
        call set_work_bg
        show her serious at midright
        show brennan at midleft
        with dissolve
        her concerned "Excuse me, please."
        brennan "Are you alright? You don't look so good."
        her sad "I just need... to rest for a bit..."
        menu:
            "I sat down and put my head on my desk. Slowly, the dizziness subsided, but I didn't feel like eating."
            "Go home":
                her serious "Brennan, I'm feeling sick. Can you take care of things here for a bit; I'm going to go home."
                brennan "Are you sure you're up to walking? Want me to call [his_name]?"
                her normal "I'll be fine, thanks."
                "The fresh air and walking seemed to help some, but I was still glad to finally get home."
            "Try and get some work done":
                "I went back out and was able to finish up the day's work, taking two more breaks when I started to feel too light-headed."
        scene bg farm_interior with fade
        show him normal at midright with dissolve
        show her serious at midleft with moveinleft
        "It felt good to get home. I still wasn't feeling well so I decided to lie down."
        him surprised "Are you feeling any better?"
        her concerned "Not really."
        him sad "Sorry to hear that, [her_nickname]. Do you want to stop by the clinic in the morning?"
        her serious "I'm not feeling {b}that{/b} bad, but..."
        menu:
            "What should I do?"
            "Go to the Clinic":
                her "It can't hurt to check it out."
                him serious "I'll come with you tomorrow."
                "We walked to the clinic holding hands, not saying anything, just watching the sun rise and feeling together."
                scene bg clinic with fade
                show him serious at midleft
                show her serious at midright
                with moveinleft
                if (profession == "doctor"):
                    "I reviewed my own symptoms in my head and decided to take a urine sample first."
                else:
                    "The doctor at the clinic listened to my symptoms and had me give a urine sample."
                "The results said..."
                him surprised "You're pregnant?!"
                her surprised "Oh! I've been so busy I haven't even been thinking about that lately. But...yes, I guess I am."
                        
            "Don't go":
                her serious "I'll be fine. If I don't feel better in a few days, I'll have it checked out."
                him normal "Alright."
                "I didn't feel better, but I didn't feel much worse, either. My chest ached, sometimes, though, and I got headaches when I never used to."
                "Finally it dawned on me..."
                her surprised "Maybe I'm pregnant?"
                "Sure enough, I went to the clinic and tested positive for pregnancy."
                
            "Run some tests" if (profession == "doctor"):
                her normal "I'll just run some tests at work today, no big deal."
                scene bg clinic with fade
                if (loved >= 0):
                    him normal "I'll come with you."
                    "We walked to the clinic holding hands. It felt so good not to be alone right now."
                    show him serious at left
                else:
                    him "Okay, let me know what happens."
                show her serious at midright
                show brennan at quarterleft
                with moveinleft
                her serious "Brennan, will you please help me get a blood sample?"
                brennan "From who?"
                her normal "From me."
                brennan "Well, sure. That's a bit hard to do yourself, isn't it?"
                "I started laughing, but it wasn't that funny. Somehow that just made it funnier. Brennan wasn't laughing, just looking at me quizzically."
                "He took the blood sample and we ran the standard tests on it."
                "Everything was normal except--"
                brennan "You're pregnant?"
                her surprised "I guess...I am!"
                "That explained everything."
                
        scene bg farm_interior with fade
        show him normal at midright
        show her normal at midleft
        with dissolve
        him happy "[her_name], that's great!"
        menu:
            "How do I feel about it?"
            "It's awesome!":
                her happy "Yeah! We're gonna be parents!"
            "It's strange.":
                her concerned "I guess it is. At least I know now what was wrong with me."
            "It's awful.":
                her annoyed "I hope I don't feel this bad the whole time. I don't know if I can take nine months of feeling this sick."
        him concerned "I wish it didn't have to be so hard for you, but our little baby is worth it!"
        her serious "Our little baby..."
        "This was going to take some getting used to."
        $ is_pregnant = True

    # They want kids but didn't make love enough
    elif (want_kids):
        her concerned "[his_name]... it's been over a year since we've been trying to have a baby."
        him concerned "Yeah, I guess sometimes it takes a while."
        her sad "We haven't made love very often, have we?"
        him concerned "Well, we have both been busy, and tired..."
        menu:
            "Should we change things?"
            "No rush":
                her normal "I guess there's no need to rush, right? In fact, it's probably good that I'm not pregnant, so we can have things setup better when it happens."
                if (loved >= 0):
                    him normal "Yeah, that's true. Come here, [her_nickname] - we have plenty of time. Plenty of time for you, and me, and whoever else might join us in the future..."
                    "He held me close for a long time, stroking my hair. I snuggled up under his chin and just enjoyed being close to him."
                    $ made_love += 1
                    $ loved += 5
                else:
                    him annoyed "Is that why you haven't wanted sex lately?"
                    her surprised "No! That's not it at all! I'm just trying to see the bright side of things."
                    him angry "The only bright side is that there's no kids to be hurt by our unstable relationship."
                    her angry "Unstable?!"
                    him annoyed "People who are married don't act this way. We never do things together; we never make love. And when I try and do things for you, it's like I can never do anything right."
                    her sad "Is that really how you see us?"
                    him sad "It's true, isn't it? We have to turn things around if we want this to work, and especially if we want to bring kids into this family."
                    "We talked about it some more, and we both agreed to try and put the other person as more of a priority in our own life. But I wonder if we can actually do it... or if our marriage is already doomed."

                    # Reset loved a little closer to zero to give the relationship another chance
                    if (loved < -10):
                        $ loved = -10
                    else:
                        $ loved = 0

            "Let's make a baby!":
                her flirting "Come on over here, [his_nickname], and make me a baby!"
                him flirting "You want me to turn you into a baby?"
                her laughing "Ohhh, you!"
                him laughing "Sorry, I mean, 'Yes ma'am'!"
                $ made_love += 2
                $ loved += 5

    # they don't want kids
    else:
        her concerned "[his_name], there's something we need to discuss."
        him surprised "Oh? What's that?"
        her concerned "When I went to try to get more birth control, they informed me that they only had enough for us for six more months. 'We need everyone to help populate the colony,' they said."
        him serious "Six months, huh? Do you think we'll be ready by then?"
        menu:
            "What should I say?"
            "No way!":
                her angry "No way! We can barely take care of our farm and a horse; how can we take care of a baby?!"
                him concerned "I think we're doing pretty good."
                her annoyed "It just feels like one more thing to worry about; I'm already stressed out about food, work, and this whole crazy planet."
                him normal "Don't worry; we'll figure something out. We can always... get creative."
                her flirting "I like it when you get creative."
            "Maybe...":
                her concerned "I guess we could be, but...I just don't feel ready yet. Maybe things will be different in six months... or we could always use other methods."
                him normal "Yeah, I feel ready, but you're the one that will be carrying the baby, so we can do whatever you think is best."
                her serious "Let's not worry about it now. We'll see in six months."
                if (loved >= 0):
                    him normal "Okay, [her_name]. I love you."
                    her normal "I love you, too."
                else:
                    him serious "Okay."
                    her serious "Yeah."
                    "And that was that."
 
            "I'm ready now.":
                her surprised "You know, I think I'm ready now."
                him surprised "Yeah? You've changed your mind from last year?"
                her serious "Yeah...let's stop the birth control now, and just see what happens."
                him flirting "Yes, momma."
                her flirting "Oh, ick, don't call me momma!"
                him laughing "You better get used to it! Someday a bunch of kids are going to call you that all the time!"
                her laughing "That's so... weird! But at least they'll be calling you 'daddy', so I won't be alone."
                him serious "You'll never be alone."
                $want_kids = True
                $made_love += 1   
            
    return

# MONTH 15 Fertility and Food and Community
label monthly_event_15:
    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    if (is_pregnant):
        him happy "I made you breakfast, so eat up, [her_name]! You're eating for two!"
        her flirting "Yeah, but one of us is the size of a pea..."
        her surprised "Eggs? Bacon?! Where did you get this stuff?!"
        him happy "Well, when Mrs. Peron heard about your 'condition', she insisted that you needed to eat eggs to have a healthy baby. And when I told Ilian the good news, he pulled this out of some stash in the storehouse."
        her annoyed "Wait, you told them I'm pregnant?"
        him surprised "Yeah, why not?"
        her concerned "I don't know if I'm ready for people to know, yet."
        him concerned "Oh... well, when I told Mrs. Peron, she posted a message about it on the colony message board..."
        her serious "So everyone knows?"
        him serious "Yeah, pretty much."
        her annoyed "I haven't even told my parents yet!"
        him surprised "What's stopping you?"
        her concerned "I guess... I wanted to tell them in person, or at least call, but that's just not possible, is it?"
        him serious "No... but we can send them a message."
        her sad "But what if something goes wrong, like a miscarriage?"
        him angry "Don't say that!"
        her angry "Well, it's a possibility, isn't it?!"
        him serious "Yeah, but... Whatever happens, I want to face it with friends and family knowing everything."
        menu:
            "How do I feel?"
            "I'd rather keep it to myself":
                her concerned "I disagree. I'd rather face our problems on our own, if we can."
            "I guess you're right":
                her serious "Yeah, that makes sense. Hopefully nothing bad will happen."
            "I can't believe you did that":
                her angry "I can't believe you told other people without talking to me first!"
                him angry "What, so you want to decide what I can and can't tell people?"
                her "No, but it's something important enough that we should have decided on it together!"
                $ loved -= 3

        him annoyed "..."
        her annoyed "..."
        if (loved >= 5):
            him concerned "I'm sorry; I probably should have talked to you about it first."
            her normal "It's okay. At least I got a delicious breakfast out of it."
        else:
            him annoyed "Sorry, love, but at least you got a good breakfast out of it, right?"
            her annoyed "Yeah..."

    elif (want_kids):
        him happy "I made you breakfast, so eat up! Soon you might be eating for two."
        her laughing "Ha ha, we'll see..."
        her happy "Yum, is this berries and cream?! Where did you get it?"
        him normal "Well, when Mrs. Nguyen heard we were trying to have kids, she insisted that you needed to eat cream to have a healthy baby. So she gave me some from her goats."
        her surprised  "Wait, how does she know we are trying to have a baby?"
        him normal "Well, I might have mentioned it to Thuc...and I guess he told his wife?"
        her annoyed "So basically the whole colony knows."
        him surprised "Is that a problem?"
        menu:
            "What should I say?"
            "Not really":
                her annoyed "I guess not. It's just kind of weird. As long as they don't start serenading us with fertility songs or anything it doesn't really matter."
                him flirting "Okay, I'll post that to the message board. 'Thanks for the well-wishes, but no fertility rites, please.'"
                her flirting "Shut up and try some of this."
            "It's annoying":
                her annoyed "That's really annoying. I don't want people to be asking me all the time if I'm pregnant yet, or giving well-meaning but idiotic advice, or looking at me like I'm a time bomb or something."
                him serious "I'm not sure you can prevent that, anyway. I mean, they're going to know sooner or later, right?"
                if (loved >= 0):
                    her serious "Yes, but I wanted it to be on my terms."
                    him concerned "I see.  I'm sorry, [her_name], I didn't even think about it."
                    her normal "It's all right; we'll deal with it. Come on and eat breakfast with me, okay?"
                    him happy "No problem."
                else:
                    her angry "Yes, but I wanted to decide that! It's my body, you know!"
                    him annoyed "It's *our* child."
                    her angry "It doesn't even exist yet! What if I change my mind, or something goes wrong?"
                    him angry "I thought we had already decided."
                    her annoyed "Well, we didn't decide to tell people about it, that's for sure."
                    him annoyed "Look, I'm sorry. I just wanted to tell somebody, and Thuc's probably the best friend I have here, except for you."
                    her serious "Well, we can't change it now. Just come eat some breakfast."
                $ loved -= 2
                $ relaxed -= 2
            "I'm mortified":
                her surprised "I'm mortified! I don't want people thinking about us conceiving a baby!"
                him serious "Don't you think it's pretty obvious? I mean, healthy, newly-married couple on a colony, that's kind of why we're here?"
                her sad "Yeah, but... it should be more private than that."
                him annoyed "I guess I don't see it that way."
                her annoyed "So you're totally okay with people looking at us thinking, 'I wonder if they got it on last night?'"
                him serious "I don't think anyone's thinking that. And if they are, you can't stop them."
                her annoyed "Ugh, whatever, let's just eat breakfast."
                $ loved -= 5
                $ relaxed -= 5
    else:
        him happy "I made you breakfast."
        her surprised "Oh! Thank you!"
        her happy "Wow, berries and cream, what a treat!"
        him normal "Yeah, Thuc's wife gave them to me. She said they might help if you were having, uh, female problems."
        her surprised "What?!"
        him concerned "I think she was trying to help us have a baby."
        her laughing "Ha ha, it'll take more than berries and cream..."
        him happy "Well, we can enjoy the food anyway, right?"
        her flirting "We? She sent this for me!"
        him happy "Oh, so you want me to tell her that we're not trying to have a baby?"
        her flirting "Don't say that! Then she won't send any more!"
        him happy "Better share, then!"
        menu:
            "Should I share it?"
            "Share":
                her happy "Here, have some."
                him happy "Mmmm, thank you."
                $ loved += 2
            "Don't share":
                her annoyed "Hands off, this is mine!"
                him angry "Alright, alright! Sheesh!"
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
    show her serious at midright
    show him normal at midleft
    with dissolve
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
            her concerned "Do you want this? I'm not hungry..."
            him normal "What? Sure, OK."
            $ loved += 2

    scene black with fade
    "I felt better at work, and lunchtime was no problem, but as I was walking home, I felt sick again. I ended up throwing up by the side of the road, which wouldn't have been too bad except some of it got on my clothes. Now I had to do laundry, and it was my turn to make dinner..."
    scene bg farm_interior with fade
    show her serious at midright with dissolve
    #TODO: cellar background?
    menu:
        "What should I do?"
        "Cook something simple":
            "I went to the cellar to look at what we had for dinner. Nothing looked good."
            if (is_pregnant):
                "I wanted fried chicken or ice cream or french fries or fresh rolls, but all we had was turnips and carrots and beans."
            else:
                "We had been eating a lot of soups with turnips and carrots and beans lately, and I was starting to get used to them, but what I really wanted was to just open a can and be done. All the foods we had took so much work..."
            "I knew it was so silly, but I felt like crying. I remembered when if I craved a food, I'd just stop by the store on my way home from work and buy it, without thinking anything of it. I didn't even realize how decadent that was!"
            "That's how [his_name] found me, crying in the cellar over the food he worked so hard to grow."
        "Lie down and take a nap":
            "I wasn't hungry; why should I make dinner? What I really needed was a nap..."
            "I took off my dirty clothes and dozed for a while, and woke up to the sound of [his_name] opening the door."
        "Ask [his_name] for help":
            "I decided to ask [his_name] for help. After all, that's why we have each other, isn't it?"
            "Finally, he came home."

    show him serious at midleft with moveinleft
    him surprised "Hey, [her_name], what's for dinner?"
    menu:
        "What should I say?"
        "I'm sick":
            her concerned "I don't feel good..."
            if (loved >= 0):
                him serious "You don't look good. You go lie down; I'll make my own dinner."
            else:
                him annoyed "I thought it was your turn."
                her sad "It is, but..."
                him serious "OK, I'll trade you nights, since you're not feeling good."
            $ loved += 2
        "Make your own dinner" if (relaxed <= 0):
            her annoyed "Make your own damn dinner, I'm not hungry!"
            him surprised "Hey, hey! Calm down!"
            her angry "Calm down?! I don't have time to calm down! I need to wash out this vomit and make dinner out of vegetables I hate and try not to die while doing it, because everything on this planet is trying to kill us!!"
            if (loved >= 0):
                him concerned "Okay, it seems like you could use a little break, so why don't you go lie down?"
                her concerned "I don't have time to--"
                him serious "Laundry can wait, I'll make dinner, and nothing's trying to kill us at the moment, so go rest, okay?"
            else:
                him annoyed "Quit overreacting. You're just making excuses."
                her angry "I hate this place! I hate this food! I hate not having anything when we need it! I hate the animals, I hate the plants, I hate the moons that can't make up their mind whose turn it is to be in the sky!"
                him annoyed "Anything else?"
                menu hate_stuff:
                    "I hate the sun":
                        her sad "I hate the stupid sun and its temperamental solar flares."
                        him serious "Yeah, I hate that, too."
                        $ loved += 2
                    "I hate you":
                        her "Sometimes, I hate you."
                        him surprised "..."
                        her surprised  "..."
                        him sad "I was about to say, 'At least we'll always have each other.'  Now I don't know what to say."
                        $ loved -= 10
                    "I hate my job":
                        her serious "I hate my job here."
                        him annoyed "It seems pretty easy compared to mine."
                        her annoyed "Well, not all of us are tough farmers like you!"
                        him "Maybe you should be."
                        $ loved -= 2
                    "I'm sorry":
                        her concerned "I'm sorry; I'm sounding pretty hysterical, aren't I?"
                        him normal "Yeah, but I love you anyway."
                        $ loved += 5
                
        "Just a minute" if (relaxed >= 0):
            her sad "I'm working on it, just a minute."
            him surprised "Hey, are you crying?"
            her sad "Just a little."
            him surprised "What's wrong?"
            menu:
                "It's morning sickness" if (is_pregnant):
                    her concerned "It's morning sickness, I think."
                    him serious "Aw, I hear that can be rough."
                    her sad "It's not that bad, but..."
                    him normal "You want me to cook tonight?"
                    her normal "Yeah, thank you. I'm not even hungry."
                    $ loved += 2
                "I'm sick" if (not is_pregnant):
                    her concerned "I'm sick."
                    him surprised "Really? We haven't had much illness here..."
                    her annoyed "Well, I sure didn't throw up all over myself just for fun."
                    him annoyed "Ohh, is that what that smell is?"
                    her concerned "Yeah..."
                    him serious "Well, you should take it easy, then, I'll make myself something."
                    $ loved += 2
                "It's this place":
                    her concerned "It's this place... I'm so sick of everything here."
                    him surprised "Like what?"
                    her sad "I hate not having foods that I like, and feeling like there's dangerous things around every corner, and being so far away from everyone."
                    him serious "Anything else?"
                    jump hate_stuff

    "I went to lie down, and he made dinner for himself."
    $ relaxed += 2
    scene bg bedroom with fade
    if (is_pregnant):
        "I felt better after a little rest. I felt a little sick almost every morning for a few weeks, but that was the worst day."
    else:
        "I had to visit the outhouse several more times before my stomach finally calmed down."
        if (loved >= 0):
            "He made me some tea and sat by me and held my hand."
        else:
            "[his_name] left me alone until I was feeling better."
                             
    return

# MONTH 17
# uses spiritual, creative
label monthly_event_17:
    scene bg farm_interior with fade
    "One day Sara invited me to hang out with her at the bath house. It was a lot of work to fetch and heat water for a bath, so it was more worth it to share the work and the bath."
    #scene bg bath with fade
    show sara at midright
    show her normal at midleft
    her happy "This was a good idea! I never thought taking a bath would be such a luxury..."
    sara "It's a lot faster with you helping me haul water."
    her normal "Is the hot water ready yet?"
    sara "Yeah, it's boiling."
    her "Alright, let's pour it in!"
    show her at sitting
    show sara at sitting
    sara "Nice and hot! Not like our house; it's always freezing in there!"
    her surprised "Really? It hasn't been that cold..."
    sara "Well, Ilian never wants to use the heater. He's so stingy with everything!"
    her normal "Like what?"
    sara "Ohhh, like, the storehouse had some apples, right? The last ones from Earth. So I was like, 'It's our anniversary! We should eat some!' Well, apparently that wasn't a special enough occasion. So he keeps saving them."
    her serious "Okay..."
    sara "Then, yesterday, I was helping him sort through some stuff, and I happened to find the apples under another crate, and they're all moldy!"
    her concerned "Oh no!"
    sara "Since we both work in town and don't grow our own food, he's always bringing home whatever leftovers somebody else didn't want, so I can never plan anything and we're always eating the food nobody else wanted." 
    sara "He could bring home some MREs, or something yummy that someone brought by, but no! It's eggplants and turnips, or whatever there's extra of that will go bad if no one eats it."
    menu:
        "What should I say?"
        "[his_name] brings home food I hate, too.":            
            her annoyed "Ohhh, I know what you mean. I am so sick of [hated_food], but [his_name] keeps growing them!"
            sara "I know, right? It's better than back on Earth though; we'd argue about money all the time."
            her normal "It's nice not to have to worry about money."
            sara "Yeah, instead we just have to worry about food..."
        "He's just trying to be efficient.":
            her concerned "He's probably just trying to be efficient with the food. It is a limited resource."
            sara "I know... but he doesn't seem to get how much I hate those foods!"
        "{i}That's hard...Could you get food somewhere else?{/i}" if (skill_creative >= 50):
            her concerned "That's hard... do you think you could get food somewhere else?"
            sara "Where?"
            her normal "Maybe some of the other farmers? I mean, they bring their extra food to the storehouse, usually, but maybe you could ask them to let you have some first?"
            sara "Why would they do that?"
            her surprised "Well, maybe you could offer to do something for them in return?"
            sara "Like what? I'm not good at anything here."
            her happy "I bet some of them could use a babysitter for a while, or just an extra pair of hands helping sometimes."
            sara "Ahhh, I'm scared of kids!"
            her surprised "Really?"
            sara "Well, I just don't have much experience with them..."
            her happy "Maybe it would be good to start now, then!"
            sara "Yeah, maybe so..."
            $ community_level += 1
        "{i}That's hard...Have you talked to him about how you feel?{/i}" if (skill_spiritual >= 50):
            her "That's hard... Have you talked to Ilian about how you feel?"
            sara "Yeah, but he just says 'That's what we have'."
            her "Maybe you could help him keep track of things in the storehouse, so that if you see something you want, you could point out how long it's been there or how much of it we have?"
            sara "That could work... at least we wouldn't let any apples go to waste if I'm keeping an eye on them!"
            $ community_level += 1
            
    her concerned "Food is a lot harder here, isn't it?"
    sara "Ohhh, what I wouldn't give for a pizza, or an ice cream bar..."
    her serious "Or blueberry muffins!"
    sara "Or a cheeseburger!"
    her normal "Or nachos!"
    sara "Ohhh..."
    her serious "Mmmm..."
    sara "Well, we can't have those, I guess, but I'm glad I'm not the only one suffering from processed food withdrawal."
    her "Yeah."

    sara "But, enough about me! What about you? What have you been up to lately?"
    if (is_pregnant):
        her normal "Well, we had an ultrasound the other day..."
        sara "For the baby?! What is it?"
        her flirting "We are pretty sure it is a human fetus."
        sara "Ohhh, you know what I mean! Girl or boy?"
        her happy "Looks like a girl!"
        sara "Yay, how fun! Have you started getting ready yet?"
        her surprised "Not yet, I was actually going to ask you what they have in the storehouse..."
        sara "Ohh, they have the teensiest little shirts and pants! And little soft blankets, and diapers - all that stuff."
        her normal "Well, that's good to know."
        sara "Come over to the storehouse sometime and I'll show you."
        her happy "Okay, I will!"
        her surprised "Oh! She's kicking right now, you can probably see her little foot poking through my skin..."
        "Sara put her hand on my belly, and after a minute the baby gave her a little kick."
        sara "Wow! There is really a baby in there!"
        her annoyed "I hope so!"
        sara "Awwww...."
        her happy "..."
        sara "So, is anything else going on?"

    menu:
        "What should I say?"
        "[his_name] and I aren't getting along." if (loved < 0):
            her concerned "[his_name] and I have been having some trouble lately..."
            sara "Uh-oh. What's he been doing?"
            her sad "I don't know... we're just both so stressed out all the time that it's hard to be nice to each other, let alone have any romance."
            sara "[his_name]'s not very romantic, is he?"
            her concerned "Not really..."
            sara "Well, it might be up to you to make some romance happen, then!"
            her surprised "Is it really romance if you have to make it happen?"
            sara "Of course! What, you think roses and feathers just fall from the sky every time two people feel in love?"
            her concerned "No, but... shouldn't it come naturally?"
            sara "Sometimes it does, sometimes it doesn't. But you're not powerless, you know - even if you can't change what he does, you can control what you do."
            her serious "That's true..."
            $ loved += 2
        "I feel so stressed out." if (relaxed < 0):
            her concerned "Work has been tough, lately, and there's always some new problem. I feel like I can never relax."
            sara "I know exactly what you mean."
            her sad "..."
            sara "... But this is is pretty relaxing, isn't it? Soaking in the hot water, looking up at the stars."
            her surprised "Hey, there's only one moon tonight - it almost looks like Earth's sky!"
            sara "Yeah! Don't you think that constellation is a bit like Orion?"
            her concerned "I don't know, it looks kind of like a woman?"
            sara "Maybe it should be Artemis, then!"
            her serious "Yeah, Artemis. I like that."
            sara "..."
            her normal "Thanks, Sara - talking with you really helps."
            sara "Anytime! You help me, too, you know!"
            $ relaxed += 2
        "I'm worried about the future":
            her concerned "I'm worried about the future. Are we going to make it? Sometimes I worry we'll all get wiped out in an earthquake, or the supply ship from Earth will never come, or wild animals will rip our throats out in our sleep..."
            sara "That last one's probably just [his_name] looking for a good time."
            her laughing "Ha ha ha!"
            her serious "Seriously, though, don't you worry sometimes?"
            sara "Yeah, I worry about those things, too. But whenever I try to talk to Ilian about it, he starts getting even more worried than me. So I try and just forget about it."
            her sad "Yeah..."
            sara "But worrying is also kind of pointless. I mean, we're all doing the best we can, right?"
            her concerned "I hope so..."
            sara "So, just keep doing your best, and things will work out. That's what I believe, anyway."
            her normal "That... makes sense. Thanks, Sara."
        "Nothing's new.":
            her normal "Nothing new happening at our house - just the same old routine."
            sara "Well, thanks for listening to me, anyway. You're always such a good friend to me."
            her serious "Thanks, Sara..."

    show her sleeping with dissolve
    "We relaxed for a bit more in the hot bath, and then went home. It was comforting to know I could depend on Sara."
    return


# MONTH 18 - he burns his hand in a tractor fire
# uses domestic, knowledge, social, technical, physical
# TODO: Finish adding emotions
label monthly_event_18:
    scene bg farm_exterior with fade
    show him normal at midleft
    show her normal at midright
    with dissolve
    him surprised "Hey, could you give me a hand for a minute?"
    if (loved >= 0):
        her normal "Sure, what for?"
    else:
        her concerned "I guess. What is it?"
    him serious "I need to jump start my tractor. Can you run these cables to the house's battery for me?"
    her surprised "Why do you need to jump start your tractor?"
    him serious "Something wrong with the battery. It won't hold a charge for very long anymore."
    if ((skill_technical >= 60) or (profession == "mechanic")):
        her normal "Want me to take a look at it?"
    else:
        her surprised "Well, shouldn't you take it in to get it fixed?"

    him serious "Don't have time. I need to use it all day today."
    her serious "Okay, if you're sure..."
    scene bg tractor with fade
    show him normal at quarterright
    show her normal at quarterleft
    with moveinleft
    "He hooked up the tractor's battery to the cables, and I attached the other end to our house battery."
    her surprised "It's hooked up!"
    him serious "Okay, now turn on the tractor!"
    show her at center with move
    "He was making sure the clamp was on the battery when I turned the tractor on. But then I heard a strange sound...and was that smoke...?"
    him surprised "Aaaahhhhh!"
    "I turned it off, and as I jumped out, I could see that the engine was on fire! [his_name] was backing away, his hand charred and red."
    her concerned "Are you okay?!"
    him angry "The fire! Get the fire!"
    show her serious
    hide her with moveoutleft
    "I ran and got our fire extinguisher from the house."
    if ((skill_technical >= 70) or (skill_knowledge >= 70) or (profession == "mechanic")):
        "As I was running back to the tractor, I skimmed the label."
        "The extinguisher said it was an ABC fire extinguisher filled with monoammonium phosphate."
        "That was the wrong type of fire extinguisher! While it might put out the fire, the tractor would be ruined!"
        "Water would only make it worse, since there was a lot of electronics in the tractor."
        "But I knew something that could work instead..."
        show her serious at center with moveinleft
        "I ran to the cellar and pulled out a can of baking soda. Yanking the top off as I ran, I dumped it on the tractor engine fire."
        $ community_level += 5
    else:
        "I pulled the trigger; why wasn't it working?! Oh yeah, the pin!"
        "I fumbled with removing the pin; it seemed to take forever!"
        show her serious at center with moveinleft
        "Finally, I sprayed it at the fire. It didn't seem to do much, but I kept at it."

    "Eventually, the fire died down."
    "Now that the fire was out, I turned to [his_name]. One of his hands and his forehead were singed and red."
    him serious "You put it out..."
    her concerned "You're really hurt!"
    show him concerned 
    "He started laughing. I didn't join him, though - I was too worried."
    if (profession == "doctor"):
        her serious "You're in shock; let's go to the clinic and I'll check you out."
    else:
        her serious "Let's get you to town and have the doctor check you out."
    him laughing "Check me out... check me out, you're always checking me out."
    her concerned "Alright, just don't you check out on me."
    show him concerned
    "He stared off into the distance, like he could barely hear me."
    if (skill_social >= 60):
        her serious "Stay here; I'm going to radio for help."
        "I called on the radio and Thuc and Mr. Peron came over. Together, we helped [his_name] get to the town."
    elif (skill_physical >= 40):
        her surprised "Where's Lettie?"
        "I found Lettie tied up near the barn."
        her serious "C'mon, Lettie, [his_name] needs your help, alright?"
        "I remembered what [his_name] had taught me and was able to lead her over to [his_name]. He couldn't ride her, not with his hands so badly burned, but I hitched her up to the cart."
        her serious "Get in, [his_nickname]."
        show him sad
        "He sat down, but now his laughing had turned into trembling."
        "We set off at an easy pace."
    else:
        "I didn't know what to do. I didn't feel like I could call on any of our neighbors, and I didn't know how to have Lettie pull a cart or anything..."
        "But he could still walk, so I was able to sort of guide him towards the town. I just hoped he wouldn't pass out on me or anything."
        $ relaxed -= 2

    scene bg clinic with fade
    show him serious at midright
    show her serious at midleft
    with moveinleft
    "Finally, we arrived at the clinic. [his_name] was shaking and breathing hard."
    him concerned "I don't n-n-n-need a doc-c-c-tor."
    her angry "Your hands are all blistered!"
    "He looked at his hands, but didn't appear to notice how hurt they were."
    him sad "I sh-sh-sh-should just go h-h-home."
    her serious "Just come in here, everything will be fine."
    if (profession == "doctor"):
        "I cleaned his burned skin carefully, treated his burns with ointment, and wrapped them up gently."
        "He gradually calmed down and stopped shaking, too."
        her serious "You need to let these heal for at least two weeks. Looks like mostly a second-degree burn, so it's not too serious, but it will be painful."
        him surprised "I can't use my hands at all?"
        her serious "Anything that hurts is off-limits."
    else:
        "The doctor cleaned, treated, and wrapped his burns, and [his_name] gradually calmed down and stopped shaking."
        "He was not happy to learn that he couldn't use his hands until they had healed."
        
    scene bg farm_interior with fade
    show her serious at midright
    show him serious at midleft
    with dissolve
    "After a few days of reading and resting, he started pacing the house."
    show him annoyed at left with move
    him "I should be doing something useful! I've been so lazy..."
    show him at center with move
    her concerned "You're supposed to take it easy."
    show him serious at left with move
    him "I've healed enough; I could at least take Lettie out and look around..."
    show him at midleft with move

    menu:
        "What should I say?"
        "No way!":
            her annoyed "There's no way I'm letting you out of the house. You'll just make your hands worse and it will take longer to heal."
            him annoyed "What, you're my boss now?"
            her serious "No, just someone who wants what's best for you."
            him surprised "You don't think I know what's best for me?"
            her annoyed "Maybe not, if you're going to use your hands before they've healed."
            him serious "I'm just going to look around. I need some fresh air."
            her concerned "But-"
            him angry "Get out of the way!"
            "He pushed past me and stormed out the house."
            her annoyed "(What's his problem?!)"
            "When he came back later, we were both much calmer."
            her concerned "Everything okay, [his_name]?"
            him concerned "Yeah, I was just checking on things..."
            $ loved -= 2
        "It must be frustrating for you":
            her concerned "You sound really frustrated..."
            him angry "Yeah, I'm frustrated! I'm stuck in here, while who knows what's happening to the farm outside!"
            her serious "I'm sorry it happened."
            him serious "Ah, it's okay. It's not your fault. I just hate sitting around doing nothing."
            her normal "Yeah, that's annoying. Let's go on a walk together. That should be okay, right?"
            him serious "Yeah.... I think I could use the fresh air."
            "We walked around the farm together. I could tell he was itching to get down and get to work, but instead he just took notes."
            $ loved += 2
        "I'll go with you":
            her concerned "Alright, but only if you let me go with you. Someone's got to keep you out of trouble..."
            him annoyed "Really? You don't trust me?"
            her normal "Of course I trust you. I trust that you will do anything to take care of this farm, even if it's at the expense of your own health."
            him concerned "... All right, let's go."
            "We walked around the farm together. I could tell he was itching to get down and get to work, but instead he just took notes."
            $ loved += 2
        "This is all my fault":
            her concerned "I'm so sorry, [his_name] - it's my fault you burned your hands!"
            him surprised "What? No, it's not your fault. If anything it's my fault, for trying to run the tractor instead of fixing it properly."
            her sad "I just feel so terrible about it."
            him concerned "That's not - I don't want you to feel guilty!"
            her sad "But I do..."
            him serious "Maybe there's some way you could help out..."
            her surprised "Like what?"
            $ relaxed -= 2

    him serious "Most of the farm will be okay, but the tomatoes and peppers are ready to harvest right now."
    her surprised "There must be something we can do..."
    menu:
        "What should I say?"
        "{i}Let's ask for help.{/i}" if (skill_social >= 60):
            her normal "I bet our neighbors would be willing to help out."
            him normal "We can ask..."
            "We asked around, and several neighbors said they would spend half a day working at our farm, or send one of their kids to work at our farm."
            "[his_name] didn't like sitting around watching other people work on his farm, but he didn't have much of a choice."
        "{i}I'll do the harvest!{/i}" if ((skill_domestic >= 60) or (skill_physical >= 60)):
            her happy "I can do the harvesting!"
            him surprised "Really? I know you have plenty of your own things to do..."
            her flirting "It's not that hard to pick tomatoes and peppers."
            him happy "Okay, awesome! If there's anything you need done that doesn't involve hands, maybe I can do that?"
            her concerned "Ummm... yeah, maybe you can dictate some e-mails for me?"
            him serious "Sure..."
            "(I will probably have to type them over again, anyway, but he needs something useful to do!)"
            "I was so tired going to work and then coming home and harvesting vegetables, but at least we got them all picked."
        "{i}The kids at school can help out!{/i}" if (profession == "teacher"):
            her happy "Picking tomatoes and peppers is not that hard; why don't I have my students help out?"
            him surprised "The kids at school? Sure, it could be educational!"
            show him happy
            her laughing "A {b}field{/b} trip!"
            scene bg fields with fade
            "[his_name] instructed the kids on how to tell when the vegetables were ripe, and how to store them so they would keep fresh longer."
            "The little kids got tired quickly, but with everyone helping, we were able to pick all the ripe ones."
            "It was cute to watch [his_name] explain things to the kids... they really listened to him."
        "The farm can wait.":
            her annoyed "The farm can wait. Your health is more important."
            him angry "You can't just let the food go to waste! I worked hard growing those!"
            her concerned "Well, I don't have time to pick them."
            him angry "Someone needs to!"
            "In the end, [his_name] found a friend to help him pick some of the vegetables."
            "I helped a little, but the farm was his thing, not mine."
            $ loved -= 2

    scene bg clinic with fade
    show him normal at midleft
    show her normal at midright
    with dissolve
    "Finally, the bandages came off and [his_name] could use his hands again."
    him flirting "I know the first thing I want to touch when we get home."
    her flirting "Hmmm, are you talking about Lettie? I know she's missed you..."
    if (loved >= 0):
        him surprised "Haven't you missed me, just a little?"
        her flirting "Maybe..."
        scene bg bedroom with fade
        show him serious at midleft
        show her serious at center
        show overlay night
        with dissolve
        "That night, he held me gently, his hands caressing my skin as if for the first time. His skin was still rough from the burns, but I didn't care."
        him serious "Mmmm, the touch of your skin... I've missed {b}you{/b}, [her_nickname]."
        her concerned "I missed you, too..."
        scene black with fade
    else:
        him annoyed "That's not what I was thinking of, but I did miss Lettie, too. I better go see how she's doing."
        her annoyed "..."
    
    "I was glad [his_name] was back to normal again, though he still had to be careful with his hands for a while."
    return

# MONTH 19 - Clothing wearing out, stiff, doesn't fit anymore if pregnant.
# clothes don't fit anymore (bras, etc); air drying makes they stiff and uncomfy, what to do?
# use domestic, social, creative
label monthly_event_19:
    scene bg farm_interior with fade
    "Fashion was one thing we never had to worry about."
    "We mainly had our colony-issue shirts and pants, made of special durable, breathable, material, and whatever extra clothes we managed to fit in our one allotted suitcase."
    "Since we did laundry by hand, we only did it once a week, so we ended up wearing the same clothes for several days in a row."
    "I did get a little tired of wearing the same thing all the time, but everyone else on the colony was in the same situation, so it wasn't something I worried about."
    if (is_pregnant):
        "But now that my belly was growing, the pants were starting to get uncomfortable. They weren't made to stretch this much. The shirt was getting tight, too."
        "I had to do something about it, but what?"
        menu maternity_clothing:
            "What should I do?"
            "Check the storehouse":
                scene bg storehouse with fade
                show ilian at midright with dissolve
                show her normal at midleft with moveinleft
                her surprised "Hey, Ilian, do we have any extra clothes here?"
                ilian "A few..."
                "I found a large men's shirt that wasn't very flattering, but would fit."
                "They had a pair of larger pants, but they were very baggy and also too long. Well, I'd just have to roll them or hem them or something."
                "How did they expect people to grow the colony by having kids if they didn't even have maternity clothes?!"
            "{i}Modify your pants{/i}" if ((skill_domestic >= 60) or (skill_creative >= 60)):
                "I decided to turn one of the pairs of Earth pants I had into maternity pants."
                "After all, I wasn't going to be pregnant forever, so I didn't want to ruin my nice space uniform."
                "So I took a pair of low-rise jeans and added a strip of stretchy material."
                "But what about the shirt?"
                "I found some scrap material and added some panels. I couldn't decide if it looked really good, or like I'd escaped from the circus, but either way, it would fit for the rest of my pregnancy."
                "It was kind of tedious sewing by hand, but I got it done."
                $ relaxed += 2
            "Ask [his_name]":
                show her normal at midleft
                show him normal at midright
                with dissolve
                her surprised "Hey, [his_name], could I borrow some of your clothes?"
                him flirting "Only if you let me borrow some of yours."
                her annoyed "For what? There's no way they'd fit you..."
                him happy "I'm just kidding. I don't have a lot of clothes, but there's one pair you could have."
                her happy "Thanks!"
                "He handed me an old pair of jeans and a t-shirt. They fit okay right now, but I could tell they wouldn't fit the whole pregnancy."
                "Well, I'd figure something else out later."
                $ relaxed -= 2
            "Try nudity":
                "I guess I didn't need to wear clothes around the house - it felt so good not to have that waistband constricting my growing belly!"
                show her normal at midleft
                show him normal at midright
                show her sitting
                show him sitting
                with dissolve
                him flirting "Hey, is it no pants day? How come I didn't get the memo?"
                her normal "It just feels so much more comfortable this way..."
                him normal "Good idea."
                play sound "sfx/cloth.mp3"
                "Pretty soon [his_name] was walking around free as a bird, too."
                scene black with fade
                "That led to some interesting results..."
                $ made_love += 1
                scene bg farm_interior with fade
                "But I was pretty sure I had to wear clothes to work, so I needed to try something else, too."
                $ relaxed += 2
                jump maternity_clothing
            "{i}Ask around{/i}" if (skill_social >= 60):
                "I knew Helen was also expecting, so I decided to send her a message and see what she had done."
                play sound "sfx/message.mp3"
                her "Hey, Helen, what are you doing for maternity clothes?"
                helen "Oh, I just made a big tent dress out of a hospital gown. It doesn't look very good, but it's very comfortable."
                her "Do you think you could show me how?"
                helen "Well, I'm sort of stuck in bed because of this pregnancy... but send me your measurements and I'll make you one!"
                her "Really?!"
                helen "Sure, I've got nothing else to do all day, and I'm sick of crocheting baby clothes..."
                "About a week later Sven dropped the dress off at work for me."
                "Sure enough, it looked kind of terrible. But it fit, and was comfy, so I wore it a lot."
                $ relaxed += 2

    else:
        "But for some reason this month it really bothered me. I was sick of the uniform's fabric, its unisex cut, and the sameness of it all."
        "But what could I do about it?"
        menu:
            "Make a new accessory" if (skill_creative >= 60):
                "I knew how to crochet, so I decided to make myself some long fingerless gloves. Luckily, someone had made some yarn from shearing their sheep and donated it to the storehouse."
                "They color was pretty plain, but they definitely stood out and looked unique."
                $ relaxed += 2
            "Host a clothing swap party" if (skill_social >= 60):
                "I figured I wasn't the only one getting tired of the same clothes every day, so I posted a message on the colony message board and invited everyone to bring one outfit to the community center, and we could all trade."
                "Not everyone was the same size, but we also didn't have much to choose from, so we weren't picky."
                "For some reason, it felt so good to sift through the clothes - I didn't think I'd miss shopping, but it felt so luxurious to have several different things to choose from and make my own."
                $ relaxed += 2
            "Decorate old clothes" if (skill_domestic >= 60):
                "I thought I'd just decorate some of the clothes I already had to look different."
                "I printed out a design I liked from the internet, printed it out on paper, and cut out parts of it to make a stencil. Then I sprayed bleach over the stencil until the part with the cut-outs faded. Then I dunked it in water to wash the bleach out."
                "It was like having a whole new shirt. It was just a little thing, but it was something I could exercise control over."
                $ relaxed += 2
            "Nothing. Who cares?":
                "It was too much work. We had more important things to worry about than clothes, anyway."
    return

# TODO: is this boring? Add argument?
label monthly_event_20:
    scene bg bedroom with fade
    show her normal at midright
    show him normal at midleft
    show overlay night
    with dissolve

    if (is_pregnant):
        "One night I lay down for bed, and, of course, that's when the baby decides to practice martial arts on my bladder."
        her annoyed "Not again..."
        him surprised "Everything okay?"
        her normal "I can't sleep while I'm being pummeled from the inside."
        "He put his hand on my belly and felt the tiny movements."
        him happy "Wow, that's an energetic kid!"
        her sad "I'm just so tired..."
        him sad "Have you not been sleeping well?"
        her serious "Every time I fall asleep, something wakes me up in an hour or two. Either I have to use the bathroom, or the baby's moving, or my back hurts, or, worst of all, it's morning."
        her "And I don't want to take any medicine or herbs because I'm worried it might hurt the baby."

    else:
        "I'd had trouble sleeping lately; my back hurt whenever I lay in one place for too long."
        her annoyed "Oww..."
        him surprised "You okay?"
        her annoyed "Yeah, my back's been hurting; makes it hard to sleep."
        if (profession == "doctor"):
            him serious "Did you try taking some medicine for it?"
        else:
            him serious "Did you see the doctor about it?"

        her concerned "Yeah, it didn't really seem to help."

    if (loved >= 0):
        him serious "That sounds hard."
        her concerned "Yeah..."
        him surprised "Is there anything you can do about it?"
        her serious "I don't know; I'm still thinking about it."
    else:
        him annoyed "I can't do anything about that."
        her angry "You don't have to do anything about it! Can you just listen?!"
        him serious "..."
            
    menu:
        "I decided to:"
        "{i}Make a pillow to support my knees{/i}" if (skill_creative >= 70):
            "After doing some research, some people said it helped their back pain to put a pillow between their knees."
            "But how could I make a pillow?"
            "I knew some people stuffed pillows with beans, so I got some from the storage room."
            "But a bean pillow was way too heavy for my knees. I decided to put the bean pillow under my head, and used the other pillow between my knees. It did seem to help my back a little."
            $ relaxed += 5
        "{i}Ask Sister Naomi{/i}" if (skill_spiritual >= 70):
            "I talked to Sister Naomi about my sleep problems."
            scene bg church with fade
            show naomi at midright
            show her normal at midleft
            with dissolve
            naomi "Do you meditate before bed?"
            her surprised "Meditate? No, I usually just fall into bed and try and get to sleep."
            naomi "You might want to try it. It can help put your mind at ease."
            naomi "If you have any problems bothering you, write them down so that you know you will remember to do something about them tomorrow. Then your meditation and your sleep can be peaceful and uninterrupted."
            her serious "I can try it..."
            
            scene bg bedroom with fade
            show her serious at center
            show overlay night
            with dissolve
            "I took a few minutes before bed to do what Sister Naomi suggested."
            "My back still hurt, but when I wrote down ideas or things to do the next day, I didn't have to worry about them anymore, so I was able to sleep a little bit better."
            $ relaxed += 5
        "Take more naps":
            "I thought maybe I'd just take naps more often. Maybe right after work?"
            "But when I got home from work, there was always so much to do around the house that by the time I thought about taking a nap, it was time for dinner, and then it was too late in the day."
            her annoyed "(Well, this back pain won't last forever. I can deal with it.)"
        "Go to bed earlier":
            "I thought I'd try going to bed earlier, but I wasn't tired earlier. The one time I tried it I just lay there staring and thinking for several hours, and didn't get any sleep or get anything done."
            her annoyed "(Well, this back pain won't last forever. I can deal with it.)"
        "Don't change anything.":
            "There was no point in doing anything different; it'd be hard to sleep no matter what I did. I'd just have to deal with it."           

    return

# Early frost kills lots of crops
# uses knowledge, technical, social
label monthly_event_21:
    scene bg farm_interior with fade
    "The weather was usually fairly mild on Talam. It didn't snow in the winter, and the summer was hot but not unbearable. It was much colder near the poles, of course, but we were near the equator and the ocean."
    "But one week was a lot colder than usual."
    show her normal at midright
    show him normal at midleft
    with dissolve
    him concerned "It was so cold today... with no clouds, either. Dr. Lily says it might freeze..."
    her surprised "Well, we have our heater, so we'll be fine, right? Do we need to chop some more wood?"
    him "Yeah, maybe - but it's not us I'm worried about."
    her flirting "Oh, is it going to be too cold for Lettie? Maybe she'd like to sleep in bed with us?"
    him annoyed "Of course not. Horses are incredibly strong and can handle the cold no problem. It's the quinoa that might not make it."
    her surprised "The quinoa?"
    him normal "Well, I planted it a week ago. Even though it's technically still winter here, we don't have any records of freezing weather in this area, so I thought it would be safe..."
    her concerned "Is there anything we can do?"
    him serious "Well, that's what I'm thinking about."
    menu:
        "What should we do?"
        "{i}Cover the quinoa{/i}" if (skill_knowledge >= 60):
            her serious "Can we cover it up with blankets or something?"
            him serious "Yeah, that's one of the things I was thinking of, but I don't think we have enough fabric to cover very many plants."
            her annoyed "Well, we don't have to use fabric."
            him surprised "What do you think we should use?"
            her normal "Anything insulating that breathes well - paper, cloth, wood, cardboard, baskets..."
            him annoyed "There's tons of that stuff on Earth, but how much do we have here?"
            if (skill_social >= 60):
                her normal "The whole colony should help - I'll ask around and get everyone to give us what they can."
                "Everyone let us use their sheets, curtains, towels, and extra clothes. I was going to have to wash them before I gave them back, but it would be worth it."
            else:
                her serious "I'll ask at the storehouse."
                "They had some surplus fabric, clothes, blankets, and towels, and they said we could use them as long as we washed them and brought them back afterwards."
            scene bg fields with fade
            "We worked all afternoon covering up the acres of plants."
            show overlay night
            "We were still working when it started getting dark. We worked until about midnight, when we had finally covered up all the plants."
            "We kept the covers on for several nights until the danger of freezing had passed."
        "Build a fire near the quinoa":
            her surprised "Could we use fire to keep it warm?"
            him surprised "What, like have a bunch of bonfires in the fields all night long?"
            her sad "Sorry, that's probably a dumb idea..."
            him annoyed "No, it could work... We'll need a lot of fuel, though."
            scene bg fields with fade
            if (skill_social >= 60):
                "We got some of our neighbors to help us gather wood and stacked it in piles near the crops."
            else:
                "We worked all afternoon gathering wood and branches and stacking them near the crops."
            show overlay night
            "Then we stayed up all night tending the fires."
            "We slept all day, and did the same thing the next night, until finally the freezing weather had passed."
            $ relaxed -= 5
        "{i}Make a crop heater{/i}" if (skill_technical >= 60):
            her normal "I bet I could make something that would help the crops stay warm..."
            him normal "Let's draw it out together."
            "We did some research, and decided on a combination heater and blower system. We made a fan out of spare parts from the shuttle, and decided to just light a fire for the heat part."
            scene bg fields with fade
            "The fan blew the hot air over the crops, hopefully drying out any dew before it froze on them, and keeping the plants warm enough that their cells wouldn't freeze."
            "But one fan wouldn't be enough... We didn't have time to build more, but I did build a rotating stand so it could rotate and blow across a wider angle of plants."
            show overlay night
            "I got up several times in the night to check on the fan while [his_name] tended the fire, so we were pretty tired the next day."
            "We repeated this every night for a few days, until the danger of freezing had passed."
        "It's not my problem":
            her concerned "That's too bad, but it's not really my problem."
            him angry "What, you don't want to have food to eat?"
            her angry "That's your job."
            him angry "You're no help at all."
            "I felt a little bad, but what could I do? I was no farmer..."
            "Anyway, he and Thuc figured something out, I guess, because he was gone all night and I saw the plants a little later and they looked fine."
            $ loved -= 5
            return
            
    him normal "I think the quinoa should be safe, now."
    if (loved >= 0):
        him happy "Thanks for all your help, [her_name]."
        $ loved += 2
    her concerned "Yay... now I'm going to sleep for a week."  

    return

# TODO: Write this event
# Include name for baby?
label monthly_event_22:
    scene bg farm_interior with fade
    "Month 22 is not finished yet."
    # If pregnant, work out name for baby girl
    if (is_pregnant):
        "We finally picked a name for the baby!"
        
    # Otherwise, make a plan for future?
    else:
        "We thought about how we wanted to live the rest of our lives?"
    return

# Climax - epic conflict leading to either "We'll always be together" or "I just want to get away from you!"  Conflict: Worried about new baby, pregnant if made_love a lot or affair with Brennan, otherwise, discussion about quality of sex
label monthly_event_23:
    scene bg farm_interior with fade
    show her serious at center with dissolve

    if (is_pregnant):
        "I was getting huge. I felt like I couldn't eat very much at a time, not only because of the terrible heartburn, but it just didn't feel like there was any room inside me for anything else."
        "Some days I couldn't believe that I had been pregnant for so long, and other days I wished it would last longer because I didn't feel ready yet."
        
        # who will take care of the baby during the day?
        scene bg bedroom with fade
        show her normal at midright
        show him normal at midleft
        with dissolve

        her concerned "Do you feel ready?\n...For the baby, I mean?"
        him serious "Well, we made a little crib, and we have plenty of rags for diapers, and I thought you said you got some clothes from the storehouse..."
        her annoyed "No, I mean, ready to be parents. Ready to be responsible for a little helpless person twenty-four hours a day..."
        him concerned "Ohhh...well, I figured we'll take turns taking care of her, so we can each have a break sometimes. So that's really only more like twelve hours a day, right?"
        her angry "No! Even if someone else is taking care of the baby at the moment, you and I are still responsible - we're the parents! This isn't a job you can just do part-time!"
        him normal "Well, yeah, of course."
        "It was clear he was not as worried about it as I was."
        her sad "What if I can't figure out how to nurse her, or the diapers are unsanitary and make us all sick, or I have really bad post-partum depression, or my body never recovers, or--"
        him concerned "Hey, hey, it'll be okay."
        her angry "It won't be okay just by saying, \"It's okay\"!"
        him angry "All right, then, let's figure some of these things out."
        him concerned "Mrs. Nguyen already is helping you with the birth, right?"
        her concerned "Yeah..."
        him "Well, I bet she knows a lot about nursing babies, and could help you out there. But even if something happens and you can't nurse the baby, they have some formula in the storehouse."
        her normal "That's good to know..."
        him normal "And we have a great doctor here, in case anything goes wrong. I don't think that will happen, but it's good to know."
        if (profession == "doctor"):
            her "Hey, I'm the doctor..."
            him happy "Yeah, and you're great!"
            her concerned "But I can't really perform surgery on myself! What if I need a C-section or something?!"
            him concerned "I hadn't thought of that..."
            her angry "I'll just have to teach Mrs. Nguyen and Brennan how."
            him angry "Brennan!"
            her "Do you know of anyone else?!"
            him concerned "Well...I've done a C-section on a cow before, so I could probably help out."
            her surprised "A cow? That's not very reassuring."
            her concerned "I can just use local anaesethetic, so I can stay conscious and instruct you... but I sure hope we never have to do that."
            him concerned "We'll do what we have to."
        
        her surprised "What are we going to do with the baby during the day?"
        him concerned "Well...I thought she would hang out with you."
        her concerned "Will that really be okay at work?"
        "I tried to imagine going to work with a baby."
        her surprised "I guess she could ride around with me some of the time, and maybe lie in the corner in a little bed sometimes?"
        her angry "But why is it always the woman who takes care of the baby more?"
        him happy "Because you're the one whose awesome body can squirt out perfect baby food?"
        menu:
            "What should I say?"
            "True.":
                her annoyed "Well, yeah, but..."                
            "Gross!":
                her angry "I can't believe you just said that."
                him surprised "What, it's true, isn't it?"
                her annoyed "..."
                him annoyed "Okay, let me rephrase that for you. \"Because your female body is capable of producing optimum infant nourishment for your offspring.\" Is that better?"
                her serious "Yes."
            "That's what technology is for.":
                her annoyed "That's so old-fashioned. That's why we have pumps and formula, so women don't have to be the only ones that the baby is dependent on."

        him serious "Also, it'd be dangerous around all the heavy farm equipment."
        her annoyed "Not really any more dangerous than my work..."
        him annoyed "Well, maybe we'll take turns, depending on what's going on at work, if you wanted to pump milk so the baby can still eat."
        her concerned "The idea of pumping milk still sounds pretty weird to me, but I guess we should probably save the formula for emergencies, huh?"
        him surprised "Pumping milk is not any weirder than milking cows, right?"
        her annoyed "...You did not just compare me to a cow."
        him annoyed "Sorry, cows are just what I know. I've never been a dad before!"
        him happy "But people do it all the time, so how hard can it be?"
        if (community_level >= COMMUNITY_LEVEL_OK):
            her normal "You're right...and our community is so close-knit, I'm sure one of the other moms will help me out if I need it."
        else:
            her concerned "You're right...I just wish I felt closer to the other moms, so I would feel better asking them if I needed help."
        
        if (loved >= 0):
            him serious "I'm right here, with you, and our love is so strong, there's nothing we can't do together."
            her annoyed "The \"power of love\", huh?"
            him annoyed "I'm serious! Whatever you, and the baby need, I'll do it! I'll beg from total strangers! I'll cook dinner every night! I'll do laundry!"
            him sad "...I'd even give up Lettie, if I had to."
            her surprised "You would?"
            him serious "Of course!"
            her serious "[his_name]...thank you. We'll both have to make some sacrifices and work hard, but we can do it together, can't we?"
            "We held each other tightly, my huge belly between us, and the baby kicked."
            him laughing "See, she agrees!"
            show her laughing
        else:
            him serious "Well, we'll make it work somehow."
            her concerned "Thanks, [his_name]."

    elif ((want_kids) or (cheated_on_him)):
        $ is_pregnant_later = True
        "Lately I'd been feeling a little sick. My breasts were sore (for no reason), and I had to go to the bathroom all the time."
        her surprised "Come to think of it, shouldn't my period have started by now?"
        if (want_kids):
            "I felt a sudden thrill go through me. Was I pregnant?"
        else:
            "I had a sudden fear, right in my lower belly. I couldn't be pregnant, right? I mean, we always used birth control..."
            if (cheated_on_him):
                her concerned "(Except for that one time with Brennan...!)"

        scene bg clinic
        "I went to the doctor. I had to know for sure."
        her annoyed "(They didn't have enough room to bring a long a few more condoms, but there's plenty of pregnancy tests...)"
        "Sure enough, the test read positive."
        her surprised "(I can't believe this...!)"

        scene bg farm_interior
        show her concerned at midright
        show him normal at midleft with moveinright
        "I had to tell [his_name]. As soon as he came into the house, I blurted it out."
        her concerned "I'm pregnant!"
        if (want_kids or (loved >= -5)):
            him happy "Really? That's great!"
            if (want_kids):
                her happy "I know! I just didn't think it would happen so fast..."
            else:
                her concerned "..."
                him concerned "I mean, well, I guess we had planned on having a baby later, right? But there's no reason why it wouldn't work out now!"
                her sad "I'm not ready, [his_name]!"
                him serious "Can we just try it, [her_nickname]? I'll work hard with you, to take care of this little baby, and take care of you, too."
                her "..."
            him normal "Think of it as another adventure - we didn't know what this planet was really going to be like until we got here, right?"
            him surprised "What if we had never come here - we would have missed out on so much!"
            her normal "I guess when you think about it, it's not that scary. I mean, people have been having babies since, well, forever, so it can't be too hard..."
            him happy "Yeah! That's the spirit! We can do this!"
            "Could this really work out? I guess we could try..."
            if (cheated_on_him):
                menu:
                    "He didn't need to know that the baby might be Brennan's, right?"
                    "He doesn't need to know":
                         "I decided he didn't need to know; I didn't want to ruin what we had."
                         $ loved -= 5
                    "He should know":
                        "(He should know, but... can I bring myself to tell him about it?)"
                        her concerned "[his_name], there's something you should know..."
                        him concerned "What is it?"
                        her sad "I did something really stupid. I mean, it was just one mistake, but it's the kind of thing that's hard to forgive, so I just want you to know that I'm really sorry, and it's not your fault."
                        him concerned "Just tell me, okay? Whatever it is, we'll work it out."
                        her concerned "I...slept with Brennan. One time. It was a huge mistake, and I feel terrible about it, and I'm sure it will be hard to forgive me, but...will you please try?"
                        him angry "WHAT?!"
                        her sad "..."
                        "He just stood there for a moment, shaking his head, trying to figure out what to say. But he didn't meet my eyes."
                        him serious "I'm... glad you told me."
                        her "You're...glad?"
                        him concerned "I mean...I'm also furious and ashamed and humiliated and annoyed, but I'm at least glad I found out from you and not someone else."
                        her concerned "Do you think you can forgive me?"
                        him sad "..."
                        him serious "I can't. Not right now. Just...give me time."
                        scene black
                        "Things were very awkward around the house for awhile..."
                        scene bg farm_interior with fade
                        show her concerned  at midleft
                        show him concerned at quarterright
                        with dissolve
                        her surprised "Umm, [his_name], I think it's your turn to make dinner...but I could do it instead!"
                        him sad "No, it's okay, I'll do it."
                        her sad "..."
                        him sad "..."
                        him angry "How are you going to make sure it doesn't happen again?"
                        her surprised "What?"
                        him concerned "I mean, you guys have to work together every day, right? So how will you make sure that never happens again?"
                        her sad "My word isn't enough?"
                        him sad "Not anymore."
                        her surprised "Well, I can make sure I'm not in that sort of situation again... I won't go to his house without other people around, and..."
                        him concerned "What else?"
                        her surprised "When we're not working, I'll make sure we're around other people...like maybe I'll see if I can have lunch with Sarah or something."
                        him serious "That could work."
                        her sad "..."
                        
                        # Workplace Scene
                        scene black with fade
                        "I thought I should talk to Brennan, too."
                        call set_work_bg

                        show her serious at midleft
                        show brennan at midright
                        with dissolve
                        brennan "Good morning, [her_name]. Sleep well?"
                        her serious "Hey, good morning..."
                        brennan "What is it?"
                        her concerned "It's never going to happen again."
                        brennan "What isn't?"
                        her "You and me... doing anything that's not work."
                        brennan "Ah. Did [his_name] forbid you from being friends with me?"
                        her surprised "What? No, {b}I{/b} decided that we should be more distant, because I don't want to make that mistake again."
                        brennan "Oh, I see, I'm a mistake."
                        her annoyed "Don't make this harder than it is!"
                        brennan "I don't like how he treats you."
                        her angry "What are you talking about?! He's trying to forgive me, even though I totally betrayed him and our marriage!"
                        brennan "Don't you have any freedom? He's just being selfish, and not letting you follow your heart. You can't tell me I mean nothing to you..."
                        her annoyed "Is that what it will take for you to believe me?"
                        brennan "You won't say it."
                        her angry "You. Mean. Nothing. To. Me."
                        brennan "..."
                        her sad "I'm sorry...but I have to do this. I can't be alone with you outside of work - even if nothing happens, I don't want it to look like something's going on between us."
                        brennan "Sure. Fine. No problem."
                        her concerned "Are you sure?"
                        brennan "Just bloody drop it, all right?!"
                        her surprised "Okay, okay."
                        hide brennan with moveoutright
                        "Brennan kind of ignored me after that, except for when we needed to talk for work. I felt bad, because I knew he didn't have many friends... but my marriage is more important than anything else right now."
                        scene black with fade
                        "Even after I worked things out with Brennan, I could tell [his_name] still hadn't forgiven me..."
                        scene bg bedroom with fade
                        show overlay night
                        show her serious at quarterleft
                        show him concerned at midright
                        with dissolve
                        her serious "Good night, [his_nickname]..."
                        show her at center with moveinleft
                        show him at quarterright with move
                        him concerned "Good night."
                        show her at quarterleft with move
                        her sad "..."                
                        scene black with fade
                        "But finally, after about two weeks of walking on eggshells..."
                        scene bg farm_exterior with fade
                        show overlay night
                        show her concerned at midleft
                        show him concerned at quarterright
                        her normal "Welcome home, [his_nickname]."
                        show him at midright with move
                        him normal "It's good to be home, [her_nickname]."
                        show her at center with move
                        "When he hugged me, for the first time in way too long, that was when I knew everything would be okay. Things weren't back to normal; I don't know if they ever would be like they had been. But they were okay."
                        $ loved += 10
                        return
                
            her surprised "I never thought of myself as a parent, you know."
            him normal "Doesn't mean we can't do it. Humans are made to be parents, right?"
            her flirting "At least I have you..."
            "He held me tight, cradling my head in his hand. I relaxed onto his shoulder, and he placed tiny kisses on my neck."
            "We really did need each other..."
            $ loved += 2
            $ made_love += 1

        # loved < -5
        else:
            him annoyed "Oh, great, that's just what this marriage needs."
            her annoyed "What?!"
            him angry "I mean, you and I can barely get along as it is, and the last thing we need is something else to argue about."
            her angry "I thought you wanted kids! It's not like I got pregnant by myself; you're half responsible, too!"
            him concerned "Yeah, probably."
            her surprised "What's that supposed to mean?!"
            if (cheated_on_him):
                him annoyed "Are you having an affair with Brennan?"
                her surprised "(Oh no.)"
                menu:
                    "What should I say?"
                    "No":
                        her annoyed "No."
                        him annoyed "\"No\"? That's it?"
                        her "That's it."
                        him "Hmph."
                        "I could tell he didn't believe me. And now he didn't trust me to tell the truth, either."
                        "We didn't talk much after that. We tried to pretend nothing was wrong, but I didn't know what else to do."
                        $ loved -= 5
                        $ relaxed -= 5
                    "Yes":
                        her sad "...yes."
                        him angry "What!"
                        her sad "I mean, it was just that one time, but..."
                        him concerned "When did you- Never mind, I don't want to know."
                        him angry "I can't believe this..."
                        her annoyed "I'd say I'm sorry, but it's clear he loves me more than you ever will."
                        him annoyed "It's clear, huh? He's that good?"
                        her angry "It's not just about the sex!"
                        him serious "Sure it's not."
                        her serious "I mean, not just that. He listens to me! He has time for me."
                        him angry "Yeah, because he's a useless prick! He doesn't even know how to do anything useful, so they had you babysitting him! Guess that's like having the sheep babysit the wolf..."
                        her angry "Look, I was going to say I was sorry, but what's the point?! Clearly, you are done with this relationship."
                        him angry "Clearly, there was never much of a relationship here to begin with. I'm sorry for not seeing it sooner."
                        "We didn't talk much after that. We both knew it was over, but we kept pretending nothing had happened..."
                        $ loved -= 5

                    "What about you?":
                        her concerned "Are {b}you{/b} having an affair with Thuc?"
                        him surprised "What? Of course not."
                        her angry "Well, that's how ridiculous your suggestion is. So drop it."
                        him annoyed "...Okay."
                        "I wasn't sure if he believed me or not. But he started acting more distant, and I felt he didn't trust me."
                        $ loved -= 5

                # Tell Brennan about the baby
                if (cheated_on_him):
                    "I decided to tell Brennan about the baby. I wasn't sure it was his, but part of me hoped it was."

                    scene black with fade
                    "I needed to feel like someone was on my side..."
                    call set_work_bg
                    show her serious at quarterleft
                    show brennan at midright
                    with dissolve
                    brennan "What's wrong, my lovely? Did you decide you can't live another moment without me?"
                    her concerned "...I'm pregnant."
                    brennan "Oh. Well... congratulations."
                    her serious "I'm pretty sure it's yours. From when we...you know."
                    brennan "...What?"
                    her sad "It all happened so fast, we weren't careful- [his_name] was always very careful- I mean, the timing fits, and--"
                    brennan "Have you told [his_name]?"
                    her concerned "I've told him I'm pregnant, but he doesn't know about- about us."
                    brennan "Oh? Is there an 'us' now?"
                    her concerned "I wish we could be together..."
                    brennan "Well then, let's do it!"
                    her surprised "What?"
                    brennan "Get a divorce! This isn't the dark ages, where people torture themselves with unhappy marriages."
                    her serious "Would you... want both of us? Me and the baby, I mean."
                    brennan "I don't care if you bring a flock of crabirds with you. As long as I get you, I'll be happy."
                    her concerned "..."
                    brennan "Although, you should know I'm planning on leaving."
                    her surprised "Leaving?!"
                    brennan "On the next ship. They're dropping off more supplies, and colonists, and my orders are to report back to Earth. But you could come, too."
                    her concerned "Leave Talam... I'll have to think about it."
                    brennan "You have a month or two before the ship arrives. So, let me give you a little something to think about in the meantime..."
                    scene black with fade
                    "He kissed me softly, not full of passion like before, but the tender kiss of a lover's promise..."
                    
            # if you haven't cheated on him, but want_kids and love <-5
            else:
                him concerned "I just know things have been... difficult, lately."
                her annoyed "Well, it's not like I've had sex with anyone else!"
                him sad "..."
                her surprised "Wait, you haven't-"
                him surprised "Haven't what?"
                her concerned "You haven't cheated on me, have you?"
                him sad "...No."
                her surprised "...?"
                him concerned "I thought about it, but decided not to."
                her angry "You thought about it?!"
                him concerned "There was an...opportunity, but I told her no."
                her surprised "Who was it?"
                him annoyed "It was-"
                her annoyed "No, no, don't tell me. I don't want to know."
                him serious "I mean, I know we don't always agree, but we promised to stay together. I'm yours, [her_name]."
                her serious "Show me."
                "He approached me slowly. Had it been so long that it seemed strange? My heart beat fast like it did when we were first dating."
                "I hadn't realized how much I missed him. I missed his touch, his laugh, his soft kisses on my back, everything we had ever shared together."
                "Together, we remembered it all."
                $ loved += 5
                $ made_love += 1
                
    # Not pregnant, don't want kids, and didn't cheat on him
    # How to talk about sex
    else:
        scene bg bedroom
        show her annoyed at midright
        show him sleeping at midleft
        with dissolve
        show overlay night
        
        "[his_name] was generally a good lover, but sometimes he was finished before I was."
        "Then he'd fall asleep, just as I was finally getting in the mood."
        hide overlay night
        him happy "Mmmm, good morning, my amazing sweet bundle of loveliness."
        her annoyed "Good morning..."
        if (loved >= 0):
            him surprised "Oh. Hey. Ummm, did {b}you{/b} have a good time last night?"
        else:
            him annoyed "What? What's with the icy glare?"

        menu:
            "What should I say?"
            "You only think about yourself!" if (relaxed < 0):
                her angry "You are a terrible lover. All you think about is your own satisfaction!"
                him angry "Well, why didn't you say something last night!"
                her angry "You were {b}asleep{/b}!"
                him angry "You couldn't have been trying very hard, then!"
                her sad "..."
                him sad "...Sorry... Sometimes it feels kind of one-sided, so I thought I'd get it over with so you could get to sleep..."
                
                her annoyed "I'd rather take longer and get more out of it."
                him annoyed "Well, okay, now I know."
                if (loved < 0):
                    her angry "If you really loved me, you would have asked me what was wrong last night, instead of just getting what you wanted and then dropping off to sleep!"
                    him angry "Oh, so if I make one mistake, suddenly I don't love you anymore?"
                    her angry "This is not the only time this has happened!"
                    him angry "All right! Let's bring up every imperfect thing the other person has ever done, right now! Do you want to do that?!"
                    her sad "No, I just--"
                    him annoyed "Tch. Forget it."
                    $ loved -= 2

                "He left, closing the door behind him slightly harder than was necessary."
                "I got dressed and fixed myself a cup of tea."
                "It wasn't selfish to tell him how I felt, was it?"
                "Maybe if I wasn't so stressed out about everything else, I could have communicated better..."
                "Well, now he knew how I felt, anyway, so maybe next time would be better."
                "But we didn't make love again for a long time..."
                $ loved -= 2
                
            "Last night was not really very good for me." if (relaxed >= 0):
                her annoyed "Well, I didn't really get to enjoy last night very much..."
                him concerned "Oh, I'm sorry, [her_name]. I fell asleep again, huh?"
                her concerned "It's okay, I just... it was hard for me to sleep, and then I felt all mad at you, and I don't want to feel mad at you."
                him sad "That was pretty rotten of me. I'm sorry."
                her surprised "No, no, it's okay, it's not that big of a deal. I just wanted to tell you how I felt."
                him normal "Well, I'm glad you did. And I think I know just how to solve this problem."
                her surprised "How's that?"
                him flirting "Lots of practice!"
                her annoyed "[his_name]..."
                "He's kind of exasperating, but afterwards I could tell he was really trying to make sure I felt loved and appreciated, too."
                $ loved += 2
                $ relaxed += 2
            "Let's slow it down next time." if (loved >= 0):
                her flirting "As much as I love that you are like a runaway stallion, can you maybe not gallop away quite so fast next time?"
                him surprised "Ummm..."
                her annoyed "You know, slow down a bit?"
                him surprised "Oh! Yeah. Sorry, I'm still trying to wrap my head around your horse imagery."
                her laughing "Don't think about it too hard."
                $ loved += 2
                $ relaxed += 2
            "(Lie) Everything's fine.":
                her concerned "Everything's fine."
                him serious "Okay, if you say so..."
                "I just didn't want to talk about it. Maybe I could communicate to him what I wanted in some other way..."
                $ relaxed -= 5
            "I don't have time for this.":
                her annoyed "I have to go to work. I'll see you later."
                him annoyed "Okay, bye, then."
                $ loved -= 2
                $ relaxed -= 5
    
    return

# Birth or leave Talam
label monthly_event_24:
    if (is_pregnant):
        scene bg farm_interior with fade
        "I felt like a whale. No, that's not big enough. I felt like a brontosaurus."
        "My belly had been growing larger and larger for the past few months, but it still felt foreign to me, like a mosquito bite or a new haircut."
        "And the heartburn! It was like morning sickness's young apprentice come back for revenge every time I ate."
        "I knew this baby had to come out sometime, but it seemed impossible. I had been pregnant for so long, I almost couldn't imagine things changing so quickly."
        show her normal at midright with dissolve
        show him normal at midleft with moveinleft
        him surprised "How are you feeling today?"
        her annoyed "The same, I guess."
        him "Any contractions?"
        her angry "No."
        him concerned "Okay. Well, I'll have my radio with me, just in case."
        her annoyed "Right."
        him annoyed "..."
        her sad "I'm sorry, [his_name]. It's hard not knowing when the baby will come..."
        him happy "Well, this just means you have a few more days of carefree irresponsibility! How do you want to celebrate?!"
        her flirting "I think we left all the carefree irresponsibility back on Earth."
        call set_work_bg
        show her normal at center
        "Work wasn't much better."
        "Everyone treated me like a ticking time bomb."
        show her at midright with move
        show brennan at midleft with moveinleft
        brennan "No baby yet, eh?"
        her annoyed "No. I'm sure everyone will know when the baby arrives."
        brennan "Yes, well, you just let me know if you, uh, need to leave or anything."
        her concerned "..."
        "At last I could escape for lunch."
        scene bg farm_interior flip
        show sara at midright
        show her normal at midleft
        with dissolve
        sara "So, how've you been feeling? You're nine months along now, huh?"
        her angry "YES! Yes, I am nine months pregnant now, and any minute, without warning, an strange creature could come bursting out! Stand back!"
        sara "Whoa, feeling a little sensitive?"
        her sad "Sorry... it's just that it's all anyone ever talks to me about anymore."
        sara "I'm sorry; do you want to talk about something else?"
        her normal "Yes, please! Tell me you've read a good book, or found a cool new place, or something!"
        sara "Yeah, there's this spot by the river where it's kind of like a little beach. It's great for wading and sunbathing."
        her happy "That sounds great! Will you show me sometime?"
        sara "Of course! Do you want to go after work today?"
        her sad "Well... I probably shouldn't. I mean, what if we went, and I went into labor out there in the wilderness?"
        sara "Ha ha, yeah, if this was a movie that'd totally be what would happen."
        her normal "You know what? Let's go. I feel fine; we'll bring a radio; and I could certainly use the exercise."
        sara "Okay, if you're sure!"
        scene bg pond with fade
        "After work we hiked for twenty minutes until we got to the riverside spot she mentioned. The sun shone down on us fiercely, but it was a little cooler when we finally got to the shade by the river."
        show her normal at midright
        show sara at midleft
        with moveinleft
        her happy "This is cool!"
        sara "Yeah, I've never seen anyone else here, so I like to come here and relax, sometimes."
        her normal "The sound of the water is so peaceful..."
        her concerned "But I feel a little tired after walking so far. I think I'll just lie down for a minute."
        show her at sitting
        show sara at sitting
        "We sat there for awhile, just enjoying the sounds of the river."
        sara "..."
        her normal "..."
        sara "So, the shuttle comes next month!"
        her happy "Yeah! That was always our goal, wasn't it? To just make it until the shuttle came with more supplies?"
        sara "I guess they'll be bringing some more people, too..."
        her surprised "That's true! We'll have new neighbors."
        sara "And maybe they'll have something tasty from Earth."
        her normal "You know, I don't miss it that much anymore."
        sara "I do. I don't know that I'll ever get used to all the work it takes to make food here... and then it's not even very good."
        her sad "..."
        sara "Sorry. I should be more positive."
        her concerned "No, it's good to be able to be honest about how you feel."
        sara "..."
        her flirting "Like, for example, did you know I've been having contractions this whole time?"
        sara "What?!"
        her serious "Just small ones. I guess they call them practice contractions. I've been getting them a lot lately whenever I exercise or get tired. That's why I wanted to lie down."
        sara "So, we don't need to radio for help or anything?"
        her normal "No. But we should probably head back."
        scene bg mountains with fade
        show sara at quarterright
        show her normal at right
        with moveinright
        "We started walking back. The sun felt hotter than ever, and I started feeling really thirsty."
        show her at midright
        show sara at center
        with move
        her serious "You don't have any water, do you?"
        sara "No, sorry. Hey, are you okay?"
        her concerned "Yeah, let's just get back."
        "The contractions started to get stronger. I could still walk, but I had to concentrate more on just walking and breathing. I realized Sara was saying something."
        show her at midleft
        show sara at left
        with move
        sara "-really shouldn't have said that. Don't you think?"
        her concerned "Can't really...talk right now."
        sara "Oh, oh, oh, are you in labor?!"
        her serious "I don't know, I just need to get home."
        sara "Should we go straight to the clinic? Should I radio the doctor?"
        if (profession == "doctor"):
            sara "What am I saying, you are the doctor!"
        her concerned "No, just- mmmmmm-. Hmmmmm. Hmmmmm."
        "All I could think about was breathing, and noticing the pain and pressure but keeping my distance from it. Finally, that contraction subsided."
        her serious "Just walk with me."
        "I didn't even really notice where we were going; I was just following Sara. She took me to the clinic."
        
        scene bg clinic with fade
        show her serious at center
        show sara at midright
        with moveinleft
        sara "Here's some water; drink this."
        her concerned "Thank you."
        show him serious at midleft with moveinleft
        him surprised "Are you in labor?"
        "What was he doing here? Sara must have called him..."
        her serious "I don't know; I'm just having some contractions every now and then."
        him happy "That's great! Hey, little baby, we're ready for you!"
        her annoyed "Speak for yourself!"
        "Now that I was resting and had had some water, the contractions seemed to be slowing down."
        show julia at midleft with moveinleft
        show him at midright with move
        show sara at quarterright with move
        julia "I got your message, [his_name]. Now, [her_name], tell me what's going on."
        her serious "Well, I just went on a little walk and then started feeling some contractions on the way back... but I think they went away."
        julia "That wouldn't surprised me at all. Shall we check and see how things are going?"
        her serious "Yeah..."
        "I started to take off my pants."
        sara "Ummmm, do you want me to stay? I mean, I could, but if you want your privacy..."
        menu:
            "What should I say?"
            "Please stay.":
                her normal "I'd like you to stay, if you can. We might need help."
                julia "Yes, I would appreciate some assistance."
                sara "Okay, then I'll stay."
            "You can stay if you want.":
                her normal "I don't mind if you want to stay. It might help you when you have a baby someday."
                julia "I could certainly use your help."
                sara "Okay, then I'll stay."               
            "Please leave.":
                her normal "Thanks for your help, but you can go home now."
                sara "Okay, I'll come check on you later!"
                hide sara with moveoutright

        "Julia put on a sterile glove and felt my cervix."
        julia "Good. Hmmm. Well, the baby's head is engaged, and she's started working her way down... You're dilated to about 3.5cm..."
        him surprised "That's a lot, right?"
        julia "When she gets close to 10, it's time to start pushing."
        him serious "Oh."
        "We waited around in the clinic for awhile, but instead of getting stronger, the contractions got weaker and farther apart."
        julia "I don't think you're going to have this baby tonight. Why don't you go home, and let me know when the contractions are more regular."
        her serious "Okay. Any idea when that might be?"
        julia "No. It could be tomorrow, it could be next week. But, perhaps you can take some comfort in the fact that your body is certainly getting ready and has started moving your baby closer to birth."
        her concerned "Okay..."
        hide julia with moveoutleft
        if ( renpy.showing("sara")):
            sara "Good luck, [her_name]. Sorry you have to wait some more."
            hide sara with moveoutleft
        her concerned "Sorry for all the fuss over nothing..."
        him serious "Hey, it's okay. It's a little disappointing, but the baby has to come eventually, right?"
        her annoyed "It feels like it's taking forever!"
        him annoyed "Sorry, there's not much we can do about it."
        scene bg bedroom
        show overlay night
        "We had dinner, and I went to bed early."
        "I felt frustrated and tired of waiting and wished I had more control over my own body."
        hide night
        "I woke up in the early morning to more contractions. I didn't want to wake up [his_name] yet, so I walked around outside as the sun was just starting to come up."
        scene bg sunset with fade
        show her serious at center with dissolve
        her annoyed "(It's probably just false labor again!)"
        if (skill_spiritual >= 30):
            her happy "(But at least I get to enjoy this beautiful sunrise...)"
            $ relaxed += 2
        elif (skill_knowledge >= 30):
            her happy "(But even 'false labor' is helping the baby get closer to being born, right?)"
            $ relaxed += 2

        show him normal at midleft with moveinleft
        him flirting "Good morning, [her_nickname]! How're you feeling?"
        her serious "More contractions...who knows if it's really labor or not, though?"
        him serious "Want me to time them?"
        her normal "Sure."
        "As he timed them, they got stronger and more uncomfortable."
        her serious "Hmmmmmmmmmmmmmmm."
        him surprised "Okay...They're about four minutes apart, so maybe this is really it?"
        her annoyed "Let's go find out."
        "He called Julia and asked her to meet us at the clinic, and grabbed a bag with a few things I had packed."
        scene bg path with fade
        show him serious at midright
        show her concerned at midleft
        with moveinleft
        "We walked into town, just the two of us. I slowed down a little whenever the pressure made walking too uncomfortable. On the way there, I threw up by the side of the road."
        her sad "Sorry about that."
        him serious "No problem. Can you still walk?"
        her serious "Yeah, yeah, just, let me stop if I need to."
        if (loved >= 5):
            "Once I stopped and leaned against a tree. He rubbed my back and waited patiently for me."
        if (loved >= 15):
            "During one of the contractions, I wrapped my arms around his neck and leaned into him while he held me. It was comforting to know I could depend on him."
        "The trip to the clinic never felt so long as that day when I was in labor. But, finally, we arrived."
        hide him
        hide her
        with moveoutright

        scene bg clinic with fade
        show julia at midright with dissolve
        show her serious at center
        show him serious at midleft
        with moveinleft

        "Julia checked me, pronounced me officially in labor, and then listened to the baby."
        julia "Her heartrate sounds good. I'll keep checking, but you are doing great. She is already further down than she was last night."
        
        show brennan at left with moveinleft
        brennan "[her_name]! Are you having a baby?!"
        her serious "I'm working on it."
        brennan "Should I go fetch a bucket of water or something?"
        her annoyed "A bucket of water?"
        brennan "Yeah, isn't that what people are supposed to bring you when you're in labor?"
        him annoyed "..."
        brennan "That's what they do in movies..."
        julia "Yes, by all means, go boil some water. That will be all, Brennan."
        brennan "You can count on me!"
        hide brennan with moveoutright
        julia "That's usually what they tell people to get them out of the way so they won't distract the laboring mother."
        her serious "Okay, yeah, great."

        scene bg clinic with fade
        show her concerned at midright
        show him concerned at midleft
        "Time passed... I just tried to make it through one contraction at a time."
        scene bg clinic with fade
        show her sad at midleft
        show him serious at midright
        show julia at right
        him surprised "Is it supposed to take this long?"
        her angry "I'm working as hard as I can!!!"
        julia "It may not seem like it, but she's progressing well. The body needs to gradually stretch to avoid tearing."
        her sad "It just seems like nothing's happening..."
        julia "You're close. You've come so far. This baby is coming out soon!"
        him serious "You can do this..."
        her annoyed "Of course I can do this. I'm doing it right now, aren't I?!"
        if (loved >= 0):
            him normal "Yes, yes you are!"
        else:
            him annoyed "..."
        her serious "Ohhhh, here comes another one-"
        her sad "Hooooooo. Hmmmmmm. Ahhhhh! AHHHHH!"
        her angry "I feel like... I should... push!"
        julia "Okay, your body's ready, go ahead!"
        "I yelled and pushed through most of the next contraction. It was hurting a lot, but it felt so good to finally be getting somewhere!"
        him surprised "What should I do?"
        julia "See if she wants to lean on you."
        him serious "Ummm, do you want to lean on me?"
        "I couldn't concentrate on anything except breathing and pushing. Talking was impossible."
        julia "Don't use words, just be there."
        show her at center with move
        show him at midleft with move
        show julia at midright with move
        "I pushed five more times. Every muscle in my body felt so tired that I started shaking all over. I felt ready to give up, but that was impossible."
        "I managed to gasp out the one thing that was running through my head."
        her concerned "I guess it's, too late, to, change my mind?"
        julia "Yes, dear. But don't worry, another four or five pushes and you'll be there!"
        "After three more pushes I felt like I was done. I had nothing left. If it was a race, I would have quit long ago."
        her sad "Is this, even, doing anything?!"
        julia "Yes! I can see the top of her head!"
        "Suddenly, I felt centered. I had almost forgotten why I was going through all this pain in the first place. This wasn't about me, or about proving something, or winning, or anything stupid like that. This was about our baby, our tiny creature who needed my help just to exist!"
        "I took a deep breath, and pushed again, stretching past fire and pain and breathing and my own body. Even that wasn't quite enough; I pushed again!"
        him happy "Yeah! There she is!"
        julia "One more little push, [her_name], and then you just lie back and relax a bit."
        show her serious
        "I closed my eyes. I think [his_name] was holding the baby while Julia cut the cord. It was finished. I did it."
        "Something small and floppy was placed on my chest. I opened my eyes."
        if (loved >= 0):
            him happy "Hey, little one, this here's your momma. She is one awesome woman, but you don't need me to tell you that, right?"
        else:
            him normal "Here she is, our baby!"
        
        "I looked down at the tiny face in my arms. I couldn't even fathom that this was the same being that I had nourished for these last nine months. I guess I was supposed to feel intense love? I don't know; mostly I was just tired and in awe."
        julia "I think she looks like you, [her_name]."
        him surprised "Really?"
        her normal "I think she looks more like...a baby, than either one of us. Babies all look alike to me..."
        julia "Well, they won't so much now that you have one of your own."
        "One of my own... that was still so strange."
        her happy "Our little [baby_name]..."
        
    else:
        scene bg farm_interior with fade
        show her normal at midright
        show him normal at midleft
        with dissolve
        her surprised "The shuttle from Earth is supposed to be coming soon!"
        him happy "I know! Do you think they might have brought more chocolate?"
        her concerned "I guess some people are taking the shuttle back to Earth..."
        him surprised "The shuttle's not staying, like ours did?"
        her serious "No, they're loading it up with samples and returning it to Earth."
        him surprised "Who's going back?"
        her concerned "The Matthew's, and Brennan..."
        him annoyed "Don't know the Matthews very well. As for Brennan- well, good riddance."
        her surprised "[his_name]!"
        $ brennan_action = "flirt"
        if (cheated_on_him):
            $ brennan_action = "sleep"
        him annoyed "What? He's always been pretty useless around here, he never fit in, and he tries to [brennan_action] with all the women."
        her annoyed "Well, I'm starting to think it's a good idea."
        him surprised "What, [brennan_action]ing with women?"
        her annoyed "No! Leaving this stupid planet behind! Going back to Earth, where there's toilets and plenty of food and stores and family and doctors and, and..."
        if (is_pregnant_later):
            her sad "I don't want the baby to grow up like this, [his_name]. To grow up never knowing Earth, to know only work or die every day..."
        if (loved < 0):
            him angry "I've been working as hard as I can! But I can't make all that stuff appear overnight!"
            her surprised "You shouldn't have to work so hard! There's an easier way!"
            him angry "I don't want to do things the easy way. I did that on Earth; it was boring."
            her annoyed "I'd rather be bored and know I'll survive."
            him annoyed "That kind of life is not even worth living. I've never felt more alive than here on Talam."
            her angry "Really? You feel alive when you realize that bugs just ate all your food and you might starve? Or when you almost get your hands burned off?"
            him angry "Yes! It's better than all the idiotic stuff people do on Earth."
            him angry "All they care about is how to make more money so they can buy more stuff so they can distract themselves from the fact that nothing they do matters!"
            him annoyed "Here, everything matters. Every day you have to get up and do your job, because if you don't, everyone will suffer."
            if (community_level <= COMMUNITY_LEVEL_OK):
                him annoyed "But I guess you wouldn't understand that."
                her surprised "What do you mean?"
                him angry "You're so lazy! You just do the bare minimum you need and that's all. Things will never get better if you don't work at them!"
                her angry "I work plenty hard! But there's other things that are important, too!"
                him angry "Really? Like what! What's more important than surviving, than building up our community?!"
                her annoyed "How about my sanity?! Have you ever considered that? No! Because you don't think about how anyone else feels! You just think everyone else must feel like you do!"
                him annoyed "I know how you feel; you're just wrong."
                her angry "That's exactly what I'm talking about! You don't give my feelings any weight at all if they don't agree with yours!"
            him concerned "..."
            her concerned "..."
        else:
            him sad "You miss it that much? I thought we were doing pretty good here..."
            her sad "Well... yeah, sometimes."
            him sad "I've tried to work hard and give you everything you need..."
            her concerned "I know you have. It's not your fault."
            if (community_level <= COMMUNITY_LEVEL_OK):
                him concerned "But, you know, you need to work at it, too."
                her annoyed "What's that supposed to mean?!"
                him concerned "If we want things to be better here, it's up to us to make it happen. We can't just do the bare minimum and hope for the best."
                her angry "The bare minimum?! Is that what you think I've been doing?!"

                him concerned "Anyway, no matter what, I'm staying here. I love Talam. I love the challenge and the adventure. But if you really need to leave... I, I won't-"
        him sad "I won't try to stop you."
        menu:
            "What should I say?"
            "I'll never leave you." if (loved >= 0):
                "He looked almost ready to cry; he really thought I might leave him. But, even so, he still wanted what was best for me."
                her serious "Oh, [his_name], I'll never leave you!."
                him serious "I need you, [her_name]. You're the reason I work, and the reason I come home."
                "We held each other so tightly, as if we were made of a thousand pieces that would fall apart if the other person didn't hold them all together."
            "I need to leave." if ((loved <= 0) and (community_level < COMMUNITY_LEVEL_OK)):
                her sad "I can't stay here, [his_name]."
                $ wants_to_leave = True
                him sad "..."
                "He nodded sadly, and slowly turned away and walked out the front door."
                "I didn't go after him."
            "I'm not sure yet.":
                her concerned "I just don't know..."
                him serious "Then stay! You already know what kind of life you'll have on Earth - boring, predictable, pointless. But here - who knows what could happen?!"
                her serious "I'll think about it..."
                "He squeezed my hand gingerly, as if worried that if he reached for more I'd run away."
                "I squeezed back, but I was still thinking. I couldn't just do what was best for him. I had to think about myself, too."

    return
