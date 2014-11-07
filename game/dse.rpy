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

    dp_period("Work", "job_focus_act")
    dp_choice("Focus on Work", "act_work")
    dp_choice("Take it Easy", "act_skip_work", enable="(month>1) and (month<25)")

    dp_period("Skills", "skill_focus_act")
    dp_choice("Domestic", "act_domestic", enable="skill_domestic < 100")
    dp_choice("Creative", "act_creative", enable="skill_creative < 100")
    dp_choice("Technical", "act_technical", enable="skill_technical < 100")
    dp_choice("Spiritual", "act_spiritual", enable="skill_spiritual < 100")
    dp_choice("Social", "act_social", enable="skill_social < 100")
    dp_choice("Knowledge", "act_knowledge", enable="skill_knowledge < 100")
    dp_choice("Physical", "act_physical", enable="skill_physical < 100")

    dp_period("Free Time", "relaxation_focus_act")
    dp_choice("Together", "act_relax_together", enable="not ((month>=24) and wants_to_leave)")
    dp_choice("Alone", "act_relax_alone")

    dp_period("Monthly Event", "monthly_event_act")
    dp_choice("No Actual Choices", "act_monthly", False)

    
# This is the entry point into the game.
# jump month01 when you want to start the schedule.
label month01:
    
    $ month = 0
    scene black with fade
    # TODO: how do you do this in Android? Does help file work there?
    # TODO: Have a tutorial about the computer pad.
    if renpy.variant('touch'):
        "To access the menu and save your game, right-click or press \"Esc\". For more help, click on \"Help\"."
    else:
        "To access the menu and save your game, right-click or press \"Esc\". For more help, click on \"Help\"."

    jump day

# This is the label that is jumped to at the start of a day
# Or, in our case, month.
label day:

    # Increment the month it is.
    $ month += 1
    $ save_name = "Month %d" % month
    stop music fadeout 1.0
    scene bg talaam_space with fade

    $ year = 1
    $ local_month = month
    $ season = ""
    $ weather = ""

    # Compute the year and what month in the year it is, on Talaam and Earth
    while (local_month > 7):
        $ year += 1
        $ local_month -= 7        

    # There are 196 27-hour days per year on Talaam, and 356 24-hour days on Earth
    $ earth_months = int(month*((196.0*27.0) / (356.0*24.0)))
    $ earth_month = earth_months
    $ earth_year = 1
    while (earth_month > 12):
        $ earth_year += 1
        $ earth_month -= 12

    if ((local_month == 1) or (local_month == 2)):
        $ season = "spring"
        $ weather += "warm and rainy"
    if ((local_month == 3) or (local_month == 4)):
        $ season = "summer"
        $ weather = "hot and dry"
    if (local_month == 5):
        $ season = "fall"
        $ weather = "mild and breezy"
    if ((local_month == 6) or (local_month == 7)):
        $ season = "winter"
        $ weather = "cold and rainy"

    # calculate pregnancy progress
    $ pregnant_months = 0
    $ trimester = "None"
    if (is_pregnant):
        $ pregnant_months = month - 14
    if (is_pregnant_later):
        $ pregnant_months = month - 23
    if (pregnant_months < 4):
        $ trimester = "first"
    elif (pregnant_months < 7):
        $ trimester = "second"
    elif (pregnant_months <= 10):
        $ trimester = "third"
    else:
        $ trimester = "done"
        
    # TODO: Play a season-specific sound (like rain or wind)?

    "Time to decide what to do this month..."
    
    #"Loved = [loved], Relaxed = [relaxed], community_level = [community_level], made_love = [made_love]"
    if (month == 25):
        "The shuttle should be coming some time this month!"

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available to him.

    $ job_focus_act = None
    $ skill_focus_act = None
    $ relaxation_focus_act = None
    $ monthly_event_act = None

    if (month == 1):
        menu:
            "Would you like to see the Tutorial?"
            "Yes":
                call tutorial
            "No":
                $pass
        
    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.
    scene bg gray_silk
    call screen computer_pad(["Work", "Skills", "Free Time"]) 

    
    # We process each of the three periods of the day, in turn.
label job_focus:

    scene black
    # Tell the user what month it is.
    centered "{color=#ffffff}Month [month] of 25\n\nAt Work{/color}"
    play music "music/Isaiah.ogg" fadeout 3.0

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below. 
    $ period = "job_focus"
    $ act = job_focus_act

    # Ensure that the stats are in the proper range.
    $ normalize_stats()
    
    # Execute the events for the job_focus.
    call events_run_period

    # That's it for the job_focus, so we fall through to the
    # skill_focus.

label skill_focus:

    # It's possible that we will be skipping the skill_focus, if one
    # of the events in the job_focus jumped to skip_next_period. If
    # so, we should skip the skill_focus.
    if check_skip_period():
        jump relaxation_focus

    # The rest of this is the same as for the job_focus.
    scene black
    centered "{color=#ffffff}Month [month] out of 25\n\nSkill Focus{/color}"
    play music "music/OceansApart.ogg" fadeout 3.0

    $ period = "skill_focus"
    $ act = skill_focus_act

    $ normalize_stats()
    
    call events_run_period


label relaxation_focus:
    
    # The relaxation_focus is the same as the skill_focus.
    if check_skip_period():
        jump monthly_event

    scene black
    centered "{color=#ffffff}Month [month] out of 25\n\nFree Time{/color}"

    $ period = "relaxation_focus"
    $ act = relaxation_focus_act
    if (act == "act_relax_together"):
        play music "music/Reflections.ogg" fadeout 3.0
    else:
        play music "music/Will.ogg" fadeout 3.0

    $ normalize_stats()
    
    call events_run_period

label monthly_event:
    if check_skip_period():
        jump end_of_month
    
    scene black
    centered "{color=#ffffff}Month [month] out of 25\n\nEvent!{/color}"
    play music "music/RainSea.ogg" fadeout 3.0

    $ period = "monthly_event"
    $ act = monthly_event_act
    
    $ normalize_stats()

    call events_run_period

label end_of_month:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.
    
    scene black
    #centered "{color=#ffffff}End of the Month{/color}"

    "We made it through another month on Talaam..."

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
    #$ narrator("What should I focus on this month?", interact=False)
    $ display_stats()

    return
