# This file contains the definitions for events that will be part of the 
# game.  We define when each event can happen and what label it should
# jump to.  The events themselves are split up into events-morning,
# events-afternoon, and events-evening.  So if you want to add an event, 
# first define when it happens in this file, then add the label and the 
# appropriate content in egent_whatever
  
init:
    # First up, we define some simple events for the various actions, that
    # are run only if no higher-priority event is about to occur.
    # Special events are defined later in the file, after these

    # Morning Events
    $ event("act_work", "act == 'act_work'", event.solo(), priority=200)
    $ event("act_skip_work", "act == 'act_skip_work'", event.solo(), priority=200)

    # Afternoon Events
    $ event ("act_domestic", "act == 'act_domestic'", event.solo(), priority=200)
    $ event ("act_creative", "act == 'act_creative'", event.solo(), priority=200)
    $ event ("act_technical", "act == 'act_technical'", event.solo(), priority=200)
    $ event ("act_spiritual", "act == 'act_spiritual'", event.solo(), priority=200)
    $ event ("act_social", "act == 'act_social'", event.solo(), priority=200)
    $ event ("act_knowledge", "act == 'act_knowledge'", event.solo(), priority=200)
    $ event ("act_physical", "act == 'act_physical'", event.solo(), priority=200)

    # Evening Events
    $ event("act_relax_together", "act == 'act_relax_together'", event.solo(), priority=200)
    $ event("act_relax_alone", "act == 'act_relax_alone'", event.solo(), priority=200)


# TODO: How should these affect stats and/or emotional state?


# Below here are special events that are triggered when certain
# conditions are true. 

# SPECIAL MORNING EVENTS

# This is an introduction event, that runs once when we first go
# to work. 
init:
    $ event("work_intro", "act == 'act_work'", event.once(), event.only())



# SPECIAL AFTERNOON EVENTS

    # Domestic Events
    $ event("domestic_1",

            # This takes place if we work on domestic, and our stat is at least 10
            "act == 'act_domestic' and skill_domestic >= 10",

            # It runs only once.
            event.once(),

            # It requires the introduction event to have run at least
            # one day before.
            event.depends("act_domestic"))

    $ event("domestic_2",
            "act == 'act_domestic' and skill_domestic >= 20",
            event.once(),
            event.depends("domestic_1"))


# SPECIAL EVENING EVENTS
