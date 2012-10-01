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
        "Not at all.":
            $ want_kids = True
            her "I don't think that's crazy. We're both adults; we know we can provide a good home; what more is there to wait for?"
            him "Yeah, you're right! I think you'd be a great mom! And...well, I probably wouldn't mess the kids up too much."
            her "You will be a wonderful father, as long as you don't treat the kids the way you treat your horse."
            him "Hey! I'm good to Lettie!"
            her "Too good! You'll spoil the kids with treats!"
        "I don't know.":
            $ want_kids = False
            her "Maybe someday, but I don't think I'm ready for that yet."
            him "Someday, definitely. Let's just focus on us, for now."
            her "Oh yeah? What part of \"us\" are you focusing on?"
            him "I think...this part right here. Mmmm...this part is good, too."
            her "Don't forget this..."
            him "Ohhh. Wow, I will never forget that."
            # TODO: is this TMI?
        "Really crazy.":
            $ want_kids = False
            her "I'm not sure we'd be the best parents."
            him "You don't think so? Can't you just picture me on my horse with a kid in my lap? Maybe a little girl?"
            her "She would probably fall off."
            him "No way! Lettie would never let anyone fall off her."

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

    "We talked about lots of other things, of course."

    # TODO: Add something about a birthday on the ship?

# When we want to start with the daily schedule, we will run:
#    jump day
    return
