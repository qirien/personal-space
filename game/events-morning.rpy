# Event content for all the events that can happen in the morning,
# either at work or skipping work.

# Basic Morning Events
label act_work:

    #Have events every three months or so
    # TODO: mention that the mayor's favorite song is "It's the End of the World"
    # Emergency where she can't help everyone in time, leading to 
    # the mayor offering to find her some help.
    if (month == 3):
        #Different event for each profession
        if (profession == "doctor"):
            "Doctor Month 3"
        elif (profession == "crafter"):
            "Crafter Month 3"
        elif (profession == "auto mechanic"):
            "Mechanic Month 3"
        elif (profession == "teacher"):
            "Teacher Month 3"

    # Introduce co-worker Brennan Callahan
    elif (month == 6):
        #Different event for each profession
        if (profession == "doctor"):
            "Doctor Month 6"
        elif (profession == "crafter"):
            "Crafter Month 6"
        elif (profession == "auto mechanic"):
            "Mechanic Month 6"
        elif (profession == "teacher"):
            "Teacher Month 6"

    # Something bad happens and she confides in co-worker
    elif (month == 9):
        #Different event for each profession
        if (profession == "doctor"):
            "Doctor Month 9"
        elif (profession == "crafter"):
            "Crafter Month 9"
        elif (profession == "auto mechanic"):
            "Mechanic Month 9"
        elif (profession == "teacher"):
            "Teacher Month 9"

    elif (month == 12):
        #Different event for each profession
        if (profession == "doctor"):
            "Doctor Month 12"
        elif (profession == "crafter"):
            "Crafter Month 12"
        elif (profession == "auto mechanic"):
            "Mechanic Month 12"
        elif (profession == "teacher"):
            "Teacher Month 12"

    elif (month == 15):
        #Different event for each profession
        if (profession == "doctor"):
            "Doctor Month 15"
        elif (profession == "crafter"):
            "Crafter Month 15"
        elif (profession == "auto mechanic"):
            "Mechanic Month 15"
        elif (profession == "teacher"):
            "Teacher Month 15"

    elif (month == 18):
        #Different event for each profession
        if (profession == "doctor"):
            "Doctor Month 18"
        elif (profession == "crafter"):
            "Crafter Month 18"
        elif (profession == "auto mechanic"):
            "Mechanic Month 18"
        elif (profession == "teacher"):
            "Teacher Month 18"

    elif (month == 21):
        #Different event for each profession
        if (profession == "doctor"):
            "Doctor Month 21"
        elif (profession == "crafter"):
            "Crafter Month 21"
        elif (profession == "auto mechanic"):
            "Mechanic Month 21"
        elif (profession == "teacher"):
            "Teacher Month 21"

    elif (month == 24):
        #Different event for each profession
        if (profession == "doctor"):
            "Doctor Month 24"
        elif (profession == "crafter"):
            "Crafter Month 24"
        elif (profession == "auto mechanic"):
            "Mechanic Month 24"
        elif (profession == "teacher"):
            "Teacher Month 24"

    else:
        "I worked hard at work as usual."
        $ relaxed -= 5

    return

label act_skip_work:
    if (slacked_off == 3):
        "My boss called me in to meet with him after work."
        boss "[her_name], I'm worried about you. You haven't been putting in your usual effort at work lately."
        menu:
            "What should I say?"
            "I'm sorry.":
                her "I'm sorry. I should pay better attention to my work."
            "Things are busy at home":
                her "Sorry - things have been so busy at home, trying to get the farm started and everything."
            "It won't happen again.":
                her "I'm sorry - I won't let it happen again."
            "Whatever.":
                her "Whatever."
                boss "Excuse me?"
                her "As long as I get my job done, what's the big deal?"
                boss "Well, just see that you do get it done."
                $ slacked_off = 1
                return
        boss "I understand, but this can't happen all the time. We need you here."
        her "All right, thanks for understanding."
        $ slacked_off = 0
        $ relaxed -= 5
    else:
        "I took a little time off work and didn't push myself this month."
        $ relaxed += 5

    $ slacked_off += 1
    return

# Special Morning Events
label work_intro:
    "My boss was also the leader of our little community. I guess you could call him the mayor?"
    boss "All right, [her_name], ready to get to work?"
    menu:
        "Am I ready?"
        "Of course!":
            her "Of course! Where shall I start?"
        "I guess so":
            her "Yeah, I guess. What's first?"
        "No, but here I am":
            her "No, I'm pretty nervous. But I'll do my job anyway."

    #Different event for each profession
    if (profession == "doctor"):
        boss "All right! This is the clinic where people will come in if they get sick. I don't just want us to react to injuries and illness, though - we need to be proactive, and help promote good health."
        her "I helped some people out on the ship on the way here, so this should be similar. I will need some more supplies, though."
        boss "That's fine, just write up a list and give it to me to approve. Then you can go on over to the storehouse and take what you need."
    elif (profession == "crafter"):
        boss "All right! This is the shop where people will come in if they need something made they can't make themselves. We don't have a lot of materials yet, but you can requisition some from the storehouse for important projects, and there are some materials, like wood, right here on the planet."
        her "I can see that this job is going to take a lot of creativity!"
        boss "Yes, it will! Perhaps you can start by helping me out - one of the roof pieces from the Nguyen's house broke when we were unpacking it, so they are going to need a replacement."
        her "Sure, I'll take a look at the standard roofs and see if I can make something out of the wood around here."
    elif (profession == "auto mechanic"):
        boss "All right! This is the shop where people will bring machines that need to be fixed. You'll be responsible for any kind of machine people have, from datapads to tractors. We don't have many replacement parts, so do what you can to fix things up when they break."
        her "I can see that this will take a lot of creativity."
        boss "Yes, it will! Perhaps you can start by helping me with my datapad? It always freezes up when I try to access my calendar..."
        her "Sure, let me take a look at it..."
    elif (profession == "teacher"):
        boss "All right! This is the schoolhouse. There's not a lot of kids in the community yet, so we just have them all in one room with you as their teacher. Please consider what they'll need to learn in addition to the standard curriculum, and try to be flexible if kids are needed to help out back at home."
        her "I guess the kids are going to have to work hard, too..."
        boss "Yes, but they need to learn a lot, too! It will take a lot of effort to see that they don't forget about Earth, and all the things humanity has managed to learn there."
        her "Even though it seems far away, it's still our home, isn't it?"

    "I worked hard getting things set up, and even though the job seemed pretty big, I thought I would probably do okay."
    $ relaxed -= 5
    return
