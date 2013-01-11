# Event content for all the events that can happen in the evening,
# where we relax for a while.

# Basic Alone Evening Events
# These don't all have to be big events -- we could randomize between a few
# different things.


label relax_alone_0:
    "I curled up with a good book."
    $relaxed += 5
    return

label relax_alone_1:
    "I felt so tired, I decided to just go to bed early."
    $relaxed += 5
    return

label relax_alone_2:
    "I sat out on the porch and gazed at the stars."
    $relaxed += 5
    return

label relax_alone_3:
    "I listend to some of my favorite songs and reminisced about past experiences."
    $relaxed += 5

    return

label relax_alone_4:
    "I got a message from my mother. It was one she sent about a month ago, but she told me all about my siblings, and how the neighbors were doing, and I better take good care of [his_name] and is he taking care of me, that sort of thing."
    "Even though I knew it would take a month for my letter to cross the vast space between our planets, I wrote back. I told her all about the farm and [his_name] and the town and my job. I wonder how much she could understand; our life was so different here..."
    "Still, it felt good to be connected to Earth."
    $ relaxed += 10
    return

label relax_alone_5:
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
            "A documentary. It felt kind of irrelevant now that we weren't even living in the same country, but also nostalgic. Ahh, the days back when we lived on Earth..."
                
    $ relaxed += 5
    return

label relax_alone_6:
    return

label relax_alone_7:
    return

label relax_alone_8:
    return

label relax_alone_9:
    return

label relax_alone_10:
    return

label relax_alone_11:
    return

label relax_alone_12:
    return

label relax_alone_13:
    return

label relax_alone_14:
    return

label relax_alone_15:
    return

label relax_alone_16:
    return

label relax_alone_17:
    return

label relax_alone_18:
    return

label relax_alone_19:
    return

label relax_alone_20:
    return

label relax_alone_21:
    return

label relax_alone_22:
    return

label relax_alone_23:
    return
