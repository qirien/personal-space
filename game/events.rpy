# This file contains the definitions for events that will be part of the 
# game.  We define when each event can happen and what label it should
# jump to.  The events themselves are split up into events-morning,
# events-afternoon, and events-evening.  So if you want to add an event, 
# first define when it happens in this file, then add the label and the 
# appropriate content in event-whatever
  

# "init python" tells renpy this whole next thing is python code. 
# That means we don't need the '$' that we usually use for python code.
init python:
    # JOB FOCUS EVENTS
    # Default events if nothing else is going on at work
    event("act_work", "act == 'act_work'", event.solo(), priority=200)
    event("act_skip_work", "act == 'act_skip_work'", event.solo(), priority=200)

    # This is an introduction event, that runs once when we first go
    # to work. 
    event("work_0", "act == 'act_work'", event.once(), event.only())
    
    # Other special work events
    for i in range(1,9):
        event("work_" + `i`,
              "act == 'act_work' and month >= " + `i*3`,
              event.once(),
              event.happened("work_" + `i-1`))

    # SKILL FOCUS EVENTS
    # For each type of skill, we have 10 special events that happen when your skill
    # reaches a certain level.  There is also an intro event and a master event.
    for skill_type in ["domestic", "creative", "technical", "spiritual", "social", "knowledge", "physical"]:
        # Set up default events for each type of skill. These should never show up, but are reserved
        # for future use.
        event (skill_type + "_def", "act == 'act_" + skill_type + "'", event.solo(), priority=400)

        # Add special events that only happen once when you are at a certain
        # skill level in that skill type.
        for i in range(0,9):
            # event(skill_type_i, "act == 'act_skill_type' and skill_skill_type == i*10", event.once(), priority=10)
            event(skill_type + "_" + `i`,
                  "act == 'act_" + skill_type + "' and skill_" + skill_type + " == " + `i*10`,
                  event.once(),
                  priority=10)

        # This event happens when a skill reaches 100.
        event(skill_type + "_master",
              "act == 'act_" + skill_type + "' and skill_" + skill_type + " == 90",
              event.once(),
              priority = 10)



    # RELAXATION EVENTS
    # Default Events
    event("relax_together_0", "act == 'act_relax_together'", event.solo(), priority=200)
    event("relax_alone_0", "act == 'act_relax_alone'", event.solo(), priority=200)

    # One-time Relaxation events; choose next one in sequence every odd month
    for i in range(1,12):
        event ("relax_together_" + `i`, 
               "act == 'act_relax_together'", 
               event.once(), 
               event.happened("relax_together_" + `i-1`),
               event.is_month_odd()) # odd months only
        event ("relax_alone_" + `i`, 
               "act == 'act_relax_alone'", 
               event.once(), 
               event.happened("relax_alone_" + `i-1`),
               event.is_month_odd()) #odd months only

    # Default relaxation events; choose one of these randomly every even month
    for letter in range(ord('a'),ord('l')+1):
        event ("relax_together_" + unichr(letter),
               "act == 'act_relax_together'",
               event.choose_one("relax_together_random"),
               event.once(),
               event.is_month_even()) #even months only
        event ("relax_alone_" + unichr(letter),
               "act == 'act_relax_alone'",
               event.choose_one("relax_alone_random"),
               event.once(),
               event.is_month_even()) #even months only


    # MONTHLY SPECIAL EVENTS
    # Default event that we shouldn't ever see....
    event("monthly_event_0", "period == 'monthly_event'", event.solo(), priority=200)

    # Scripted Events that happen once
    event("monthly_event_1", "period == 'monthly_event'", event.once())
    for i in range(2,26):
        event ("monthly_event_" + `i`,  
               "period == 'monthly_event'", 
               event.once(), 
               event.happened("monthly_event_" + `i-1`))
