# Code to display our "Computer Pad" screen for planning the month, viewing skills,
# reading colony messages, etc.

# Clarissa says: it would be nice if the horizontal spaces lined up more so it looks less busy.
# Or separate out into different screens? Or combine boxes?

style cp_text is text:
    color "#222"
    
style cp_label_text is label_text:
    color "#222"
    size 20
    
style cp_label is label:
    xalign 0.5
    
style cp_choice_button is button:
    size_group "cp_choice_button"

screen computer_pad(periods):
    #tag month_menu
    $ renpy.choice_for_skipping()

    add "bg/silk-gray.jpg"
    add "bg/computer-pad.png"
            
    text "User {color=#888}[her_name]{/color} has logged on." size 12 xalign 0.1 ypos 20 color "FFFFFF"
    frame:
        style_group "cp"
        background None
        
        # fit our window to the size of the computer screen
        xpadding 50
        ypadding 35

        yfill True
        xfill True
        has vbox
        
        grid 3 1:
            xfill True
            spacing 5
            #has hbox
            
            # Left column
            vbox:
                yalign 0.0
                
                label "Personal Status"
                # TODO: Make these bars?
                frame:
                    xfill True
                    ypos 10
                    has vbox
                    
                    label "Relationship"
                    use heart_display
                
                frame:
                    xfill True
                    ypos 30
                    vbox:
                        xfill True
                        
                        label "Time"
                        text "Talaam: Year [year], month [local_month]"
                        text "Earth: Year [earth_year], month [earth_month]"
                        $ shuttle_months = 25-month
                        text "{i}{size=14}[shuttle_months] months until shuttle arrives.{/size}{/i}"
                
                frame:
                    xfill True
                    ypos 60
                    vbox:
                        xfill True
                        
                        
                        # Display health stats based on month, pregnancy, stress, etc.
                        label "Health"
                        if ((is_pregnant or is_pregnant_later) and (trimester != "third")):
                            text "Blood Pressure... {color=FF0000}Low{/color}"
                            text "Pulse Rate...{color=FF0000}Fast{/color}"
                        elif (relaxed <= -5):
                            text "Blood Pressure... {color=FF0000}High{/color}"
                            text "Pulse Rate...{color=FF0000}Fast{/color}"
                        else:
                            text "Blood Pressure... {color=00FF00}OK{/color}"
                            text "Pulse Rate...{color=00FF00}OK{/color}"
                        if ((month == 14) or (month == 24)):
                            text "Temperature...{color=FF0000}High{/color}"
                        else:
                            text "Temperature...{color=00FF00}OK{/color}"
                        
                        if (is_pregnant or is_pregnant_later):
                            text "Pregnancy: [trimester] trimester."
                            
                frame:
                    # TODO: this should be aligned with Colony Messages?
                    xalign 0.5
                    ypos 70
                    textbutton "Skills":
                        action Show("skill_screen")
                    
            # Middle column
            vbox:
                xalign 0.5
                
                label "Colony Status"
                frame:
                    xfill True
                    ypos 10
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
                    text "Season: [season]"
                    text "Weather: [weather]"
                    
                # TODO: have something to report community_level ?
                frame:
                    xfill True
                    xalign 0.5
                    ypos 30
                    textbutton "Colony Messages" xalign 0.5:
                        action Jump("monthly_messages")
                        
                frame:
                    xfill True
                    ymaximum 100
                    ypos 60
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
                        
                    if (current_song):
                        text "{i}[song_title]{/i} by [artist]" size 14 ypos 30 xalign 0.5
                    imagebutton auto "gui/previous_%s.png" xalign 0.3 yalign 1.0 action pop_songs.Previous()
                    if (renpy.music.is_playing()):
                        imagebutton auto "gui/pause_%s.png" xalign 0.5 yalign 1.0 action pop_songs.Stop()
                    else:
                        imagebutton auto "gui/play_%s.png" xalign 0.5 yalign 1.0 action pop_songs.Play()
                    imagebutton auto "gui/next_%s.png" xalign 0.7 yalign 1.0 action pop_songs.Next()

                        
            # Right column - skills
            vbox:
                xfill True
                use display_planner(periods)
     
    # Start music every time this screen is shown if it's not already playing.
    on "show" action If(renpy.music.is_playing(), true=None, false=pop_songs.RandomPlay())
                
label monthly_messages:
    $ message = "msg_" + `month`
    nvl clear
    call expression message
    computer "(End of messages)"
    nvl clear
    call screen computer_pad(["Work", "Skills", "Free Time"])
 
# Display our skills in a window on top of the computer pad
screen skill_screen:
        frame:
            style_group "cp"
            yalign 0.5
            xalign 0.5
            has vbox
            frame:
                xpadding 45
                ypadding 20
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
                
                textbutton _("Return"):
                        xalign 1.0
                        yalign 1.0
                        action Hide("skill_screen")
    
screen grid_test:
    frame:
        xfill True
        yfill True
        has vbox
        
        grid 3 1:
            xfill True
            vbox:
                text "grid1"
            vbox:
                text "grid2"
            vbox:
                text "grid3"
        
        hbox:
            xfill True
            vbox:
                frame:
                    text "hbox1"
            vbox:
                frame:
                    text "hbox2"
            vbox:
                frame:
                    text "hbox3"
        textbutton "Return":
            action Hide("grid_test")
            
            
screen heart_display:
    hbox:
        # Add a small headshot of her depending on how relaxed/stressed she is
        if (relaxed >= 10):
            add "her happy head"
        elif (relaxed >= 0):
            add "her normal head"
        elif (relaxed >= -5):
            add "her concerned head"
        else:
            add "her sad head"

        # Add a heart whose size depicts their relationship status
        if (loved >= LOVED_MAX):
            add "GUI/heart-largest.png"
        elif (loved >= (LOVED_MAX/1.5)):
            add "GUI/heart-larger.png"
        elif (loved >= (LOVED_MAX/3)):
            add "GUI/heart-large.png"
        elif (loved >= (LOVED_MAX/6)):
            add "GUI/heart-normal.png"
        elif (loved >= 0):
            add "GUI/heart-small.png"
        elif (loved >= -(LOVED_MAX/6)):
            add "GUI/heart-smaller.png"
        else:
            add "GUI/heart-smallest.png"
        
        # Add a small headshot of him depending on his mood.
        if (month < 4):
            add "him happy head"
        elif (month == 5):
            add "him normal head"
        elif (month == 6):
            add "him concerned head"
        elif (month == 10):
            add "him concerned head"
        elif (month == 12):
            add "him annoyed head"            
        elif (month == 13):
            add "him concerned head"
        elif (month == 15):
            add "him happy head"
        elif (month == 19):
            add "him annoyed head"
        elif (month == 20):
            add "him normal head"
        elif (month == 21):
            add "him concerned head"
            
        # If no special event, then his mood based on love stat
        else:
            if (loved >= 5):
                add "him happy head"
            elif (loved >= 0):
                add "him normal head"
            elif (loved >= -5):
                add "him concerned head"
            else:
                add "him annoyed head"
            
