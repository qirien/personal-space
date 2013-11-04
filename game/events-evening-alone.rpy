# Event content for all the events that can happen in the evening,
# where we relax for a while.

# Basic Alone Evening Events

# Relax with humor
label relax_alone_0:
    scene bg bedroom
    "I read a funny book my friend Sara recommended. Sometimes it was so funny I laughed out loud."
    "Laughing felt good. Sometimes I worried about if we would make it, but I forgot all about it when I could laugh."
    $ relaxed += 5
    $ loved -= 2
    
    return

# Can go help Sara or just relax at home.
label relax_alone_1:
    $ loved -= 2
    scene bg farm_interior
    "I was all set to spend the evening by myself when Sara sent me a message on my computer."
    sara "Are you still up? Can you please come over, [her_name]?"
    menu:
        "Should I go?"
        "I'll be right over":
            her "Sure, I'll be right there."
            "I walked to Sara's house in the dusky evening light, wondering what it was she wanted to talk about. When I got there, I could tell she'd been crying."
            sara "I got a message from Earth today...My mom died."
            $ community_level += 2
        "Can it wait?":
            her "Can it wait? I was just about to get in bed..."
            sara "I could...it's...my mom died."
            her "Oh no, I'll be right over."
            $ community_level += 1
        "I can't come tonight":
            her "Sorry, Sara, I can't tonight. Can we meet tomorrow at lunch?"
            sara "Yeah, I guess."
            $ relaxed += 2
            "The next day at lunch, Sara told me that her mom had died."

    "Since it took four years for the message to get here, her mom had actually been dead for a long time already. That didn't make it any easier for Sara, though."
    sara "All this time - I've been thinking about what she's doing back on Earth, and imagining her playing with her grandkids, and working in the garden, but really she's just been dead."
    menu:
        her "Oh Sara, I'm sorry..."        
        "How's your dad doing?":
            her "How's your dad holding up?"
            sara "He's strong, I'm sure he'll be fine, but I feel terrible! I've been asking him questions about mom and telling jokes about the two of them, and he's going to keep getting those messages from me for years! It'll make him sad every time he gets a message from me."
            her "Or maybe it will make him happy to know how much you still care about her and remember her."
            sara "Yeah, maybe so."
        "How do you feel?":
            her "How do you feel? Besides the obvious, I mean."
            sara "Well, yeah, I'm sad, but I guess everyone has to die sometime, right? And it's not like I could really talk to her, anyway."
            her "But it still feels different, somehow?"
            sara "Yes, it does. I wish she could have seen this - this place, me, a colonist, everything."
            her "I do, too."
        "{i}Maybe she's closer now{/i}" if (skill_spiritual >= 20):
            her "Maybe she's closer now."
            sara "Huh?"
            her "Maybe her spirit can be closer to you, now that her body has passed on."
            sara "You mean... like if the soul could travel through space?"
            her "Sure, why not?"
            sara "I don't know if it's true, but... that's cool to think about."
        "What's the difference?":
            her "What's the difference? You couldn't be together before, and you can't now."
            sara "Well, the difference is now she's dead, so there's nothing there to connect with."
            her "With four years time difference, all our families might as well be dead."
            sara "[her_name]! You should appreciate what you still have!"
            her "None of us have anything. The only difference is some of us realize that."
            return

    "We talked for a long time; Sara has a lot of sad days ahead, but I think I was able to help her feel a little better."
    $ relaxed += 5
    return

# Stargazing alone
label relax_alone_2:
    scene bg stars
    her "Hey, [his_name], want to sit on the porch with me?"
    him "Oh.... I kind of want to, but I'm so tired. I'm just going to go to bed."
    "I sat out on the porch and gazed at the stars. They were so different from Earth, I had to make my own constellations."

    $ relaxed += 5
    $ loved -= 2
    return

# Solo trip to bath house
label relax_alone_3:
    "I went to the bath house by myself. I brought extra wood so I could have a long, hot bath, and I carried up extra water from the river to make it a deep one. All my effort just made me appreciate it all the more."
    $ relaxed += 5
    $ loved -= 2
    return

# Emails from Home
label relax_alone_4:
    scene bg farm_interior
    "I got a message from my mother. It was one she sent several years ago, but she told me all about my siblings, and how the neighbors were doing, and I better take good care of [his_name] and is he taking care of me, that sort of thing."
    "Even though I knew it would take four years for my letter to cross the vast space between our planets, I wrote back. I told her all about the farm and [his_name] and the town and my job. I wonder how much she could understand; our life was so different here..."
    "Still, it felt good to be connected to Earth."
    if (relaxed < 0):
        $ relaxed = 0
    else:
        $ relaxed += 5
    return

# Watch a movie alone
label relax_alone_5:
    scene bg bedroom
    "There are some movies that I love that [his_name] just doesn't like. That's fine; we don't have to do things together all the time. So one night, I watched..."
    menu:
        "I watched:"
        "A musical":
            "A musical. It was cheesy, of course, but the dancing was good and the songs were moving. Something about music just communicates in a way nothing else can..."
        "A romantic comedy":
            "A romantic comedy. I was struck by how silly their disagreements were. Here we were, wondering if we were going to survive, and they were hiding petty secrets from each other. Who has time for that?"
        "A historical drama":
            "A historical drama. The situation of the immigrants in the movie reminded me a little bit of us, except instead of learning how to get along with hostile foreign people we were trying to get along with hostile natural forces."
        "A documentary":
            "A documentary. It felt kind of irrelevant now that we weren't even living on the same planet, but also nostalgic. Ahh, the days back when we lived on Earth..."
                
    $ relaxed += 5
    $ loved -= 2
    return

# Re-read a childhood book
label relax_alone_6:
    scene bg bedroom
    "I didn't mean to read the whole thing, but when I started reading one of my favorite books from my childhood I just had to finish it."
    "It wasn't as exciting and unpredictable as I remembered, but I still love the characters, and the writing swept me in as I read through the whole thing."
    $ relaxed += 5
    $ loved -= 2
    return

# Family photos
label relax_alone_7:
    scene bg farm_interior
    "I looked through some old photos of my family. The places, the people - they all felt so unreal. I'd probably never see them again."
    "It was kind of sad, but at the same time it made me appreciate even more the good times we had had together."
    $ relaxed += 5
    $ loved -= 2
    return

# These probably won't be seen, so make them simple.
label relax_alone_8:
    "I listened to some music - I didn't do anything else while listening, just lay back and really listened."
    "It made me think of summer vacation when I was a teenager back home, just lying back and reading books in the shade, going swimming, and drinking lemonade. What would our kids' summers be like?"
    $ relaxed += 5
    $ loved -= 2
    return

# He does things by himself sometimes, too.
label relax_alone_9:
    scene bg farm_interior
    show him at midleft
    show her at midright
    with dissolve

    him "You want to watch a movie or something?"
    her "Nah, I think I want to do something by myself tonight."
    him "Okay, I've got some things I want to work on, too."
    her "You don't mind, do you?"
    him "No, not really. But I do like when we can do things together."
    her "I do, too, but after being around people all day, sometimes I just need to be alone."
    him "Heh, yeah, I feel kind of the opposite. I'm usually alone all day, so at night I'd rather do something with someone..."
    her "Maybe you could hang out with someone else sometimes?"
    him "Yeah, maybe I'll see if Thuc wants to do something."
    "I felt better knowing I wasn't [his_name]'s only friend..."

    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_10:
    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_11:
    $ relaxed += 5
    return

label relax_alone_12:
    $ relaxed += 5
    return

# Events that can happen in any order
# TODO: Add more of these.

label relax_alone_a:
    scene bg farm_interior
    "I listened to some of my favorite songs and reminisced."
    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_b:
    scene bg bedroom
    "I curled up with a good book."
    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_c:
    scene bg bedroom
    "I felt so tired, I decided to just go to bed early."
    $ relaxed += 7
    $ loved -= 2
    return

label relax_alone_d:
    scene bg farm_interior
    "I wrote a letter to my family, telling them all about what happened this month."
    $ relaxed += 7
    return

label relax_alone_e:
    scene bg farm_interior
    "I played a video game that I enjoyed."
    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_f:
    scene bg path
    "I took a walk and thought about the future."
    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_g:

    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_h:

    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_i:

    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_j:

    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_k:

    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_l:

    $ relaxed += 5
    $ loved -= 2
    return
