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
    her_expressions = ["angry", "annoyed", "concerned", "flirt", "happy", "laughing", "normal", "sad", "serious", "sleeping", "surprised"]
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
    show her pregnant at left
    "Pregnant Expressions"
    $ is_pregnant = True
    show her angry at right with fade
    show her concerned at quarterright with fade
    show her flirt at midright with fade
    show her happy at center with fade
    show her laughing at midleft with fade
    show her sad at quarterleft with fade
    show her serious at left with fade
    show her surprised at center with fade
    
    "Dress Expressions"
    $ is_pregnant = False
    $ wearing_dress = True
    show her angry at right with fade
    show her concerned at quarterright with fade
    show her flirt at midright with fade
    show her happy at center with fade
    show her laughing at midleft with fade
    show her sad at quarterleft with fade
    show her serious at left with fade
    show her surprised at center with fade

    "To Be Continued..."