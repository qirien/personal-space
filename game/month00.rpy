# Month 0 - Aboard the Colony Ship

# After they get married, they board the colony ship
label colony_ship:

    play music "music/Amnesia.ogg" fadeout 1.0
    scene bg colony_ship_bunk
    show him normal at center
    show her normal at right
    "What a honeymoon -- on board a cramped space shuttle with a hundred other people for a month. Of course, back on Earth four years had passed, since we were travelling so close to light speed. We spent a lot of it talking about the future..."
    him "What do you think about having kids?"
    her "In general, or us specifically?"
    him "You and me, becoming parents. Sounds kind of crazy, doesn't it?"

    # Do they want to have kids right away?
    menu:
        "\"Sounds kind of crazy, doesn't it?\""

        # Want to have kids
        "Not at all.":
            $ want_kids = True
            her "I don't think that's crazy. We're both adults; we know we can provide a good home; what more is there to wait for?"
            him "Yeah, you're right! I think you'd be a great mom! And...well, I probably wouldn't mess the kids up too much."
            her "You will be a wonderful father, as long as you don't treat the kids the way you treat your horse."
            him "Hey! I'm good to Lettie!"
            her "Too good! You'll spoil the kids with treats!"

        # Not sure about kids
        "I don't know.":
            $ want_kids = False
            label want_kids_maybe:
                her "Maybe someday, but I don't think I'm ready for that yet."
                him "Someday, definitely. Let's just focus on us, for now."
                her "Oh yeah? What part of \"us\" are you focusing on?"
                him "I think...this part right here. Mmmm...this part is good, too."
                her "Don't forget this..."
                him "Ohhh. Wow, I will never forget that."
                $ made_love += 1
                # TODO: is this TMI?

        # Definitely no kids
        "Really crazy.":
            $ want_kids = False
            her "I'm not sure we'd be the best parents."

            # Is she sure about that?
            menu:
                him "You don't think so? Can't you just picture me on my horse with a kid in my lap? Maybe a little girl?"
                "She would probably fall off.":
                    her "She would probably fall off."
                    him "No way! Lettie would never let anyone fall off her."
                "Maybe...":
                    "(Aww, that does sound kind of cute...)"
                    jump want_kids_maybe

            # Why doesn't she want kids?
            menu: 
                "I thought..."
                "It's not Lettie I'm worried about.":
                    her "It's not Lettie I'm worried about!"
                    him "You don't trust me?"
                    menu:
                        "\"You don't trust me?\""
                        "That's right":
                            her "Sorry, I just can't picture you as a father."
                            #show him sad
                            him "Oh..."
                            #show him laughing
                            him "I get it, it's hard to believe someone as good-looking as me could ever be a father."
                            her "Yes, that's exactly right."
                        "I don't trust myself":
                            her "No, I'm more worried about me - I don't think I'd be a good mom."
                            him "Oh. Well, for what it's worth, I disagree with you. But, we've got plenty of time. No need to worry about it now."
                        "I don't want to share you":
                            her "I don't want to share you with anyone else just yet."
                            him "Yeah...that makes sense. I'm not sure how I feel about sharing you with a baby, either."
                "What about you?":
                    her "What about that time you fell off and sprained your wrist?"
                    him "That was completely my fault! Lettie had nothing to do with it."

# After talking about having kids
# Background about Talam
    "We talked about lots of other things, of course. We talked about space, about what we would miss from Earth, about what our families were probably doing.  We studied what the pre-colonization team of scientists had reported so far."
    scene bg talam
    "Even though Talam was technically a \"garden planet\", meaning humans could breathe and there were plants and animals, it wasn't very much like modern Earth.  There were a lot of sandy areas with little vegetation, and there were reports of some large, dangerous creatures that lived in the water."
    # TODO: Would this be more exciting with some dialogue?
    "The planet was also a lot less protected from its small Sun, since it was a lot closer.  The building materials we'd brought along would help protect us from solar flares and radiation, but only if we were inside. They taught us about the early-warning system they put in place so people would know when it was not safe to be outdoors."

    # He remembers her birthday
    scene bg colony_ship_bunk
    show him normal at center
    show her normal at right
    play music "music/Prelude22.ogg" fadeout 1.0

    "Time felt strange on the ship, too. Though there was no sunrise or sunset, they did dim the lights for ten hours every night. One night I came back to our room and found a surprise waiting for me."

    him "Happy Birthday, [her_name]."
    her "What? It's not my birthday!"
    him "Actually, according to Earth time you've had two birthdays while we've been travelling, and it seemed sad to let them go by without any sort of celebration, so... Well, it's not much, but I wanted to make sure I didn't forget."
    "He programmed his computer pad to display \"Happy Birthday, [her_name]\", and there's some sort of streamers hanging down from the ceiling. And... is that cake on the table?"
    menu:
        her "You...used toilet paper for streamers? That's very..."
        "Amazing":
            her "amazing! It's so inventive, and I can tell you went to a lot of work just for me."
            him "I'm glad you like it. Yeah, it's weird, but what matters is that we do something a little different to celebrate you, right?"
        "Creative":
            her "creative. Definitely unexpected; it's very different."
            him "You're trying to be polite, but I can tell you don't really like it. But, that's okay! What matters is that it's a fun change, right?"
        "Gross":
            her "...gross. Sorry, but toilet paper hanging from the walls does not really create a festive mood."
            him "Sorry, I thought you'd think it was funny."
    him "Anyway, who cares about the decor? I think you need to open your present!"
    her "A present? Where on earth did you find something?"
    him "Ha ha, not on Earth, that's for sure! Here."
    her "(It's wrapped in tissues...with hearts drawn on them)"
    her "(It looks like a poem)"
    "Surrounded by stars, in the darkness of space \nEmptiness presses; the universe waits"
    "Though silently fades the memory of time, \nThere's one special thing I won't leave behind."
    "[her_name], my sweetest lover and friend. \nI'll always be with you, till eternity ends."

    menu:
        "The poem is..."
        "Sweet":
            her "Aww, it's sweet, [his_name], thank you."
            him "...it's not very good."
            her "I like it just how it is."
            him "I'm glad, [her_name]. I don't always tell you how much you mean to me, but I hope you know."
        "Sappy":
            her "This is very... sweet."
            him "It's too much, isn't it?"
            her "Yeah, but I like it anyway. Thank you, [his_name]."
            him "You're welcome."
        "...":
            her "..."
            him "It's bad, isn't it?"
            her "...thank you for thinking of me, [his_name]."
            him "You're welcome. Sorry it's so bad..."
    him "Enough poetry! On to the cake!"
    her "What {b}is{/b} that edible-looking thing on the table, anyway?"
    him "Well...it turns out that cake is considered a terrible waste of weight and space by the Food Manager. So there isn't any actual cake. But-"
    her "But?"
    him "But I tried to make some out of what I could get. Just taste it, and tell me if it's good!"
    menu:
        her "(It look like chocolate, but...)"
        "Try it":
            #TODO is this second-person instead of first-person awkward?
            "(It tastes like bread with sugar and chocolate on it. In fact, on closer inspection, you can see that it {b}is{/b} a piece of bread, sprinkled with sugar, and with pieces of chocolate pressed into it.)"
            her "This is actually kind of good. Here, try some."
            him "Oh, thanks."
        "Don't try it.":
            her "I'm sorry, but I can't eat this."
            him "C'mon, are you sure? It's just bread and sugar and chocolate..."
            her "You first."
            him "Okay..."
            "He takes a small bite. The texture seems chewy, like bread, and he doesn't cringe at the taste."
            him "It's good! A little too sweet, maybe, but try it!"
            "You gingerly take a bite of the strange \"cake\"."
            her "It's not cake, but it's pretty good."
    her "Where did you get these ingredients, anyway? Usually we only get chocolate once a week."
    him "I've been saving them."
    her "This sugar is from our coffee ration, isn't it? You went without sugar, and your weekly chocolate so you could make this for me?"
    him "Well, I couldn't think of any other way to get you something yummy. Sorry it's not much, but happy birthday."
    menu:
        "Thank you, [his_name]":
            her "Thank you, [his_name]...it's the best space birthday I've ever had."
        "Happy birthday to you.":
            her "Happy birthday to you, too, [his_name]. Now I feel bad I didn't get you anything."
        "What's the point?":
            her "What's the point of celebrating birthdays? One year older, one year closer to dying...that's not a cause to party."
            him "It is if it means it's one more year I've been able to spend with you."
    "He pulls you close in a gentle hug, then holds you tightly, as if you would drift off into space without him."
    him "[her_name]..."
            
    # Land on the planet and get settled
    play music "music/You.ogg" fadeout 1.0
    scene bg talam
    "The first month on Talam was really busy. Luckily, we arrived in the dry season, so the weather was sunny and clear and the nights were not too cold. We all worked together to get everyone's houses up right away. The first one took the longest, as we had to figure out how to put all the pieces together."
    "Finally, our house was put up. We were so glad to stop sleeping in the shuttle and have our own space."
    scene bg farm_interior
    show her normal at right
    her "Well, now instead of feeling like we're sleeping on a train, it will be like camping! Where do you think we should put our sleeping bags?"
    show him normal at left
    him "Well, there's this end- or that end."
    her "How about the end with the stove can be the kitchen, and the other end can be the bedroom?"
    him "Sounds fine to me."
    "The house really was pretty small- just one room. One end had a wood-burning/electric hybrid stove/heater as well as a battery that the solar panels could charge, and the other end had a window. No plumbing, electricity only when it was sunny or while our battery lasted, and no furniture other than our sleeping bags and a folding table."
    "As soon as we got the house up, [his_name] started putting up a piece of paper he unfolded from his bag. When I got closer, I could see it was a picture of his family. I realized I hadn't brought any pictures of my family."
    menu:
        "He's putting up a picture of our family. It's right by our bed."
        "Could you put that somewhere else?":
            her "[his_name], do you think you could put that somewhere else? I don't really want to stare at your parents when we're making love."
            him "Where else should I put it? There's not a lot of room, and I don't want it to catch fire near the stove."
            her "I don't know; anywhere else!"
            him "Fine."
            "He moved it to another wall. It was still near the bed, but not where I had to see it all the time."
            him "Is that better?"
            menu:
                "Was it better?"
                "Yes.":
                    her "Yes."
                "Yes, thank you.":
                    her "Yes, thank you."
                    him "You're welcome."
                "Don't get mad at me.":
                    $ loved -= 5
                    her "Don't get so mad; it's just a picture."
                    him "Yeah, well, it's important to me. How come you don't have a picture to hang up?"
                    her "I guess I only made room for the most important things."
                    him "What could be more important than your family?!"
                    her "Hey, family's important to me, too!"
                    him "We'll see."
                    menu:
                        "That wasn't fair."
                        "(Slap him)":
                            "That was just too much; I slapped him on the face, harder than I meant to."
                            him "Hey!"
                            her "Don't you dare question my commitment to family! I just gave up my world, literally my ACTUAL WORLD, and flew across the universe to be with you! You're my family now!"
                            him "And is this how you treat your family? No wonder you didn't bring any pictures of them."
                            "I didn't have an answer to that, so I just left the house and slammed the door. I couldn't decide whether to cry or scream."
                            $ loved -= 5
                            $ relaxed -= 5
                        "(Start crying)":
                            "I started to sob."
                            him "Aww, hey, [her_name], don't cry."
                            her "How can you question my commitment to family? I just gave up my whole world and flew across the universe to be with you. {b}You're{/b} my family now."
                            him "Hey, nobody forced you to come here. I thought you wanted this."
                            "I cried harder."
                            him "[her_name]...look, I'm sorry, okay? It's not worth fighting over."
                            her "That's true...I'm sorry."
                        "Why did you even marry me?":
                            her "Do you really think that? Why would you have married me if you thought that?"
                            him "No, I don't really think that, I just- sometimes it seems like other things are more important to you."
                            her "Well, they're not. You're my family now."
                            him "Okay, well, you're my family, but they still are, too, even if I never see them again."
                            her "Okay."
                            
            return
            
        "When was this taken?":
            her "When was this taken?"
        "Do you miss them a lot?":
            her "Do you miss them a lot?"

    him "This was taken at my parents' farm, right before I met you. My sister and her husband and their kids drove for two days to come and visit, and my little brother flew in from overseas. Good thing, too, because it was the last time we'd all be together."
    her "Have you heard from them lately?"
    him "Yeah, I had three or four emails a day when we first left, but now they write about once a month. My mom was really sick last time my dad wrote to me; she's probably better by now, but it takes a month for messages to get through, so there's no way for me to know."
    her "I'm sorry, [his_name], I didn't know..."
    him "It's all right. They're important to me, but you're my family now."
    "We kissed, and looked out the window at the alien hills surrounding our little cabin. It felt surreal, like I was in a movie theatre and any minute the lights would come up and the credits would roll. I held [his_name] tightly; he was here; he was real."
    $ loved += 5

    # After we land on the planet, we start the monthly routines
    stop music
    jump month01
    return
