﻿## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## These control the width and height of the screen.

    config.screen_width = 1024
    config.screen_height = 600

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = "Our Personal Space"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Our Personal Space"
    config.version = "1.4"
    
    config.window_icon = "GUI/window-icon.png"
    config.windows_icon = "GUI/windows-icon.png"

    config.load_failed_label = "day" #If it can't find where to return to, just replay the current month

    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.a_white_tulip(
        ## Theme: A White Tulip
        ## Scheme Muted Horror

        ## The color of an idle widget face.
        widget = "#777777",

        ## The color of a focused widget face.
        widget_hover = "#73735C",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#000000",

        ## The color of a disabled widget face.
        disabled = "#73735C",

        ## The color of a frame containing widgets.
        frame = "#555544",
        
        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "bg/title-screen.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "bg/silk-gray.jpg",

        ## The fonts used by this theme. The default fonts may not be
        ## suitable for non-English languages.
        regular_font = serif_font
        #bold_font = "DejaVuSerifBold.ttf",

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    # style.window.background = Frame("frame.png", 12, 12)
    style.window.background = Frame("GUI/textbox-frame.png", 80, 80)    

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 100
    style.window.right_margin = 100
    style.window.top_margin = 0
    style.window.bottom_margin = 0

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 25
    style.window.right_padding = 25
    style.window.top_padding = 15
    style.window.bottom_padding = 15

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 150


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = serif_font
    style.default.color="#FFFFFF"

    ## The default size of text.

    style.default.size = 19

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    #style.button.activate_sound = "sfx/click.mp3"
    #style.imagemap.activate_sound = "sfx/click.mp3"

    ## Sounds that are used when entering and exiting the game menu.

    config.enter_sound = "sfx/click.ogg"
    config.exit_sound = "sfx/click.ogg"

    ## A sample sound that can be played to check the sound volume.

    config.sample_sound = "sfx/message.mp3"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "music/LinesBuildWalls.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "Renpy-help.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = dissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolve

    ## Used between screens of the game menu.
    config.intra_transition = dissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = dissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = dissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = dissolve

    ## Used when a game is loaded.
    config.after_load_transition = dissolve

    ## Used when the window is shown.
    config.window_show_transition = dissolve

    ## Used when the window is hidden.
    config.window_hide_transition = dissolve
    
    ## Used when going from ADV to NVL, and vice versa
    config.adv_nvl_transition = zoomin
    config.nvl_adv_transition = zoomout

    # add a default dissolve transition between each say if no other transition is speficied
    config.say_attribute_transition = { "master" : Dissolve(0.5, alpha=True) }


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "OurPersonalSpace-1347408413"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 70

    #########################################
    ## More customizations can go here.
    
    config.thumbnail_width = 280
    config.thumbnail_height = 164
    
    # We only autosave monthly, on quit, or every 500 interactions
    config.autosave_on_choice = False
    config.autosave_frequency = 500
                       
## This section contains information about how to build your project into 
## distribution files.
init python:
    
    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "OurPersonalSpace-1.4"
    
    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "OurPersonalSpace"
    
    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False
    
    ## File patterns:
    ## 
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##    
    ##
    ## In a pattern:
    ##
    ## / 
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('art/**', None)
    build.classify('game/saves/**', None) #don't distribute saved games
    build.classify('game/google-play.rpy', None) #This is a private, secret file that should not be distributed!
    
    ## To archive files, classify them as 'archive'.
    
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
