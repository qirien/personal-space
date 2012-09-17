# Introduction
# Choose profession, hobby, and some character dynamics.

# Doctor; scene at hospital
label doctor:
    $ profession = "Doctor"
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
    $ profession = "Auto Mechanic"
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
    $ profession = "Teacher"
    "...the elementary school. He had come to tell all the kindergartners about life on a farm."
    jump first_date


# No matter what profession you choose, the first date is the same

label first_date:
    "Afterwards, he asked me if I wanted to come to a barbeque at his house that evening. I thought there was going to be a lot of people, but it ended up being just him and his parents."
    "It wasn't too awkward, though - we all pitched in to make dinner and then sat on the porch swing and talked and watched the stars come out."
    "But it wasn't until he first said my name that I knew I wanted to know more about him."
    $ her_name = renpy.input("What is your name?", "Mary", length=20)
    show her normal at center with moveinleft
    show him normal at right with moveinright
    him "Thanks for coming, [her_name]..."

    jump later_date

label later_date:
    "We dated for several months; long enough to feel comfortable around each other, but not long enough that I was thinking too much about the future. He was, though."
    him "[her_name], have you ever thought about what's out there?"
    her "Out . . . where?"
    him "In space! Did you know they have found a garden planet?"
    her "Is that a planet that's kind of like Earth?"
    him "Yes! People could breathe there, grow things, live there!"
    her "Theoretically, but why would they want to?"
    him "What a challenge it would be! Different animals, plants, even different seasons..."

    return
