label monthly_event_25:
    "It had been two years since we first arrived on Talam. In a way, it felt like we had been here forever. But sometimes I still expected to find myself back on Earth, waking up from a long, long dream."
    # TODO: tweak these numbers.
    if ((community_level >= COMMUNITY_LEVEL_GOOD) and (loved > LOVED_GOOD)):
        jump good_ending
    if ((community_level < COMMUNITY_LEVEL_OK) and (loved < 0)):
        jump bad_ending
    else:
        jump mediocre_ending

    return

# TODO: Check variable wants_to_leave for consistency
# ENDING 1 - Everything failing
label bad_ending:
    "Or, more like a nightmare."
    "[his_name] and I could barely speak to each other without arguing, I was swamped at work, and we were running out of materials and supplies."
    "I could tell this whole colony was going to end in failure."
    "I just wanted to go home. Home to Earth, where there were TV shows and stores and weekends."
    "Home, where we didn't have to work so hard just to survive."
    if (cheated_on_him):
        "Brennan said he was returning on the shuttle that would drop off more colonists and supplies. I decided to go with him."
    else:
        "Home, where maybe I could find someone who would appreciate me and love me no matter what."
        "[his_name] said he would stay, no matter what. But I didn't have to do what he wanted. I needed to do what was best for me."
    "I talked with the Mayor about my situation, and he agreed that the circumstances made it possible for me to divorce [his_name] and cancel my contract as a colonist and return to Earth."
    if (is_pregnant):
        "I was taking the baby with me; I could tell Jack already loved her a lot, but we decided I should have full custody."
    if (is_pregnant_later):
        "I would end up giving birth on the shuttle on the way back to Earth. Somehow I was not as worried about that as I had been about the idea of giving birth at Talaam's little clinic."
    "I didn't have much to bring with me- it reminded me again how little we had. It just wasn't enough."
    him "I guess... this is good-bye, then."
    her "Yeah. Sorry it didn't work out."
    him "..."
    her "..."
    if (cheated_on_him):
        him "You can't trust Brennan, you know."
        her "What would you know about trust?!"
        him "Hey, at least I never cheated on you."
        him "Any man who would sleep with another man's wife can't be trusted not to do it again."
        her "You don't know anything about Brennan. Or me, either, apparently."
        him "I guess not."
    else:
        him "You don't have to go. We could... start over, try again."
        her "Sorry, [his_name]. I can't live here... and I can't live with you."
        him "{size=6}I don't know if I can live without you...{/size}"
        her "What was that?"
        him "I said, I'll be fine without you. Enjoy Earth. Goodbye."
    "He turned away and walked home, never looking back. I picked up my bag and boarded the shuttle as we got ready to lift off."
        
    if (cheated_on_him):
        "Brennan put his arm around me and pulled me close. He whispered in my ear,"
        brennan "Just pretend it was all a bad dream..."
    her "At least I have a chance to start over again... this time on Earth, my favorite planet in the universe."
    
    ".:. Ending 1/3."
    jump show_credits
    return

# ENDING 2 - Community succeeding, marriage failing
# OR - Community failing, marriage succeeding
# OR - both mediocre
label mediocre_ending:
    "Things were still rough on Talam. I wasn't sure they would ever get better."
    if (community_level >= COMMUNITY_LEVEL_OK):
        "But at least I had my friends and neighbors; we all helped each other out."
    else:
        "There was always too much work to do; not just at work, but at home, too."
        "It always seemed like things were this close to falling apart completely. I felt like any day now we'd all get attacked by wild animals, or all the crops would die, or a solar flare would destroy us all."

    "There were a lot of things I missed about Earth, but there were some things I loved about this planet."
    if (loved >= 0):
        "Like [his_name] - I wanted to be where he was. Even though he loved this place and this rustic life way more than I did, I loved him enough that I could deal with anything else."
        if (cheated_on_him):
            "He even forgave me after I cheated on him. How many people would do that?!"
    else:
        "Like my job."
        if (profession == "doctor"):
            scene bg clinic with fade
            "As the only doctor on the colony, people came to me with all sorts of problems. Mostly medical ones, but sometimes other questions, too."
        elif (profession == "crafter"):
            scene bg workshop with fade
            "Every day was a new challenge; something new to build, a new material found, or some new technique to try. And nobody could make things as well as I could."
        elif (profession == "mechanic"):
            scene bg machine_shop with fade
            "When someone needed a piece of tech fixed, it wasn't just because they wanted it - they really needed it. We all needed everything to be working smoothly for the food to grow and us all to survive."
        elif (profession == "teacher"):
            scene bg classroom with fade
            "Aside from their parents, the kids on the colony didn't have any other teachers. So when they finally figured out multiplication or why history was important or read their first novel, it was because of me."
        "I felt needed and appreciated at work, even if I didn't always feel that way at home."

    if (community_level >= COMMUNITY_LEVEL_OK):
        call work_appreciation

    scene bg fields with fade
    show him normal at quarterright with moveinright
    show her normal at center with moveinleft
    if (loved >= 0):
        him "Hey, [her_nickname]! Welcome home!"
    else:
        him "Hi, [her_name]."

    her "Hi, [his_name]. What's for dinner?"
    him "Stir-fry. Lots of fresh veggies this month!"
    if (loved >= 0):
        her "Okay, well, I guess we better eat what we have."
    else:
        her "Again?"
        him "Yeah, that's what we have, so that's what we eat."
        her "..."

    "We sat down to dinner."
    call skill_appreciation
    if (is_pregnant):
        "After dinner, he played with the baby while I took a break."
    "He read, and I worked on some projects, and then it was time for bed."
    scene bg bedroom with fade
    show overlay night
    show her normal at quarterright
    show him normal at midleft
    with dissolve

    her "[his_name]?"
    him "Hmmm?"
    # TODO: Make this less cheesy: include some body language or specific details or something
    if (loved >= 0):
        her "I'm so glad to be here, with you."
        him "I'm glad to be with you, [her_nickname]!"
        her "What an adventure we've had..."
        him "Hmmm, I think our adventure is just beginning!"
        her "Ha ha, yeah... I wonder what the next year will bring?"
        him "As long as it's full of you, I'm not worried about it."
        her "Mmm-hmmmm."
    else:
        her "I'm sorry."
        him "For what, now?"
        her "I haven't always been as good to you as you deserve... "
        him "I'm sorry, too. Sometimes I know I'm hard to deal with."
        her "Thanks for not giving up on me."
        him "Let's never give up on us."
        her "Yeah."
        
    # TODO: is this too cheesy?
    "We kissed good night, but I lay awake for a little while, thinking a lot and worrying a little. I wanted to believe in our colony, to believe in our marriage, but I knew it took more than believing in something to make it come true."
    "But I had a feeling things would turn out all right."
    ".:. Ending 2/3."
    jump show_credits
    return

# Helper function for endings 2 & 3 to emphasize skills the player mastered
label skill_appreciation:
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
        "The water screw, the blender, the laundry wringer - the contraptions I built made things at home just a little easier when everything else was so much harder than back on Earth."
    return

# Helper function for endings 2 & 3 to show apprecation for work and say
# goodbye to Brennan, if he's leaving.
# TODO: Make this less cheesy by including specific people she's helped
label work_appreciation:
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

    her "I've just been trying to help out."
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
        brennan "Yeah, I never did quite fit in here. I'm not too sad about it; I missed having things to do, people to see, places to go..."
        her "That's the spirit!"

    "Brennan left, and I got ready to go."

    if (is_pregnant):
        "I stayed a few more minutes to feed the baby before walking home. She wasn't that heavy, yet, but she started to get heavy when I carried her all day long."
    return

# ENDING 4 - Community and Marriage Thriving
label good_ending:
    call work_appreciation
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
        him "That's how babies are, I guess. But someday she'll be an incredible woman like you, so it's totally worth it."
    elif (is_pregnant_later):
        her normal "I actually feel like eating today, so I took the opportunity to make a nice dinner."
        him happy "You don't have to do that! But thank you..."
    else:
        her normal "I made your favorite dinner..."
        him happy "Wow, really?! Thank you!"

    "It wasn't much of a dinner, really. We had some beans cooked with salted meat, and some greens with vinegar."
    
    call skill_appreciation
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
    her normal "[his_name]...I should be thanking {b}you{/b}. You work so hard every day - we literally couldn't survive without you. You have loved me no matter what this whole time. And there's nowhere I'd rather be than right here with you."
    him happy "Yeah...if someone came up to me, right now, and said 'All-expenses paid trip to wherever you want!', do you know what I'd say?"
    her surprised "What?"
    him flirting "I'd say, 'I want to go to my house, and be in my bed, next to my wife.'"
    her laughing "What a waste! You should pick somewhere exotic!"
    him laughing "There is no place more exotic!"
    her happy "That's true... Good choice, then."
    show him happy
    "He didn't answer, just buried his face in my hair and tightened his grip around my body. I held on tight to his arms, feeling safety and love and happiness swirling around us."
    "We were home."
    ".:. Ending 3/3."
    jump show_credits
    return

# Credits
label show_credits:

    scene black with fade
    hide text with fade
    show text "Credits" with fade
    with Pause(2.0)
    hide text with fade
    show text "Written, Produced, and Directed by Andrea Landaker" with fade 
    with Pause(2.0)
    hide text with fade
    show text "Additional Writing and Design by Rachel Helps" with fade 
    with Pause(2.0)
    hide text with fade
    show text "Sprites by Clarissa Helps" with fade 
    with Pause(2.0)
    hide text with fade
    show text "GUI Design by Luce Jumble" with fade 
    with Pause(2.0)
    hide text with fade
    #show text "Background Images\nEarth image courtesy of NASA, www.nasa.gov\nTriple-star sunset courtesy of JPL at NASA, http://www.jpl.nasa.gov/\nRed dwarf sunset CREDIT: ESO/L. Calçada\nCaledonian Sleeper Single berth by Randwick, from http://en.wikipedia.org/wiki/File:Caledonian_Sleeper_Single_berth.jpg\nFVES Classroom by Labpluto123, from http://commons.wikimedia.org/wiki/File:FVES_Classroom.jpg\nBirchip Community Library circulation desk by Wrlctech, from http://commons.wikimedia.org/wiki/File:Birchip_reno_008.jpg\nGuantanamo Captive's hospital beds in the public domain, from the U.S. Department of Defense\nKoreshan Machine Shop by Ebyabe, from http://commons.wikimedia.org/wiki/File:Koreshan_SHS_large_machine_shop_inside01.jpg\nTool Area - Workshop by Avi/Skrewtape, from http://commons.wikimedia.org/wiki/File:Tool_Area_-_Workshop.jpg\nWhite Desert Egyptian Sunset from http://www.burningwell.org\nOther photos by Wes Landaker, Andrea Landaker, Lisa Horner, and Lance Meibos" with dissolve with Pause(2.0)

    $ renpy.full_restart()
