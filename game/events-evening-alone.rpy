# Event content for all the events that can happen in the evening,
# where we relax for a while.

# Basic Alone Evening Events

# Relax with humor
label relax_alone_0:
    scene bg bedroom with fade
    "I read a funny book my friend Sara recommended. Sometimes it was so funny I laughed out loud."
    "Laughing felt good. Sometimes I worried about if we would make it, but I forgot all about it when I could laugh."
    $ relaxed += 5
    $ loved -= 2
    
    return

# Can go help Sara or just relax at home.
label relax_alone_1:
    $ loved -= 2
    $ wearing_dress = False
    scene bg farm_interior with fade
    "I was all set to spend the evening by myself when Sara sent me a message on my computer."
    play bg_sfx "sfx/message.mp3"
    sara_c "Are you still up? Can you please come over, [her_name]?"
    menu:
        "Should I go?"
        "I'll be right over.":
            her_c "Sure, I'll be right there."
            "I walked to Sara's house in the dusky evening light, wondering what it was she wanted to talk about. When I got there, I could tell she'd been crying."
            scene bg farm_interior flip
            show her serious at midleft
            show sara sad at midright
            with dissolve
            sara "I got a message from Earth today...My mom died."
            $ community_level += 2
        "Can it wait?":
            her_c "Can it wait? I was just about to get in bed..."
            sara_c "I could...it's...my mom died."
            her_c "Oh no, I'll be right over."
            scene bg farm_interior flip
            show her serious at midleft
            show sara sad at midright
            with dissolve
            $ community_level += 1
        "I can't come tonight.":
            her_c "Sorry, Sara, I can't tonight. Can we meet tomorrow at lunch?"
            sara_c "Yeah, I guess."
            $ relaxed += 2
            scene bg farm_interior flip
            show her serious at midleft
            show sara sad at midright
            with dissolve
            "The next day at lunch, Sara told me that her mom had died."

    nvl clear
    "Since it took four years for the message to get here, her mom had actually been dead for a long time already. That didn't make it any easier for Sara, though."
    sara "All this time - I've been thinking about what she's doing back on Earth, and imagining her playing with her grandkids, and working in the garden, but really she's just been dead."
    her sad "Oh Sara, I'm sorry..."
    menu:
        "What should I say?"
        "How's your dad doing?":
            her serious "How's your dad holding up?"
            sara "I'm sure he'll be fine, but I feel terrible! I've been asking him questions about mom and telling jokes about the two of them, and he's going to keep getting those messages from me for years! It'll make him sad every time he gets a message from me."
            her normal "Or maybe it will make him happy to know how much you still care about her and remember her."
            sara "Yeah, maybe so."
        "How do you feel?":
            her serious "How do you feel? Besides the obvious, I mean."
            sara "Well, yeah, I'm sad, but I guess everyone has to die sometime, right? And it's not like I could really talk to her, anyway."
            her "But it still feels different, somehow?"
            sara "Yes, it does. I wish she could have seen this - this place, me, a colonist, everything."
            her sad "I do, too."
        "{i}Maybe she's closer now{/i}" if (skill_spiritual >= 20):
            her serious "Maybe she's closer now."
            sara "Huh?"
            her normal "Maybe her spirit can be closer to you, now that her body has passed on."
            sara "You mean... like if the soul could travel through space?"
            her "Sure, why not?"
            sara "I don't know if it's true, but... that's cool to think about."
        "What's the difference?":
            her annoyed "What's the difference? You couldn't be together before, and you can't now."
            sara "Well, the difference is now she's dead, so there's nothing there to connect with."
            her concerned "With four years time difference, all our families might as well be dead."
            sara "[her_name]! You should appreciate what you still have!"
            her serious "None of us have anything. The only difference is some of us realize that."
            $ community_level -= 2
            return

    "We talked for a long time; Sara has a lot of sad days ahead, but I think I was able to help her feel a little better."
    $ relaxed += 5
    return

# Stargazing alone
label relax_alone_2:
    scene bg farm_interior with fade
    show her normal at midleft
    show him normal at midright
    with dissolve
    her surprised "Hey, [his_name], want to sit outside with me?"
    him concerned "Oh.... I kind of want to, but I'm so tired. I'm just going to go to bed."
    her "Okay... good night, then."
    hide him with moveoutright
    hide her with moveoutleft
    scene bg stars with fade
    show her serious at center with dissolve
    show her at squatting with move
    "I sat out on the porch and gazed at the stars. They were so different from Earth, I had to make my own constellations."
    her serious "Hmm, those kind of look like two lovers... and there's a sort of circle that reminds me of a UFO..."
    her flirt "And...that looks like one long, crazy dragon."
    "I wondered if eventually humans would live near some of those stars, too."
    "I sat there for a long time, feeling small and far away, but also part of something amazing - humans living on a different planet. We'd never done that before."
    "It sort of made me feel... proud."

    $ relaxed += 5
    $ loved -= 2
    return

# Emails from Home
label relax_alone_3:
    scene bg farm_interior with fade
    play bg_sfx "sfx/message.mp3"
    "I got a message from my mother."
    "It was one she sent several years ago, but she told me all about my siblings, and how the neighbors were doing, and I better take good care of [his_name] and is he taking care of me, that sort of thing."
    "Even though I knew it would take four years for my letter to cross the vast space between our planets, I wrote back. I told her all about the farm and [his_name] and the town and my job. I wonder how much she could understand; our life was so different here..."
    "Still, it felt good to be connected to Earth."
    if (relaxed < 0):
        $ relaxed = 0
    else:
        $ relaxed += 5
    return

# Watch a movie alone
label relax_alone_4:
    scene bg bedroom with fade
    "There are some movies that I love that [his_name] just doesn't like. That's fine; we don't have to do things together all the time. So one night, I watched..."
    menu:
        "I watched:"
        "A musical.":
            "A musical. It was cheesy, of course, but the dancing was good and the songs were moving. Something about music just communicates in a way nothing else can..."
        "A romantic comedy.":
            "A romantic comedy. I was struck by how silly their disagreements were. Here we were, wondering if we were going to survive, and they were hiding petty secrets from each other. Who has time for that?"
        "A historical drama.":
            "A historical drama. The situation of the immigrants in the movie reminded me a little bit of us, except instead of learning how to get along with hostile foreign people we were trying to get along with hostile natural forces."
        "A documentary.":
            "A documentary. It felt kind of irrelevant now that we weren't even living on the same planet, but also nostalgic. Ahh, the days back when we lived on Earth..."
                
    $ relaxed += 5
    $ loved -= 2
    return

# He does things by himself sometimes, too.
label relax_alone_5:
    scene bg farm_interior with fade
    show him normal at midleft
    show her normal at midright
    with dissolve
    with dissolve

    him surprised "You want to watch a movie or something?"
    her serious "Nah, I think I want to do something by myself tonight."
    him normal "Okay, I've got some things I want to work on, too."
    her surprised "You don't mind, do you?"
    him concerned "No, not really. But I do like when we can do things together."
    her concerned "I do, too, but after being around people all day, sometimes I just need to be alone."
    him normal "Heh, yeah, I feel kind of the opposite. I'm usually alone all day, so at night I'd rather do something with someone..."
    her surprised "Maybe you could hang out with someone else sometimes?"
    him normal "Yeah, maybe I'll see if Thuc wants to do something."
    "The two of them ended up surveying some land for a future field, while I took care of some things on the computer."
    "I felt better knowing I wasn't [his_name]'s only friend..."

    $ relaxed += 5
    return

# Family photos
label relax_alone_6:
    scene bg farm_interior with fade
    "I looked through some old photos of my family. The places, the people - they all felt so unreal. I'd probably never see them again."
    "I picked up my [favorite_wedding_gift] and fingered it gently. It was one of the few things I had from Earth."
    "It looked, it felt so foreign, like an ancient relic from a dead civilization. Earth seemed like another life."
    "It was kind of sad, but at the same time it made me appreciate even more the experiences I had on Earth, and the new life we were making here on Talaam."
    $ relaxed += 5
    $ loved -= 2
    return
    
# go to bed early
label relax_alone_7:
    scene bg bedroom with fade
    $ is_nude = True
    show night
    show bedroom_covers behind night        
    show her serious at midright, squatting, behind bedroom_covers
    with dissolve

    "I felt so tired, I decided to just go to bed early."
    show him serious at quarterleft 
    with moveinleft
    
    if (is_pregnant):
        "Of course, that's when the baby decides to practice martial arts on my bladder."
        her annoyed "Not again..."
        him surprised "Everything okay?"
        her serious "I can't sleep while I'm being pummeled from the inside."
        "He put his hand on my belly and felt the tiny movements."
        him happy "Wow, that's an energetic kid!"
        if (father_attitude == "grinning"):
            her annoyed "Do you have to be so happy about everything? You remind me of my dad..."
            him surprised "What's there not to be happy about? We're alive and healthy, and so's our growing baby!"
        her sad "I'm just so tired..."
        him sad "Have you not been sleeping well?"
        her serious "Every time I fall asleep, something wakes me up in an hour or two. Either I have to use the bathroom, or the baby's moving, or my back hurts, or, worst of all, it's morning."
        her "And I don't want to take any medicine or herbs because I'm worried it might hurt the baby."

    else:
        "I'd had trouble sleeping lately; my back hurt whenever I lay in one place for too long. The beds from the shuttle were sturdy, but they weren't the most ergonomic designs."
        her annoyed "Oww..."
        him surprised "You okay?"
        her annoyed "Yeah, my back's been hurting; makes it hard to sleep."
        if (profession == "doctor"):
            him serious "Did you try taking some medicine for it?"
        else:
            him serious "Did you see the doctor about it?"

        her concerned "Yeah, it didn't really seem to help."

    if (loved > 0):
        him concerned  "Sorry you're so tired."
        her concerned "Yeah..."
        him serious "Is there anything else you can do about it?"
        her serious "I don't know; I'm trying to go to bed earlier, we'll see if that helps."
        him normal "Well, I'll try not to do anything noisy and wake you up."
        her normal "Okay, thanks."
        show her sleeping
    else:
        him annoyed "Well, I can't do anything about that."
        if (relaxed <= 0):
            her angry "You don't have to do anything about it! Can you just listen?!"
            him angry "What's the point of listening if it doesn't solve anything?"
            her annoyed "It might help me feel better."
            him annoyed "That doesn't make any sense."
            her angry "Well, that's how I feel! I don't know why I'm even telling you, since obviously you don't care!"
            him angry "I care, I just don't understand you!"
            her annoyed "Well, you could try listening."
            him annoyed "Hmph."
            hide him with moveoutleft
            show her sleeping
            "I closed my eyes and tried to get to sleep, but I was too upset."
            show her concerned
            "He was supposed to be my husband, my beloved, my best friend; was it so much to ask for him to just listen to how I felt?!"
            show him nude serious at midleft, squatting behind bedroom_covers with dissolve
            show her sleeping
            "Finally, I managed to fall asleep, at about the same time I usually did. I felt like he just wasted my whole evening by being so obstinate."
            show him sleeping
            $ relaxed -= 5
            $ loved -= 2
        else:
            her concerned "I know, I just wanted to tell you how I was feeling."
            him serious "I wish there was something I could do, [her_nickname]..."
            her normal "It's okay; thanks for listening."
            $ loved += 2
    
    scene black with fade
    $ is_nude = False
    $ relaxed += 5
    $ loved -= 2
    return

# These probably won't be seen, so make them simple.
label relax_alone_8:
    scene bg bedroom with fade
    play music "music/Shanghai_20_00.ogg" fadeout 1.0
    "I listened to some music - I didn't do anything else while listening, just lay back and really listened."
    "It made me think of summer vacation when I was a teenager back home, just lying back and reading books in the shade, playing video games, going swimming, and drinking lemonade."
    "What would our kids' summers be like?"
    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_9:
    scene bg farm_interior with fade
    "I set some grains cooking overnight, so they would be nice and soft for our breakfast in the morning."
    "That way things wouldn't be rushed in the morning."
    $ relaxed += 5
    $ loved -= 2

    return

label relax_alone_10:
    scene bg farm_interior with fade
    "I listened to some of my favorite songs and reminisced."
    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_11:
    scene bg bedroom with fade
    "I curled up with a good book."

    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_12:
    scene bg farm_interior with fade
    "I played a video game that I enjoyed."

    $ relaxed += 5
    $ loved -= 2
    return

# Events that can happen in any order

# Re-read childhood book
label relax_alone_a:
    scene bg bedroom with fade
    "I didn't mean to read the whole thing, but when I started reading one of my favorite books from my childhood I just had to finish it."
    "It wasn't as exciting and unpredictable as I remembered, but I still loved the characters, and the writing swept me in as I read through the whole thing."
    $ relaxed += 5
    $ loved -= 2
    return

# browsing wikipedia
label relax_alone_b:
    scene bg farm_interior with fade
    "I was curious about horses, so I started reading about them in the encyclopedia."
    "Reading about domestication led to Mycenaean script, and that led to morphology, and before I knew it I was reading a fascinating page about Austronesian languages."
    "I'm not sure I will ever use that knowledge, but it was still interesting to read about."
    $ relaxed += 5
    $ loved -= 2
    return

# Solo trip to bath house
label relax_alone_c:
    scene bg bathhouse with fade
    show her serious
    "I went to the bath house by myself. I brought extra wood so I could have a long, hot bath, and I carried up extra water from the river to make it a deep one. All my effort just made me appreciate it all the more."
    scene bg bathhouse with fade
    $ is_nude = True
    show bathhouse_overlay
    show her serious at squatting behind bathhouse_overlay
    with dissolve
    play bg_sfx "sfx/splash.mp3"
    her normal "Ahhh...."
    $ relaxed += 5
    $ loved -= 2
    scene black with fade
    $ is_nude = False
    return

label relax_alone_d:
    scene bg farm_interior with fade
    "I wrote a letter to my family, telling them all about what happened this month."
    "I knew they wouldn't get it for years, but it still helped me feel connected to them, just a little."
    $ relaxed += 7
    return

label relax_alone_e:
    scene bg farm_interior with fade
    "I read some online newspapers and magazines from Earth..."
    "It was hard to care about what the politicians or movie stars on Earth were saying and doing. Battles and natural disasters were at least four years past already. There was no point in reading about fashion or trends - we didn't have the resources to follow them even if we had wanted to."
    "I didn't feel depressed, though - it was kind of a relief.  There was no way to keep up with everything happening on Earth when we lived there, but I could easily keep track of what was happening to everyone on Talaam."
    "I decided to spend some time writing posts on the community message board instead. Our community here was more important than anything happening on Earth, anyway."
    $ relaxed += 5
    $ loved -= 2
    $ community_level += 2
    return

label relax_alone_f:
    $ wearing_dress = False
    scene bg path with fade
    show her serious with dissolve
    "I took a walk near our house and thought about the future."
    "What would the colony look like in ten, twenty, or fifty years?"
    "How many people would live here? Would there be plenty of food?"
    "What would [his_name] and I be like in fifty years? Still alive, I hoped... would I be a grandma? It seemed impossible to imagine..."
    $ relaxed += 5
    $ loved -= 2
    return

# Hang out at the library!
label relax_alone_g:
    $ wearing_dress = False
    scene bg library with fade
    "I invited Sara to come to the library with me to hang out."
    show pete at quarterright
    with dissolve
    show sara at midleft
    show her normal at quarterleft
    with moveinleft
    sara "Why do they even have a library? Isn't everything just on computers?"
    pete happy "Almost everything. Some things, like blueprints and maps, are easier to look at on huge rolls of paper."
    sara "I guess so..."
    her normal "You can even print things out here if you need to."
    pete normal "But, make sure you recycle any papers you print out when you're done with them; we don't have a paper factory."
    hide pete with moveoutright
    show sara at center with move
    sara "Why did you want to come here, [her_name]?"
    her serious "Well, back on Earth I used to like to go to bookstores and just flip through books... This isn't really the same, though."
    sara "Oh, I just read this great book, you should take a look."
    her surprised "What's it about?"
    sara "Well, there's these fish people and the fox people, and they have like this ancient feud, but then they hold a ball at the underwater palace...It's hard to explain, you just have to read it yourself."
    her happy "That sounds interesting, at least!"
    sara "I'll send it to you!"
    "We shared a few other book recommendations and talked for hours. It felt good to get out of the house at night (even if it was just to the colony library)."
    $ relaxed += 5
    $ loved -= 2
    return

#play a farm game
label relax_alone_h:
    scene bg farm_interior with fade
    show her normal at quarterright with dissolve
    "I found this video game about trying to get a farm up and running... It was way more fun than a real farm."
    play bg_sfx "sfx/whinny.mp3"
    show him normal at quarterleft with moveinleft
    him surprised "What are you doing?"
    her happy "Feeding my horses!"
    him surprised "You have horses now?"
    her "In my game! I have to make sure they get exercise, and good food, and take them to the vet if they get sick! It's called Farm Life."
    him annoyed "Farm Life?! That's nothing like real farming!"
    her "No, it isn't. And that's why it's fun."
    if (loved <= 0):
        him serious "What a waste of time."
        her annoyed "It's just a game."
        him angry "We don't have time to mess around with stupid games. There's real work to be done!"
        her angry "Then why don't you go do it instead of spying on me!"
        him serious "You know, someday if things go all wrong, you're going to think \"There wasn't anything I could have done to stop it\". You'll think back to this night where you were playing video games about a pretend farm instead of doing real work and realize that you could have done something, but you chose not to."
        her annoyed "I'll worry about that when I have to."
        him annoyed "No, that day will never come because people like me are doing actual work saving lazy people like you."
        hide him with moveoutleft
        show her angry
        "How dare he?! I couldn't work twenty-four hours a day! Even he didn't do that!"
        show her sad
        "But... maybe I should be doing more."
        "I closed my game. It wasn't fun anymore. But I couldn't bring myself to do any work, either."
        "I just wished I was somewhere else."
        $ loved -= 5
        if (relaxed > 0):
            $ relaxed = 0
    else:
        show him at center, behind her with move
        him happy "Those are the cutest ducks I've ever seen!"
        her sad "I know! It's actually kind of sad when the farmer gets hungry and she eats one of them..."
        him normal "Awww... Hey, that guy has the hearts for you!"
        her normal "Yeah, he keeps bringing flowers, but my farmer only likes sweets! I keep trying to get her to marry him but she likes the fisherman instead."
        him serious "It's too bad we can't do real farm work just by clicking on a screen."
        her sad "I wish it was easier, too..."

        $ relaxed += 5
        $ loved -= 2
    return

# cat videos on youtube!
label relax_alone_i:
    scene bg farm_interior with fade
    show her concerned at center
    "I was too tired to do much of anything. I didn't feel motivated to read, or play a game, or even watch a movie."
    "So instead I found some funny, short videos that we had brought from Earth."
    "They weren't meaningful or profound or anything, but they made me laugh."
    her laughing "Ha ha ha! That cat... is so funny! I love cats!"
    her surprised "That's something we don't have here yet... I wonder if someone will bring cats here soon?"
    $ relaxed += 5
    $ loved -= 2
    return

# work at home
label relax_alone_j:
    scene bg farm_interior with fade
    show her normal at center
    "I tried to mostly get all my work done at work, but sometimes there was things I needed to do at home."
    "I spent the evening catching up on the latest research in my field and planning out the month at work."
    $ relaxed += 5
    $ loved -= 2
    return

label relax_alone_k:
    scene bg farm_interior with fade
    show her normal at midleft with dissolve
    "I downloaded a visual novel I found online. It looked pretty cheesy, but at least it wasn't in high school - it was about romance on a star ship."
    "Your character was an ensign on the ship as it explored the galaxies, and you could romance one of four characters."
    $ starship_man = "None"
    menu:
        "Which guy should I pick?"
        "The brave, heroic security officer.":
            "I picked the security officer. He seemed like he could hold his own in a fight."
            $ starship_man = "brave"
        "The clever engineer with a prosthetic arm.":
            "I picked the engineer. He seemed smart, and a probably had a tragic backstory where he lost his arm."
            $ starship_man = "clever"
        "The sardonic doctor.":
            "I picked the doctor. I bet he had a lot of funny things to say."
            $ starship_man = "witty"
        "The shy alien navigator.":
            "I picked the alien navigator. The fur and foreignness just made him so much more interesting."
            $ starship_man = "intruiging"

    show him normal at midright, behind her with moveinleft
    him laughing "Oh, so that's the kind of guy you like?"
    her surprised "Wahhh! You scared me! I didn't know you were watching!"
    him happy "I was just walking by when I saw all those men on your screen. I had to stop and see what was going on."
    menu:
        "What should I say?"
        "It doesn't mean anything.":
            her normal "Well, I might play through all these and see every ending, so this doesn't mean as much as you might think."
            him normal "That's fine, that's fine! I was just curious."
            her flirt "You know you're the only man for me in real life. I just feel sorry for my character in this game that has to make do with these poor imitations."
            him flirting "Yeah, yeah!"
            her happy "Ha ha, I love you, [his_nickname]."
            him happy "I love you, too, [her_nickname]."
            $ loved += 2
        "He's kind of like you.":
            her normal "He's only my type because he's kind of like you."
            him surprised "Really? You see me like that?"
            her "A little. You're both very [starship_man]."
            him laughing "Ha ha, if you say so, [her_nickname]."
        "Who's {b}your{/b} type?":
            her flirt "So who's {b}your{/b} type of woman?"
            him serious "Hmmm, what are my choices?"
            her normal "Crazy and energetic, shy and nerdy, or glamorous and serious."
            him normal "Out of those three...probably crazy."
            him laughing "I mean, anyone who could tolerate me would have to be at least half crazy!"
            her annoyed "I see your point."
            him happy "And, of course, none of those clichés compares to a real woman like you."
            her normal "Of course not!"
            him surprised "Was that the right answer?"
            her happy "Ding! Your relationship with \"[her_name]\" went up by ten points!"
            him happy "All right!"
            $ loved += 2
        "Stop spying on me!":
            her annoyed "Can't I do something on the computer without you spying on me?"
            him annoyed "Sorry, I just saw it while I was walking by."
            her angry "Well, it's really rude to look at someone else's screen without asking."
            him sad "...okay, whatever."
            $ loved -= 2
            
    $ relaxed += 5
    return

label relax_alone_l:
    scene bg farm_interior with fade
    "I chatted with Helen Jennings over the network - she lived on the other side of the colony and didn't leave the house much, so we didn't get to see each other very often."
    her_c "Hey, how are your cows doing?"
    helen_c "Good! They have plenty of room to graze, but we had to pull out a few poisonous plants we didn't know about."
    her_c "How'd you find out they were poisonous?"
    if (skill_knowledge >= 60):
        helen_c "I read your edible plants guide!"
        her_c "Wow, really?"
        helen_c "Yes! I was glad you put in the poisonous plant section so we could identify it."
        $ community_level += 2
        $ relaxed += 2
    else:
        helen_c "All the cows got sick, so we took samples of all the plants in their pasture to Dr. Lily to analyze. Luckily, they made it through, but it was a close call."

    nvl clear
    her_c "How is Pete?"
    helen_c "Doing fine - though sometimes he's pretty busy taking care of the cows and the library!"
    her_c "Yeah, [his_name] is busy a lot, too..."
    helen_c "Hey, want to come over for lunch tomorrow? Pete's meeting with the mayor, so it'll just be me and the baby."
    her_c "Sure, thanks!"
    nvl clear
    "She was a newlywed like me and we had a lot in common, so it was fun to chat together."
    $ relaxed += 5
    $ loved -= 2
    return
