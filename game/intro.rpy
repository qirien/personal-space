# Introduction
# Choose profession, hobby, and some character dynamics.

# Images
image bg porch = "farm-porch.png"
image bg wedding = "wedding.png"
image female_child normal = "female-child.png"

# Crafter; scene at craft store
label crafter:
        $ profession = "crafter"
        "...the craft store. He was looking for some elastics to braid his horse's hair for a parade."
        show her normal at left
        show him normal at right
        her "You know how to braid your horse's hair?"
        him "It's a fine art."
        her "I'll believe it when I see it."
        jump first_date

# Doctor; scene at hospital
label doctor:
    $ profession = "doctor"
    "...the hospital. He thought he had broken his wrist, but when the x-rays came back it turned out it was only sprained. I could feel his eyes on me as I helped him with the sling."
    show her normal at left
    show him normal at right
    her "How did you sprain it, anyway?"
    him "You should have seen it; it was heroic. Diving through flames, rescuing small children, wrestling wolves . . ."
    her "Really? You're lucky it was just your wrist, then."

    #show him laughing at right
    him "No, I actually just fell off my horse.  A snake spooked him."
    her "A horse?"
    him "Yes, I live on a farm outside of town. Kinda old-fashioned, but I like it."
    "I didn't know what to think about that."
    jump first_date

# Mechanic; scene at auto shop
label mechanic:
    $ profession = "auto mechanic"
    "...the car repair shop. His engine wasn't working right, and after I fixed them he wanted me to show him everything I'd done."
    #show her angry at left
    her "You don't think I fixed it right, do you?"
    show him normal at right
    him "No! It's not that at all! I just spent two days working on it and couldn't figure it out, so I'm really curious what it was. I'm really impressed, actually."
    show her normal at left
    her "Well, it's something that's easy to miss. Just take a look at this connection here..."
    hide her
    hide him
    jump first_date

# Teacher; scene at school
label teacher:
    $ profession = "teacher"
    "...the elementary school. He had come to tell all the kindergartners about life on a farm."
    show him normal at right
    him "And do you know where eggs come from?"
    show female_child normal at center
    "Kid" "Chickens!"
    him "Right!"
    "Kid" "But where do the chickens get the eggs?"
    him "They make them! Underneath those cute fluffy feathers, these birds are hard-working egg-making machines!"
    "Kid" "Really? Like a robot?!"
    him "Yes! A robot made of meat!"
    #show her laughing at left
    jump first_date


# No matter what profession you choose, the first date is the same

label first_date:
    scene bg porch
    "Afterwards, he asked me if I wanted to come to a barbeque at his house that evening. I thought there was going to be a lot of people, but it ended up being just him and his parents."
    "It wasn't too awkward, though - we all pitched in to make dinner and then sat on the porch swing and talked and watched the stars come out."
    "But it wasn't until he first said my name that I knew I wanted to know more about him."
    $ her_name = renpy.input("What is your name?", "Mary", length=20)

    scene bg stars
    show her normal at left
    show him normal at center
    him "[her_name], have you ever thought about what's out there?"
    her "Out . . . where?"
    him "In space! So many stars, so many worlds... Did you know they are sending colonists to Talam?"
    her "That's the garden planet they found, right?"
    him "Yes! It's only about four light years away. People could breathe there, grow things, live there!"

# What do you think about the new planet?
    menu:
        "I thought,"
        "Why?":
            her "Theoretically, but why would they want to?"
        "Cool!":
            her "Really?! That would be so exciting!"
        "Maybe...":
            her "It seems like it would be a lot of hard work."

    him "What a challenge it would be! Different animals, plants, even different seasons..."
    "He really was excited about it. As we grew closer, I could tell there was a lot of things about him I liked: he was funny, kind, and hardworking. I wasn't thinking about the future yet, but he was..."

# We need another date in here to show how much they love each other before the marriage proposal

label marriage_proposal:
    scene bg earth
    him "I'm going, [her_name]. To Talam."
    #show her laughing
    her "Oh really? I didn't know you were an astronaut, [his_name]."
    him "..."
    her "You're serious, aren't you?!"
    him "They need farmers to come start the colony, and I want to go."
    #show her sad
    her "..."
    him "I want you to come with me."
    her "?"
    him "As my wife. You're a great [profession], they'll need those there."
    menu:
        "I felt..."
        "Shocked":
            her "Did you... did you just ask me to marry you?!"
            him "Sorry, I should have made that part more obvious. [her_name], will you marry me!"
        "Excited":
            her "Oh [his_name], I can't think of anything that would make me happier!"
        "Worried":
            her "[his_name], I love you, but are you sure you want to go to an entirely new planet? So many things could go wrong..."
            him "I'm sure they will, [her_name], but I know it will be worth it. And when thing's do go wrong, I want you by my side."
        "Annoyed":
            her "Oh, so you only want me along because I'm such a good [profession]?"
            him "Of course not. I want you along because I'm madly in love with you, and I want to show you that every day, forever."

    scene bg wedding
    "And so we got married."
    "My mother cried; she knew we were going to space and she would probably never see me again (or any grandkids). My father..."
    menu:
        "My father..."
        "Didn't even come.":
            $ father_attitude = "apathetic"
        "Frowned seriously.":
            $ father_attitude = "serious"
        "Just grinned.":
            $ father_attitude = "grinning"
    
    "You could tell from the wedding presents that people were thinking about how we'd never see Earth again. We got a lot of survival gear, but we couldn't bring most of it and stay under the baggage quota for the colony ship."

    menu:
        "My favorite gift was:"
        "The music player":
            $ favorite_wedding_gift = "music player with my favorite music"
            "The music player. My friends all pitched in and bought a really nice one. They fit all our favorite songs on there."
        "A Swiss Army knife":
            $ favorite_wedding_gift = "Swiss army knife"
            "The Swiss Army knife. It had so many gadgets on it, it could probably bake bread. We couldn't take a lot with us, so I thought all its little tools would be handy."
        "A locket with [his_name]'s picture":
            $ favorite_wedding_gift = "locket with your photo in it"
            "A locket with [his_name]'s picture. I thought it was kind of weird at first that his mom gave it to me, but now I understand she was sharing with me her most precious posession of all - her son."
        "My mom's recipe book":
            $ favorite_wedding_gift = "my mother's recipe book"
            "My mom's recipe book. She's not that great of a cook, but she put in recipes for all the foods she regularly cooks. Those foods bring back so many childhood memories."

    jump colony_ship


# After they get married, they board the colony ship
label colony_ship:
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
            him "I think...this part right here. Oh, this part is good, too."
            her "Don't forget this..."
            him "Wow, I will never forget that."
            #is this TMI?
        "Really crazy.":
            $ want_kids = False
            her "I'm not sure we'd be the best parents."
            him "You don't think so? Can't you just picture me on my horse with a kid in my lap? Maybe a little girl?"
            her "She would probably fall off."
            him "No way! Lettie would never let anyone fall off her."
            # maybe give some more choices here
            her "It's not Lettie I'm worried about."
            him "You don't trust me?"
            her "No, I'm more worried about me - I don't think I'd be a good mom."
            him "Oh. Well, for what it's worth, I disagree with you. But, we've got plenty of time. No need to worry about it now."

    "We talked about lots of other things, of course."
    return
