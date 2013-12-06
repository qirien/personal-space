label monthly_event_25:
    "It had been two years since we first arrived on Talam. In a way, it felt like we had been here forever. But sometimes I expected to find myself back on Earth, waking up from a long, long dream."
    if ((community_level < 50) and (loved <= 10)):
        jump fail_bad_ending
    elif ((community_level >= 50) and (loved <= 10)):
        jump succeed_bad_ending
    elif ((community_level < 50) and (loved > 10)):
        jump fail_good_ending
    elif ((community_level >= 50) and (loved > 10)):
        jump succeed_good_ending

    jump credits

# ENDING 1 - Everything failing
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

# ENDING 2 - Community succeeding, marriage failing
label succeed_bad_ending:
    "The community was thriving, but my marriage was falling apart."

    ".:. Ending 2/4."
    jump credits
    return

# ENDING 3 - Community failing, marriage succeeding
label fail_good_ending:
    "Even though our colony wasn't going to make it, at least we had each other."

    ".:. Ending 3/4."
    jump credits
    return

# ENDING 4 - Community and Marriage Thriving
label succeed_good_ending:
    if (profession == "doctor"):
        scene bg clinic with fade
        boss "[her_name], I don't know what we'd do without you. You've worked so hard to keep everyone on the colony healthy."
    elif (profession == "crafter"):
        scene bg workshop with fade
        boss "[her_name], I don't know what we'd do without you. Everyone has something you've made in their house or on their farm. And you've taught others how to make useful things, too."
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
        boss "[her_name], I don't know what we'd do without you. All our machines would be broken and useless if not for your hard work fixing them up all the time."
    elif (profession == "teacher"):
        scene bg classroom with fade
        boss "[her_name], I don't know what we'd do without you. All the kids love your enthusiasm for learning, and you've worked hard to make sure they know about Earth and learn the things they need to succeed here on Talam."

    her "I do like my job..."
    boss "I just wanted to let you know how much we all appreciate your hard work and expertise."
    her "Thank you, that's nice to hear."
    "Even though it sounded cheesy, it was true. I felt needed, and appreciated - there really was no one else on the colony who could do the things I could do, but people didn't resent that."
    "They just knew that sometime I'd need them as much they needed me."

    brennan "He's right, you know. We'd all be lost without you."
    her "That's an exaggeration!"
    if (wants_to_leave or cheated_on_him):
        brennan "I suppose you've changed your mind about wanting to leave?"
        her "Yes... sometimes it has seemed hopeless, but I thought about it, and I'm happy right where I am."
    if (exposed_brennan):
        brennan "It'll be your turn to send a message on the quantum entanglement device... what will you say?"
        her "I'll have to think about it - there's a lot to fit into 150 characters."
        brennan "Well, it turns out the brass in Washington want me to stay longer - since the device works, I don't have to return to Earth to make my report in person."
        her "That's good news!"
    else:
        brennan "I don't think anyone will be sad to see me go."
        if (brennan_relationship >= 2):
            her "Of course we'll miss you! But maybe you won't miss Talam?"
        else:
            her "We'll miss you, Brennan. But I think it'll be good for you to do something else."
        brennan "Yeah, I never did quite fit in here. I'm not too sad about it; there's loads more birds back home, anyway."
        her "That's the spirit!"

    "Brennan left, and I got ready to go."

    if (is_pregnant):
        "I stayed a few more minutes to feed the baby before walking home. She wasn't that heavy, yet, but she started to get heavy when I carried her all day long."
    "I headed home, enjoying the warm sun and a light breeze."

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
    
    if (skill_domestic >= 100):
        "I told [his_name] about my latest post on the No Space Like Home blog. I had been experimenting to see all the different kinds of vegetables you could pickle."
    if (skill_creative >= 100):
        "As we ate, I traced my hand around the pattern I had inlaid on the edge of the dishes we used. All around were things I had made to make our lives a little better - placemats, potholders, rope, crates - it made our little house seem more like our home."
    if (skill_knowledge >= 100):
        "We talked about some of the research Lily and I had been doing about pharmaceutical properties of Talam's plants. Making our own medicines would be a huge boon for us."
    if (skill_physical >= 100):
        "As I took another bite of beans, the juicy meat tasted so good. We'd dried it to preserve it, but when it soaked with the beans it regained some of its original texture."
    if (skill_social >= 100):
        her "We had a colony leadership meeting today."
        him "Oh yeah? How'd it go?"
        her "Pretty good. Though sometimes I wish people would just work out their own problems."
        him "Like what?"
        her "Oh, like \"Someone's goat is getting onto my property! Do something!\" when really they should just go tell Thuc, \"Hey, your goat came in my fields, can I help you fix your fence?\""
        him "Ha ha, I know exactly what you're talking about."
        her "I just have to remember that we can't make everyone be happy, and they're not going to come tell us all the good things that are going on."
        him "Sounds like you've got a good perspective."
    if (skill_spiritual >= 100):
        "I thought of all the little things that had happened to help us succeed. We had plenty of bad things, too, but somehow no matter what happened we managed to make it through."
        "Not on our own, though - I noticed some people in the colony who were always looking out for everyone else, even at great cost to themselves."
        "I wanted to be one of those people."
    if (skill_technical >= 100):
        "Looking around at our house, I noticed how different it was from when we first moved in."
        "The water screw, the blender, the laundry wringer - the contraptions I built made things at home a little simpler when everything else was so much harder than back on Earth."

    if (is_pregnant):
        "After dinner, [his_name] joked and held the baby on his lap and tickled her chin, and then we talked and read books and went to sleep all snuggled up together."
    else:
        "After dinner, [his_name] joked and we laughed and talked and read books and went to sleep curled up next to each other."

    scene bg bedroom with fade
    show overlay night
    show her normal at midright
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
