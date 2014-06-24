# Code to display our "Day Planner" -> "Month Planner" -> "Computer Pad" screen

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
            
        


screen computer_pad:
    tag month_menu
    
    frame:
        yfill True
        xfill True
        has vbox
        
        text "Welcome, [her_name]." size 30
        textbutton "GridTest":
            action Show("grid_test")
       # hbox:
        grid 3 1:
            xfill True
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
                    text "Talaam: Year %(year)d, month %(local_month)d"
                    text "Earth: Year %(earth_year)d, month %(earth_month)d"
            
                frame:
                    xfill True
                    has vbox
                    
                    label "Health"
                    if (month == 14):
                        text "You are in fair health."
                    else:
                        text "You are in good health."
                    if (is_pregnant or is_pregnant_later):
                        text "Trimester: [trimester]"                
                        
                frame:
                    xalign 0.5
                    textbutton "Skills":
                        action Show("skill_screen")
                    
            # Middle column - skills
            # TODO: make these buttons that integrate with DSE
            vbox:
                yfill True
                label "Focus"
                frame:
                    xfill True
                    has vbox
                    
                    label "Work"
                    vbox:
                        text "Do your best!"
                        text "Take it easy"
                
                frame:
                    xfill True
                    has vbox
                    
                    label "Skills"
                    text "Domestic"
                    text "Physical"
                    text "Creative"
                    text "Technical"
                    text "Social"
                    text "Knowledge"
                    text "Spiritual"
                    
                frame:
                    xfill True
                    has vbox
                    
                    label "Free Time"
                    vbox:
                        text "Together"
                        text "Alone"
                    
            # Right column
            vbox:
                yfill True
                
                label "Colony Status"
                frame:
                    xfill True
                    has vbox
                    
                    label "South Camera View"
                    text "Season: [season]"
                    text "Weather: [weather]"
                    
                frame:
                    xfill True
                    label "Colony Messages"            
                
                frame:
                    xalign 1.0
                    yalign 1.0
                    textbutton _("GO!"):
                            action Return()    
    
        
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
        label _("Display Stats Here")
        
    frame:
        textbutton _("Return"):
            action Return()
    