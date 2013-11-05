# Month 0 - Aboard the Colony Ship

# After they get married, they board the colony ship
label colony_ship:

    scene bg colony_ship_bunk with fade
    "What a honeymoon -- on board a cramped space shuttle with a hundred other people for a month. Of course, back on Earth four years had passed, since we were travelling so close to light speed. We spent a lot of it talking about the future..."
    play music "music/Amnesia.ogg" fadeout 1.0
    show him normal at midright
    show her normal at midleft
    with dissolve
    him surprised "What do you think about having kids?"
    her flirt "In general, or us specifically?"
    him concerned "You and me, becoming parents. Sounds kind of crazy, doesn't it?"

    # Do they want to have kids right away?
    menu:
        "What should I say?"

        # Want to have kids
        "Not at all.":
            $ want_kids = True
            her normal "I don't think that's crazy. We're both adults; we know we can provide a good home; what more is there to wait for?"
            him happy "Yeah, you're right! I think you'd be a great mom! And...well, I probably wouldn't mess the kids up too much."
            her flirt "You will be a wonderful father, as long as you don't treat the kids the way you treat your horse."
            him surprised "Hey! I'm good to Lettie!"
            her happy "Too good! You'll spoil the kids with treats!"
            $ loved += 5
            $ relaxed += 5

        # Not sure about kids
        "I don't know.":
            $ want_kids = False
            label want_kids_maybe:
                her concerned "Maybe someday, but I don't think I'm ready for that yet."
                him normal "Someday, definitely. Let's just focus on us, for now."
                her flirt "Oh yeah? What part of \"us\" are you focusing on?"
                him flirt "I think...this part right here. Mmmm...this part is good, too."
                her "Don't forget this..."
                him surprised "Ohhh. Wow, I will never forget that."
                scene bg stars with fade
                $ made_love += 1

        # Definitely no kids
        "Really crazy.":
            $ want_kids = False
            her sad "I'm not sure we'd be the best parents."
            him surprised "You don't think so? Can't you just picture me on my horse with a kid in my lap? Maybe a little girl?"
            # Is she sure about that?
            menu:
                "What should I say?"
                "She would probably fall off.":
                    her flirt "She would probably fall off."
                    him annoyed "No way! Lettie would never let anyone fall off her."
                "Maybe...":
                    "(Aww, that does sound kind of cute...)"
                    jump want_kids_maybe

            # Why doesn't she want kids?
            menu: 
                "I thought..."
                "It's not Lettie I'm worried about.":
                    her annoyed "It's not Lettie I'm worried about!"
                    him surprised "You don't trust me?"
                    menu:
                        "\"You don't trust me?\""
                        "That's right":
                            her annoyed "Sorry, I just can't picture you as a father."
                            $ loved -= 5
                            him sad "Oh..."
                            him laughing "I get it, it's hard to believe someone as good-looking as me could ever be a father."
                            her annoyed "Yes, that's exactly right."
                        "I don't trust myself":
                            her sad "No, I'm more worried about me - I don't think I'd be a good mom."
                            him concerned "Oh. Well, for what it's worth, I disagree with you. But, we've got plenty of time. No need to worry about it now."
                        "I don't want to share you":
                            her concerned "I don't want to share you with anyone else just yet."
                            him annoyed "Yeah...that makes sense. I'm not sure how I feel about sharing you with a baby, either."
                            $ loved += 5
                "You've fallen off before":
                    her annoyed "What about that time you fell off and sprained your wrist?"
                    him surprised "That was completely my fault! Lettie had nothing to do with it."

# After talking about having kids
# Background about Talam
    "We talked about lots of other things, of course. We talked about space, about what we would miss from Earth, about what our families were probably doing.  We studied what the pre-colonization team of scientists had reported so far."
    scene bg talam with fade
    "Even though Talam was technically a \"garden planet\", meaning humans could breathe and there were plants and animals, it wasn't very much like modern Earth.  The plants were all quite different, and most of the animals were similar to amphibians or insects."
    "Time on Talam would be different, too: days lasted longer, but a year was only about two-thirds of a year on Earth."
    # TODO: Would this be more exciting with some dialogue?
    "The planet was also a lot less protected from its small Sun, since it was a lot closer.  The building materials we'd brought along would help protect us from solar flares and radiation, but only if we were inside."
    # TODO: Maybe she builds this?
    #"They taught us about the early-warning system they put in place so people would know when it was not safe to be outdoors."

    # He remembers her birthday
    scene bg colony_ship_bunk with fade
    show him normal at center
    show her normal at right
    play music "music/Prelude22.ogg" fadeout 1.0

    "Time felt strange on the ship, too. Though there was no sunrise or sunset, they did dim the lights for ten hours every night. One night I came back to our room and found a surprise waiting for me."

    him happy "Happy Birthday, [her_name]."
    her surprised "What? It's not my birthday!"
    him normal "Actually, according to Earth time you've had two birthdays while we've been travelling, and it seemed sad to let them go by without any sort of celebration, so... Well, it's not much, but I wanted to make sure I didn't forget."
    "He programmed his computer pad to display \"Happy Birthday, [her_name]\", and there's some sort of streamers hanging down from the ceiling. And... is that cake on the table?"
    show her surprised
    menu:
        her "You...used toilet paper for streamers? That's very..."
        "Amazing":
            her happy "amazing! It's so inventive, and I can tell you went to a lot of work just for me."
            him happy "I'm glad you like it. Yeah, it's weird, but what matters is that we do something a little different to celebrate you, right?"
        "Creative":
            her normal "creative. Definitely unexpected; it's very different."
            him annoyed "You're trying to be polite, but I can tell you don't really like it. But, that's okay! What matters is that it's a fun change, right?"
        "Gross":
            her annoyed "...gross. Sorry, but toilet paper hanging from the walls does not really create a festive mood."
            him annoyed "Sorry, I thought you'd think it was funny."
    him normal "Anyway, who cares about the decor? I think you need to open your present!"
    her surprised "A present? Where on earth did you find something?"
    him flirt "Ha ha, not on Earth, that's for sure! Here."
    her surprised "(It's wrapped in tissues...with hearts drawn on them)"
    her normal "(It looks like a poem)"
    "Surrounded by stars, in the darkness of space \nEmptiness presses; the universe waits"
    "Though silently fades the memory of time, \nThere's one special thing I won't leave behind."
    "[her_name], my sweetest lover and friend. \nI'll always be with you, till eternity ends."

    menu:
        "The poem is..."
        "Sweet":
            her happy "Aww, it's sweet, [his_name], thank you."
            him sad "...it's not very good."
            her normal "I like it just how it is."
            him normal "I'm glad, [her_name]. I don't always tell you how much you mean to me, but I hope you know."
        "Sappy":
            her normal "This is very... sweet."
            him concerned "It's too much, isn't it?"
            her happy "Yeah, but I like it anyway. Thank you, [his_name]."
            him happy "You're welcome."
        "...":
            her concerned "..."
            him sad "It's bad, isn't it?"
            her normal "...thank you for thinking of me, [his_name]."
            him concerned "You're welcome. Sorry it's so bad..."
    him surprised "Enough poetry! On to the cake!"
    her surprised "What {b}is{/b} that edible-looking thing on the table, anyway?"
    him normal "Well...it turns out that cake is considered a terrible waste of weight and space by the Food Manager. So there isn't any actual cake. But-"
    her surprised "But?"
    him happy "But I tried to make some out of what I could get. Just taste it, and tell me if it's good!"
    show her concerned
    menu:
        her "(It look like chocolate, but...)"
        "Try it":
            "(It tastes like bread with sugar and chocolate on it. In fact, on closer inspection, I can see that it {b}is{/b} a piece of bread, sprinkled with sugar, and with pieces of chocolate pressed into it.)"
            her normal "This is actually kind of good. Here, try some."
            him normal "Oh, thanks."
        "Don't try it.":
            her concerned "I'm sorry, but I can't eat this."
            him annoyed "C'mon, are you sure? It's just bread and sugar and chocolate..."
            her flirt "You first."
            him "Okay..."
            "He takes a small bite. The texture seems chewy, like bread, and he doesn't cringe at the taste."
            him surprised "It's good! A little too sweet, maybe, but try it!"
            "You gingerly take a bite of the strange \"cake\"."
            her surprised "It's not cake, but it's pretty good."
    her surprised "Where did you get these ingredients, anyway? Usually we only get chocolate once a week."
    him normal "I've been saving them."
    her concerned "This sugar is from our coffee ration, isn't it? You went without sugar, and your weekly chocolate so you could make this for me?"
    him concerned "Well, I couldn't think of any other way to get you something yummy. Sorry it's not much, but happy birthday."
    menu:
        "Thank you, [his_name]":
            her happy "Thank you, [his_name]...it's the best space birthday I've ever had."
            him happy "You're welcome."
        "Happy birthday to you.":
            her normal "Happy birthday to you, too, [his_name]. Now I feel bad I didn't get you anything."
            him flirt "Don't feel bad. You're the only present I need."
        "What's the point?":
            her sad "What's the point of celebrating birthdays? One year older, one year closer to dying...that's not a cause to party."
            him normal "It is if it means it's one more year I've been able to spend with you."
    scene black with fade
    "He pulls you close in a gentle hug, then holds you tightly, as if you would drift off into space without him."
    $ loved += 5
    $ made_love += 1
    $ relaxed += 5
    him normal "[her_name]..."
    jump settling_in

label settling_in:         
    # Land on the planet and get settled
    play music "music/You.ogg" fadeout 1.0
    scene bg talam with fade
    "The first month on Talam was really busy. We arrived at the end of winter, so it was still a bit cold and rainy. We all worked together to get everyone's houses up right away. The first one took the longest, as we had to figure out how to put all the pieces together."
    "Finally, our house was put up. We were so glad to stop sleeping in the shuttle and have our own space."
    scene bg farm_interior with fade
    show her normal at quarterright
    her happy "Well, now instead of feeling like we're sleeping on a train, it will be like camping! Where do you think we should put our sleeping bags?"
    show him normal at quarterleft
    him happy "Well, there's this end- or that end."
    her surprised "How about the end with the stove can be the kitchen, and the other end can be the bedroom?"
    him normal "Sounds fine to me."
    "The house really was pretty small- just one room. One end had a wood-burning/electric hybrid stove/heater as well as a battery that the solar panels could charge, and the other end had a window. No plumbing, electricity only when it was sunny or while our battery lasted, and no furniture other than our sleeping bags and a folding table."
    scene bg bedroom with fade
    show him normal at quarterleft
    show her normal at quarterright
    with dissolve
    "As soon as we got the house up, [his_name] started putting up a piece of paper he unfolded from his bag. When I got closer, I could see it was a picture of his family. I realized I hadn't brought any pictures of my family."
    menu:
        "He's putting up a picture of our family. It's right by our bed."
        "Could you put that somewhere else?":
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
                        "(Slap him)":
                            "That was just too much; I slapped him on the face, harder than I meant to."
                            him surprised "Hey!"
                            her angry "Don't you dare question my commitment to family! I just gave up my world, literally my ACTUAL WORLD, and flew across the universe to be with you! You're my family now!"
                            him angry "And is this how you treat your family? No wonder you didn't bring any pictures of them."
                            "I didn't have an answer to that, so I just left the house and slammed the door. I couldn't decide whether to cry or scream."
                            $ loved -= 5
                            $ relaxed -= 5
                        "(Start crying)":
                            "I started to sob."
                            him concerned "Aww, hey, [her_name], don't cry."
                            her sad "How can you question my commitment to family? I just gave up my whole world and flew across the universe to be with you. {b}You're{/b} my family now."
                            him annoyed "Hey, nobody forced you to come here. I thought you wanted this."
                            "I cried harder."
                            him sad "[her_name]...look, I'm sorry, okay? It's not worth fighting over."
                            her normal "That's true...I'm sorry."
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

    him normal "This was taken at my parents' farm, right before I met you. My sister and her husband and their kids drove for two days to come and visit, and my little brother flew in from overseas"
    him concerned "Good thing, too, because it was the last time we'd all be together."
    her surprised "Have you heard from them lately?"
    him normal "Yeah, they write about once a month, but now that that we've stopped travelling so fast I haven't heard from them at all."
    him sad "My mom was really sick last time my dad wrote to me; she's probably better by now, but it takes so long for messages to get through, so there's no way for me to know."
    her concerned "I'm sorry, [his_name], I didn't know..."
    him normal "It's all right. They're important to me, but you're my family now."
    "We kissed, and looked out the window at the alien hills surrounding our little cabin. It felt surreal, like I was in a movie theatre and any minute the lights would come up and the credits would roll. I held [his_name] tightly; he was here; he was real."
    $ loved += 5
    jump end_settling_in

label end_settling_in:
    # After we land on the planet, we start the monthly routines
    stop music
    jump month01
    return
