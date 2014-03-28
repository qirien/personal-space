# Afternoon Events
# Physical

# Default
label physical_def:
    scene bg path with fade
    "I went for a run around the farm."
    $ skill_physical += 10
    
# Intro Event
label physical_0:
    scene bg farm_exterior with fade
    "We lived a little farther away from the town, so that we had plenty of farmland around us. The other farms were arranged in sort of a circle around the town, too. But it meant that we were a little more isolated than the people who lived in the town."
    "We didn't have a car; [his_name] had his horse, but he rode her around the farm most days. We wanted to save the tractor fuel for farming, so if I wanted to get to town I had to walk -- or run."
    scene bg path with fade
    "I thought it would be pretty useful to be able to get to town (and work) more quickly, so I decided to jog or run when I could."
    "For the first week I could only jog for a minute or so until I got out of breath and had to walk. But I didn't give up. I went to town all the time, so I had plenty of opportunities to practice."
    "Slowly, my running started to improve."
    $ skill_physical += 10

    return

# hike to pond with leeches
label physical_1:
    scene bg talam with fade
    "I decided to do some exploring. Here I was, living on a completely new planet, and all I had ever seen was the town and my own little farm. There was a ridge to the south, so I decided to hike over the top and see what was there."
    "The ridge was steeper than it looked, but I was able to scramble up to the top. From the top of the ridge I could see all the way to town to the north, and to the south was a vast expanse of wild rolling hills with sparse shrubs, a few of the taller plants we called trees, and over all the ground the blue-green lichen that seemed to live everywhere on Talaam."
    "And, as the ridge descended before me, at its base I could see a grove of trees that looked out-of-place."
    show her normal at center with dissolve
    her surprised "There must be water there!"
    "Sure enough, the stream that ran through the valley formed a pond that the trees drew water from. As I descended the slope, the fragrant smell of new plants reached me. At the bottom, the shade and cool water looked inviting and calm."
    play sound "sfx/stream-3.mp3" loop
    scene bg pond with fade
    show her normal at center with dissolve
    her serious "Whew...I've been hiking for almost two hours now -- time for a break!"
    "I took off my shoes and socks and dipped my feet in the water. The rocks at the bottom were a little slimy with a strange magenta substance that I assumed was algae, but it still felt good."
    show her normal at sitting with move
    "I sat down on a rock and took a long drink from the water I brought."
    if (skill_creative >= 20):
        "The pond was so familiar, and yet so distinct from anything I'd seen on Earth, I felt like I had to draw it, so I took out my sketchpad and got to work."
    if (skill_domestic >= 30):
        "I decided to bring some of the sweet-smelling herbs back to the house and see if the scientists had tested their edibility."
    
    show her serious
    "When I had rested long enough, I started to bring my legs out of the water. However, they were completely numb! They weren't just cold; and they weren't tingly like they had fallen asleep - it felt more like some kind of anaesthesia."
    "I had to use my hands to pull my legs out of the water. I noticed some black spots on them, but when I tried to wipe off the spots..."
    her surprised "It's not mud...are these some kind of leech?!"
    play music "music/NoSilencePlease.ogg" fadeout 3.0

    "I was able to pry it off, and, sure enough, they were attached to my skin with little jaws just like leeches. They must secrete some kind of anesthetic..."
    if (skill_knowledge >= 20):
        "I thought I would bring one back for the scientists to analyze, so after removing it I stuck it in my now-empty water bottle."
    "There must have been twenty or thirty on my legs, and by the time I had removed them all, the sun was setting. When I tried to stand up, my legs wobbled and I splashed back in the pond."
    show her concerned with vpunch
    her "My legs are too numb to walk..."
    "Luckily, I had brought my radio with me, so I decided to try and call for help."
    play sound "sfx/radio.mp3"
    her serious "Can anyone hear me? I'm at the south ridge, and I can't walk... please help!"
    her sad "...I repeat, this is [her_name], I'm stuck past the south ridge and need assistance, can anyone hear me?!"
    if (skill_technical >= 20):
        her serious "(The hill must be in the way... but maybe if I angle the antenna a different way... I could also touch this tree to try and send the signal through there!)"
        her "I need help over the south ridge, can anyone hear me?"
        play sound "sfx/radio.mp3"
        him "[her_name]?! Is that you?"
        her normal "Yes! It's me! I need help!"
        him "You're over the south ridge? I'll be right there!"
    elif (profession == "doctor"):
        show her serious
        "An adrenaline rush might help counteract the leeches' natural anesthetic..."
        "I don't have any medications with me, but I might be able to get my body to release adrenaline on its own."
        "I imagined all the scariest creatures that had been documented to live on this planet, all converging on the water hole for an evening drink, and I, unable to move, helpless...I breathed quickly to try to bring on my body's natural fight-or-flight response."
        show her angry at center with move
        show her with vpunch
        her "HRRRRGH!"
        show her serious
        "I stumbled up the hill, heading north. The sun was setting, but I couldn't enjoy it."
    else:
        her concerned "(I guess no one can hear my radio transmission...)"
        "I kept trying to move my legs, and I finally managed a slow sort of crawl away from the pond. It was impossible for me to enjoy the glowing sunset; all I could think of was getting out of there."
    stop sound fadeout 3.0
    scene bg talam with fade
    show her serious at quarterleft
    him "[her_name]! [her_name]!"
    her surprised "I'm here!"
    him "Keep talking to me, I'm coming!"
    her concerned "I can't move very well."
    him "It's okay, I'll get you home."
    play music "music/You.ogg" fadeout 3.0
    show him serious at midright with moveinright
    "I saw [his_name] appear on the top of the ridge. He was riding Lettie, his eyes scanning the landscape fiercely, until he finally saw me."
    show him at midleft with move
    "Before I could even explain what had happened, he had picked me up and was holding me close. I could barely breathe!"
    him serious "You're safe..."
    her normal "Thanks for coming for me. I was worried some vicious alien animal was going to come gobble me up, and I've already been nibbled on one too many times this evening."
    him flirting "Don't worry, [her_name], I'm the only one that will be gobbling you up now."
    "He nibbled on my ear playfully, and set me on Lettie. He held my hand all the way home."

    scene bg farm_interior with fade
    play music "music/Amnesia.ogg" fadeout 3.0
    "After I had cleaned up and my legs were functioning again, I fell asleep. But the next morning, [his_name] wanted to talk."
    show her normal at midright
    show him normal at midleft
    with dissolve
    him annoyed "I don't think it's a good idea for you to go hiking by yourself."
    menu:
        "What should I say?"
        "Don't tell me what to do.":
            her annoyed "Don't tell me what to do."
            him surprised "I'm just saying, who knows what's out there? We don't even know half the creatures on this planet. It's too dangerous."
            her concerned "That's not for you to decide."
            him annoyed "Promise me you won't go off by yourself again."
            her annoyed "I'm not promising anything!"
            him angry "Dammit, [her_name], I need you! I need you alive, here with me, not as a carcass torn apart by some alien beast!"
            her angry "And I need you to trust me to make my own decisions."
            him sad "I...do trust you. But, please, be more careful, [her_name]..."
            $ loved -= 5
        "Want to come next time?":
            her flirting "Want to come with me next time? We can take a picnic."
            him flirting "Sure, just as long as I don't have to share you with the pond creatures."
            her laughing "Yeah, that would suck."
            him annoyed "Ohhhhhhh."
            her normal "Sorry, that was a bad joke."
        "I'll be more careful.":
            her normal "I'll be more careful next time."
            him annoyed "Next time?! Are you planning on doing that again?!"
            her happy "Of course. I want to know what's out there, just a few kilometers from our house. Who knows, maybe I'll find something useful?"
            him angry "Maybe you'll find something lethal!"
            menu:
                "What should I say?"
                "That's the fun":
                    her normal "That's the fun of it! It wouldn't be an adventure if it wasn't just a little bit dangerous, would it?"
                    him serious "You're not indestructible, like some action hero. If you die out there, you can't just load your game and try again."
                    her serious "You're right; it's not a game. We can't just follow some mini-map to the next plot point; there could be something we need just minutes away from our house that we didn't find because we were too afraid to look."
                    him concerned "I'm not against exploring; I just think we should do it more carefully."
                    her serious "I'll be careful, but you have to accept that bad things might happen. There are no guarantees that we're the heroes of this story and everything will turn out well for us."
                    him serious "No, that's true..."
                "Come with me, then.":
                    her flirting "Why don't you come with me next time, then? You can protect me from all the scary monsters out there."
                    him concerned "I...sure. That's a good idea. Just, don't go alone, okay?"
                    her serious "All right. But neither should you."
                    him serious "I won't."
                    her flirting "Do we need to pinkie promise?"
                    him flirting "I can think of a better way to seal this promise."
                    "The argument melted away into kisses."
                "Whatever.":
                    her serious "Whatever. It's not that bad."
                    him sad "I guess there's no point in trying to convince you, is there? You're never going to listen."
                    $ loved -= 15
        "Maybe you're right.":
            her normal "Maybe you're right. Don't worry, I'm not planning on any more blood-donation excursions anytime soon."
            him concerned "Thank you, [her_name]. I...need you."
            
    $ loved += 5
    $ skill_physical += 10
    return

# chopping wood
label physical_2:
    scene bg fields with fade
    show her serious at center with dissolve
    "We needed firewood to burn for cooking and heating. I got an axe and split logs to build up a huge supply for later."
    play sound [ "sfx/wood-logs-1.mp3", "sfx/wood-logs-2.mp3" ]
    show him normal at midleft with moveinleft
    show her at midright with move
    him happy "Wow, I didn't know I married a lumberjack."
    menu:
        "You're lucky.":
            her normal "Lucky thing for you, huh? Now you don't have to chop the wood."
            him flirting "Nope, instead I just get to watch you work that beautiful body and get all hot and sweaty."
            her annoyed "Hmm, maybe you should chop the wood next time."
            him happy "No chance! I could sit here and watch you all day."
            her annoyed "No, I'm done! Your turn!"
            "He took the axe from me and setup a log. Even though it was getting cold, he took his shirt off and threw it at me."
            her angry "Ew! I don't want your sweaty shirt!"
            show him flirting
            "He flexed his muscles exaggeratedly before setting up a log. I laughed."
            show her laughing
            her happy "Putting on quite the show, aren't you?"
            him serious "You're my only audience."
            play sound [ "sfx/wood-logs-1.mp3", "sfx/wood-logs-2.mp3" ]
            "It was sort of mesmerizing, watching the axe rise with smooth grace and fall with brutal finality. He was quite practiced at chopping wood."
            her normal "You're pretty good at that."
            him flirting "I'm good at a lot of things."
            her flirting "Mmmm, maybe after dinner you'll show me some more of your...talents."
            him "Only if you show me yours."
            $ loved += 5
            $ made_love += 1
        "Are you disappointed?":
            her flirting "I hope you're not disappointed. I could put on an apron and go fuss around in the kitchen instead."
            him happy "No, no! Chop away! I'll get dinner ready."
            hide him with moveoutleft
            "Chopping required a surprising amount of concentration. Balance the log at the optimum angle, bring up the axe, aim at the middle of the log, let it down, repeat again."
            play sound [ "sfx/wood-logs-2.mp3", "sfx/wood-logs-1.mp3" ]
            "I chopped and chopped until I felt that someone was watching me."
            show him normal at midleft with moveinleft
            her concerned "How long have you been watching me?"
            him flirting "Only a few minutes. I was going to tell you that dinner was ready, but I was mesmerized by your hot moves."
            her annoyed "I'm chopping wood, not pole dancing!"
            him happy "That could be good, too."
            her normal "Well, anyway, thanks for cooking."
            him normal "Thanks for chopping. That'll help us stay warm for quite a while."
            her flirting "You'll keep me warm for quite a while."
            him flirting "Yeah, for approximately... forever."
            $ loved += 5
        "This is your job.":
            her annoyed "Well, {b}somebody{/b} had to chop wood for the stove, or we'll be having a cold dinner tonight."
            him annoyed "Sorry, I've been working on the fields all day."
            her "Firewood is important, too."
            him "Not as important as not starving."
            her concerned "I think we will both starve if we have to eat everything raw. Anyway, I'm almost done."
            him surprised "Speaking of not starving, what's for dinner?"
            menu:
                "What should I say?"
                "You're asking {b}me{/b}?!" if (relaxed <= 5):
                    her angry "I hadn't gotten to that yet because I had to chop up all this stupid wood!"
                    stop sound
                    play sound "sfx/ice-block-drop-01.mp3"
                    "I threw the axe on the ground in a way that probably wasn't good for the axe or the ground, but it felt good."
                    him annoyed "I just asked a question, you don't have to throw things around."
                    her annoyed "You implied that I should have already started on dinner."
                    him "Well, maybe if you had chopped this wood earlier, you could have."
                    her angry "Or if {b}you{/b} had done it earlier!"
                    him angry "You know what? Never mind; I'll just make my own dinner."
                    $ loved -= 5
                "You tell me.":
                    her annoyed "Why don't you tell me?"
                    him normal "Well, I picked some chard and thought maybe we could add a little salt pork, if that's not too much trouble for you."
                    her normal "Oh, [his_name], that sounds great, actually.  Thank you."
                "Sorry, I don't know." if (relaxed >= 5):
                    her concerned "I'm sorry, [his_name], I was going to make it earlier, but then I found out we needed more wood, and now it's getting late..."
                    him happy "Want me to make something? I picked chard today..."
                    her normal "Oh, that would be great. Thank you, [his_name]."
                    $ loved += 5
                "Get your own dinner.":
                    her angry "Well, I'm having some leftovers. You can make your own dinner."
                    "I stomped away in a huff and ate by myself. It didn't taste as good as it should have, though."
                    $ loved -= 5
                    

    $ skill_physical += 10

    return

# ditch digging
label physical_3:
    scene bg fields with fade
    show him serious at midright
    show her serious at midleft
    with dissolve
    play sound "sfx/shovel.mp3"
    "[his_name] needed a ditch dug for the new field, so I volunteered to help. We dug and dug and dug, and finally, the ditch was finished."
    stop sound fadeout 3.0
    him normal "Thanks for your help, [her_name]. You are actually pretty good at shovelling."
    her flirting "Me and my hidden talents..."
    him flirting "Yes, I wonder what else you are hiding?"
    her "Come and find out."
    $ loved += 2
    $ made_love += 1

    $ skill_physical += 10

    return

#Learn how to ride a horse
label physical_4:
    scene bg barn with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    her surprised "[his_name], will you teach me to ride a horse?"
    him surprised "You don't know how?"
    her normal "I assume there's more to it than just sit and hold the reins."
    him happy "Well, yeah! There's a lot, actually. But I'd be happy to teach you."
    "We decided that every weekend this month we'd have a riding lesson. He started at the very beginning."
    him serious "Now, you can't just jump on Lettie and start riding. Approach her from the left side, and let her get to know you a bit. Try talking to her."
    her surprised "What should I say?"
    him normal "Just like, 'Hey there, good girl' or something. The words don't matter as much as the intent behind them."
    her serious "Why don't the words matter?"
    him serious "Horses are smart - they know if you're scared or nervous. But if you are calm and in charge, Lettie will be calm, too."
    "I didn't even get on Lettie the first lesson. He taught me to saddle and bridle her, and when to brush her and feed her, and what would scare her or annoy her."
    "It was cute to see how much he loved that horse - he knew just what she liked."

    $ skill_physical += 10
    return

#Yoga
label physical_5:
    scene bg farm_interior with fade
    show her serious at center
    play sound "sfx/rain-02.mp3" loop
    "On mornings when we had a solar flare warning, or if it was raining, I had to stay indoors."
    "I know yoga is so 21st century, but my grandma taught me some of the poses when I was young."
    "After warming up I had to decide what to do next."
    menu:
        "What should I do?"
        "Meditate in sitting and prone poses":
            show her sleeping at sitting with move
            "I spent time sitting and lying down just focusing on my breathing. "
            "I felt both more energized, and more relaxed."
            $ relaxed += 5 
            $ skill_physical += 5
            return
        "Practice balancing with long standing poses":
            "I tried to balance on one leg with my upper body in various poses."
            show her at midright with move
            show him normal at midleft with moveinleft
            him surprised "I didn't know you knew yoga."
            her serious "It's good to practice putting your body in different positions."
            him flirting "You don't practice that enough with me?"
            if (relaxed > 0):
                her flirting "We could practice together."
                $ made_love += 1
            else:
                her annoyed "Yoga is different."
        "Do sun salutations.":
            "I switched rapidly between several poses until I worked up a sweat."
            show her at midright with move
            show him at midleft with moveinleft

            him "Ohhh, sweaty [her_nickname], my favorite."
            menu:
                "What should I say?"
                "I feel so gross when I'm sweaty.":
                    her annoyed "Not my favorite. I hope I can get to the bath house tonight."
                    him normal "I'll come with you."
                    menu:
                        "What should I say?"
                        "I'd prefer to go by myself tonight.":
                            her serious "No need, I can take care of cleaning myself by myself."
                        "Looking forward to it.":
                            her flirting "Great. We'll have dessert afterwards."
                            him flirting "I'll try to work up a sweat after the flare to make it worth the trip."
                            $ made_love += 1
                "Oh yeah?":
                    her surprised "You find me sexy like this?"
                    him flirting "Oh yeah. We're stuck inside; we might as well make the most of it."
                    $ made_love += 1
    
    "It felt good to not just sit around while it was raining."
    $ skill_physical += 10
    stop sound
    return

# Go hiking again. Find a hot spring. If you bring him, you both enjoy a long soak and feel invigorated. If you don't bring him, you have to decide if you will tell him about it (even though you sort of promised not to hike alone)
label physical_6:
    scene bg farm_interior with fade
    "I wanted to go hiking again. I just knew there were all sorts of interesting and useful places out there, if only we could find them."
    "Should I tell [his_name] about it? He might want to come, too."
    menu:
        "What should I do?"
        "Tell him":
            show her normal at midright
            show him normal at midleft
            with dissolve
            her "Hey, [his_nickname], I'm going hiking tomorrow; want to come?"
            him "Yeah, I'm all caught up on the farm work here, and that sounds like fun."
            her flirting "And if I run into any ravenous wild animals, I'll be there to protect you."
            him happy "Ha ha, yeah, something like that."
            scene bg mountains with fade
            "We set off towards the mountains to the west, and climbed and climbed all morning long."
            show him normal at quarterleft
            show her normal at left
            with moveinleft
            him surprised "Do you smell that?"
            her surprised "Yeah, it's... sulfur?"
            him happy "There might be a hot spring! Let's follow it!"
            her serious "Sure, but let's make sure it's not full of acid or something before we get in it."
            him normal "Picky, picky."
            hide him with moveoutright
            hide her with moveoutright
            scene bg stream with fade
            play sound "sfx/stream-3.mp3" loop
            "Soon we came to a rocky area by a stream. We saw steam wafting off of a pool of water."
            show her normal at midleft
            show him normal at center
            with moveinleft
            him surprised "Ow! It's {b}really{/b} hot!"
            her surprised "Too hot to dip our feet in?"
            him serious "Yes, it's probably hot enough to boil eggs."
            show her serious
            "The rocks nearby were colorful, especially near the water. We stood admiring them for a few minutes, and then we heard a puffing sound. Steam started billowing from the center of the pool."
            play sound [ "sfx/puff.mp3", "sfx/geyser.mp3" ]
            if (skill_knowledge >= 50):
                her surprised "It's a geyser; get out of the way!"
                "I dragged [his_name] backwards with me as a fountain of steaming hot water shot up into the air from the middle of the pool."
            else:
                her surprised "What's that sound?"
                "Steaming hot water shot upwards into the air from the middle of the pool. We started running away, but some of it landed on our backs."
                her concerned "Ow ow ow!"
                him surprised "Tch, that burns!"
                "Luckily, we weren't burned too badly."
            
            her serious "I didn't know there were geysers here."
            him serious "Well, that could explain why the soil is so good here - maybe this mountain used to be a volcano."
            her normal "It looks really cool."
            him normal "Yeah, now that we don't have to worry about getting cooked!"
            "After a few minutes the geyser died down."
            stop sound fadeout 3.0
            her "Let's look around some more."
            him serious "Sure, but be careful - there might be others."

            scene bg hotspring with fade
            play sound "sfx/stream-3.mp3" loop fadein 1.0
            "We followed the stream up the mountain further, until we found a spot where the stream was deeper and no plants grew around it."
            show her normal at center
            show him normal at midleft
            with moveinleft
            her "This one's not too hot; feels like a bathtub."
            menu:
                "What should we do?"
                "Take a sample to Dr. Lily":
                    her normal "I'll take a sample to Dr. Lily; she can make sure it'd be safe for us to bathe in."
                    him serious "Good idea."
                    stop sound fadeout 3.0
                    "I put some of the water into an old water bottle and we brought it back with us."
                    scene bg lab with fade
                    show lily at midright with dissolve
                    show her at midleft with moveinleft
                    her surprised "Dr. Lily, I found a hot spring up in the mountains; would you mind testing the water for us?"
                    lily "Not a problem. Let me get my pH strips and put some under the microscope..."
                    lily "The water is slightly alkaline, and it has several kinds of minerals in it. I do see some bacteria, however, but they are not a kind we know about, so I don't know if they are dangerous or not."
                    her "Okay, thanks."
                    lily "Thanks for reporting this; our initial scans showed geothermal activity in that area, but you've confirmed it. We may eventually use the springs for energy."
                    $ community_level += 3

                "Try it out":
                    play music "music/Reflections.ogg" fadeout 3.0
                    her normal "It seems fine; I'll try it out."
                    him normal "I'm game!"
                    show her at sitting
                    show him at sitting
                    with move
                    "We stripped down and got in the warm water. The water felt soft and slippery."
                    "There was a slight breeze whispering through the trees, but everything else was quiet."
                    show her sleeping
                    show him sleeping
                    with dissolve
                    if (loved >= 0):
                        "I pulled [his_name] close and squeezed his hand. He nuzzled my neck playfully."
                        $ loved += 2
                    "It was so relaxing..."
                    if (relaxed < 0):
                        $ relaxed = 0
                    else:
                        $ relaxed += 5
                "Look around some more":
                    her "Let's look around some more."
                    him "Okay."
                    "We hiked around and found a few more hot springs of different temperatures; no more geysers, though."
            stop sound fadeout 3.0
            "It was neat to find hot springs and geysers not too far from the house. Maybe they'd be useful to us in the future."

        "Don't tell him":
            "I didn't tell him; he'd just worry. But I left a note saying where I went. If something went wrong, he'd find the note and know where I went. But if nothing went wrong, I'd be home before him and I could throw the note away before he found it."
            scene bg mountains with fade
            "I set off west, towards the mountains, until I found a stream meandering down from them."
            scene bg stream with fade
            show her at center with moveinleft
            play sound "sfx/stream-2.mp3" loop fadein 1.0
            "I followed the stream up the hill until I came to a rocky area with steam coming out of it. It smelled like rotten eggs."
            play sound ["sfx/puff.mp3", "sfx/geyser.mp3" ]
            if (skill_knowledge >= 50):
                her "Looks like there's geothermal activity in this area; I should be careful."
                "Sure enough, as I was looking around, I heard a gurgling sound and steam billowed out of the center of the water."
            else:
                "I heard a gurgling sound and steam billowed out of the center of the water."
            "A geyser erupted into the air as tall as a house. Some of the water sprayed on me."
            her surprised "Ahhh, it's hot!"
            "I stood back to a safe distance and watched the water spray for a few minutes, until it died down."
            her serious "I didn't know they had geysers on this planet! I wonder if there's anything else interesting nearby..."
            "I hiked a little further and found a warm spring"
            her normal "Feels about the same temperature as a bathtub..."
            menu:
                "Take a soak?"
                "Sure, why not?":
                    show her at sitting with move
                    "The water felt soft and slippery."
                    "There was a slight breeze whispering through the trees, but everything else was quiet."
                    her happy "Ahhhhhh..."
                    if (relaxed < 0):
                        $ relaxed = 0
                    else:
                        $ relaxed += 5
                "It could be dangerous...":
                    her concerned "I better not; it could be dangerous."

            stop sound fadeout 3.0
            her normal "The hot spring is a neat find; maybe I should tell [his_name]? But then he'll know I went hiking without him... Maybe I'll tell Dr. Lily; she can see if it's safe for us to use."
            menu:
                "Whom should I tell?"
                "Tell [his_name]":
                    scene bg farm_interior with fade
                    "When I got back, I told [his_name] all about what I had found."
                    show him at midright with dissolve
                    show her at midleft with moveinleft
                    him concerned "That sounds really cool... but I thought we agreed that we shouldn't go hiking alone here."
                    her annoyed "You just proclaimed that; I never agreed to it!"
                    him annoyed "What if you got burned by that geyser?"
                    her angry "I left a note!"
                    him angry "A note isn't going to chase away wild animals or help you if you get hurt!"
                    her annoyed "Well, I guess we just disagree on this."
                    him annoyed "No, you're just wrong."
                    her angry "Whatever."
                "Tell Dr. Lily":
                    scene bg lab with fade
                    show lily at midright with dissolve
                    show her at midleft with moveinleft
                    "When I got back, told Dr. Lily about the place I found. I asked her to keep it a secret that I was the one who found it."
                    lily "This will be very useful! Not only can we harvest minerals from the springs, but the geothermal energy might be useful, too."
                    her surprised "It's not dangerous, right?"
                    lily "What? You mean to soak in? Yes, as long as the temperature is suitable."
                    her normal "That's good to know."
                    her concerned "(I don't think [his_name] will find out...)"
                    $ loved -= 2
                    $ relaxed -= 2
                    $ community_level += 3
                "Don't tell anyone":
                    "I decided not to tell anyone about it - it would be my very own secret spot."
                    $ community_level -= 3
                    $ loved -= 2
    $ skill_physical += 10
    return

# Go hunting and bring back some meat
label physical_7:
    scene bg bedroom with fade
    show her normal at midright
    show him sleeping at midleft
    with dissolve
    show overlay night
    "I woke up early and couldn't go back to sleep. All I could think of was how hungry I was for meat."
    "I felt like stealing one of my neighbor's chickens and roasting it, but I knew we needed them more for their eggs."
    "I'd seen plenty of animals by the river. They didn't look like the tastiest creatures, but at that point I didn't care."
    "I went to the storehouse and borrowed a large net. I'd done lots of virtual practice on the way over, and I wanted to test my skills."
    "Maybe I should wake up [his_name] and ask him to come with me..."
    menu:
        "What should I do?"
        "Wake him up!":
            her normal "Hey, [his_nickname], I've got a craving for meat. Want to come hunting with me?"
            if loved >= 10:
                him annoyed "It's so early!"
                him normal "But I'd love a change of pace. Let's go!"
                $ he_hunts = True
            else: 
                him sad "Can I just go back to sleep?"
                her normal "Yeah, that's fine. Don't worry about me, I'll be careful."
                show him sleeping with dissolve
        "Let him sleep.":
            "I left him a message so he wouldn't worry about where I was."
    scene bg stream with fade
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
    play music "music/Prelude22.ogg" fadeout 3.0
    "Some of the colonists had taken to playing soccer on Saturday mornings. I decided to join them and see if I liked playing."
    scene bg path with fade
    show kid at right
    show brennan at center
    show ilian at quarterright
    show sara at midright
    with dissolve
    show her normal at midleft with moveinleft
    sara "Look out, here comes [her_name]!"
    brennan "You going to join us today?"
    her normal "Yeah, if you don't mind."
    brennan "Sure. Now we can have seven to a side."
    "The teams were very mixed, but they seemed pretty fair, with each side having some kids, and some men and women of varying ages." 
    "The rules were pretty standard, except they had a rule that at least three different people had to touch the ball before making a goal, to encourage teamwork."
    "I hadn't played a lot of soccer, but since I was in pretty good shape I was able to do OK. Still, running up and down the field made me really tired."
    "It was the last quarter of the game and our teams were tied. Brennan passed me the ball, and so I was taking it down towards the goal. I had to pass it to someone, but who?"
    "Sara was really good at making goals, but Ilian hadn't had the ball much, and I was trying to help him get extra practice. They were both open."
    menu:
         "Whom should I pass to?"
         "Sara":
              her serious "Sara! It's yours!"
              "I passed the ball to Sara, who promptly shot it in."
              "We won the game!"
         "Ilian":
              her happy "Ilian! Take it on down!"
              "I passed it to Ilian. Victory was not as important as practice and team spirit."
              "The other team won, but I could tell our team felt strong and happy about how we played."
              $ community_level += 1
         "Keep the ball":
              "I decided to try and shoot it in myself. I managed to make it in, but since three people hadn't touched it yet, it didn't count, and the other team won the game."
              $ community_level -= 1
         
    brennan "Good game, [her_name]"
    "Not only was soccer good exercise, but I feel like it's good for our sense of community, too."
    $ skill_physical += 10
    $ community_level += 2
    return

# Lift heavy ?
label physical_9:
    scene bg barn with fade
    show her normal at midright with dissolve
    "I was rearranging the cellar storage again when [his_name] walked in."
    show him normal at midleft with moveinleft
    him serious "There you are. What's for dinner? I was thinking of picking some spinach but I wanted to check if it would go with whatever we're having."
    her surprised "Oh, um, I guess we could have a spinach salad."
    him surprised "Wow, you completely rearranged everything. Some of these crates are pretty heavy."
    her normal "Yeah, I know it's not much but rearranging all this food just makes me feel productive."
    him surprised "You're just rearranging it all willy-nilly?"
    if ((skill_domestic >=30) or (skill_knowledge >= 30)):
        her flirting "No, don't be silly. I put all the most perishible items in the front, so we'll use them first."
        him happy "Nice."
    else:
        her concerned "No, I've been putting the heavier things on the bottom shelves, where they'll be easier to get."
        him serious "I guess that makes sense."
    if is_pregnant:
        him surprised "You shouldn't be doing heavy lifting while you're pregnant. You've got a heavy enough load as it is."
        menu:
            "Oh, yeah.":
                her concerned "Yeah, you're right. I'll hurt my back if I do much more of this."
                him happy "I'm glad you're feeling up to working though! How about that dinner?"
                her flirting "I'm on it."
            "Ugh, being pregnant is such a pain.":
                her angry "I can't do anything useful when I'm pregnant. What am I supposed to do, sit at home and twiddle my thumbs?"
                him serious "You can still do useful things. You just can't lift heavy objects."
                her annoyed "And I can't have raw anything anymore."
                him happy "Well, you can still go for walks and cook and clean, right?"
                her annoyed "That doesn't sound fun at all!"
                him concerned "I'm sure there's something fun you can do."
                her normal "I guess I can still watch movies and tell jokes."
                him happy "And you can still beat me at space chess!"
                her happy "You bet I can!"
            "I'm not worried.":
                her concerned "I read that when you're pregnant you can still exercise a little as long as you were in shape before you got pregnant."
                him concerned "I don't think that includes heavy lifting."
                her annoyed "If I'm wrong, I'll strain something and have to take it easy for a few days, so what's the big deal?"
                him sad "You could miscarry if you're too stressed."
                her annoyed "Yeah, and if we keep arguing about it I will be stressed."
                him concerned "I just want you to be healthy and happy."
                her serious "And completely bored."
                him serious "You can still hunt and play soccer. I think you'll be fine."
                her flirting "So hunting is better than lifting heavy things?"
                him normal "As long as I come with you!"
    else:
        him normal "I know the Perons just built new shelves in their cellar and want to rearrange their storage, but I haven't had time to help them. Could you do that?"
        her happy "Yes, I sure can!"
        "I spent the next day at the Peron's taking all their vegetables and fruits out of their cellar and then rearranging them. Natalia told me where to put things, and she helped with some of the smaller veggies."
        $ community_level += 1
             
    $ skill_physical += 10
    return

# Lead a group hunt
label physical_master:
    scene bg talam with fade
    play music "music/NoSilencePlease.ogg" fadeout 3.0
    "One week a huge herd of six-legged grazing animals crossed the river near our colony into some wooded scrubland. We were able to hunt some from a distance, but they kept hiding in the bushes where we couldn't see them or get clear shots."
    "They were good to eat, partly because they tasted good dried and salted into jerky. We could always use more food, so I decided to organize a hunt."
    scene bg community_center with fade
    show pavel at midright, behind her with dissolve
    boss "Let's hear [her_name]'s idea, everyone. I hope you give her your full support."
    show her normal at midleft with moveinleft
    her serious "It would be much easier to catch these animals with some help. We need some people to scare the animals out of the scrub and into the open, and some people to wait on the other side and hunt them as they come out."
    "Our brightly colored uniforms stood out clearly from the bushes, and we picked a spot where the startlers would be protected by a hillside after they scared the game."
    "I lined the shooters up carefully so they wouldn't hit each other or anyone else."
    "I had the startlers run up on the animals, banging pots and pans and yelling. Sure enough, the animals skittered out of the brush and into the open."
    play sound "sfx/gunshots.mp3"
    "There were so many animals, it was almost impossible to miss. We shot a good number of them, and then let the rest of the herd go. We wanted them to come back next year."
    "We had a big party where we cooked up a big batch of the critters, and we all worked together to take off their shells and smoke and salt the ones we couldn't eat right away."
    "I felt reassured to know that, even if all the crops failed, we could survive off of local meat for awhile, even if it did sort of remind me of frog legs."

    $ skill_physical += 10
    $ community_level += 10
    return
