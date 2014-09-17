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
                yfill True
                
                label "Personal Status"
                frame:
                    xfill True
                    has vbox
                    
                    label "Relationship"
                    text "Loved: [loved]"
                
                frame:
                    xfill True
                    has vbox
                    
                    label "Time"
                    text "Talaam: Year [year], month [month]"
                    text "Earth: Year [earth_year], month [earth_month]"
            
                frame:
                    # TODO: Make these bars?
                    xfill True
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
                    textbutton "Skills":
                        action Show("skill_screen")
                        # Test the new DSE here, but our custom one is better.
                        #action Show("display_stats")
                    
            # Middle column
            vbox:
                yfill True
                xalign 0.5
                
                label "Colony Status"
                frame:
                    xfill True
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
                    
                #TODO: Add music selector, remember track and show artist/title
                #      Dandelion, Shanghai, Alpha
                frame:
                    xfill True
                    xalign 0.5
                    textbutton "Colony Messages" xalign 0.5:
                        # TODO: make this work
                        action Jump("monthly_messages")
                        
            # Right column - skills
            vbox:
                yfill True
                xfill True
                use display_planner(periods)
                    
                
               
label monthly_messages:
        $ message = "msg_" + `month`
        nvl clear
        call expression message
        nvl clear
        # TODO: add the needed parameter here
        call screen computer_pad
 
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
            
        
