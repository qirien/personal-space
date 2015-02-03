# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:
    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False
    default tt = Tooltip("")
    
    # Use the quick menu.
    use quick_menu

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

        
     
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl
screen nvl:
    
    # I guess sometimes this is called with no dialogue, so I put in this check.
    if (dialogue):
        # use our message board screen unless it's a note        
        if (dialogue[0][0] != "note"):
            use message_board
            
        # it's a handwritten note
        else:
            add "bg/paper.jpg"
            window:
                style "nvl_window"
                xpadding 50
                ypadding 50

                yfill True
                xfill True

                has vbox:
                    style "nvl_vbox"

                # Display dialogue.
                for who, what, who_id, what_id, window_id in dialogue:
                    window:
                        id window_id

                        has hbox:
                            spacing 10

    #                    if who is not None:
    #                        text who id who_id

                        text what id what_id style "nvl_note" color "#000" font "fonts/danielbd.ttf"

                # Display a menu, if given.
                if items:

                    vbox:
                        id "menu"

                        for caption, action, chosen in items:

                            if action:

                                button:
                                    style "nvl_menu_choice_button"
                                    action action

                                    text caption style "nvl_menu_choice"

                            else:

                                text caption style "nvl_dialogue" color "#000" font "fonts/danielbd.ttf"

            add SideImage() xalign 0.0 yalign 1.0
        
        #use quick_menu
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    vbox:
        style_group "mm"
        xalign .98
        yalign .98

        if (renpy.newest_slot() is not None):
            $ recent_save = renpy.newest_slot("[^_]")
            if (recent_save is not None):
                $ recent_save_page, recent_save_name = recent_save.split("-")
                textbutton _("Continue") action FileLoad(recent_save_name, page=recent_save_page) text_size 42
                #textbutton _("Load Game") action ShowMenu("load")
        if (persistent.times_beaten):
            textbutton _("New Game+") action Start()
        else:
            textbutton _("New Game") action Start()
              
        textbutton _("Extras") action ShowMenu("extras")
        #textbutton _("Help") action Help()
        textbutton _("Config") action ShowMenu("preferences")                  
        textbutton _("Quit") action Quit(confirm=False)
        
        
##############################################################################
# Extras Screen
#
# Screen to access omake, image gallery, credits, etc.
#
screen extras:
    tag menu
    
    window:
        style "mm_root"
        
    vbox:
        style_group "mm"
        xalign 0.98
        yalign 0.98
        
        textbutton _("Return") action Return()
        if (persistent.got_all_endings):
            textbutton _("Omake") action Start("omake")
        textbutton _("Gallery") action ShowMenu("cg_gallery")
        textbutton _("Trailer") action Start("trailer")
        textbutton _("Credits") action Start("show_credits")


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    vbox:
        style_group "gm_nav"
        xalign .98
        yalign .98
        
        textbutton _("Return") action Return()
        textbutton _("Config") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        #textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.     
    
screen file_picker:
    tag menu

    frame:
        style "file_picker_frame"
        xalign 0.1
        yalign 0.1
        xmaximum 875
        xpadding 15

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            xalign 0.5
            
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            #textbutton _("Quick"):
            #    action FilePage("quick")

            for i in range(1, 5):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 2
                
        label _("")
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            spacing 10
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    # Format the description, and add it as text.
                    $ description = "% 2s. %s\n{b}%s{/b}" % (
                        FileSlotName(i, columns * rows),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))

                    text description

                    key "save_delete" action FileDelete(i)
                    
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu
    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu

    # Include the navigation.
    use navigation
    frame:
        background None
        xalign 0.1
        yalign 0.1
        
#        top_padding 40
#        bottom_padding 20
#        left_padding 50
#        right_padding 55

        # Put the navigation columns in a three-wide grid.
        grid 3 1:
            style_group "prefs"
            xfill True
            spacing 15
            

            # The left column.
            vbox:
                spacing 15
                label "Display Options" text_style
                
                frame:
                    style_group "pref"
                    has vbox
                    label _("Size")
                    hbox:
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                    label _("")
                    label _("Transitions")
                    hbox:
                        textbutton _("All") action Preference("transitions", "all")
                        textbutton _("None") action Preference("transitions", "none")

                    label _("")
                    label _("Text Speed")
                    bar value Preference("text speed")

                frame:
                    style_group "pref"
                    has vbox

                    textbutton _("Joystick...") action Preference("joystick")

            vbox:
                spacing 15
                label "Skipping Options"
                frame:
                    style_group "pref"
                    has vbox

                    label _("Skip")
                    hbox:
                        textbutton _("Seen Messages") action Preference("skip", "seen")
                        textbutton _("All Messages") action Preference("skip", "all")
                    
                    textbutton _("Begin Skipping") action Skip()

                    label _("")
                    label _("After Choices")
                    hbox:
                        textbutton _("Stop Skipping") action Preference("after choices", "stop")
                        textbutton _("Keep Skipping") action Preference("after choices", "skip")
                    
                    label _("")
                    label _("Auto Mode")
                    hbox:
                        textbutton _("Enabled") action Preference("auto-forward", "enable")
                        textbutton _("Disabled") action Preference("auto-forward", "disable")

                    label _("")
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
            
            vbox:
                spacing 15
                label "Audio Options"
                frame:
                    style_group "pref"
                    has vbox

                    label _("Music Volume")
                    bar value Preference("music volume")

                    label _("")
                    label _("Sound Volume")
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton "Test":
                            action Play("sound", config.sample_sound)
                            style "soundtest_button"

                    if config.sample_voice:
                        textbutton "Test":
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"



##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True
    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
        
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:
    zorder -1
    # Add an in-game quick menu.
    
    vbox:
        style_group "quick"
        xpos 55
        ypos 460
        spacing 12
        imagebutton:
            auto "gui/save_%s.png"
            action ShowMenu('save')
            hovered tt.Action("Save")
        imagebutton:
            auto "gui/config_%s.png"
            action ShowMenu('preferences')
            hovered tt.Action("Config")
        imagebutton:
            auto "gui/quit_%s.png"
            action Quit(confirm=True)
            hovered tt.Action("Quit")
    text tt.value ypos 420 xpos 55 outlines [(1, "#111", 1, 1)]