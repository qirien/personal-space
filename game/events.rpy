# This file contains the events that will be part of the game. It's
# expected that the user will add and remove events as appropriate
# for this game.

  
# First up, we define some simple events for the various actions, that
# are run only if no higher-priority event is about to occur.

init:
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

# Morning Events
label act_work:
    "The morning seems to fly by at work."
    
    return

label act_skip_work:
    "I wasn't feeling well, so I decided to skip work."

    return

# Afternoon Events
label act_domestic:
    "I cleaned the house and got dinner ready."
    $ skill_domestic += 10

    return

label act_creative:
    "I worked on a quilt for our bedroom."
    $ skill_creative += 10

    return

label act_technical:
    "I tuned up some of the farm equipment."
    $ skill_technical += 10

    return

label act_spiritual:
    "I took a walk and spent some time just thinking."
    $ skill_spiritual += 10

    return

label act_social:
    "I went to town and helped out at the library."
    $ skill_social += 10

    return

label act_knowledge:
    "I read up on the latest science research."
    $ skill_knowledge += 10

    return

label act_physical:
    "I went for a run and lifted some weights."
    $ skill_physical += 10

    return

# Evening Events

label act_relax_together:
    "We watched a movie together and talked."

    return

label act_relax_alone:
    "I curled up with a good book."

    return

# Below here are special events that are triggered when certain
# conditions are true. 

# This is an introduction event, that runs once when we first go
# to class. 

init:
    $ event("work_intro", "act == 'act_work'", event.once(), event.only())

label work_intro:
    "I had met my new boss before, but today was my first day working for him. He put me to work right away.  I was so busy, I didn't even have time to think about anything else until it was over."

    return
