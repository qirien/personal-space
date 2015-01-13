########################################################
#   Android keyboard input
init python:
    text_list1=[["Q","W","E","R","T","Y","U","I","O","P"],
                ["A","S","D","F","G","H","J","K","L"],
                ["Z","X","C","V","B","N","M"]]
    text_list2=[["q","w","e","r","t","y","u","i","o","p"],
                ["a","s","d","f","g","h","j","k","l"],
                ["z","x","c","v","b","n","m"]]
    input_text = ""
    text_list=text_list1
    text_group=1
    initial_caps=True
    caps_lock = False
    
style inputter_text is sans_text:
    color "000000"
    size 30
    
style inputter_button_text is sans_text:
    size 30
    
style inputter_keys:
    font "fonts/courbd.ttf"
    size 40    

screen inputter(input_header="NAME:"):
    default caps_lock = False
    default input_text = ""
    if initial_caps:
        $ caps_lock = True
        $ initial_caps = False
    if caps_lock:
        $text_list=text_list1
    else:
        $text_list=text_list2
         
    frame:
        style_group "inputter"        
        xpos 0.5
        ypos 0.1
        xanchor 0.5
        yanchor 0
        xminimum 450

        vbox:
            $ display_text = input_header+" "+input_text
            text display_text
            text ""
            hbox:
                xalign 0.5
                textbutton "Backspace" action SetScreenVariable("input_text", input_text[:-1])
                textbutton "Delete all" action [ SetScreenVariable("input_text", ""),
                                                 SetScreenVariable("initial_caps", True) ]
                if (not caps_lock):
                    textbutton "Caps (On)" action SetScreenVariable("caps_lock", True)
                else:
                    textbutton "Caps (Off)" action SetScreenVariable("caps_lock", False)
            text ""
            vbox:
                xalign 0.5
                for text_row in text_list:
                    hbox:
                        xalign 0.5
                        for text_code in text_row:
                            textbutton text_code text_style "inputter_keys" action [ SetScreenVariable("input_text", input_text + text_code),
                                                          SetScreenVariable("caps_lock", False) ]
                text ""
                textbutton "Done" xalign 0.5 action Return(input_text)

