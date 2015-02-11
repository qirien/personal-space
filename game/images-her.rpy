# Load all the images for her and put them in the proper conditions.


# Script for auto finding images, called
# define_characters(folder, num_folders_to_exclude, include_flips)
init python:
    import os
    import re
    def define_characters(characterImageFolder, excludeFirstXFolders=0, flip=True):
        for path in renpy.list_files():
            if path.startswith(characterImageFolder + "/"):
                path_list = re.split("[/-]", path)
                path_list[-1] = os.path.splitext(path_list[-1])[0]
                path_list = tuple(path_list[excludeFirstXFolders:])
                renpy.image(path_list, path)
                if flip:
                    renpy.image(path_list + ("flip", ), im.Flip(path, horizontal=True))
                    
    # Load images for her
    #define_characters("sprites/her", 1)               

# Define images for her (nude, pregnant, dress, normal)
init python:
    her_expressions = ["angry", "annoyed", "concerned", "flirt", "happy", "laughing", "normal", "sad", "serious", "sleeping", "surprised", "yelling"]
    # For each expression, add a nude, pregnant, dress, and normal version
    for expression_name in her_expressions:
        renpy.image(("her", expression_name), ConditionSwitch(
            "is_nude", "sprites/her/nude-%s.png" % expression_name, 
            "is_pregnant and (month > 19) and (month <= 24)", "sprites/her/pregnant-%s.png" % expression_name,
            "wearing_dress", "sprites/her/dress-%s.png" % expression_name, 
            "True", "sprites/her/%s.png" % expression_name))
    
    # Also have one for no expression given
    renpy.image("her", ConditionSwitch(
        "is_nude", "sprites/her/nude-normal.png",
        "is_pregnant and (month > 19) and (month <= 24)", "sprites/her/pregnant-normal.png", 
        "wearing_dress", "sprites/her/dress-normal.png", 
        "True", "sprites/her/normal.png"))

label test_her_sprites:
    scene bg fields with fade
    
    "Normal Expressions"
    show her yelling at center with dissolve
    show her concerned with dissolve
    show her flirt with dissolve
    show her happy with dissolve
    show her laughing with dissolve
    show her sad with dissolve
    show her serious with dissolve
    show her surprised with dissolve
    
    "Nude Expressions"
    scene bg bedroom with fade
    $ is_nude = True
    show her yelling at center with dissolve
    show her concerned with dissolve
    show her flirt with dissolve
    show her happy with dissolve
    show her laughing with dissolve
    show her sad with dissolve
    show her serious with dissolve
    show her surprised with dissolve
    
    "Pregnant Expressions"
    scene bg farm_interior with fade    
    $ is_nude = False
    $ is_pregnant = True
    $ month = 23
    show her yelling at center with dissolve
    show her concerned with dissolve
    show her flirt with dissolve
    show her happy with dissolve
    show her laughing with dissolve
    show her sad with dissolve
    show her serious with dissolve
    show her surprised with dissolve
    
    "Dress Expressions"
    scene bg farm_exterior with fade    
    $ is_pregnant = False
    $ wearing_dress = True
    show her yelling at center with dissolve
    show her concerned with dissolve
    show her flirt with dissolve
    show her happy with dissolve
    show her laughing with dissolve
    show her sad with dissolve
    show her serious with dissolve
    show her surprised with dissolve

    "To Be Continued..."