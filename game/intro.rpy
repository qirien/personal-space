# Introduction
# Choose profession, hobby, and some character dynamics.

# CARPENTER; scene at craft store
label carpenter:
    $ profession = "carpenter"
    scene bg workshop with fade
    show her normal at midleft with dissolve
    "...the hardware store. He was looking for some wire to fix a fence on his farm."
    show him normal at quarterright with moveinright
    him surprised "What gauge do you think I should use?"
    her serious "Well, the larger wire will have a stronger hold, but the thinner wire is easier to work with. What sort of force does it need to hold against?"
    him serious "Well, I had a gate, but it came off..."
    her serious "You might just need a new fitting. Take a look over here..."

    jump first_date

# Doctor; scene at hospital
label doctor:
    $ profession = "doctor"
    scene bg clinic with fade
    show her normal at midleft
    show him normal at quarterright
    with dissolve
    "...the hospital. He thought he had broken his wrist, but when the x-rays came back it turned out it was only sprained. I could feel his eyes on me as I helped him with the sling."
    her surprised "How did you sprain it, anyway?"
    him happy "You should have seen it; it was heroic. Diving through flames, rescuing small children, wrestling wolves . . ."
    her annoyed "Really? You're lucky it was just your wrist, then."

    him normal "No, I actually just fell off my horse.  A snake spooked her."
    her normal "Is your horse okay?"
    him happy "Oh yeah, Lettie's fine. She seemed like she was almost laughing at me."
    jump first_date

# Mechanic; scene at auto shop
label mechanic:
    $ profession = "mechanic"
    scene bg machine_shop with fade
    show her normal at midleft with dissolve
    "...the car repair shop. His engine wasn't working right, and after I fixed it he wanted me to show him everything I'd done."
    show him normal at quarterright with moveinright
    her angry "You don't think I fixed it right, do you?"
    him surprised "No! It's not that at all! I just spent two days working on it and couldn't figure it out, so I'm really curious what it was. I'm really impressed, actually."
    her normal "Well, it's something that's easy to miss. Just take a look at this connection here..."
    jump first_date

# Teacher; scene at school
label teacher:
    $ profession = "teacher"
    scene bg classroom with fade
    show her normal at quarterleft
    show him normal at center
    with dissolve
    "...the elementary school. He had come to tell all the kindergartners about life on a farm."
    him happy "And do you know where eggs come from?"
    show female_child at quarterright with dissolve
    "Kid" "Chickens!"
    him normal "Right!"
    "Kid" "But where do the chickens get the eggs?"
    him serious "They make them! Underneath those cute fluffy feathers, these birds are hard-working egg-making machines!"
    "Kid" "Really? Like a robot?!"
    show her happy with dissolve
    him happy "Yes! A robot made of meat!"
    show her normal
    jump first_date


# No matter what profession you choose, this date is the same

label first_date:
    hide him with moveoutright
    "As he was leaving, he slipped me a note."
    note "Hey there, my [her_name]!\n\nI've been thinking a lot about us lately..."
    note "How I want to be with you all the time."
    note "How I keep thinking about you, even when I'm up to my knees in manure.{size=-6}(was that romantic or what?!){/size}"
    her happy "(Somehow, that is romantic...)"
    note "How I can't imagine how a woman could be more perfect than you."
    her flirting "(If he thinks I'm perfect, he's delusional)"
    note "How it's time we said goodbye to this little town and started something new on our own..."
    note "How I love you heart, body, and soul, every minute of every day..."
    note "Anyway, I want to tell you more, in person! So come to my folks' tonight for a barbeque, okay? Right after work.\n\nLove,\n       your [his_name]"

    nvl clear
    her surprised "(I wonder what's up, he sounds so serious!)"
    scene bg porch with fade
    show her normal at midleft
    show him normal at midright
    with dissolve
    show overlay night
    play music "music/Run.ogg" fadeout 3.0
    "At the barbeque, I thought there was going to be a lot of people, but it ended up being just him and his parents."
    "It wasn't too awkward, though - we all pitched in to make dinner and then afterwards when I offered to help with the dishes, his parents told us to go relax outside."
    "So we sat on the porch swing and talked and watched the stars come out."
    "It was so relaxing to just talk with him - he was always funny and listened to me. He didn't always have the best advice, but I could tell he wanted to help."

    him surprised "[her_name]... have you ever thought about what's out there?"
    her surprised "Out... where?"
    show bg stars with fade
    him happy "In space! So many stars, so many worlds..."
    him normal "Did you know they are sending colonists to Talaam?"
    show bg talaam_space with fade
    her normal "That's the garden planet they found, right?"
    him happy "Yes! It's only about four light years away. People could breathe there, grow things, live there!"

# What do you think about the new planet?
    menu:
        "I thought,"
        "Why?":
            her serious "Theoretically, but why would they want to?"
        "Cool!":
            her happy "Really?! That would be so exciting!"
            $ relaxed += 1
        "Maybe...":
            her concerned "It seems like it would be a lot of hard work."
            $ relaxed -= 1

    him "What a challenge it would be! Different animals, plants, even different seasons..."
    her surprised "Why are you so interested in this planet all of a sudden?"
    jump marriage_proposal

label marriage_proposal:
    scene bg porch with fade
    show her normal at midleft
    show him normal at midright
    with dissolve
    him serious "I'm going there, [her_name]. To Talaam."
    her laughing "Oh really? I didn't know you were an astronaut, [his_name]."
    him annoyed "..."
    her surprised "You're serious, aren't you?!"
    him normal "They need farmers to come start the colony, and I want to go."
    him serious "It's a chance to leave this world behind and focus on the things that really matter in life."
    him concerned "And... you know my parents are getting older. Farming on Talaam will pay enough that I can help my folks retire."
    her sad "..."
    him serious "I want you to come with me."
    her surprised "...?"
    him "As my wife. You're a great [profession], they'll need those there."

    # How does she feel about getting married and going to new planet?
    menu:
        "I felt..."
        "Shocked.":
            her "Did you... did you just ask me to marry you?!"
            him laughing "Sorry, I should have made that part more obvious. [her_name], will you marry me?!"
        "Excited.":
            her happy "Oh [his_name], I can't think of anything that would make me happier!"
            $ loved += 5
            $ relaxed += 5
        "Worried.":
            her concerned "[his_name], I love you, but are you sure you want to go to an entirely new planet? So many things could go wrong..."
            him normal "I'm sure they will, [her_name], but I know it will be worth it. And when things do go wrong, I want you by my side."
            $ loved += 5
            $ relaxed -= 5
        "Annoyed.":
            her annoyed "Oh, so you only want me along because I'm such a good [profession]?"
            him annoyed "Of course not. I want you along because I'm madly in love with you, and I want to show you that every day, forever."

    her happy "[his_name]...I would love to create a new life together, even if it is on a different planet."
    scene bg wedding with fade
    play music "music/Reflections.ogg" fadeout 3.0
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
        "The music player.":
            $ favorite_wedding_gift = "music player from my friends"
            "The music player. My friends all pitched in and bought a really nice one. They fit all our favorite songs on there."
        "A Swiss Army knife.":
            $ favorite_wedding_gift = "Swiss army knife"
            "The Swiss Army knife. It had so many gadgets on it, it could practically bake bread. We couldn't take a lot with us, so I thought all its little tools would be handy."
        "A locket with [his_name]'s picture.":
            $ favorite_wedding_gift = "locket from {}'s mom".format(his_name)
            "A locket with [his_name]'s picture. I thought it was kind of weird at first that his mom gave it to me, but now I understand she was sharing with me her most precious possession of all - her son."
        "My mom's recipe book.":
            $ favorite_wedding_gift = "my mother's recipe book"
            "My mom's recipe book. She's not that great of a cook, but she put in recipes for all the foods she regularly cooks. Those foods bring back so many childhood memories."

    scene bg porch with fade
    show her normal at midleft
    show him normal at midright
    with dissolve
    
    him "Today's the day, blackberry."
    her surprised "\"Blackberry?\""
    him surprised "Don't you like it? I thought it was cute."
    show her normal with dissolve

    menu:
        "What should he call you?"
        "Blackberry.":
            $ her_nickname = "blackberry"
            her "You can call me \"[her_nickname]\"; that's cute."
        "Sweetie.":
            $ her_nickname = "sweetie"
            her "You could call me \"[her_nickname]\"."
        "Sugar.":
            $ her_nickname = "sugar"
            her "You could call me \"[her_nickname]\"."
        "Something else.":
            if not renpy.variant('touch'):
                $ her_nickname = renpy.input("He calls me:", "lovebug", length=20)
            else:
                "He calls me..."
                $ text_group = 1
                $ input_text = ''
                $ input_header = 'Nickname:'
                call inputter
                $ her_nickname = input_text or "lovebug"
            her "You could call me \"[her_nickname]\"."

    him flirting "Alright, then, you're my [her_nickname]!"

    menu:
        "I realized I didn't have a name for him. I thought fast and decided to call him:"
        "Dear.":
            $ his_nickname = "dear"
        "Lover.":
            $ his_nickname = "lover"
        "Honey.":
            $ his_nickname = "honey"
        "Something else.":
            if not renpy.variant('touch'):
                $ his_nickname = renpy.input("I call him:", "asparagus", length=20)
            else:
                "I call him..."
                $ text_group = 1
                $ input_text = ''
                $ input_header = 'Nickname:'
                call inputter
                $ his_nickname = input_text or "asparagus"

    her flirting "And you're my \"[his_nickname]\"."
    him surprised "You're calling me [his_nickname]?"
    him happy "Well, okay. You can call me whatever you want as long as you come with me on the shuttle today!"

    jump colony_ship
