# Code to display our "Computer Pad" screen for planning the month, viewing skills,
# reading colony messages, etc.

style cp_text is sans_text:
    color "#222"
    
style cp_label_text is sans_text:
    color "#000"
    #size 18
    bold True

style cp_header_text is sans_text:
    color "#FFF"
    size 22
    #bold True    
    
style cp_label is label:
    xalign 0.5
    
style cp_choice_button is button:
    size_group "cp_choice_button"

screen computer_pad(periods):
    tag month_menu

    add "bg/silk-gray.jpg"
    add "bg/computer-pad.png"
            
    text "{font=fonts/Exo2.otf}User {color=#888}[her_name]{/color} has logged on.{/font}" size 12 xalign 0.1 ypos 20 color "FFFFFF" alt ""
    textbutton "?" xpos 877 ypos 18 style "no_border" action Jump("tutorial_ask") alt "Tutorial"
    textbutton "             " xpos 885 ypos 18 style "no_border" action ShowMenu("preferences") keyboard_focus False

    frame:
        style_group "cp"
        background None
        
        # fit our window to the size of the computer screen
        top_padding 40
        bottom_padding 20
        left_padding 50
        right_padding 55

        yfill True
        xfill True
        has vbox
        
        grid 3 1:
            xfill True
            spacing 15
            #has hbox
            
            # Left column
            vbox:
                yalign 0.0
                
                label "Personal Status" text_style "cp_header_text"
                frame:
                    xfill True
                    ypos 10
                    ysize 140
                    has vbox
                    
                    label "Relationship"
                    use heart_display(month, loved, relaxed)
                
                frame:
                    xfill True
                    ypos 25
                    ysize 118
                    vbox:
                        xfill True
                        
                        label "Time"
                        text "Talaam: Year [year], month [local_month]"
                        text "Earth: Year [earth_year], month [earth_month]"
                        $ shuttle_months = 25-month
                        if (month >= 2):
                            text "{i}{size=14}[shuttle_months] months until shuttle arrives.{/size}{/i}"
                
                frame:
                    xfill True
                    ypos 40
                    ysize 148
                    vbox:
                        xfill True
                        
                        use health_stats(month, is_pregnant, is_pregnant_later, trimester, relaxed)
                
            # Middle column
            vbox:
                xalign 0.5
                
                label "Colony Status" text_style "cp_header_text"
                frame:
                    xfill True
                    ypos 10
                    ysize 275
                    has vbox
                    xalign 0.5
                    
                    label "South Camera View"
                    if (season == "summer"):
                        add "bg/weather-summer.jpg" xalign 0.5
                    elif (season == "fall"):
                        add "bg/weather-fall.jpg" xalign 0.5
                    elif (season == "winter"):
                        add "bg/weather-winter.jpg" xalign 0.5
                    else:
                        add "bg/weather-spring.jpg" xalign 0.5
                    text ""
                    $ upper_season = season.capitalize()
                    $ upper_weather = weather.capitalize()
                    text "Season: [upper_season]"
                    text "Weather: [upper_weather]"
                    
                use colony_messages_button(read_messages)
                
                frame:
                    xfill True
                    ysize 100
                    ypos 10
                    use music_player()
                    
            # Right column - skills
            vbox:
                xfill True
                use display_planner(periods)
                
    # Start music every time this screen is shown if it's not already playing.
    on "show" action If(renpy.music.is_playing(), true=None, false=pop_songs.RandomPlay())
                
# Screen to show "NEW" if unread, and colony messages button
# This is a separate screen so that we can make it update with the read_colony_messages variable
screen colony_messages_button(read_colony_messages):
    if (not read_colony_messages):
        text "{color=#FF0}{b}NEW!{/b}{/color} " ypos 30 xalign 0.0 outlines [(1, "#000", 1, 1)] alt "New Messages"
    else:
        text "" ypos 30 xalign 0.0 # We have to have this here or it messes up all the positions
    
    textbutton "Colony Messages" xalign 0.5:
        action Jump("monthly_messages")                        

# Music Player that shows current track, previous, stop/play, and next buttons
screen music_player():
    label "Music Player"
    $ current_song = renpy.music.get_playing()
    $ artist = ""
    $ song_title = ""
    if (current_song):
        if "Dandelion" in current_song:
            $ artist = "Kalabi"
            $ song_title = "Dandelion"
        elif "Shanghai" in current_song:
            $ artist = "Attic Trax"
            $ song_title = "Shanghai 20 00"
        elif "Alpha" in current_song:
            $ artist = "TranceVision"
            $ song_title = "Alpha"
        elif "YouUndone" in current_song:
            $ artist = "Anonymph"
            $ song_title = "You Undone"
        
    if (current_song):
        text "{i}[song_title]{/i} by [artist]" size 14 ypos 30 xalign 0.5
    else:
        text "Stopped" size 14 ypos 30 xalign 0.5 alt "Music Stopped"
    imagebutton auto "gui/previous_%s.png" xalign 0.3 yalign 1.0 alt "Previous Song" action [
        pop_songs.Previous(),
        renpy.restart_interaction # This makes the screen refresh after we switch songs.
        ]
    if (renpy.music.is_playing()):
        imagebutton auto "gui/pause_%s.png" xalign 0.5 yalign 1.0 alt "Pause Music" action [
            pop_songs.Stop(),
            renpy.restart_interaction
            ]           
    else:
        imagebutton auto "gui/play_%s.png" xalign 0.5 yalign 1.0 alt "Play Music" action [
            pop_songs.Play(),
            renpy.restart_interaction
            ]           
    imagebutton auto "gui/next_%s.png" xalign 0.7 yalign 1.0 alt "Next Song" action [
        pop_songs.Next(),
        renpy.restart_interaction
        ]        
    
                
label monthly_messages:
    $ message = "msg_" + `month`
    $ read_messages = True
    nvl clear
    call expression message from _call_expression
    computer "\n(End of messages)"
    nvl clear
    call screen computer_pad(["Work", "Skills", "Free Time"])
 
# Display our skills in a window on top of the computer pad
screen skill_screen():
    modal True
    zorder 1
    frame:
        style_group "cp"
        yalign 0.5
        xalign 0.5
        has vbox
        label "Skills"
        grid 2 4:
            spacing 20
            $ v = 0
            for s in dse_stats:
                frame:
                    vbox:
                        xmaximum 250
                        xalign 0.5
                        $ v = getattr(store, s.var)
                        hbox:
                            xfill True
                            text s.name xalign 0.0
                            text "%d/%d" % (v, s.max) xalign 1.0
                        bar value v range s.max
                        
            vbox:
                text ""
        
        textbutton _("Done"):
            xalign 1.0
            yalign 1.0
            action Hide("skill_screen")
    
            
screen heart_display(month, loved, relaxed):
    hbox:
        # Add a small headshot of her depending on how relaxed/stressed she is
        if (relaxed >= 10):
            add "her happy head"
            text "" alt "her mood: happy"
        elif (relaxed >= 0):
            add "her normal head"
            text "" alt "her mood: content"
        elif (relaxed >= -5):
            add "her concerned head"
            text "" alt "her mood: concerned"
        else:
            add "her sad head"
            text "" alt "her mood: stressed"

        # Add a heart whose size depicts their relationship status
        if (loved > LOVED_MAX):
            add "GUI/heart-full.png"
            text "" alt "love: maximum"
        elif (loved >= (LOVED_MAX/1.3)):
            add "GUI/heart-largest.png"
            text "" alt "love: very high"
        elif (loved >= LOVED_GOOD):
            add "GUI/heart-larger.png"
            text "" alt "love: high"
        elif (loved >= (LOVED_MAX/3)):
            add "GUI/heart-large.png"
            text "" alt "love: medium high"
        elif (loved >= (LOVED_MAX/6)):
            add "GUI/heart-normal.png"
            text "" alt "love: medium"
        elif (loved >= 0):
            add "GUI/heart-small.png"
            text "" alt "love: low"
        elif (loved >= -(LOVED_MAX/6)):
            add "GUI/heart-smaller.png"
            text "" alt "love: very low"
        else:
            add "GUI/heart-smallest.png"
            text "" alt "love: none"
        
        # Add a small headshot of him depending on his mood.
        if (month < 4):
            add "him happy head"
            text "" alt "his mood: happy"
        elif (month == 5):
            add "him normal head"
            text "" alt "his mood: content"
        elif (month == 6):
            add "him concerned head"
            text "" alt "his mood: worried"
        elif (month == 10):
            add "him concerned head"
            text "" alt "his mood: worried"
        elif (month == 12):
            add "him annoyed head"
            text "" alt "his mood: annoyed"            
        elif (month == 13):
            add "him concerned head"
            text "" alt "his mood: worried"
        elif (month == 15):
            add "him happy head"
            text "" alt "his mood: happy"
        elif (month == 19):
            add "him annoyed head"
            text "" alt "his mood: annoyed"
        elif (month == 20):
            add "him normal head"
            text "" alt "his mood: content"
        elif (month == 21):
            add "him concerned head"
            text "" alt "his mood: worried"
            
        # If no special event, then his mood based on love stat
        else:
            if (loved >= 5):
                add "him happy head"
                text "" alt "his mood: happy"
            elif (loved >= 0):
                add "him normal head"
                text "" alt "his mood: content"
            elif (loved >= -5):
                add "him concerned head"
                text "" alt "his mood: worried"
            else:
                add "him annoyed head"
                text "" alt "his mood: annoyed"

screen health_stats(month, is_pregnant, is_pregnant_later, trimester, relaxed):
    # Display health stats based on month, pregnancy, stress, etc.
    label "Health"
    if ((is_pregnant or is_pregnant_later) and (trimester != "third")):
        text "Blood Pressure... {color=EA0000}Low{/color}"
        text "Pulse Rate...{color=EA0000}Fast{/color}"
    elif (relaxed <= -5):
        text "Blood Pressure... {color=EA0000}High{/color}"
        text "Pulse Rate...{color=EA0000}Fast{/color}"
    else:
        text "Blood Pressure... {color=00AA00}OK{/color}"
        text "Pulse Rate...{color=00AA00}OK{/color}"
    if ((month == 14) or (month == 24)):
        text "Temperature... {color=EA0000}High{/color}"
    else:
        text "Temperature... {color=00AA00}OK{/color}"
    
    if ((is_pregnant or is_pregnant_later) and (trimester != "done")):
        text "Pregnancy... [trimester] trimester"