label monthly_event_25:
    "It had been two years since we first arrived on Talam. In a way, it felt like we had been here forever. But sometimes I expected to find myself back on Earth, waking up from a long, long dream."
    if ((community_level < 40) and (loved <= 10)):
        jump fail_bad_ending
    elif ((community_level >= 40) and (loved <= 10)):
        jump succeed_bad_ending
    elif ((community_level < 40) and (loved > 10)):
        jump fail_good_ending
    elif ((community_level >= 40) and (loved > 10)):
        jump succeed_good_ending

    jump credits


label fail_bad_ending:
    "Everything was falling apart."
    "[his_name] and I could barely speak to each other without arguing, I was swamped at work, and we were running out of materials and supplies."
    "I could tell this whole colony was going to end in failure."
    "I just wanted to go home. Home to Earth, where there were TV shows and stores and weekends."
    "Home, where I didn't have to work so hard just to survive."
    if (cheated_on_him):
        "Brennan said he was returning on the shuttle that would drop off more colonists and supplies. I decided to go with him."
    else:
        "Home, where maybe I could find someone who would appreciate me and love me no matter what."
    "I talked with the Mayor about my situation, and he agreed that the circumstances made it possible for me to divorce [his_name] and cancel my contract as a colonist and return to Earth."
    "I didn't have much to bring with me- it reminded me again how little we had. It just wasn't enough."
    if (cheated_on_him):
        "Brennan put his arm around me held me close. He whispered in my ear,"
        brennan "Just pretend it was all a bad dream..."
    her "A chance to start over again... this time on Earth, my favorite planet in the universe."
    
    ".:. Ending 1/4."
    jump credits
    return

label succeed_bad_ending:
    "The community was thriving, but my marriage was falling apart."

    ".:. Ending 2/4."
    jump credits
    return

label fail_good_ending:
    "Even though our colony wasn't going to make it, at least we had each other."

    ".:. Ending 3/4."
    jump credits
    return

label succeed_good_ending:
    scene bg fields with fade
    show him normal at quarterright with moveinright
    show her normal at center with moveinleft

    her surprised "There you are! How come you're so late?"
    him "Just had to finish up out here."
    if (is_pregnant):
        her normal "The baby's taking a nap, so I took the opportunity to make a nice dinner."
        him surprised "You sure you shouldn't be sleeping, too?"
        her annoyed "I can't sleep all the time! Besides, I feel like all I ever do is feed and change the baby and wash her diapers..."
        him "That's how babies are, I guess. But someday she be an awesome woman like you, and so it's totally worth it."
    elif (is_pregnant_later):
        her normal "I actually feel like eating today, so I took the opportunity to make a nice dinner."
        him happy "You don't have to do that! But thank you..."
    else:
        her normal "I made your favorite dinner..."
        him happy "Wow, really?! Thank you!"

    "It wasn't much of a dinner, really. We had some beans cooked with salted meat, and some greens with vinegar."
    if (is_pregnant):
        "[his_name] joked and held the baby on his lap and tickled her chin, and then we talked and read books and went to sleep all snuggled up together."
    else:
        "[his_name] joked and we laughed and talked and read books and went to sleep curled up next to each other."

    scene bg bedroom with fade
    show overlay night
    show her normal at center
    show him normal at midleft
    with dissolve

    him surprised "[her_name]?"
    her surprised "What?"
    him normal "Thank you."
    her laughing "Again? Hey, dinner wasn't that good!"
    him normal "No, not just for dinner. For taking a chance on me, and for trusting me enough to come to Talam with me. For working so hard at your job and all the things you do at home. For loving me even when I'm grouchy or make mistakes."
    her normal "[his_name]...Thank {b}you{/b}. You work so hard every day - we literally couldn't survive without you. You have loved me no matter what this whole time. And there's nowhere I'd rather be than right here with you."
    him surprised "Yeah...if someone came up to me, right now, and said 'All-expenses paid trip to wherever you want!', do you know what I'd say?"
    her surprised "What?"
    him flirt "I'd say, 'I want to go to my house, and be in my bed, next to my wife.'"
    her laughing "What a waste! You should pick somewhere exotic!"
    him laughing "There is no place more exotic!"
    her happy "That's true... Good choice, then."
    show him happy
    "He didn't answer, just buried his face in my hair and tightened his grip around my body. I held on tight to his arms, feeling safety and love and happiness swirling around us."
    "We were home."

    ".:. Ending 4/4."
    jump credits
    return


label credits:
    "Credits"

    $ renpy.full_restart()
