label monthly_event_24:
    "It had been two years since we first arrived on Talam. In a way, it felt like we had been here forever. But sometimes I expected to find myself back on Earth, waking up from a long, long dream."
    if ((community_level < 100) and (loved <= 0)):
        jump fail_bad_ending
    elif ((community_level >= 100) and (loved <= 0)):
        jump succeed_bad_ending
    elif ((community_level < 100) and (loved > 0)):
        jump fail_good_ending
    elif ((community_level >= 100) and (loved > 0)):
        jump succeeed_good_ending

    jump credits


label fail_bad_ending:
    "Everything was falling apart."

    ".:. Ending 1/4."
    return

label succeed_bad_ending:
    "The community was thriving, but my marriage was falling apart."

    ".:. Ending 2/4."
    return

label fail_good_ending:
    "Even though our colony wasn't going to make it, at least we had each other."

    ".:. Ending 3/4."
    return

label succeed_good_ending:
    "We built a colony, a home, and a family."

    ".:. Ending 4/4."
    return


label credits:
    "Credits"

    $ renpy.full_restart()
