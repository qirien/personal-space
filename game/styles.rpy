#
# Styles for use everywhere in the game
#

# Chinese fonts
translate chinese style default:
    font "fonts/NotoSansSC-Regular.otf"

translate chinese python:
    gui.text_font = "fonts/NotoSansSC-Light.otf"

# Consolidate Sans fonts so you only have to change them 1 place
style sans_text is text:
    font sans_font

style cursive_text is text:
    font "fonts/Kristi.ttf"

style say_dialogue:
    color "#FFFFFF"

style fixed_text is text:
    font "fonts/Exo2.otf"

style no_border:
    activate_sound "sfx/click.ogg"

style no_border_text is fixed_text:
    color "#FFFFFF"
    hover_color "#b3b3b3"
    bold True
    size 17

style gallery_caption_text is cursive_text:
    color "#FFFFFF"
    xalign 0.5
    size 35

style button:
    background Frame("GUI/button_idle.png", 15, 15)
    hover_background Frame("GUI/button_selected.png", 15, 15)
    insensitive_background Frame("GUI/button_insensitive.png", 15, 15)
    selected_background Frame("GUI/button_selected.png", 15, 15)
    yminimum 40
    activate_sound "sfx/click.ogg"

style mm_button:
    background Frame("GUI/redorange_button_idle.png", 15, 15)
    hover_background Frame("GUI/redorange_button_selected.png", 15, 15)
    insensitive_background Frame("GUI/redorange_button_insensitive.png", 15, 15)
    selected_background Frame("GUI/redorange_button_selected.png", 15, 15)
    yminimum 40
    activate_sound "sfx/click.ogg"
    size_group "gm_nav"
    xpadding 20

style mm_button_text is cursive_text:
    color "#fff"
    insensitive_color "#666"
    xalign 0.5
    yalign 0.5
    size 35

style gm_nav_button is mm_button:
    xpadding 10

style gm_nav_button_text is mm_button_text:
    size 25

style gm_header is cursive_text:
    xalign 0.5
    yalign 0.0
    color "#fff"
    size 80

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

style nvl_note is nvl_dialogue:
    font "fonts/danielbd.ttf"
    color "#000000"

style nvl_window:
    background None

# Preferences Styles
style pref_frame:
    xfill True
    xmargin 5
    top_margin 0

style pref_label is label:
    xalign 0.5

style pref_label_text is sans_text:
    bold True
    color "#000"

style pref_vbox:
    #xfill True
    xalign 0.5
    ypadding 20

style pref_text:
    color "#000"

style pref_button:
    size_group "pref"
    xalign 0.5

style pref_slider is bar:
    xmaximum 200
    xalign 0.5

style soundtest_button:
    xalign 1.0

style prefs_label_text is gallery_caption_text

style prefs_label is label:
    xalign 0.5
