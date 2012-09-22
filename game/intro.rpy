# Introduction
# Choose profession, hobby, and some character dynamics.

# Images
image bg porch = "farm-porch.png"
image bg wedding = "wedding.png"
image female_child normal = "female-child.png"

# Doctor; scene at hospital
label doctor:
    $ profession = "doctor"
    "...the hospital. He thought he had broken his wrist, but when we the x-rays came back it turned out it was only sprained. I could feel his eyes on me as I helped him with the sling."
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
    him "Yes! It's only 4.3 light years away. People could breathe there, grow things, live there!"

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

label marriage_proposal:
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

    return
