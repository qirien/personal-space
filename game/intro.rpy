# Introduction
# Choose profession, hobby, and some character dynamics.

# Crafter; scene at craft store
label crafter:
    $ profession = "crafter"
    scene bg workshop with fade
    show her normal at midleft
    show him normal at midright
    "...the craft store. He was looking for some elastics to braid his horse's hair for a parade."
    show her surprised
    her "You know how to braid your horse's hair?"
    show him flirty
    him "It's a fine art."
    show her normal
    her "I'll believe it when I see it."
    jump first_date

# Doctor; scene at hospital
label doctor:
    $ profession = "doctor"
    scene bg clinic with fade
    show her normal at midleft
    show him normal at midright
    "...the hospital. He thought he had broken his wrist, but when the x-rays came back it turned out it was only sprained. I could feel his eyes on me as I helped him with the sling."
    show her surprised
    her "How did you sprain it, anyway?"
    him "You should have seen it; it was heroic. Diving through flames, rescuing small children, wrestling wolves . . ."
    show her annoyed
    her "Really? You're lucky it was just your wrist, then."

    show him laughing at midright
    him "No, I actually just fell off my horse.  A snake spooked him."
    show her normal
    her "Is your horse okay?"
    show him normal
    him "Oh yeah, Lettie's fine. She seemed like she was almost laughing at me.
"
    jump first_date

# Mechanic; scene at auto shop
label mechanic:
    $ profession = "mechanic"
    scene bg machine_shop with fade
    show her normal at midleft
    show him normal at midright
    "...the car repair shop. His engine wasn't working right, and after I fixed it he wanted me to show him everything I'd done."
    show her angry
    her "You don't think I fixed it right, do you?"
    show him surprised
    him "No! It's not that at all! I just spent two days working on it and couldn't figure it out, so I'm really curious what it was. I'm really impressed, actually."
    show her normal
    her "Well, it's something that's easy to miss. Just take a look at this connection here..."
    hide her
    hide him
    jump first_date

# Teacher; scene at school
label teacher:
    $ profession = "teacher"
    scene bg classroom with fade
    show her normal at midleft
    show him normal at midright
    "...the elementary school. He had come to tell all the kindergartners about life on a farm."
    show him happy
    him "And do you know where eggs come from?"
    show female_child at center
    "Kid" "Chickens!"
    him "Right!"
    "Kid" "But where do the chickens get the eggs?"
    him "They make them! Underneath those cute fluffy feathers, these birds are hard-working egg-making machines!"
    "Kid" "Really? Like a robot?!"
    show him normal
    show her laughing
    him "Yes! A robot made of meat!"
    jump first_date


# No matter what profession you choose, the first date is the same

label first_date:
    scene bg porch with fade
    show her normal at midright
    show him normal at center
    "Afterwards, he asked me if I would come to a barbeque at his house that evening. I thought there was going to be a lot of people, but it ended up being just him and his parents."
    "It wasn't too awkward, though - we all pitched in to make dinner and then sat on the porch swing and talked and watched the stars come out."
    "Something about the way he said my name gave me shivers - the good kind."
    $ her_name = renpy.input("What is your name?", "Mary", length=20)

    him "[her_name]... have you ever thought about what's out there?"
    show her surprised
    her "Out... where?"
    show bg stars with moveintop
    show him happy
    him "In space! So many stars, so many worlds... Did you know they are sending colonists to Talam?"
    show her normal
    her "That's the garden planet they found, right?"
    him "Yes! It's only about four light years away. People could breathe there, grow things, live there!"

# What do you think about the new planet?
# TODO: Make these choices actually affect something.
    menu:
        "I thought,"
        "Why?":
            her "Theoretically, but why would they want to?"
        "Cool!":
            show her happy
            her "Really?! That would be so exciting!"
        "Maybe...":
            show her concerned
            her "It seems like it would be a lot of hard work."

    him "What a challenge it would be! Different animals, plants, even different seasons..."
    show her surprised
    her "Why are you so interested in this planet all of a sudden?"
    jump marriage_proposal

# TODO: We need another date in here to show how much they love each other before the marriage proposal

label marriage_proposal:
    scene bg porch with fade
    show her normal at midright
    show him normal at center
    him "I'm going there, [her_name]. To Talam."
    show her laughing
    her "Oh really? I didn't know you were an astronaut, [his_name]."
    show him annoyed
    him "..."
    show her surprised
    her "You're serious, aren't you?!"
    show him normal
    him "They need farmers to come start the colony, and I want to go."
    show her sad
    her "..."
    him "I want you to come with me."
    show her surprised
    her "?"
    him "As my wife. You're a great [profession], they'll need those there."

    # How does she feel about getting married and going to new planet?
    menu:
        "I felt..."
        "Shocked":
            her "Did you... did you just ask me to marry you?!"
            show him laughing
            him "Sorry, I should have made that part more obvious. [her_name], will you marry me?!"
        "Excited":
            show her happy
            her "Oh [his_name], I can't think of anything that would make me happier!"
            $ loved += 5
            $ relaxed += 5
        "Worried":
            show her concerned
            her "[his_name], I love you, but are you sure you want to go to an entirely new planet? So many things could go wrong..."
            show him normal
            him "I'm sure they will, [her_name], but I know it will be worth it. And when thing's do go wrong, I want you by my side."
            $ loved += 5
            $ relaxed -= 5
        "Annoyed":
            show her annoyed
            her "Oh, so you only want me along because I'm such a good [profession]?"
            show him annoyed
            him "Of course not. I want you along because I'm madly in love with you, and I want to show you that every day, forever."

    show her normal
    her "[his_name]...I would love to create a new life together, even if it is on a different planet."
    scene bg wedding with fade
    "And so we got married."
    "My mother cried; she knew we were going to space and she would probably never see me again (or any grandkids). My father..."
    menu:
        "My father..."
        "Didn't even come.":
            $ father_attitude = "apathetic"
            "...didn't even come. He'd never been there for me before; I wasn't sure why I thought my own wedding would make a difference to him."
        "Frowned seriously.":
            $ father_attitude = "serious"
            "...frowned seriously. I couldn't tell if he was sad, or just thinking about work or something."
        "Just grinned.":
            $ father_attitude = "grinning"
            "...just grinned. I felt good knowing he was so happy for me."
            $ relaxed += 5
    
    "My mind was so full of thoughts of the future, I almost didn't notice when it was my turn to say \"I do.\" It felt like a dream..."
    "You could tell from the wedding presents that people were thinking about how we'd never see Earth again. We got a lot of survival gear, but we couldn't bring most of it and stay under the baggage quota for the colony ship."

    menu:
        "My favorite gift was:"
        "The music player":
            $ favorite_wedding_gift = "music player with my favorite music"
            "The music player. My friends all pitched in and bought a really nice one. They fit all our favorite songs on there."
        "A Swiss Army knife":
            $ favorite_wedding_gift = "Swiss army knife"
            "The Swiss Army knife. It had so many gadgets on it, it could practically bake bread. We couldn't take a lot with us, so I thought all its little tools would be handy."
        "A locket with [his_name]'s picture":
            $ favorite_wedding_gift = "locket with your photo in it"
            "A locket with [his_name]'s picture. I thought it was kind of weird at first that his mom gave it to me, but now I understand she was sharing with me her most precious posession of all - her son."
        "My mom's recipe book":
            $ favorite_wedding_gift = "my mother's recipe book"
            "My mom's recipe book. She's not that great of a cook, but she put in recipes for all the foods she regularly cooks. Those foods bring back so many childhood memories."

    scene bg porch with fade
    show her normal at midright
    show him normal at center
    
    him "Today's the day, lovebug."
    show her surprised
    her "Lovebug?"
    him "Don't you like it? I thought it was cute."
    show her normal

    menu:
        "What should he call you?"
        "Lovebug":
            $ her_nickname = "lovebug"
            her "You can call me '[her_nickname]'; that's cute."
        "Sweetie":
            $ her_nickname = "sweetie"
            her "You could call me '[her_nickname]'."
        "Sugar":
            $ her_nickname = "sugar"
            her "You could call me '[her_nickname]'."
        "Something else":
            $ her_nickname = renpy.input("He calls me:", "sweetie", length=20)
            her "You could call me '[her_nickname]'."
    show him flirt
    him "Hey, I like that. You're my [her_nickname]."

    menu:
        "I realized I didn't have a name for him. I thought fast and decided to call him:"
        "Dear":
            $ his_nickname = "dear"
        "Lover":
            $ his_nickname = "lover"
        "Honey":
            $ his_nickname = "honey"
        "Something else":
            $ his_nickname = renpy.input("I call him:", "honey", length=20)

    show her flirt
    her "And you're my '[his_nickname]'."
    show him surprised
    him "You're calling me [his_nickname]? Well, okay. You can call me whatever you want as long as you come with me on the shuttle today!"

    jump colony_ship
