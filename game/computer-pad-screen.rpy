# Code to display our "Day Planner" -> "Month Planner" -> "Computer Pad" screen


screen computer_pad:
    tag menu
    
    window:
        hbox:
            #style_group = "cpad"
            xalign 0.5
            yalign 0.5
            # Left column
            vbox:  
                frame:
                    label _("Relationship")
                
                frame:
                    label _("Chat")
                    
                frame:
                    label _("Skill Status")
                
            # Middle column
            vbox:
                frame:
                    label _("Planner")
                
                frame:
                    label _("Message Board")
                    
            # Right column
            vbox:
                frame:
                    label _("South Camera View")
                    
                frame:
                    label _("Weather")
                
                frame:
                    textbutton _("GO!"):
                            action Return()