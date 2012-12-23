# Event content for all the events that can happen in the morning,
# either at work or skipping work.

# Basic Morning Events
label act_work:
    "I worked hard at work as usual"
    $ relaxed -= 2
    return

label act_skip_work:
    "I took some time off work and didn't push myself this month."
    $ relaxed += 5
    return

# Special Morning Events
label work_intro:
    "I had met my new boss before, but today was my first day working for him. He put me to work right away.  I was so busy, I didn't even have time to think about anything else until it was over."
    $ relaxed -= 5
    return
