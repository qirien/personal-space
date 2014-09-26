# Code to display our "Computer Pad" screen for planning the month, viewing skills,
# reading colony messages, etc.

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
    tag month_menu
    $ renpy.choice_for_skipping()

    # TODO: should you be able to change the wallpaper here?!
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
                    has vbox
                    
                    label "Time"
                    text "Talaam: Year [year], month [month]"
                    text "Earth: Year [earth_year], month [earth_month]"
            
                frame:
                    xfill True
                    ypos 60
                    has vbox
                    
                    label "Health"
                    if (month == 14):
                        text "You are in poor health."
                    else:
                        text "You are in good health."
                    
                    $ stress_level = "normal"
                    if (relaxed <= -5):
                        $ stress_level = "high"
                    elif (relaxed >= 5):
                        $ stress_level = "low"
                    text "Your stress level is [stress_level]."
                    if (is_pregnant or is_pregnant_later):
                        text "Trimester: [trimester]"                
                        
                frame:
                    xalign 0.5
                    ypos 100
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
                    if season == "summer":
                        add "bg/weather-summer.jpg" xalign 0.5
                    elif season == "fall":
                        add "bg/weather-fall.jpg" xalign 0.5
                    elif season == "winter":
                        add "bg/weather-winter.jpg" xalign 0.5
                    else:
                        add "bg/weather-spring.jpg" xalign 0.5
                    text "Season: [season]"
                    text "Weather: [weather]"
                    
                frame:
                    xfill True
                    ymaximum 100
                    ypos 30
                    label "Music Player"
                    # TODO: after reloading, music does not play? or shows as "None"?
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
                frame:
                    xfill True
                    xalign 0.5
                    ypos 60
                    textbutton "Colony Messages" xalign 0.5:
                        action Jump("monthly_messages")
                        
            # Right column - skills
            vbox:
                xfill True
                use display_planner(periods)
     
    # Start music every time this screen is shown
    on "replace" action pop_songs.Play()
                

# TODO: using a jump messes up our call stack here, so the next things won't work
label monthly_messages:
    $ message = "msg_" + `month`
    nvl clear
    call expression message
    computer "(End of messages)"
    nvl clear
    call screen computer_pad(["Work", "Skills", "Free Time"])
 
# Display our skills in a window on top of the computer pad
# TODO: Make sure the order matches the order on the Skill Button section.
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
    $ image_name = "GUI/heart-normal.png"
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
    
        
