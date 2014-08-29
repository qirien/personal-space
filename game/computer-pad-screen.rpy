# Code to display our "Day Planner" -> "Month Planner" -> "Computer Pad" screen

style cp_text is text:
    color "#000"
    
style cp_label_text is label_text:
    bold True
    size 20
    
style cp_label is label:
    xalign 0.5
    
style cp_choice_button is button:
    size_group "cp_choice_button"

screen computer_pad:
    tag month_menu

    add "bg/computer-pad.png"
    frame:
        style_group "cp"
        background None
        
        # fit our window to the size of the computer screen
        xpadding 50
        ypadding 25

        yfill True
        xfill True
        has vbox
        
        text "Welcome, [her_name]." size 30 xalign 0.5 bold True
        #textbutton "GridTest":
        #    action Show("grid_test")
       # hbox:
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
                    
            # Middle column - skills
            # TODO: make these buttons that integrate with DSE
            # TODO: Incorporate new DSE
            vbox:
                yfill True
                label "Focus"
                frame:
                    xfill True
                    has vbox
                    
                    label "Work"
                    hbox:
                        style_group "cp_choice"
                        xfill True
                        textbutton "Do your best!"
                        textbutton "Take it easy"
                
                frame:
                    xfill True
                    has vbox
                    
                    label "Skills"                    
                    grid 2 4:
                        style_group "cp_choice"
                        xfill True
                        textbutton "Domestic"
                        textbutton "Physical"
                        textbutton "Creative"
                        textbutton "Technical"
                        textbutton "Social"
                        textbutton "Knowledge"
                        textbutton "Spiritual"
                        text ""
                    
                frame:
                    xfill True
                    has vbox
                    
                    label "Free Time"
                    hbox:
                        style_group "cp_choice"
                        xfill True
                        textbutton "Together"
                        textbutton "Alone"
                    
            # Right column
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
                    
                frame:
                    xfill True
                    xalign 0.5
                    textbutton "Colony Messages" xalign 0.5:
                        action Jump("monthly_messages")
                
                frame:
                    xalign 0.9
                    yalign 0.9
                    textbutton _("GO!"):
                            action Return()    
    
label monthly_messages:
        $ message = "msg_" + `month`
        nvl clear
        call expression message
        nvl clear  
        call screen computer_pad
        
screen computer_pad_imagemap:        
    imagemap:
        ground "gui/monthmenu-base.png"
        idle "gui/monthmenu-idle.png"
        hover "gui/monthmenu-hover.png"
        
        hotspot (268, 117, 70, 60) action SetVariable(job_focus_act, "act_work")
        hotspot (268, 561, 46, 43) action Jump("room_computer3")        
        hotspot (0,0, 10, 10) action Start("job_focus")
        #style_group = "cpad"
        xalign 0.5
        yalign 0.5
        
 
screen skill_screen:
    frame:
        style_group "cp"
        xpadding 45
        ypadding 20
        yalign 0.5
        xalign 0.5
        has vbox
        label "Skills"
        grid 2 4:
            spacing 25
            $ v = 0
            for s in dse_stats:
                vbox:
                    xmaximum 200
                    xalign 0.5
                    $ v = getattr(store, s.var)
                    hbox:
                        xfill True
                        text s.name xalign 0.0
                        text "%d/%d" % (v, s.max) xalign 1.0
                    bar value v range s.max
                    
            vbox:
                text ""
            
        frame:
            xalign 1.0
            yalign 1.0
            textbutton _("Return"):
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
            
        
