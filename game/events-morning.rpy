# Event content for all the events that can happen in the morning,
# either at work or skipping work.

# Basic Morning Events
label act_work:

    #Have events every three months or so
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
        $ relaxed -= 2

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
                return
        boss "I understand, but this can't happen all the time. We need you here."
        her "All right, thanks for understanding."
    else:
        "I took a little time off work and didn't push myself this month."
        $ relaxed += 5

    $ slacked_off += 1
    return

# Special Morning Events
label work_intro:
    "I had met my new boss before, but today was my first day working for him. He put me to work right away.  I was so busy, I didn't even have time to think about anything else until it was over."
    boss "You did just fine today; we're all figuring things out here on this new colony, but I can tell you're going to be a big help."
    her "Thank you."
    $ relaxed -= 5
    return
