# Month 0 - Aboard the Colony Ship

# After they get married, they board the colony ship
label colony_ship:

    scene bg colony_ship_bunk with fade
    play music "music/Amnesia.ogg" fadeout 1.0
    "What a honeymoon -- on board a cramped space shuttle with two hundred other people for a month. Of course, back on Earth four years had passed, since we were travelling so close to light speed."
    "We spent a lot of it talking about the future..."
    show him normal at midright
    show her normal at midleft
    with dissolve
    him surprised "So, [her_nickname], what do you think about having kids?"
    her flirt "In general, or us specifically?"
    him concerned "You and me, becoming parents. Sounds kind of crazy, doesn't it?"

    # Do they want to have kids right away?
    menu:
        "What should I say?"

        # Want to have kids
        "That doesn't sound crazy.":
            $ want_kids = True
            her normal "I don't think that's crazy. We're both adults; we know we can provide a good home; what more is there to wait for?"
            him happy "Yeah, you're right! I think you'd be a great mom! And...well, I probably wouldn't mess the kids up too much."
            her flirt "You will be a wonderful father, as long as you don't treat the kids the way you treat your horse."
            him surprised "Hey! I'm good to Lettie!"
            her happy "Too good! You'll spoil the kids with treats!"
            $ loved += 5

        # Not sure about kids
        "I don't know.":
            $ want_kids = False
            label want_kids_maybe:
                her concerned "I don't think I'm ready for that yet."
                him surprised "Really? What are you waiting for?"
                menu:
                    "What should I say?"
                    "When we get to Talaam.":
                        $ want_kids = True
                        her normal "I at least want to be on a planet, not hurtling through the air. I mean, have they done studies on the effects of near-light speed travel on fetuses?"
                        him surprised "Probably not. I hadn't thought of that. Though Pete and Helen just had their baby, and he seems fine."
                    "When everything's settled.":
                        $ want_kids = True
                        her serious "Maybe when we've got things figured out on Talaam. Who knows what it will be like there?"
                        him serious "Yeah... but what if we never get everything figured out?"
                        her annoyed "Not everything! Just food, clothing, shelter - I want to make sure we can provide for a kid."
                        him serious "Yeah, that makes sense."
                    "Maybe never.":
                        her serious "Maybe never. I'm not sure if I want kids at all."
                        him surprised "Really? I always thought you wanted a family."
                        her concerned "There's been so many changes lately - we just barely got married, we're moving to a new planet - I can't even think about adding another change right now."
                        him normal "Okay, let's just focus on us, for now."
                        her flirt "Oh yeah? What part of \"us\" are you focusing on?"
                        show him at center with move
                        him flirting "I think...this part right here. Mmmm...this part is good, too."
                        her "Don't forget this..."
                        him surprised "Ohhh. Wow, I will never forget that."
                        scene bg stars with fade
                        $ made_love += 1

        # Definitely no kids
        "That's really crazy.":
            $ want_kids = False
            her sad "I'm not sure we'd be the best parents."
            him surprised "You don't think so? Can't you just picture me on my horse with a kid in my lap? Maybe a little girl?"
            # Is she sure about that?
            menu:
                "What should I say?"
                "She would probably fall off.":
                    her flirt "She would probably fall off."
                    him annoyed "No way! Lettie would never let anyone fall off her."
                    her annoyed "It's not Lettie I'm worried about!"
                    him surprised "You don't trust me?"
                    menu:
                        "What should I say?"
                        "That's right.":
                            her annoyed "Sorry, I just can't picture you as a father."
                            $ loved -= 5
                            him sad "Oh..."
                            him laughing "I get it, it's hard to believe someone as good-looking as me could ever be a father."
                            her annoyed "Yes, that's exactly right."
                        "I don't trust myself.":
                            her sad "No, I'm more worried about me - I don't think I'd be a good mom."
                            him concerned "Oh. Well, for what it's worth, I disagree with you. But, we've got plenty of time. No need to worry about it now."
                        "I don't want to share you.":
                            her concerned "I don't want to share you with anyone else just yet."
                            him serious "Yeah...that makes sense. I'm not sure how I feel about sharing you with a baby, either."
                            $ loved += 5

                "That does sound kind of cute...":
                    her normal "(That does sound kind of cute, but...)"
                    jump want_kids_maybe

# After talking about having kids
    "We talked about lots of other things, of course. We talked what we would miss from Earth, and what our families were probably doing.  We studied what the pre-colonization team of scientists had reported so far."
# Background about Talaam
    scene bg talaam_space with fade
    "Even though Talaam was technically a \"garden planet\", meaning humans could breathe and there were plants and animals, it was only superficially like modern Earth.  The plants looked similar, but had completely different biologies, and most of the animals were more like prehistoric amphibians or insects."
    "Time on Talaam would be different, too: days lasted longer, but a year was only about two-thirds of a year on Earth."
    "The planet was also a lot less protected from its small sun, since it was closer than Earth.  The building materials we'd brought along would help protect us from solar flares and radiation, but only if we were inside."
    "That's why they had setup a warning system to tell everyone when a solar flare was coming."

    # He remembers her birthday
    scene bg colony_ship_bunk with fade
    play music "music/Prelude22.ogg" fadeout 1.0

    "Time felt strange on the ship, too. Though there was no sunrise or sunset, they did dim the lights for ten hours every night. One night I came back to our room and found a surprise waiting for me."
    show him normal at midleft with dissolve
    show her normal at midright with moveinright
    him happy "Happy Birthday, [her_name]."
    her surprised "What? It's not my birthday!"
    him normal "Actually, according to Earth time you've had two birthdays while we've been travelling, and it seemed sad to let them go by without any sort of celebration, so... Well, it's not much, but I wanted to make sure I didn't forget."
    "He programmed his computer pad to display \"Happy Birthday, [her_name]\", and there's some sort of streamers hanging down from the ceiling. And... is that cake on the table?"
    her surprised "You...used toilet paper for streamers?"
    menu:
        "What should I say?"
        "That's amazing.":
            her happy "That's amazing! It's so inventive, and I can tell you went to a lot of work just for me."
            him happy "I'm glad you like it. Yeah, it's weird, but what matters is that we do something a little different to celebrate you, right?"
        "That's very...creative.":
            her serious "That's...creative. Definitely unexpected; it's very different."
            him annoyed "You're trying to be polite, but I can tell you don't really like it. But, that's okay! What matters is that it's a fun change, right?"
        "That's just gross.":
            her annoyed "That's...gross. Sorry, but toilet paper hanging from the walls does not really create a festive mood."
            him annoyed "Sorry, I thought you'd think it was funny."
            $ loved -= 2
    him normal "Anyway, who cares about the decor? I think you need to open your present!"
    her surprised "A present? Where on earth did you find something?"
    him flirting "Ha ha, not on Earth, that's for sure! Here."
    her surprised "(It's wrapped in a handkerchief...It looks like a poem.)"
    note "{size=+3}Surrounded by stars, in the darkness of space \nEmptiness presses; the universe waits{/size}"
    note "{size=+3}Though silently fades the memory of time, \nThere's one special thing I won't leave behind.{/size}"
    note "{size=+3}[her_name], my sweetest lover and friend. \nI'll always be with you, till eternity ends.{/size}"
    note "{size=+3}\nlove on your birthday and always,\nyour [his_name]{/size}"
    nvl clear

    menu:
        "The poem is..."
        "Sweet.":
            her happy "Aww, it's sweet, [his_name], thank you."
            him sad "...it's not very good."
            her normal "I like it just how it is."
            him normal "I'm glad, [her_name]. I don't always tell you how much you mean to me, but I hope you know."
            $ loved += 2
        "Sappy.":
            her concerned "This is very... sweet."
            him concerned "It's too much, isn't it?"
            her happy "Yeah, but I like it anyway. Thank you, [his_name]."
            him happy "You're welcome."
            $ loved += 2
        "Awful.":
            her concerned "..."
            him sad "It's bad, isn't it?"
            her normal "...thank you for thinking of me, [his_name]."
            him concerned "You're welcome. Sorry it's so bad..."
            $ loved -= 2
    him happy "Enough poetry! On to the cake!"
    her surprised "What {b}is{/b} that edible-looking thing on the table, anyway?"
    him normal "Well...it turns out that cake is considered a terrible waste of weight and space. So there isn't any actual cake. But-"
    her surprised "But?"
    him happy "But I tried to make some out of what I could get. Just taste it, and tell me if it's good!"
    her concerned "(It looks like chocolate, but...)"
    menu:
        "What should I do?"
        "Try it":
            "(It tastes like bread with sugar and chocolate on it. In fact, it {b}is{/b} a piece of bread, sprinkled with sugar, and with pieces of chocolate pressed into it.)"
            her normal "This is actually kind of good. Here, try some."
            him normal "Oh, thanks."
            $ loved += 2
        "Don't try it.":
            her concerned "I'm sorry, but I can't eat this."
            him annoyed "C'mon, are you sure? It's just bread and sugar and chocolate..."
            her flirt "You first."
            him "Okay..."
            "He takes a small bite. The texture seems chewy, like bread, and he doesn't cringe at the taste."
            him surprised "It's good! A little too sweet, maybe, but try it!"
            "You gingerly take a bite of the strange \"cake\"."
            her surprised "It's not cake, but it's pretty good."
            $ loved -= 2
    her surprised "Where did you get these ingredients, anyway? Usually we only get chocolate once a week."
    him normal "I've been saving them."
    her concerned "This sugar is from our coffee ration, isn't it? You went without sugar, and your weekly chocolate so you could make this for me?"
    him concerned "Well, I couldn't think of any other way to get you something yummy. Sorry it's not much, but happy birthday."
    menu:
        "Thank you, [his_name].":
            her happy "Thank you, [his_name]...it's the best space birthday I've ever had."
            him happy "You're welcome."
        "Happy birthday to you.":
            her normal "Happy birthday to you, too, [his_name]. Now I feel bad I didn't get you anything."
            him flirting "Don't feel bad. You're the only present I need."
        "What's the point?":
            her sad "What's the point of celebrating birthdays? One year older, one year closer to dying...that's not a cause to party."
            him normal "It is if it means it's one more year I've been able to spend with you."
            $ relaxed -= 5
    scene bg stars with fade
    "He pulled me close in a gentle hug, then held me tightly, as if I would drift off into space without him."
    $ made_love += 1
    $ relaxed += 2
    $ loved += 2
    him normal "[her_name]..."
    jump settling_in

label settling_in:         
    # Land on the planet and get settled
    #scene bg talaam_space with CropMove(1.0, "slideleft")
    scene talaam-approach:
        #size (1024,600) crop (0,0,1920,1079)
        crop (0,0,1024,600)
        easein 10.0 crop (884, 272, 1024, 600)
        #easein 5.0 crop (480,240, 1024, 600) 
        #easein 5.0 crop (776, 452, 386, 226)
        
    play music "music/You.ogg" fadeout 1.0        
    "Finally, we arrived."
    "The first month on Talaam was really busy. We arrived at the end of winter, so it was cold and rainy. We all worked together to get everyone's houses up right away. The first one took the longest, as we had to figure out how to put all the pieces together."
    "But when I looked at the map of the colony's layout, our farm was at the very edge."
    scene bg talam with fade    
    show her normal at midright
    show him normal at midleft
    with dissolve
    her annoyed "Why is our house so far from everyone else?"
    him serious "I picked this spot on purpose. It's close enough that you can walk to work easily, but far enough away that we have plenty of room."
    her surprised "Room for what?"
    him normal "Room to grow! Room to breathe! Room to do whatever we want! We can yodel, or have loud parties, or make love in the backyard, or do anything we want! No nosy neighbors!"
    her annoyed "Yeah, but you're not the one who has to walk two kilometers to work every day..."
    him normal "I think you'll like it. There's no room for a big farm in town, anyway."
    her concerned "I guess you're right."
    "Finally, our house was put up. We were so glad to stop sleeping in the shuttle and have our own space."
    scene bg farm_exterior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    him happy "Here it is! Home, sweet home!"
    her happy "This might actually work!"
    him normal "Come on inside, let's setup our stuff."
    scene bg farm_interior with fade
    show her normal at quarterright
    show him normal at quarterleft
    with dissolve
    her serious "Not bad, not bad..."
    him happy "Isn't it awesome?! It's so small, it'll be easy to clean. And it's cozy, for just the two of us."
    "The house really was pretty small- just one room. One end had a biomass/electric hybrid stove/heater as well as a battery that the solar panels could charge, and the other end had a window."
    "There was no plumbing, electricity only when it was sunny or while our battery lasted, and no furniture other than our bunk and a folding table."
    her flirt "Good thing we didn't waste any space on frivolous things like bathrooms."
    him serious "The outhouse is not that far!"
    her serious "It'll work. It will just be kind of like camping. Where do you think we should put our bed?"
    him happy "Well, there's this end- or that end."
    her normal "How about the end with the stove can be the kitchen, and the other end can be the bedroom?"
    him normal "Sounds fine to me."
    scene bg bedroom with fade
    show him normal at quarterleft
    show her normal at quarterright
    with dissolve
    "We dragged in our bunk from the shuttle and put our bedding on it."
    "Afterwards, [his_name] started putting up a piece of paper he unfolded from his bag. When I got closer, I could see it was a picture of his family. I realized I hadn't brought any pictures of my family."
    "He put it right next to his side of the bed."
    menu:
        "What should I say?"
        "Could you put that somewhere else?":
            $ loved -= 2
            her concerned "[his_name], do you think you could put that somewhere else? I don't really want to stare at your parents when we're making love."
            him annoyed "Where else should I put it? There's not a lot of room, and I don't want it to catch fire near the stove."
            her annoyed "I don't know; anywhere else!"
            him annoyed "Fine."
            "He moved it to another wall. It was still near the bed, but not where I had to see it all the time."
            him annoyed "Is that better?"
            menu:
                "Was it better?"
                "Yes.":
                    her annoyed "Yes."
                    him annoyed "..."
                "Yes, thank you.":
                    her normal "Yes, thank you."
                    him normal "You're welcome."
                "Don't get mad at me.":
                    $ loved -= 5
                    her annoyed "Don't get so mad; it's just a picture."
                    him annoyed "Yeah, well, it's important to me. How come you don't have a picture to hang up?"
                    her annoyed "I guess I only made room for the most important things."
                    him angry "What could be more important than your family?!"
                    her angry "Hey, family's important to me, too!"
                    him concerned "We'll see."
                    menu:
                        "That wasn't fair."
                        "(Slap him.)":
                            "That was just too much; I slapped him on the face, harder than I meant to."
                            him surprised "Hey!"
                            her angry "Don't you dare question my commitment to family! I just gave up my world, literally my ACTUAL WORLD, and flew across the universe to be with you! You're my family now!"
                            him angry "And is this how you treat your family? No wonder you didn't bring any pictures of them."
                            "I didn't have an answer to that, so I just left the house and slammed the door. I couldn't decide whether to cry or scream."
                            $ loved -= 5
                            $ relaxed -= 5
                        "(Start crying.)":
                            show her sad
                            "I started to sob."
                            him concerned "Aww, hey, [her_name], don't cry."
                            her concerned "How can you question my commitment to family? I just gave up my whole world and flew across the universe to be with you. {b}You're{/b} my family now."
                            him annoyed "Hey, nobody forced you to come here. I thought you wanted this."
                            "I cried harder."
                            show her sad
                            him sad "[her_name]...look, I'm sorry, okay? It's not worth fighting over."
                            her serious "That's true...I'm sorry."
                            $ loved += 2
                            $ relaxed -= 2
                        "Why did you even marry me?":
                            her angry "Do you really think that? Why would you have married me if you thought that?"
                            him annoyed "No, I don't really think that, I just- sometimes it seems like other things are more important to you."
                            her annoyed "Well, they're not. You're my family now."
                            him normal "Okay, well, you're my family, but they still are, too, even if I never see them again."
                            her normal "Okay."
                            $ relaxed -= 2
                            
                    jump end_settling_in
            
        "When was this taken?":
            her surprised "When was this taken?"
        "Do you miss them a lot?":
            her surprised "Do you miss them a lot?"
            him sad "A bit."

    him normal "This was taken at my parents' farm a few years ago. My sister and her husband and their kids drove for two days to come and visit, and my little brother flew in from overseas."
    him concerned "Good thing, too, because it was the last time we'd all be together."
    her surprised "Have you heard from them lately? I know they wrote you a lot on the shuttle..."
    him normal "They write me all the time, but the messages took longer and longer to reach us, so I haven't heard from them for a few months."
    her sad "How's your mom? I know she was sick..."
    him sad "She's probably better by now, but it takes so long for messages to get through, there's no way to know for sure."
    her concerned "I'm sorry, [his_name], I didn't know..."
    him normal "It's all right. They're important to me, but you're my family now."
    show him serious at center with move
    show her serious at midright with move
    "We kissed, and looked out the window at the alien hills surrounding our little cabin. It felt surreal, like I was in a movie theatre and any minute the lights would come up and the credits would roll. I held [his_name] tightly; he was here; he was real."
    $ loved += 2
    jump end_settling_in

label end_settling_in:
    # After we land on the planet, we start the monthly routines
    stop music fadeout 5.0
    scene black with fade
    "Once we arrived, we soon settled into a routine. Every day he would work on the farm while I worked as a [profession]. I had a little free time after work, and then we ate dinner together. After dinner we tried to relax, mostly."
    "There were plenty of things I could choose to do in my free time, but I usually chose just one or two to focus on. I didn't have to be good at everything; I wanted to get really good at a few things."
    "But maybe if I had made different choices... \nWould things be different?"
    "Did all those little decisions really matter? At least some of them did..."
        
    jump month01
    return
