# Credits
label show_credits:
    scene black with fade
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
   
    if (ending != "none"):   
        "You scored [loved_ceiling] out of [LOVED_MAX] relationship points, and [community_ceiling] out of [COMMUNITY_LEVEL_MAX] community points."
    

    # If the user has beat the game before, allow them to skip the credits.
    $ skippable = not persistent.times_beaten
    scene black with fade    
    hide text with fade
    
    show text "Credits" with fade    
    $ renpy.pause(2.0, hard=skippable)
    hide text with fade
    
    show text "Written, Produced, and Directed by\nAndrea Landaker" with fade 
    if ((community_level < COMMUNITY_LEVEL_OK) and (ending != "none")):
        show pavel sad at quarterright, rising behind text
        show naomi sad at right, rising behind text
    else:
        show pavel at quarterright, rising behind text
        show naomi at right, rising behind text
    with dissolve
    $ renpy.pause(3.0, hard=skippable)
    hide pavel
    hide naomi
    with dissolve    
    hide text with fade
    
    show text "Additional Writing and Design by\nRachel Helps" with fade
    if ((community_level < COMMUNITY_LEVEL_OK) and (ending != "none")):
        show ilian at quarterleft, rising behind text
        show sara sad at left, rising behind text
    else:
        show ilian happy at quarterleft, rising behind text
        show sara normal at left, rising behind text
    show baby black at leftbaby, babyrising behind text
    with dissolve
    $ renpy.pause(3.0, hard=skippable)
    hide ilian
    hide sara
    hide baby
    with dissolve    
    hide text with fade
    
    show text "Character Art by\n{a=http://clarissahelps.com}Clarissa Helps{/a}" with fade 
    if ((community_level < COMMUNITY_LEVEL_OK) and (ending != "none")):
        show pete at right, rising behind text
        show helen at quarterright, rising behind text
    else:
        show pete happy at right, rising behind text
        show helen happy at quarterright, rising behind text
    show baby boy at rightbaby, babyrising behind text
    with dissolve
    $ renpy.pause(3.0, hard=skippable)
    hide pete
    hide helen
    hide baby boy
    with dissolve
    hide text with fade
    
    show text "With music by:\nEhren Starks\nJan Hanford\nChad Lawson\nGiorgio Costantini\nKalabi\nBenji Goodrich\nGianmarco Leona\nFalling You\nAttic Trax\nTrancevision\nRuben van Rompaey\nDa Camera\nWillem Brons\nAnonymph\n\nLicensed from {a=http://www.magnatune.com}Magnatune{/a}\nunder the\n {a=http://creativecommons.org/licenses/by-nc-sa/1.0/}BY-NC-SA Creative Commons License{/a}" with fade
    if ((community_level < COMMUNITY_LEVEL_OK) and (ending != "none")):
        show julia mad at left, rising behind text
        show thuc sad at midleft, rising behind text
        show van wince at quarterleft, rising behind text
        show kid frown at left, rising behind text
    else:
        show julia at left, rising behind text
        show thuc at midleft, rising behind text
        show van at quarterleft, rising behind text
        show kid at left, rising behind text        
    with dissolve
    $ renpy.pause(6.0, hard=skippable)
    hide julia
    hide thuc
    hide van
    hide kid
    with dissolve
    hide text with fade     
    
    show text "With background images by:\nLisa Horner\nWes Landaker\nAndrea Landaker\nNASA\nBurningwell\n\nAnd the following Wikimedia Commons users:\nRandwick\nLabpluto123\nWrlctech\nEbyabe\nAvi/Skrewtap\nMarcus Budde\nAluter\nDorothea Witter-Rieder\nAnna Frodesiak\nAndrei Stroe\nJean-Pierre\n\nFiltered with Fotosketcher" with fade
    if ((community_level < COMMUNITY_LEVEL_OK) and (ending != "none")):   
        show martin sad at right, rising behind text        
        show natalia at quarterright, rising behind text
    else:
        show martin at right, rising behind text
        show natalia at quarterright, rising behind text        
    show raul at right, rising behind text
    with dissolve    
    $ renpy.pause(6.0, hard=skippable)
    hide natalia
    hide martin
    hide raul
    with dissolve
    hide text with fade
    
    show text "Sound Effects by:\nSoundjay.com\nFirearm SFX Library\n\nAnd Freesound.org users:\ndobroide, alienistcog, jackofall29,\nfoxen10, Walter_Odington, powpowrider,\n saint_leibowitz, pushkin, jadend2,\nOhrwurm, OwlStorm, ERH,\n soundscalpel.com, Timbre"
    if ((community_level < COMMUNITY_LEVEL_OK) and (ending != "none")):    
        show brennan mad at right, rising behind text
        show lily upset at quarterleft, rising behind text
    else:
        show brennan at right, rising behind text
        show lily at quarterleft, rising behind text        
    with dissolve
    $ renpy.pause(6.0, hard=skippable)
    hide brennan
    hide lily
    with dissolve
    hide text with fade
    
    # TODO: Add more beta testers
    show text "Beta Testing by:\nWes Landaker\nLisa Horner\nCatherine White"
    show lettie_head at right behind text with longmoveinright
    show goat_flip at left behind text with longmoveinleft
    with dissolve
    $ renpy.pause(4.0, hard=skippable)
    hide lettie_head
    hide goat_flip
    with dissolve
    hide text with fade   
    
    show text "The code for this work is licensed under the {a=http://www.gnu.org/licenses/gpl.html}GPL{/a}, and the text is licensed under a {a=http://creativecommons.org/licenses/by-sa/4.0/}Creative Commons Attribution-ShareAlike 4.0 International License{/a}.\nFor other licenses used, see accompanying License.html" with fade
    $ renpy.pause(3.0, hard=skippable)
    hide text with fade        
    
    show text "Made with Ren'Py" with fade 
    if (ending == "bad"):
        show him concerned at farleft, rising behind text
        show her concerned at farright, rising behind text
        if (is_pregnant or is_pregnant_later):
            show baby girl at rightbaby, babyrising behind text
    elif (ending == "mediocre"):
        show him normal at right, rising behind text
        show her normal at quarterright, rising behind text
        if (is_pregnant or is_pregnant_later):
            show baby girl at quarterrightbaby, babyrising behind text 
    else:
        show him happy at right, rising behind text
        show her flirt at quarterright, rising behind text
        if (is_pregnant or is_pregnant_later):
            show baby girl at quarterrightbaby, babyrising behind text
    with dissolve
    $ renpy.pause(6.0, hard=skippable)
    if (ending == "bad"):
        hide him with moveoutleft
        hide her with moveoutright
        hide baby with moveoutright
    else:
        hide him
        hide her
        hide baby girl
        with dissolve    
    hide text with fade

    if (ending == "none"):
        return
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
        
    if (persistent.got_good_ending and persistent.got_mediocre_ending and persistent.got_bad_ending):
        if (not persistent.got_all_endings):
            "You have experienced all the endings and unlocked the Omake from the Extras Menu!"
        $ persistent.got_all_endings = True
        
    "Thanks for playing! If you have feedback, I'd love to hear from you at {a=mailto:qirien@icecavern.net?subject=Our Personal Space}qirien@icecavern.net{/a}"
    show text "{size=100}{font=fonts/Kristi.ttf}The End{/font}{/size}" with fade
    stop music fadeout 1.0
    $ renpy.pause(5.0, hard=skippable)
    
    $ renpy.full_restart()
