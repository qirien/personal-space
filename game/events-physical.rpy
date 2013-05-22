# Afternoon Events
# Physical

# Intro Event and the default
label physical_0:
    if (skill_physical < 10):
        "We lived a little farther away from the town, so that we had plenty of farmland around us. The other farms were arranged in sort of a circle around the town, too. But it meant that we were a little more isolated than the people who lived in the town."
        "We didn't have a car; [his_name] had his horse, but he rode her around the farm most days. We wanted to save the tractor fuel for farming, so if I wanted to get to town I had to walk -- or run."
        "I thought it would be pretty useful to be able to get to town (and work) more quickly, so I decided to jog or run when I could."
        "For the first week I could only jog for a minute or so until I got out of breath and had to walk. But I didn't give up. I went to town all the time, so I had plenty of opportunities to practice."
        "Slowly, my running started to improve."
    else:
        "I went for a run around the farm."
    $ skill_physical += 10

    return

# hike to pond with leeches
label physical_1:
    scene bg talam with fade
    "I decided to do some exploring. Here I was, living on a completely new planet, and all I had ever seen was the town and my own little farm. There was a ridge to the south, so I decided to hike over the top and see what was there."
    "The ridge was steeper than it looked, but I was able to scramble up to the top. From the top of the ridge I could see all the way to town to the north, and to the south was a vast expanse of wild rolling hills with sparse shrubs, a few of the taller plants we called trees, and over all the ground the blue-green lichen that seemed to live everywhere on Talam."
    "And, as the ridge descended before me, at its base I could see a grove of trees that looked out-of-place."
    scene bg pond with fade
    show her normal at right
    her "There must be water there!"
    "Sure enough, the stream that ran through the valley formed a pond that the trees drew water from. As I descended the slope, the fragrant smell of new plants reached me. At the bottom, the shade and cool water looked inviting and calm."
    her "Whew...I've been hiking for almost two hours now -- time for a break!"
    "I took off my shoes and socks and dipped my feet in the water. The rocks at the bottom were a little slimy with a strange magenta substance that I assumed was algae, but it still felt good.  I sat down on a rock and took a long drink from the water I brought."
    if (skill_creative >= 20):
        "The pond was so familiar, and yet so distinct from anything I'd seen on Earth, I felt like I had to draw it, so I took out my sketchpad and got to work."
    if (skill_domestic >= 30):
        "I decided to bring some of the sweet-smelling herbs back to the house and see if the scientists had tested their edibility."

    "When I had rested long enough, I started to bring my legs out of the water. However, they were completely numb! They weren't just cold; and they weren't tingly like they had fallen asleep - it felt more like some kind of anaesthesia."
    "I had to use my hands to pull my legs out of the water. I noticed some black spots on them, but when I tried to wipe off the spots..."
    her "It's not mud...are these some kind of leech?!"
    play music "music/Prelude02.ogg" fadeout 1.0

    "I was able to pry it off, and, sure enough, they were attached to my skin with little jaws just like leeches. They must secrete some kind of anesthetic..."
    if (skill_knowledge >= 20):
        "I thought I would bring one back for the scientists to analyze, so after removing it I stuck it in my now-empty water bottle."
    "There must have been twenty or thirty on my legs, and by the time I had removed them all, the sun was setting. When I tried to stand up, my legs wobbled and I splashed back in the pond."
    her "My legs are too numb to walk..."

    if (skill_technical >= 20):
        "Luckily, I brought my radio with me and was able to call for help."
        him "You're over the south ridge? I'll be right there!"
    elif (profession == "doctor"):
        "An adrenaline rush might help counteract the leeches' natural anesthetic..."
        "I don't have any medications with me, but I might be able to get my body to release adrenaline on its own."
        "I imagined all the scariest creatures that had been documented to live on this planet, all converging on the water hole for an evening drink, and I, unable to move, helpless...I breathed quickly to try to bring on my body's natural fight-or-flight response."
        her "HRRRRGH!"
        "I stumbled up the hill, heading north. The sun was setting, but I couldn't enjoy it."
    else:
        "I kept trying to move my legs, and I finally managed a slow sort of crawl away from the pond. It was impossible for me to enjoy the glowing sunset; all I could think of was getting out of there."

    him "[her_name]! [her_name]!"
    her "I'm here!"
    him "Keep talking to me, I'm coming!"
    her "I can't move very well."
    him "It's okay, I'll get you home."
    play music "music/You.ogg" fadeout 1.0
    "I saw [his_name] appear on the top of the ridge. He was riding Lettie, his eyes scanning the landscape fiercely, until he finally saw me."
    "Before I could even explain what had happened, he had picked me up and was holding me close. I rested my head on his chest."
    him "You're safe..."
    her "Thanks for coming for me. I was worried some vicious alien animal was going to come gobble me up, and I've already been nibbled on one too many times this evening."
    him "Don't worry, [her_name], I'm the only one that will be gobbling you up now."
    "He nibbled on my ear playfully, and set me on Lettie. He held my hand all the way home."

    scene bg farm_interior with fade
    "After I had cleaned up and my legs were functioning again, I fell asleep. But the next morning, [his_name] wanted to talk."
    menu:
        him "I don't think it's a good idea for you to go hiking by yourself."
        "Don't tell me what to do.":
            her "Don't tell me what to do."
            him "I'm just saying, who knows what's out there? We don't even know half the creatures on this planet. It's too dangerous."
            her "That's not for you to decide."
            him "Promise me you won't go off by yourself again."
            her "I'm not promising anything!"
            him "Dammit, [her_name], I need you! I need you alive, here with me, not as a carcass torn apart by some alien beast!"
            her "I need you to trust me to make my own decisions."
            him "I...do trust you. Please, be more careful, [her_name]"
            $ loved -= 5
        "Want to come next time?":
            her "Want to come with me next time? We can take a picnic."
            him "Sure, just as long as I don't have to share you with the pond creatures."
            her "Yeah, that would suck."
            him "Ohhhhhhh."
            her "Sorry, that was a bad joke."
        "I'll be more careful.":
            her "I'll be more careful next time."
            him "Next time?! Are you planning on doing that again?!"
            her "Of course. I want to know what's out there, just a few miles from our house. Who knows, maybe I'll find something useful?"
            him "Maybe you'll find something lethal!"
            menu:
                him "Maybe you'll find something lethal!"
                "That's the fun":
                    her "That's the fun of it! It wouldn't be an adventure if it wasn't just a little bit dangerous, would it?"
                    him "You're not indestructible, like some action hero. If you die out there, you can't just load your game and try again."
                    her "You're right; it's not a game. We can't just follow some mini-map to the next plot point; there could be something we need just minutes away from our house that we didn't find because we were too afraid to look."
                    him "I'm not against exploring; I just think we should do it more carefully."
                    her "I'll be careful, but you have to accept that bad things might happen. There are no guarantees that we're the heroes of this story and everything will turn out well for us."
                    him "No, that's true..."
                "Come with me, then.":
                    her "Why don't you come with me next time, then? You can protect me from all the scary monsters out there."
                    him "I...sure. That's a good idea. Just, don't go alone, okay?"
                    her "All right. But neither should you."
                    him "I won't."
                    her "Do we need to pinkie promise?"
                    him "I can think of a better way to seal this promise."
                    "The argument melted away into kisses."
                "Whatever.":
                    her "Whatever. It's not that bad."
                    him "I guess there's no point in trying to convince you, is there? You're never going to listen."
                    $ loved -= 15
        "Maybe you're right.":
            her "Maybe you're right. Don't worry, I'm not planning on any more blood-donation excursions anytime soon."
            him "Thank you, [her_name]. I...need you."
            
    $ loved += 5
    $ skill_physical += 10
    jump events_skip_period
    return

# chopping wood
label physical_2:
    scene bg fields with fade
    "We needed firewood to burn for cooking and heating. I got an axe and split logs to build up a huge supply for later."
    menu:
        him "Wow, I didn't know I married a lumberjack."
        "You're lucky.":
            her "Lucky thing for you, huh? Now you don't have to chop the wood."
            him "Nope, instead I just get to watch you work that beautiful body and get all hot and sweaty."
            her "Hmm, maybe you should chop the wood next time."
            him "No chance! I could sit here and watch you all day."
            her "No, I'm done! Your turn!"
            "He took the axe from me and setup a log. Even though it was getting cold, he took his shirt off and threw it at me."
            her "Ew! I don't want your sweaty shirt!"
            "He flexed his muscles exaggeratedly before setting up a log. I laughed."
            her "Putting on quite the show, aren't you?"
            him "You're my only audience."
            "It was sort of mesmerizing, watching the axe rise with smooth grace and fall with brutal finality. He was quite practiced at chopping wood."
            her "You're pretty good at that."
            him "I'm good at a lot of things."
            her "Mmmm, maybe after dinner you'll show me some more of your...talents."
            him "Only if you show me yours."
            $ loved += 5
            $ made_love += 1
        "Are you disappointed?":
            her "I hope you're not disappointed. I could put on an apron and go fuss around in the kitchen instead."
            him "No, no! Chop away! I'll get dinner ready."
            "Chopping required a surprising amount of concentration. Balance the log at the optimum angle, bring up the axe, aim at the middle of the log, let it down, repeat again."
            "I chopped and chopped until I felt that someone was watching me."
            her "How long have you been watching me?"
            him "Only a few minutes. I was going to tell you that dinner was ready, but I was mesmerized by your hot moves."
            her "I'm chopping wood, not pole dancing!"
            him "That could be good, too."
            her "Well, anyway, thanks for cooking."
            him "Thanks for chopping. That'll help us stay warm for quite a while."
            her "You'll keep me warm for quite a while."
            him "Only forever."
            $ loved += 5
        "This is your job.":
            her "Well, {b}somebody{/b} had to chop wood for the stove, or we'll be having a cold dinner tonight."
            him "Sorry, I've been working on the fields all day."
            her "Firewood is important, too."
            him "Not as important as not starving."
            her "I think we will both starve if we have to eat everything raw. Anyway, I'm almost done."
            him "Speaking of not starving, what's for dinner?"
            menu:
                "What's for dinner?"
                "You're asking {b}me{/b}?!" if (relaxed < 5):
                    her "I hadn't gotten to that yet because I had to chop up all this stupid wood!"
                    "I threw the axe on the ground in a way that probably wasn't good for the axe or the ground, but it felt good."
                    him "I just asked a question, you don't have to throw things around."
                    her "You implied that I should have already started on dinner."
                    him "Well, maybe if you had chopped this wood earlier, you could have."
                    her "Or if {b}you{/b} had done it earlier!"
                    him "You know what? Never mind; I'll just make myself something."
                    $ loved -= 5
                "You tell me.":
                    her "Why don't you tell me?"
                    him "Well, I picked some chard and thought maybe we could add a little salt pork, if that's not too much trouble for you."
                    her "Oh, [his_name], that sounds great, actually.  Thank you."
                "Sorry, I don't know." if (relaxed >= 5):
                    her "I'm sorry, [his_name], I was going to make it earlier, but then I found out we needed more wood, and now it's getting late..."
                    him "Want me to make something? I picked chard today..."
                    her "Oh, that would be great. Thank you, [his_name]."
                    $ loved += 5
                "Get your own dinner.":
                    her "Well, I'm having some leftovers. You can make your own dinner."
                    "I stomped away in a huff and ate by myself. It didn't taste as good as it should have, though."
                    $ loved -= 5
                    

    $ skill_physical += 10

    return

# ditch digging
label physical_3:
    "[his_name] needed a ditch dug for the new field, so I volunteered to help. We dug and dug and dug, and finally, the ditch was finished."
    him "Thanks for your help, [her_name]. You are actually pretty good at shovelling."
    her "Me and my hidden talents..."
    him "Yes, I wonder what else you are hiding?"
    her "Come and find out."
    $ loved += 2
    $ made_love += 1

    $ skill_physical += 10

    return

#Learn how to ride a horse
label physical_4:
    her "[his_name], will you teach me to ride a horse?"
    him "You don't know how?"
    her "I assume there's more to it than just sit and hold the reins."
    him "Well, yeah! There's a lot, actually. But I'd be happy to teach you."
    "We decided that every weekend this month we'd have a riding lesson."
    "I enjoyed learning more about horses and riding Lettie."

    $ skill_physical += 10
    return

#Yoga
label physical_5:
    "On mornings when we had a solar flare warning, or if it was raining, I had to stay indoors."
    "I know Yoga is so 21st century, but my grandma taught me some of the poses when I was young."
    "I've warmed up. How should I do my Yoga workout?"
    menu:
        "Meditate in sitting and prone poses":
            "I spent time sitting and lying down just focusing on my breathing. "
            $ relaxed += 5 
            $ skill_physical += 5
            $ skill_spiritual += 5
            return
        "Practice balancing with long standing poses":
            "I tried to balance on one leg with my upper body in various poses."
            him "I didn't know you knew yoga."
            her "It's good to practice putting your body in different positions."
            him "You don't practice that enough with me?"
            if (relaxed > 0):
                her "We could practice together."
                $ made_love += 1
            else:
                "Yoga is different."
        "Do sun salutations.":
            "I switched rapidly between several poses until I worked up a sweat."
            him "Oh, sweaty [her_nickname], my favorite."
            menu:
                "I feel so gross when I'm sweaty.":
                    her "Not my favorite. I hope I can get to the bath house tonight."
                    him "I'll come with you."
                    menu:
                        "I'd prefer to go by myself tonight.":
                            her "No need, I can take care of cleaning myself by myself."
                        "Looking forward to it.":
                            her "Great. We'll have dessert afterwards."
                            him "I'll try to work up a sweat after the flare to make it worth the trip."
                            $ made_love += 1
                "Oh yeah?":
                    her "You find me sexy like this?"
                    him "Oh yeah. We're stuck inside; we might as well make the most of it."
                    $ made_love += 1
    
    $ skill_physical += 10
    return

# Go hiking again. Find a hot spring. If you bring him, you both enjoy a long soak and feel invigorated. If you don't bring him, you have to decide if you will tell him about it (even though you sort of promised not to hike alone)
label physical_6:
    "I wanted to go hiking again. I just knew there were all sorts of interesting and useful places out there, if only we could find them."
    menu:
        "Should I tell [his_name] about it? He might want to come, too."
        "Tell him":
            her "Hey, [his_nickname], I'm going hiking tomorrow; want to come?"
        "Don't tell him":
            "I didn't tell him; he'd just worry. But I left a note saying where I went. If something went wrong, he'd find the note and know where I went. But if nothing went wrong, I'd be home before him and I could throw the note away before he found it."
        
    $ skill_physical += 10
    return

# Go hunting and bring back some meat
label physical_7:
    "I woke up early and couldn't go back to sleep. All I could think of was how hungry I was for meat."
    "I felt like stealing one of my neighbor's chickens and roasting it, but I knew we needed them more for their eggs."
    "I went to the storehouse and borrowed a large net. I'd done lots of virtual practice on the way over, and I wanted to test my skills."
    menu: 
        "Should I wake up [his_name] to come with me?"
        "Wake him up!":
            her "[his_nickname], I've got a craving for meat. Want to come hunting with me?"
            if loved > 10:
                him "It's so early! But I'd love a change of pace. Let's go!"
                $ he_hunts == True
            else: 
                him "Can I just go back to sleep?"
                her "Yeah, that's fine. Don't worry about me, I'll be careful."
        "Let him sleep.":
            "I left him a message so he wouldn't worry about where I was."
    if (he_hunts == True):
        "We went exploring into the forest where another villager had seen groups of what we called land-lobsters."
        "We found a group of a few of them engaging in whatever their species does instead of sleeping. [his_name] got behind them so he could try to catch one if I missed and it ran away."
        "With [his_name]'s help, we caught five of the land-lobsters. Since they're best fresh, we gave some to our neighbors."
    else: 
        "I went exploring on my own to find land-lobsters."
        "I managed to catch two of the crawly crustaceans. On the way back, I thought I heard a large animal moving in the brush, but I didn't see anything."
        "[his_name] and I enjoyed eating the fresh land crabs as soon as I got back. They were delicious."

    $ loved += 5    
    $ skill_physical += 10
    $ community_level += 2
    return

# Participate in community soccer team
label physical_8:

    $ skill_physical += 10
    $ community_level += 2
    return

label physical_9:

    $ skill_physical += 10
    return

label physical_master:

    $ skill_physical += 10
    return
