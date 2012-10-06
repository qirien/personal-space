# Month 0 - Aboard the Colony Ship

# Backgrounds
image bg colony_ship_bunk = "bg/colony-ship-bunk.png"

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
    "Even though Talam was technically a \"garden planet\", meaning humans could breathe and there were plants and animals, it wasn't very much like modern Earth.  There were a lot of sandy areas with little vegetation, and there were reports of some large, dangerous creatures that lived in the water."
    # TODO: Would this be more exciting with some dialogue?
    "The planet was also a lot less protected from its small Sun, since it was a lot closer.  The building materials we'd brought along would help protect us from solar flares and radiation, but only if we were inside. They taught us about the early-warning system they put in place so people would know when it was not safe to be outdoors."

    # He remembers her birthday
    # TODO: Add fun music
    "Time felt strange on the ship, too. Though there was no sunrise or sunset, they did dim the lights for ten hours every night. One night I came back to our room and found a surprise waiting for me."

    him "Happy Birthday, [her_name]."
    her "What? It's not my birthday!"
    him "Actually, according to Earth time you've had two birthdays while we've been travelling, and it seemed sad to let them go by without any sort of celebration, so... Well, it's not much, but I wanted to make sure I didn't forget."
    "He programmed his computer to display \"Happy Birthday, [her_name]\", and there's some sort of streamers hanging down from the ceiling. And... is that cake on the table?"
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
            

# When we want to start with the daily schedule, we will run:
#    jump day
    return
