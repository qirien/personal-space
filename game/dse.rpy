# This is the main program. This can be changed quite a bit to
# customize it for your program... But remember what you do, so you
# can integrate with a new version of DSE when it comes out.

# Set up our daily schedule options
init python:
    register_stat("Domestic", "skill_domestic", 0, 100)
    register_stat("Creative", "skill_creative", 0, 100)
    register_stat("Technical", "skill_technical", 0, 100)
    register_stat("Spiritual", "skill_spiritual", 0, 100)
    register_stat("Social", "skill_social", 0, 100)
    register_stat("Knowledge", "skill_knowledge", 0, 100)
    register_stat("Physical", "skill_physical", 0, 100)

    dp_period("Morning", "morning_act")
    dp_choice("Go to Work", "act_work")
    dp_choice("Stay Home", "act_skip_work")

    dp_period("Afternoon", "afternoon_act")
    dp_choice("Farm/Home", "act_domestic")
    dp_choice("Crafting", "act_creative")
    dp_choice("Repairs", "act_technical")
    dp_choice("Meditation", "act_spiritual")
    dp_choice("Volunteer", "act_social")
    dp_choice("Research", "act_knowledge")
    dp_choice("Exercise", "act_physical")

    dp_period("Evening", "evening_act")
    dp_choice("Do something with [his_name]", "act_relax_together")
    dp_choice("Do something alone", "act_relax_alone")

    
# This is the entry point into the game.
# jump month01 when you want to start the schedule.
label month01:
    $ day = 0
    
    scene black
    "Once we arrived, we soon settled into a routine. Every day he would work on the farm while I worked as a [profession]. I had a little free time after work, and then we ate dinner together."

    jump day

# This is the label that is jumped to at the start of a day.
label day:

    # Increment the day it is.
    $ day += 1
    stop music

    # We may also want to compute the name for the day here, but
    # right now we don't bother.

    "It's month %(day)d."

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available to him.

    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None

    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.
    call day_planner(["Morning", "Afternoon", "Evening"])

    
    # We process each of the three periods of the day, in turn.
label morning:

    # Tell the user what period it is.
    centered "Morning"

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below. 
    $ period = "morning"
    $ act = morning_act

    # Ensure that the stats are in the proper range.
    $ normalize_stats()
    
    # Execute the events for the morning.
    call events_run_period

    # That's it for the morning, so we fall through to the
    # afternoon.

label afternoon:

    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump evening

    # The rest of this is the same as for the morning.

    centered "Afternoon"

    $ period = "afternoon"
    $ act = afternoon_act

    $ normalize_stats()
    
    call events_run_period


label evening:
    
    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    centered "Evening"

    $ period = "evening"
    $ act = evening_act

    $ normalize_stats()
    
    call events_run_period


label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "Night"

    "We kissed good night, and turned out the light."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day
         

# This is a callback that is called by the day planner. One of the
# uses of this is to show the statistics to the user.
label dp_callback:

    # Add in a line of dialogue asking the question that's on
    # everybody's mind.
    $ narrator("What should I do today?", interact=False)
    $ display_stats()

    return

