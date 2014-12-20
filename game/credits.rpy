# Credits
label show_credits:
    
    if (ending == "good"):
        play music "music/Blessed.ogg" fadeout 1.0
    else:
        play music "music/YouUndone.ogg" fadeout 1.0
    
    $ loved_ceiling = loved
    if (loved_ceiling > LOVED_MAX):
        $ loved_ceiling = LOVED_MAX
        
    if (loved_ceiling < 0):
        $ loved_ceiling = 0
    
    $ community_ceiling = community_level
    if (community_ceiling > COMMUNITY_LEVEL_MAX):
        $ community_ceiling = COMMUNITY_LEVEL_MAX
        
    "You scored [loved_ceiling] out of [LOVED_MAX] relationship points, and [community_ceiling] out of [COMMUNITY_LEVEL_MAX] comunity points."
    
    # TODO: show images from the game during this?  omake?
    # TODO: Double check EVERYTHING we used is in here!  Check Credits.txt, music, sfx, bg directories
    
    # If the user has beat the game before, allow them to skip the credits.
    $ skippable = not persistent.times_beaten
    scene black with fade
    hide text with fade
    show text "Credits" with fade
    $ renpy.pause(2.0, hard=skippable)
    hide text with fade
    show text "Written, Produced, and Directed by Andrea Landaker" with fade 
    $ renpy.pause(3.0, hard=skippable)
    hide text with fade
    show text "Additional Writing and Design by Rachel Helps" with fade 
    $ renpy.pause(3.0, hard=skippable)
    hide text with fade
    show text "Character Art by {a=http://clarissahelps.com}Clarissa Helps{/a}" with fade 
    $ renpy.pause(3.0, hard=skippable)
    hide text with fade
    show text "With music by:\nEhren Starks\nJan Hanford\nChad Lawson\nGiorgio Costantini\nKalabi\nBenji Goodrich\nGianmarco Leona\nFalling You\nRuben van Rompaey\nDa Camera\nWillem Brons\n\nLicensed from {a=http://www.magnatune.com}Magnatune{/a} under the {a=http://creativecommons.org/licenses/by-nc-sa/1.0/}BY-NC-SA Creative Commons License{/a}" with fade
    $ renpy.pause(6.0, hard=skippable)
    hide text with fade     
    show text "With background images by:\nLisa Horner\nWes Landaker\nAndrea Landaker\nNASA\nBurningwell\nESO/L. Calçada\n\nAnd the following Wikimedia Commons users:\nRandwick\nLabpluto123\nWrlctech\nEbyabe\nAvi/Skrewtap\nMarcus Budde\nAluter\nDorothea Witter-Rieder\nAnna Frodesiak\nAndrei Stroe\nJean-Pierre\n\nFiltered with Fotosketcher" with fade
    $ renpy.pause(8.0, hard=skippable)
    # TODO: Add sound Credits
    
    hide text with fade
    show text "Beta Testing by:\nWes Landaker\nLisa Horner\nCatherine White"
    $ renpy.pause(6.0, hard=skippable)
    
    hide text with fade   
    show text "The code for this work is licensed under the {a=http://www.gnu.org/licenses/gpl.html}GPL{/a}, and the media is licensed under a {a=http://creativecommons.org/licenses/by-nc-sa/4.0/}Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License{/a}." with fade 
    $ renpy.pause(3.0, hard=skippable)
    
    hide text with fade   
    show text "Made with Ren'Py" with fade 
    $ renpy.pause(3.0, hard=skippable)
    hide text with fade

    scene bg stars with fade
    "You have now unlocked New Game+! If you play again, you can keep your progress in your skills up to level [SKILL_SAVED_MAX], to make mastering skills easier and to be able to see more of the events."
    
    # in case a future game wants to use this information, we'll save it here
    $ mp.jack_name = his_name
    $ mp.kelly_name = her_name
    $ mp.baby_name = baby_name
    $ mp.save()
    
    # New Game+ saving of skills here
    $ persistent.skill_domestic = save_skill(persistent.skill_domestic, skill_domestic)
    $ persistent.skill_creative = save_skill(persistent.skill_creative, skill_creative)
    $ persistent.skill_technical = save_skill(persistent.skill_technical, skill_technical)    
    $ persistent.skill_spiritual = save_skill(persistent.skill_spiritual, skill_spiritual)
    $ persistent.skill_social = save_skill(persistent.skill_social, skill_social)    
    $ persistent.skill_knowledge = save_skill(persistent.skill_knowledge, skill_knowledge)
    $ persistent.skill_physical = save_skill(persistent.skill_physical, skill_physical)
    
    if not persistent.times_beaten:
        $ persistent.times_beaten = 1
    else:
        $ persistent.times_beaten += 1
        
    # TODO: Also unlock images for an image gallery, if we have CGs...
    if (persistent.got_good_ending and persistent.got_mediocre_ending and persistent.got_bad_ending):
        if (not persistent.got_all_endings):
            "You have experienced all the endings and unlocked the Omake from the Main Menu!"
        $ persistent.got_all_endings = True
        
    "Thanks for playing! If you have feedback, I'd love to hear from you at {a=mailto:qirien@icecavern.net?subject=Our Personal Space}qirien@icecavern.net{/a}"
    show text "{size=80}{font=fonts/danielbd.ttf}{b}The End{/b}{/font}{/size}" with fade
    stop music fadeout 1.0
    $ renpy.pause(5.0, hard=skippable)
    
    $ renpy.full_restart()
