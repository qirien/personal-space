# This contains code for the new day planner. You probably
# don't want to change this file, but it might make sense to
# change many of the variables or styles defined here from
# other files.

# The frame containing the day planner.
style dp_frame is frame
 
# The frame and vbox containing a single choice. 
style dp_choice:
    xalign 0.5

style dp_choice is default:
    xalign 0.5
    
# Buttons    
style dp_choice:
    size_group "dp_choice_button"
style dp_choice_button is button
style dp_choice_button_text is button_text
    
# Labels    
style dp_label is label

style dp_label_text is text:
    color "#000"
    font sans_font
    bold True


init -100 python:
    
    # The title of the done button.
    dp_done_title = "All Done"

    # A map from period name to the information we know about that
    # period.
    __periods = { }

    # The period we're updating.
    __period = None
    
    class __Period(object):

        def __init__(self, name, var):
            self.name = name
            self.var = var
            self.acts = [ ]

    def dp_period(name, var):
        __periods[name] = store.__period = __Period(name, var)

    __None = object()
        
    def dp_choice(name, value=__None, enable="True", show="True"):

        if not __period:
            raise Exception("Choices must be part of a defined period.")

        if value is __None:
            value = name
        
        __period.acts.append((name, value, enable, show))

    def __set_noncurried(var, value):
        setattr(store, var, value)
        return True
        
    __set = renpy.curry(__set_noncurried)
        
# Our Day Planner displays the stats, and buttons for the user to choose what to do
# during each period of time defined in "periods".
screen day_planner(periods):
    # indicate to Ren'Py engine that this is a choice point
    $ renpy.choice_for_skipping()
    window:  
        use display_stats(True, True, True, True)
        use display_planner(periods)            
            
screen display_planner(periods):            
        vbox xfill True:
            style_group "dp"        
            label "Focus" yalign 0.0 xalign 0.5 text_style "cp_header_text"
            vbox:
                $ can_continue = True
                frame:
                    ysize 437
                    has vbox
                    for p in periods:
                        vbox:
                            label p alt p + ": Choose One"
                            if (p == "Skills"):
                                textbutton " Current Skill Progression " xalign 0.5 text_bold True:
                                    action Show("skill_screen")                            
                            if p not in __periods:
                                $ raise Exception("Period %r was never defined." % p)
                            $ this_period = __periods[p]
                            $ selected_choice = getattr(store, this_period.var)
                            $ valid_choice = False
                            $ num_choices = len(this_period.acts)
                            $ choice_rows = ((num_choices-1) // 2) + 1
                            grid 2 choice_rows: 
                                style_group "dp_choice"
                                for name, curr_val, enable, should_show in this_period.acts:
                                    $ show_this = eval(should_show)
                                    $ enable = eval(enable)

                                    $ selected = (selected_choice == curr_val)
                            
                                    if show_this:
                                        if enable:
                                            textbutton name action SetField(store, this_period.var, curr_val) alt p + ": " +  name
                                        else:
                                            textbutton name 
                                    #if we're not showing this, leave a blank space in the grid
                                    else: 
                                        text ""
                
                                    if show_this and enable and selected:
                                        $ valid_choice = True

                                if not valid_choice:
                                    $ can_continue = False
                                    
                                # We need an extra blank spot if there are an odd number of choices
                                # and we didn't fill up our grid
                                if ((2 * choice_rows) != num_choices):
                                    text ""                                
            hbox xfill True:
#                textbutton "Help" xalign 0.0 xpos 10:
#                    action Show("help_screen_1")                                                       
                if (can_continue):
                    textbutton dp_done_title style "dp_done_button" xalign 1.0 action Jump("job_focus")
                else:
                    textbutton dp_done_title style "dp_done_button" xalign 1.0

