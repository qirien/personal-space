# This file contains styles for the day planner.

init python:

    # Place the day planner.
    style.dp_frame.ypos = 0
    style.dp_frame.yanchor = 0.0
    style.dp_frame.xalign = 0.5

    # Spacing betweeen the choices and the done button.
    style.dp_vbox.box_spacing = 10

    # Spacing between the choice columns.
    style.dp_hbox.box_spacing = 20

    # Center the choices.
    style.dp_choice.xalign = 0.5

    # Center the label of each choice.
    style.dp_label.xalign = 0.5

    style.dp_label_text.text_align = 0.5

    # Make each choice button the same size, and centered.
    style.dp_choice_button.size_group = "dp_choice"
    style.dp_choice_button.xalign = 0.5
    style.dp_choice_button_text.size = 16

    # Center the done button.
    style.dp_done_button.xalign = 0.5

    # Put a margin on the stats frame.
    style.stats_frame.xmargin = 10
    style.stats_frame.ymargin = 5

    # Space between the label and the stats.
    style.stats_vbox.box_first_spacing = 10

    # Put blank space around each stat name, and right-justify.
    style.stat_label.xminimum = 100
    style.stat_label.xmaximum = 110
    style.stat_label_text.xalign = 1.0
    style.stat_label_text.yalign = 0.5
    style.stat_label.xmargin = 5
    style.stat_label_text.size = 16
    
    # Put blank space around each stat value, and right-justify.
    style.stat_value_label.xminimum = 80
    style.stat_value_label.xmaximum = 100
    style.stat_value_label_text.yalign = 0.5
    style.stat_value_label_text.xalign = 0.0
    style.stat_value_label_text.size = 16
        
    # Center the stat bar vertically.
    style.stat_bar.yalign = 0.5
    style.stat_bar.xminimum = 200
    style.stat_bar.xmaximum = 200
