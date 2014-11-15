#
# Styles for use everywhere in the game
#

# Consolidate Sans fonts so you only have to change them 1 place
style sans_text is text:
    font sans_font

#style say_window is window:
#    xoffset 25
    
style say_dialogue:
    color "#FFFFFF"
    
style button:
    background Frame("GUI/button_idle.png", 15, 15)
    hover_background Frame("GUI/button_selected.png", 15, 15)
    insensitive_background Frame("GUI/button_insensitive.png", 15, 15)
    selected_background Frame("GUI/button_selected.png", 15, 15)
    yminimum 40
    activate_sound "sfx/click.ogg"

style button_text is sans_text:
    color "#fff"
    insensitive_color "#666"
    xalign 0.5
    yalign 0.5
    font sans_font

style quick_frame:
    xpadding 10
    ypadding 10

style quick_button:
    background Frame("GUI/textbox-frame.png", 15, 15)
    activate_sound "sfx/click.ogg"
    xalign 0.5
    yalign 0.5

style large_button:
    background Frame("GUI/button_idle.png", 15, 15)
    hover_background Frame("GUI/button_selected.png", 15, 15)
    insensitive_background Frame("GUI/button_insensitive.png", 15, 15)
    selected_background Frame("GUI/button_selected.png", 15, 15)
    yminimum 80
    xminimum 40
    activate_sound "sfx/click.ogg"

style large_button_text is sans_text:
    color "#fff"
    insensitive_color "#666"
    size 16
    xalign 0.5
    
style label_text:
    color "#222"

style frame:
    background Frame("GUI/frame.png", 10, 10)

# NVL Styles
style nvl_label is sans_text:
    size 26
    yalign 0.0
    text_align 0.0
    
style nvl_dialogue is sans_text:
    size 20
    #xpos 100

# Preferences Styles
style pref_frame:
    xfill True
    xmargin 5
    top_margin 5
    
style pref_vbox:
    xfill True
    
style pref_button:
    size_group "pref"
    xalign 1.0
    
style pref_slider:
    xmaximum 192
    xalign 1.0
    
style soundtest_button:
    xalign 1.0
    