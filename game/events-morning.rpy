# Event content for all the events that can happen in the morning,
# either at work or skipping work.

# Default work event if there's no special event
label act_work:
    # TODO: mention that the mayor's favorite song is "It's the End of the World"
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade

    if (relaxed <= -10):
        "I worked hard at work. I was starting to feel burned out, though."
    elif (relaxed >= 10):
        "I breezed through work. Everything seemed easy."
    else:
        "I worked hard at work as usual."
    $ relaxed -= 5
    $ community_level += 1
    $ times_worked += 1
    return

label act_skip_work:
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade

    if (slacked_off == 3):
        "My boss called me in to meet with him after work."
        boss "[her_name], I'm worried about you. You haven't been putting in your usual effort at work lately."
        menu:
            "What should I say?"
            "I'm sorry.":
                her "I'm sorry. I should pay better attention to my work."
            "Things are busy at home":
                her "Sorry - things have been so busy at home, trying to get the farm started and everything."
            "It won't happen again.":
                her "I'm sorry - I won't let it happen again."
            "Whatever.":
                her "Whatever."
                boss "Excuse me?"
                her "As long as I get my job done, what's the big deal?"
                boss "Well, just see that you do get it done."
                $ slacked_off = 1
                return
        boss "I understand, but this can't happen all the time. We need you here."
        her "All right, thanks for understanding."
        $ slacked_off = 0
        $ relaxed -= 2  #it's stressful to get caught slacking off
        $ community_level -= 10
    else:
        "I took a little time off work and didn't push myself this month."
        $ relaxed += 5

    $ slacked_off += 1
    return

# Special Morning Events
label work_0:
    $ times_worked += 1

    scene bg community_center
    "My boss was also the leader of our little community. I guess you could call him the mayor?"
    "Right after we landed, he called a meeting for everyone where he gave a speech."
    boss "We made it this far! Now, as you know, we've arrived right at the beginning of this planet's spring, so it's time to get seeds in the ground! We would like for our colony to become self-sufficient as far as necessities are concerned."
    boss "In two years, another colony ship will come with supplies and more colonists. So, until then, we're on our own."
    boss "Are there any questions?"
    menu boss_meeting:
        "Do I have any questions?"
        "How much food do we have?":
            her "How much food do we have in storage now?"
            boss "We brought enough in our storehouse for everyone for one year. It will last much longer than that unopened, so I'd like to keep it for emergencies and use the food we grow as much as possible."
            jump boss_meeting
        "What about medicine?":
            her "What about medicine?"
            boss "We have a good supply of the most common medicines, and Dr. Lily has the tools to synthesize new medicines if needed. But our supply is not unlimited, so try and use them sparingly."
            jump boss_meeting
        "Do we have spare parts?":
            her "Do we have spare parts for when things break?"
            boss "We have the 3D printers at the library for spare parts, but we have a limited supply of plastic and metal, so let's make sure we recycle and use native materials where possible."
            jump boss_meeting
        "Any weapons?":
            her "Do we have any weapons?"
            boss "We do have a few hunting weapons that you can check out from the storehouse if you would like to try your hand at hunting, though I'd check with Dr. Lily first and make sure that the animal is edible!"
            jump boss_meeting
        "Is the ship coming in two Earth years or Talam years?":
            her "Is the ship coming in two Earth years or Talam years?"
            boss "Good question; that's two Earth years, which makes about..."
            lily "About 26 Talam months. Since there are seven months a year here, that makes a little over three Talam years."
            boss "Right...hopefully that answers your question!"
            jump boss_meeting
        "No questions.":
            her "(I don't have any questions.)"

    "After the meeting, the mayor met with me to show me around where I'd work."

    #Different event for each profession
    # DOCTOR
    if (profession == "doctor"):
        scene bg clinic with fade
        boss "All right! This is the clinic where people will come in if they get sick. I don't just want us to react to injuries and illness, though - we need to be proactive, and help promote good health."
        her "I helped some people out on the ship on the way here, so this should be similar. I will need some more supplies, though."
        boss "That's fine, just write up a list and give it to me to approve. Then you can go on over to the storehouse and take what you need."

    # CRAFTER
    elif (profession == "crafter"):
        scene bg workshop with fade
        boss "All right! This is the shop where people will come in if they need something made they can't make themselves. We don't have a lot of materials yet, but you can requisition some from the storehouse for important projects, and there are some materials, like wood, right here on the planet."
        her "I can see that this job is going to take a lot of creativity!"
        boss "Yes, it will! Perhaps you can start by helping me out - one of the roof pieces from the Nguyen's house broke when we were unpacking it, so they are going to need a replacement."
        her "Sure, I'll take a look at the standard roofs and see if I can make something out of the wood around here."

    # MECHANIC
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
        boss "All right! This is the shop where people will bring machines that need to be fixed. You'll be responsible for any kind of machine people have, from datapads to tractors. We don't have many replacement parts, so do what you can to fix things up when they break."
        her "I can see that this will take a lot of creativity."
        boss "Yes, it will! Perhaps you can start by helping me with my datapad? It always freezes up when I try to access my calendar..."
        her "Sure, let me take a look at it..."

    # TEACHER
    elif (profession == "teacher"):
        scene bg classroom with fade
        boss "All right! This is the schoolhouse. There's not a lot of kids in the community yet, so we just have them all in one room with you as their teacher. Please consider what they'll need to learn in addition to the standard curriculum, and try to be flexible if kids are needed to help out back at home."
        her "I guess the kids are going to have to work hard, too..."
        boss "Yes, but they need to learn a lot, too! It will take a lot of effort to see that they don't forget about Earth, and all the things humanity has managed to learn there."
        her "Even though it seems far away, it's still our home, isn't it?"

    "I worked hard getting things set up, and even though the job seemed pretty big, I thought I would probably do okay."

    # TODO: Have Sara stop by and say hi? 

    $ relaxed -= 5
    return

# Emergency where she can't help everyone in time, leading to 
# the mayor offering to find her some help.
label work_1:
    $ times_worked += 1
    if (relaxed > 10):
        $ relaxed = 0
    else:
        $ relaxed -= 10
    $ community_level += 2

    # DOCTOR
    if (profession == "doctor"):
        scene bg clinic with fade
        "Usually things were pretty quiet at the clinic. I made an appointment with each colonist to learn about each person's medical conditions, and sometimes made suggestions for how to deal with chronic problems. We had a few minor injuries setting up, but nothing serious."
        "But one day in particular was extremely busy."
        her "Oh! What happened?"
        "Thuc carried James in and set him in the exam table. I could tell his leg was hurt but he was not in immediate danger. I took his vitals while Thuc filled me in."
        thuc "We were working on putting together a mill for grain. But one of the heavy cast iron rollers fell on James here. We tried not to move his leg while we carried him over."
        her "Good, thank you. You'll be all right, James."
        "James" "Thanks, doc. Hurts like hell, though."
        "The x-rays showed where his femur was crushed into several pieces."

        her "It's a comminuted fracture; it will take quite a while to heal."
        "I was just about to put him under so I could put in some pins when the radio crackled and I heard Sara."
        "Sara on the radio" "Doctor! You've gotta come right away; My brother stopped breathing - I think he swallowed something."
        "I started out the door while I talked to her on the radio. I hated to leave James alone, but this was urgent."
        her "I'm on my way. How old is he?"
        "Sara on the radio" "It's Sasha, he's three!"
        her "Do you know how to do the Heimlich?"
        "Sara on the radio" "Yes! I mean, I've never done it before, but..."
        her "Do it! Put your fist right above his belly button, support it with your other hand, and push in and up forcefully."
        "Sara on the radio" "Mom's doing what you said; it's not working!!"
        her "Keep trying! Then use your finger to sweep through his mouth to see if you can dislodge anything."
        "Sara on the radio" "Hurry, [her_name], he's starting to turn blue!"

        if (skill_physical < 20):
            "By the time I got there, the little boy was unconscious."
            "I moved quickly. I was able to get the peanut out of his throat, and performed CPR. Mrs. Blair watched me grimly."
            "I was tired from running all the way over there, but I did the best I could."
        else:
            "When I got there, he was blue but still conscious."
            "I moved quickly. I was able to get the peanut out of his throat, and performed CPR. Mrs. Blair watched me hopefully."

        "Finally, he coughed and started to breathe."
        "Mrs. Blair" "Sasha! Oh, my boy!"
        "I didn't have time to stick around for adulation, though - James was still waiting for me to help his leg in the clinic."
        her "Sorry to leave you waiting so long; I know you're hurting- oh!"
        "I had bandaged up his leg, but the wound had reopened and he was bleeding a lot."
        "James" "I tried to, to, stop the bleeding..."
        her "It's okay, I'm here now. You're going to be just fine..."
        "I took care of his leg, and several hours later, James woke up."
        "James" "Hey, is Sasha okay?"
        her "Sasha? Oh, yes, I got there just in time."
        "James" "They really ought to have someone in here helping you out. I mean, what if you were in the middle of surgery or something?"
        menu:
            "Do I need help?"
            "I need help":
                her "You are right...I can't do this by myself. I'll ask the mayor if there's someone that could assist me."
            "I can do it myself":
                her "It's not a problem most of the time. I can handle it."

        "Word got around about my two close calls in one day."
        boss "Doctor, I'm so sorry about what happened today."
        her "It's not your fault, Mayor Grayson."
        boss "Well, it partly is my fault. It's obvious you need an assistant. Perhaps not full-time, but someone who can come quickly and help out during busy times."
        her "That would be helpful, actually."
        boss "Well, I'll see who has some medical experience and get back to you about that."
        her "Thank you."

    # CRAFTER
    elif (profession == "crafter"):
        scene bg workshop with fade
        "They kept me pretty busy making things for all the colonists. I made a lot of farm tools and fences, and started working on some woodworking tools. We didn't have a lot of metal, so I was trying to make tools out of local materials, but it wasn't going very well."
        "Today, however, I didn't have time for any of that. I was working on a roof for a chicken coop."
        boss "[her_name], have you finished the barrels for the storehouse yet?"
        her "No, I thought you said you wouldn't need those for another week."
        boss "Well, the Engel's carrots grew faster than they anticipated, and they need a place to put them."
        her "Well, I can start on them now, but the Peron's really wanted this roof for their chicken coop - they've already lost two chickens to some nighttime predator."
        boss "I think the chicken coop takes priority here. But you're starting to have a lot of work to do, aren't you?"
        menu:
            "Way too much":
                her "I'm a little overwhelmed, honestly."
            "Sometimes":
                her "Sometimes. It seems like when one person needs something right away, everyone else suddenly needs something, too."
            "No problem":
                her "Nothing I can't handle."
        boss "Well, I'll see if I can get someone that you can call on when you get a lot of work."
        her "That would be great, thanks."
        "Eventually, I got everything done, but I was looking forward to having some help sometimes."

    # MECHANIC
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
        "Back on Earth, I only worked on cars. But here on Talam, people brought me all kinds of machines to try and fix. If it had moving parts or electricity and it broke, it came to my shop."
        "Usually I could fix things pretty quickly, but after several months of hard farming, a lot of things were breaking down. It wouldn't have been so bad except that we had only a small reserve of spare parts, so I tried to only use them when there was no other way to fix things."
        him "Hey, [her_nickname], is the tractor fixed yet?"
        her "No, sorry, I've been working on the clinic's radio all afternoon."
        him "Oh..."
        her "..."
        her "I'll let you know when it's done."
        him "It just seems like tractors should be a pretty high priority, since that's how we're growing all the food we're going to live on."
        her "Yeah, but the clinic needs the radio in case someone on one of the farms is hurt. We don't have phones, and the computer pads are unreliable."
        him "Well, how long is it going to take?"
        menu:
            "A day or two":
                her "Probably another day or two. Sorry, [his_nickname]."
                him "All right, well, maybe I'll just hitch Lettie up to the plow and see what she can do."
                her "Lettie can do anything!"
            "As long as it takes":
                her "It'll take as long as it takes, okay? It depends on whether I can make it work without putting in a new belt."
                him "All right, I guess I'll just have to trust you."
                her "I'll get it done."
            "It'll go faster if you leave me alone":
                her "It'll go faster if you leave me alone!"
                him "Okay! I'm leaving!"
                her "Good!"
                $ loved -= 2

        boss "Everything all right in here?"
        her "Yes, it's just a busy day."
        boss "Are those all the things that need to be repaired?"
        her "Yes, I've got quite a backlog right now."
        boss "Seems to me like you could use a little help sometimes."
        her "That'd be great, actually."
        "It turned out that the radio just had a loose connection, so I soldered it back together, and then turned my attention to the tractor. I was able to get it fixed just before sundown. [his_name] would be happy, but it sure was a busy day for me. Hopefully the mayor would be able to find someone soon."
        
    # TEACHER
    elif (profession == "teacher"):
        scene bg classroom with fade
        "Normally twenty-three students would be a nice size for a classroom. But my students are all different ages and skill levels. We have some good technology to help us out, but sometimes it's not enough..."
        her "On your computer pad you will see that I have sent each of you some reading about ancient Rome, appropriate for your skill level. Please read the selection, and then answer the questions at the end."
        "It took some of the kids five minutes, and others needed at least two hours. I decided to start a science experiment with the younger kids."
        her "We're going to make some different shapes out of paper, and see which ones will fly the best."
        "They all liked that idea, but the kids that were still reading didn't want to miss out on paper airplanes, so they ended up building those instead of doing their history work."

        "At recess, one of the kids fell and got a bloody nose. While I was helping him, two of the teenage boys started arguing on the other side of the field."
        "One of them punched the other. Soon they were wrestling and rolling on the ground yelling. I ran to try to stop them."
        #show her angry at left
        her "Stop! Stop it, now!"
        "They kept fighting. The kid with the bloody nose was crying, some of the kids were screaming and some were chanting and jeering, and I was trying to pull them apart."
        "One of the punches missed the kid and hit me in the head. I must have blacked out for a minute, because when I woke up the fight was over and all the kids were looking down at me worriedly."
        "I separated the two fighters, and somehow I managed to make it through the rest of that day. Just as the children were all leaving, the mayor came by."
        boss "[her_name], are you all right?"
        her "Yes...though I may have a black eye tomorrow."
        boss "That's terrible! You shouldn't be all by yourself here, not every day."
        her "Well, part of it is that those boys really don't need to be here every day. They could do most of their work from home."
        boss "That may be a good idea, but I want to find someone to help you out on the days when you have all the kids here."
        menu:
            "Do I need help?"
            "I need help":
                her "You are right...I can't do this by myself."
                boss "I'll see what I can do to find someone to help you out some of the time."
            "I can do it myself":
                her "It's not a problem most of the time. I can handle it."
                boss "I appreciate your confidence, but let me see if I can find someone, at least for part of the time."
        her "Thanks, Mayor Grayson."
        "That wasn't the only rough day, but it was the worst one for quite some time."
    return

# Introduce co-worker Brennan Callahan
label work_2:
    $ times_worked += 1
    $ relaxed -= 5

    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade
        
    show her normal at left
    show brennan at right
    "I was ready for another busy day at work when the mayor walked in with someone new. I remembered seeing him on the shuttle; he had an infectious smile and just the hint of an accent."
    boss "[her_name], I'd like you to meet Mr. Callahan. He's sort of a jack-of-all-trades here, helping out wherever we need it. He can help you out some of the time."
    brennan "Call me Brennan. And I know we've met already; I'd never forget a pretty face like yours."
    menu:
        "What should I say?"
        "Nice to meet you":
            her "Nice to meet you, Brennan. It will be good to have some help sometimes."
            brennan "You're quite welcome."
        "I remember you, too.":
            her "Yes, I remember you too, Brennan. Thanks for agreeing to help out."
            brennan "You're quite welcome."
        "I'm more than just a pretty face":
            her "I'm more than just a pretty face, I hope."
            brennan "Of course! I just meant that I remembered you. But I could understand how you might not remember me."
        "Are you going to be helpful?":
            her "Do you have any talents besides flattery?"
            brennan "A few, to be sure! Don't worry, I'll try not to distract you too much."
    "He winked at me playfully. Was he...flirting with me? I didn't have time to think about it; there was too much work to do."
    "It was nice to have him around, especially when things got busy later in the day. He didn't wait for me to ask him to do things, but he didn't get in my way, either."
    brennan "It was a pleasure working with you today, [her_name]."
    "He looked into my eyes intently as he shook my hand. His gaze was direct, friendly, and...amused? I looked away."
    her "Thanks for your help today."
    brennan "Anytime."
    scene bg farm_interior with fade
    "I walked home, trying not to think about him. When I got there, [his_name] greeted me with a kiss."
    him "How was work today?"
    menu:
        "What should I say?"
        "Great, I got some help":
            her "Great! I got some help - the mayor sent Brennan Callahan to help me out once in a while."
            him "Oh, well, that's good, I guess."
            her "What, you don't think that's a good idea?"
            him "Well, I'm just a bit suspicious of Brennan. He comes on the shuttle at the last second with no special skills, no family, and nobody else seems to think that's unusual."
            her "I guess they did ask mostly for couples and families to come..."
            him "He seems nice enough, but I'm just wondering what the real purpose is for him to be here."
            her "You think he's a spy or something?"
            him "I'm not saying that. I'm just saying that there's unanswered questions here."
            her "Interesting. Well, I'll keep an eye out, and if I see him sending coded messages to the aliens, I will let you know."
            "The next time Brennan helped out at work, he was as friendly as ever, but I didn't feel as uncomfortable as before. I treated him politely, but coolly, and we got a lot of work done."
        "Nothing special.":
            her "Just the usual. How about you?"
            him "Had to dig out some big boulders in the new field I'm working on."
            her "Oh, that sounds hard. Hungry for dinner?"
            him "I'm always hungry."
            her "Ohh, that I believe!"

            $ loved -= 5
            $ relaxed -= 5
        "I have to work with someone obnoxious.":
            her "Ugh, the mayor wants me to work with Brennan Callahan."
            him "Really? What's wrong with him?"
            her "I don't know, he's helpful enough, he's just kind of...creepy."
            him "Like in a 'secretly-a-vampire' kind of way, or a 'socially-inept' kind of way?"
            her "Like in a flirting-with-a-married-woman kind of way."
            him "... He was flirting with you?"
            her "I don't know! Maybe? Or maybe he just acts that way with everyone."
            him "I don't know; I always thought it was a little strange how he came on the shuttle at the last minute, with no special skills and no family."
            her "I guess that is unusual."
            him "Want me to talk to him?"
            menu:
                "Do I want him to talk to Brennan?"
                "No, I'll handle this":
                    her "No thanks, I can handle him."
                    him "That's what I'm afraid of."
                    her "You know that's not what I meant! You're the only man I want to handle, silly."
                    him "I know, it's okay, I don't really want to have that conversation with him, anyway. But let me know if you do want me to help you out later, okay?"
                    her "Thanks, [his_nickname]."
                    "The next time I saw Brennan, I thanked him for his help and mentioned that I expected everyone working there to maintain a professional attitude."
                    brennan "I'm sorry; I didn't mean to make you uncomfortable. Quite the opposite, actually."
                    her "Right. Now we've got work to do."
                    "Things went more smoothly after that, and we got a lot of work done."
                "Just talk to him":
                    her "By 'talk' you mean 'speak words with' not 'punch in the face', right?"
                    him "Of course, what kind of barbarian do you think I am?"
                    her "I don't know, I was just making sure!"
                    "I didn't hear anything else about it, but the next time Brennan came to help, he acted much more professionally. That sure made things easier at work."
                "No, I'm probably imagining things":
                    her "No, it's not the big of a deal. He's probably just a friendly kind of guy."
                    him "Friendly to women, you mean."
                    her "Maybe, but, whatever. I'm not interested. I've got you!"
                    "The next time Brennan helped me out, he was friendly as ever, but I didn't feel as uncomfortable as before. I treated him politely but coolly, and work went well."

    return

# MONTH 9
# working hard
label work_3:
    $ times_worked += 1

    # DOCTOR 
    if (profession == "doctor"):
        scene bg clinic with fade
        "I worked hard all month. A new baby was born, a kid got his finger chopped off, and it looked like Mr. Peron might have cancer. In addition, we were monitoring the colonist's radiation and nutrient levels to try to keep them healthy."
        "Brennan worked hard, too - he didn't have any formal medical training, but he learned to take vitals and organize blood samples and fetch equipment for me."
        "It would have been impossible to do it all by myself."

    # CRAFTER
    elif (profession == "crafter"):
        scene bg workshop with fade
        "I worked hard all month. Now that everyone was settling in, people had a lot of things they wanted. We made towels and spoons and a cradle and pots and other things."
        "Brennan worked hard, too - he had some woodworking skills, so he did a lot of that work so I could concentrate on other things."
        "Together we accomplished way more than I could have on my own. Even so, our task list never seemed to get any shorter."

    # MECHANIC
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
        "I worked hard all month. People's datapads would get corrupted if they were left out during solar flares, the farm equipment needed maintenance, and sometimes homes' solar panels or stoves would break down."
        "Some critter kept chewing through the wires at the Engels' farm, and so we were always going out there to replace those."
        "Brennan worked hard, too - he didn't know much about electronics, but he could run wires and use ordinary tools to care of the easier things."
        "We accomplished a lot more together than I could have on my own."

    # TEACHER
    elif (profession == "teacher"):
        scene bg classroom with fade
        "I worked hard all month. We had to be a lot more flexible than at a regular school, as sometimes kids were absent if they were needed at home on the farm. I wrote up an entirely new curriculum customized for teaching all ages at once, so that all the kids could be studying the same topic but at their own level."
        "Some of my lessons were not as interesting to the kids as I hoped they'd be, but usually they went over pretty well. I felt like the kids were learning a lot."
        "Brennan worked hard, too - he didn't have any experience with teaching, but he was good with kids and helped keep them on task."
        "There were times when just having another adult around was so important."

    her "Good work today, Brennan."
    brennan "Thanks, [her_name]. I really enjoy working with you."
    menu:
        "What should I say?"
        "I enjoy working with you, too":
            her "I like working with you too; you've been very helpful."
            brennan "I'm glad there's something useful I can do."
            her "You weren't doing anything useful before?"
        "Tell me about yourself":
            her "Thanks. So, what brings you to the colony, anyway?"
        "Bye":
            her "Thanks. Um, I gotta go."
            brennan "I'll see you tomorrow, [her_name]..."
            return

    $ brennan_relationship += 1
    brennan "Well, my skills aren't exactly in high demand here..."
    her "What skills are those? What did you do back on Earth?"
    brennan "I was a salesman. Not a bad one, either."
    her "So why are you here?"
    brennan "I was too good at my job. It became my life; trying to sell more than last month, trying to beat the other fellows. Finally I had to ask myself what was the point of it all?"
    brennan "On a whim I applied to be a colonist, and I suppose there was something about me they liked, because I was accepted."
    her "That's strange..."
    brennan "What, you think it's strange they found something about me they liked?"
    her "No, it's just - well, no offense, but we don't really need any salesmen here, especially ones with no family, and.... I'm sorry, that was rude of me--"
    brennan "And absolutely true. It feels lonely here, sometimes. There's no pubs or parks or any place to meet people - there's no one to meet! I don't even have my own pad or anything; they put me up in the Mayor's house."
    her "That sounds awkward."
    brennan "He's a nice enough fellow, and his wife doesn't seem to mind having me around, but they're not family."
    menu:
        "What should I say?"
        "Want to come over for dinner?":
            her "Not family, no, but you have friends here! Why don't you come have dinner with [his_name] and me tonight? I'm sure he'd like to meet you."
            brennan "Not very likely! You haven't seen the dirty looks he's been giving me?"
            her "Really?"
            brennan "Oh, sure! He's always looking at me like I'm a ravenous wolf."
            her "Well, maybe we could go for lunch together sometime."
            brennan "I'd like that, [her_name]. Thank you, for being a friend."
        "(Give him a hug)":
            her "I'm sorry you're so alone..."
            "He doesn't seem at all surprised when you reach out your arms to give him a hug. He hugs you back, holding you a second longer than you meant to, and then you let go."
            her "(This is probably the first hug he's had in months... poor guy.)"
            brennan "Thank you, [her_name]. I'm glad you're my friend."
        "We're all family":
            her "We're all family here, right?"
            brennan "I suppose so, though you're the only one I feel close enough to to call family."
            her "Sure, I'll be your big sister."
            brennan "Sister! Ha, that's...nice. Thank you, [her_name]."
    
    return

# MONTH 12
# Something bad happens - Brennan helps out.
label work_4:
    $ times_worked += 1
    $ relaxed -= 5
    $ community_level += 2
    play music "music/NoOneWillKnow.ogg" fadeout 2.0

    # Doctor - problems with new local bacteria (no viruses, though)
    if (profession == "doctor"):
        scene bg clinic with fade
        "There were not a lot of illnesses so far - they took great pains to make sure none of the colonists were carrying infectious diseases, and the viruses here probably hadn't had time to adapt to us yet."
        "But there were plenty of injuries, as people tried to adjust to new equipment, the different climate and atmosphere, and a new way of life."
        "Then, we met our first big challenge - the Streaks."
        "The first incidence was with one of the kids. She fell down, got a scrape on her hand, and kept playing. The next day, the scrape was swollen and had red streaks all around it - like a child's drawing of the Sun."
        "Brennan and I cleaned out the wound and put a fresh bandage on it. We weren't too worried - it was a small scrape, and the kid was mostly acting fine."
        "But the next day, she came back. She had a fever and the wound wasn't healing well."
        her "Take a culture sample; looks like a bacterial infection."
        brennan "Alright."
        "I borrowed a microscope from the science lab and examined the culture. It was like no bacteria in any of the reference books."
        her "Brennan, we need to quarantine the clinic. I'll send out a message to everyone urging them to stay away, wash wounds promptly, and watch out for these symptoms."
        "Would this bacteria respond to traditional antibiotics? They seemed to have cell walls, just like bacteria on Earth, so we decided to give it a try."
        "We stayed up all night with the girl, but the next day she was shaking, and her hand was starting to turn white around the cut. And now her brother was in the clinic with similar symptoms on his knee."
        "We continued treatment all that day, but the wounds still didn't seem to be improving. Instead, the infection appeared to be spreading. I hoped we wouldn't have to amputate; it seemed like we had time to try one last thing."
        menu:
            "What should we do?"
            "Use maggots":
                her "Brennan, we need some maggots."
                brennan "Maggots?! What for?"
                her "They will eat the infected tissue but leave healthy tissue alone. We'll need a lot of them; hundreds. I'll ask around, too, and we'll see what we can find."
                "We ended up with about a hundred maggots from local insects. I hoped they would work like the ones on Earth. I kept some for breeding, since we might need more, and disinfected the rest and applied them to the wounds."
                "The kids were a little grossed out, but they watched intently as we applied them and wrapped them gently with gauze."
                "Afterwards I was so tired I fell asleep at my desk."
            "Ask Dr. Lily":
                her "There's got to be something these bacteria are weak against. Maybe Dr. Lily can help."
                lily "Let's try several different kinds of antibiotics on different cultures and see if we can find what works best."
                her "Good idea."
                "We tried a little bit of all the medicines and substances we had that we thought could possibly work. We tried different chemicals, synthetic drugs, local mold, algae - anything we could think of."
                "The hardest part was waiting around for the results, while the kids were suffering."
                lily "Look at the algae culture! There's hardly any bacteria left."
                her "Hopefully the algae itself wouldn't be harmful to people..."
                lily "I can't say for sure."
                "We decided to try it. The kids just kept getting worse, and I was worried the bacteria would spread to vital systems."
                "We scraped off a little of the infected tissue and put some of the algae on with a new bandage."
                "Afterwards, I was so exhausted I fell asleep at my desk."
            "Cut out bacteria":
                her "We can't risk the bacteria spreading to vital systems. The antibiotics aren't working, and these kids' condition just keeps worsening. "
                brennan "What are you going to do?"
                her "I'm going to try to cut away the infected flesh to make it easier for the antibiocs to do their job."
                brennan "That's going to be painful."
                her "That's why your job is to keep the kid happy while I'm doing it."
                brennan "You have an awfully high opinion of my ability to keep people happy."
                her "I have local anaesthetics I can use; just help her feel better."
                "We told her what we were going to do, and then Brennan started telling her a story about faeries and flying mushrooms while I gave her the local anaesthetic. I didn't want to take out healthy skin, but I wanted to leave as little bacteria as possible, so it was pretty tricky."
                "We treated the boy the same way, and then I was so exhausted I fell asleep at my desk."
        
        "I awoke the next day in a hospital bed, disoriented. I was still in my clothes..."
        her "The kids!"        
        "I rushed over to check on them. For the first time, the kids seemed a little better. I don't know if it was our crazy idea, or if the antibiotics were finally working, or both, but I was so relieved that we could help them."
        "Brennan had fallen asleep on another bed, snoring softly."
        her "(He must have carried me in here when I fell asleep at my desk...)"
        "On my desk, my computer pad was full of messages from everyone asking about the kids and the quarantine. I looked for messages from [his_name]."
        him "1) Hey, [her_nickname], I haven't heard from you since the quarantine announcement...are you okay? I missed you today, but if anyone can help those kids, you can."
        if (loved >= 0):
            him "2) Starting to get a little worried here - any news?"
        if (loved >= 5):
            him "3) [her_name], I am seriously considering breaking my own leg so that they'll let me in there with you! You better still be alive in there!"

        her "(He was so worried about me...)"
        $ loved += 2

        "There were other outbreaks of the Streaks, but now that we knew how to treat it, we didn't worry quite so much."

    # CRAFTER - running out of plastic & wood
    elif (profession == "crafter"):
        scene bg workshop with fade
        "We made a lot of furniture and parts for the colonists - sometimes they made things on their own, but not everyone knew how. It was easier with the schematics we brought with us - the computer could easily cut complex shapes out of wood or metal, or print them out of plastic."
        "But..."
        brennan "Where's the two by fours? I wanted to start on those shelves for the school."
        her "That pile there is all we've got. The mayor said we're going to save the rest for emergencies."
        brennan "Well how do you like that! How are we supposed to build without materials?"
        her "Well, there are plenty of trees by the river..."
        brennan "We're not lumberjacks!"
        her "No, but I have an idea."
        "We didn't have a sawmill yet (I think that was one of the things that was supposed to come on the next ship), so we needed to make do with what we had."
        her "Brennan, I need you to gather or saw off or whatever a bunch of small branches, as uniform in diameter as possible."
        brennan "You're the boss..."
        "While he was gone, I started drawing up some designs that used simpler materials. Instead of using big boards for the shelves, we could lash a bunch of medium-sized branches together."
        her "We'll still need some thick, long branches for the posts... and then how should we attach the shelves to the posts?"
        "I did some research and drew up some ideas when Brennan came back. He had a trailer full of branches, and he looked sweaty and miserable."
        brennan "I hope this is enough for you."
        her "That'll do... for today."
        brennan "Today! You're a slave driver, you are."
        her "I have to be to get any work out of you, Your Laziness."
        her "Anyway, come see these plans. We'll need to strip the branches of twigs and leaves, and cut them to uniform sizes..."
        "He stripped the branches while I attached them together. It took a few tries to attach everything so it was sturdy, and it wouldn't hold as much weight as a normal shelf, but in the end, we finished it."
        
        her "I might have to have the mayor emphasize to people how much work it is to build this stuff, and maybe they won't ask for so many things."
        brennan "Or you could have them bring you the wood anytime they want you to make something."

        "I was going to have to do more research on ways to build with the wood we had here on Talaam."
        
    # MECHANIC
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
        her "This is the third one of these radios that has broken so far! I can't believe they sent such cheapo equipment on a space mission."
        brennan "I know; you'd think it might have occurred to them that we can't order new parts on a whim."
        her "And they didn't send us with many variable resistors, either."
        brennan "There's plenty of these fixed resistors, though."
        her "Well, that doesn't do us much good, unless..."
        brennan "What?"
        her "Well, we could just use a fixed resistor instead and turn it into an on/off switch instead of a volume control."
        brennan "But then you couldn't control the volume."
        her "No, but it's better than running out of variable resistors that we might need for a more vital system somewhere."
        brennan "That's true..."
        her "Although, we do have some resistive tape; we could probably make our own...but it would be more bulky than the original."
        "We worked on making a small potentiometer out of resistive tape and metal rings, but we couldn't get it small enough to fit on the handheld radio. So we had to just remove the volume control. Our solutions weren't always ideal, but we did the best we could with the materials we had."

    # TEACHER a kid claims teacher hit them
    elif (profession == "teacher"):
        scene bg classroom with fade                
        "It was the end of another school day. Even though the kids went home in the afternoon, I usually stayed around for another hour or two working on lesson plans and grading papers. Sometimes Brennan stayed and worked, too."
        "One day after school the Mayor came by to talk with me."
        boss "So, how are things going at the school?"
        her "Pretty good! I feel bad that the older kids have to spend so much time helping the younger kids, but it's really the only way to teach so many of different ages."
        boss "That's good, that's good... Well, what I came to talk to you about, is that one of the parents came to me with a concern."
        her "Oh?"
        boss "They said that their child came up with red marks on their hands, and the child said you hit their hands with a ruler."
        her "They said WHAT?!"
        brennan "[her_name]'ll be stern when the kids need it, but she's never hit anyone."
        boss "This is news to you, then."
        her "Of course it is! I would never do such a thing. Which kid is it?"
        boss "Gardenia."
        her "Gardenia... Well, a few days ago we were talking about how discipline in schools has changed, and how they used to hit kids that misbehaved with rulers or make fun of them, and how we don't do that anymore."
        brennan "I remember that. Then at recess, she was playing school with some of the other kids, and I saw them whacking each other with sticks."
        boss "So, you think it was one of the other kids pretending to be a teacher?"
        her "That's the only thing I can think of."
        boss "It sounds like this was just a misunderstanding. I'll talk to Gardenia's parents and let them know what happened."
        her "Thanks, Mayor Grayson. I wish they would have come to me about it, though."
        boss "I'll tell them that, too. Good-bye, then."
        her "Good-bye."
        her "Thanks for sticking up for me."
        brennan "Of course. I couldn't let cute little Gardenia get away with another one of her fibs."
        her "She certainly has a good imagination..."
        "Gardenia didn't give us any more trouble that month."

    return

# Month 12 - Solar flare while at work
label work_5:
    $ times_worked += 1

    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade

    "There were some days when we just had to stay inside because of strong solar flares. They had a prediction system that usually let us know a day ahead of time, so we could be prepared."
    "But one day it didn't work..."

    "It started as a normal day at work, when Dr. Lily's voice came over the radio."
    lily "Attention all colonists! This is Dr. Lily. A strong solar flare has just started. Get inside now. I repeat, there is a solar flare in progress, please get indoors."
    "The radio emitted a strong burst of static, and I could barely make out anything else she said."
    lily "...close the...stay...further notice..."
    "Our computer pads also popped up a notification from her."
    her "That's strange; usually we have more warning than this."
    brennan "Hopefully everyone can get inside in time."
    "We closed the windows and turned off unecessary electronics."

    if (profession == "doctor"):
        "We only had one patient at the time; Mr. Peron was being treated for basal-cell carcinoma."
        "We had just cut a large tumor out of his face, and I was bandaging it up."
    elif (profession == "crafter"):
        "There were just the three of us in the shop at the time - Brennan, me, and Mr. Peron, who had been explaining a farm tool he wanted us to try and make."
    elif (profession == "mechanic"):
        "Brennan and I had been watching Mr. Peron show us his method for twisting wire together to use the least amount of metal possible."
    elif (profession == "teacher"):
        "Other than that, I tried to teach class as usual. We had a guest speaker today, Mr. Peron, who was teaching the kids about chickens and how to breed and feed them, and what sort of plants they liked, and what they might eat that would make them sick."
        "He had just finished speaking and got ready to go when I stopped him."

    her "I'm afraid you're stuck here for awhile - Dr. Lily says there is a solar flare going on."
    "Mr. Peron" "What? I haven't heard anything about that."
    her "They just announced it on the radio; I don't know why we didn't have an early warning this time."
    "Mr. Peron" "I can't stay here! I have to make sure Natalia is safe!"
    her "Please calm down. I'm sure your wife knows what to do."
    "Mr. Peron" "Natalia always forgets to turn the radio on! She might not even know there is a flare! And Raul and Josephina are at home with her."
    "I tried contacting his family on the radio, but the radiation from the flare was interfering with our transmissions. I couldn't connect my computer pad to the wireless network, either."
    "Mr. Peron was getting more and more distraught. I was worried he was going to try and leave, and I wasn't sure I could stop him."
    brennan "Calm down, please! Everything will be just fine."
    "Mr. Peron" "You don't understand! If you had any family, you'd know that I have to be there!"
    "Brennan just looked at Mr. Peron, a curious expression on his face. Finally, he nodded."
    brennan "I'll go make sure everything's all right with your family."
    her "You can't do that! The radiation is too strong!"
    brennan "But he's right. I don't have a family; I don't have as much to lose."
        
    $ grays_absorbed = 3
    menu:
        "What should I do?"
        "Try and stop him":
            her "It's not worth sacrificing yourself over!"
            brennan "I'll be fine. And if I'm not, well, at least I'll have done some good here."
        "Let him go":
            her "If you really want to go, I won't stop you."
            brennan "Not that you could, anyway. But I'm glad you understand."
        "{i}Give him a lead apron{/i}" if (profession == "doctor"):
            her "Here, at least wear this lead apron. It won't completely protect you, but it's better than nothing."
            brennan "Thank you, [her_name]."
            $ grays_absorbed = 2

    "I watched him leave. The weather was deceptively placid - bright sun, a cool breeze, tree branches waving... the deadly radiation was completely invisible."
    "Neither Mr. Peron or I talked; we couldn't do anything else, either; we were too nervous."
    "The radio crackled every ten minutes - we could just barely make out that it was Dr. Lily repeating her warning."
    "The second time she repeated her warning, the radio came on again just minutes later."
    brennan "[her_name]...Peron house...got everyone inside...There was...but we...anyway. Repeat, we're...okay."
    "I let out a breath I hadn't realized I had been holding. Mr. Peron smiled and asked me to hand him the radio."
    "Mr. Peron" "Thank you, Brennan. Earlier, what I said...well, I was wrong. You have a family; you're part of ours."
    "There was silence, and static."
    brennan "...thank you."
        
    if (profession == "doctor"):
        "The flare was over after a few more hours, and Mr. Peron brought Natalia and the little kids to be treated for radiation sickness.  Afterwards, I insisted on Brennan being treated, too."
        her "You've absorbed at least [grays_absorbed] grays of radiation..."
        brennan "Grays of radiation? That makes it sound like I've got aliens living inside me."
        her "Stop joking and lie down. We need to see how bad it is."
        brennan "Hold on, I think I might--"
        "He vomited on the floor. At least it wasn't on me."
        her "That's exactly what I'm talking about. Now lie down!"
        "The amount he was exposed to was more than is usually used in chemotherapy, but if he didn't get more exposure his body would probably heal it just fine."
        "I treated his burns and gave him some medicine, and warned him to be especially careful to avoid any radiation for the next few weeks while his body healed."
    else:
        "The flare was over after a few more hours, and Mr. Peron went home, but I insisted on Brennan going to the clinic."
        "He threw up on the way there, and I could see some burns on his face and neck."
        "The doctor treated his burns and gave him some medicine and said he would probably be fine, as long as he was extra careful to avoid any radiation exposure in the next few weeks."

    "I was impressed that he had risked himself for a family he wasn't particularly close to - but maybe it was that desire for closeness that led him to do such a thing in the first place."
    "It hadn't even occurred to me to go out in the solar flare to help Mr. Peron. Was that because I was more selfish, or just not as stupid? What if it was my family out there - would I have sacrificed my health to help them?"
    "It wasn't something I had ever had to think about before."

    return

# MONTH 15 - lunch with Brennan
label work_6:
    $ times_worked += 1

    if (profession == "doctor"):
        scene bg clinic with fade
        "The clinic wasn't very busy this month, so I'd been working on writing a paper about how the nutrition of crops planted here differed from the nutrition of crops grown in Earth soil, based on comparing my own blood samples."
        "The colonists would need supplements of some minerals that were not as abundant here."
        "But soon it was lunch time."
    elif (profession == "crafter"):
        scene bg workshop with fade
        "We had the kids collect supple branches from the local trees, and we made wicker crates, baskets, and chairs out of them."
        "I went to the school and taught some of the kids the weaving techniques I had learned."
        "Soon it was lunchtime, and the kids went home to eat."
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
        "Inspired by last month's idea of replacing complicated parts with more simple ones, I set about looking at our inventory and cataloguing how parts we had a lot of could be used to substitute for parts we were running out of."
        "Soon it was lunch time."
    elif (profession == "teacher"):
        scene bg classroom with fade
        her "Class, after you read your assigned section on nomads of the Great Steppe, please write about ways our colony is similar to and different from the nomad culture. Once you've done that, you can come over here and we will learn some wood carving techniques that they used to make and decorate their furnishings."
        "I tried to include a hands-on component to all our learning, even if sometimes it wasn't completely related."
        "Of course, most of the kids just dashed off a few sentences before coming to watch Brennan teach woodcarving, so I had to make some of them go back and work on it some more."
        "Soon it was lunchtime, and the kids went home to eat."

    her "Oh no, I forgot my lunch."
    brennan "I was just going to go home for lunch; do you want to join me?"
    her "No, it's okay, I can just walk home and get something."
    brennan "That's a mile each way; you won't have any time to cook and eat anything. Come on, I'll fix you something. It's the least I can do for you, after all you've done for me."
    her "Well..."
    menu:
        "What should I say?"
        "Yes":
            her "Thank you, I'd appreciate that."
            scene bg farm_interior
            "We headed over to the mayor's house, which was as large as the Blairs', with three bedrooms and a kitchen.  I guess that's why they had Brennan staying there, too."
            "Mr. and Mrs. Grayson weren't there; it's possible they were had the community center where he had a little office."
            "Brennan pulled out a frying pan and put some oil in it, and prepared some potatoes, cabbage, eggs and spices."
            her "Do you like to cook?"
            brennan "Once in a while. Usually Mrs. Grayson cooks for all four of us, but I'll take a turn, too."
            her "What are you making?"
            brennan "Just a little hash. Ordinarily, I'd add some sausage or bacon, but they're both in short supply these days."
            her "That sounds delicious! It's kind of a treat to have someone else cook for me..."
            brennan "[his_name] doesn't cook for you?"
            her "Oh, he does, sometimes, but we often end up just cooking together."
            brennan "You're lucky to have someone who loves you so much."
            menu:
                "What should I say?"
                "I sure am" if (loved >= 0):
                    her "I sure am...I don't know what I'd do without him."
                    brennan "..."
                    her "But what about you! Aren't there any single women on the colony you could date? Or are you not interested in women?"
                    brennan "There's nothing I'm interested in more than women! But, well, let's see, single women...There's Dr. Lily, but she's at least 45 years old."
                    her "Okay, she's really smart, and nice too, actually, but that is a lot older than you."
                    brennan "And then there's the Blair's oldest daughters, who are seventeen and sixteen."
                    her "I've seen them taking care of their little siblings, but I don't know them very well."
                    brennan "Well, the oldest is all over that Thomas fellow who's about her age. I'm surprised they're not married yet."
                    her "They're only seventeen!"
                    brennan "Well, it's old enough to get into trouble, and old enough to help propagate the species..."
                    her "What about the younger sister, Miranda?"
                    brennan "You're not seriously suggesting I try and date a child, are you?"
                    menu:
                        "What should I say?"
                        "Yeah, things are different here":
                            her "Normally, I wouldn't, but..."
                            brennan "But what?"
                            her "I want you to have a future here. I can tell you're lonely, and Miranda is old enough to make her own decisions."
                            her "I'm not saying you should sleep with her or anything, but in two years, she'll be an adult. Why not see if you can be friends, and then see what happens in the future?"
                            brennan "She is only eight years younger than me...But there's no way Mr. Blair would allow her to date such a creepy older man as myself."
                            her "Don't think of it as dating! And don't, like seduce her or anything. Just... see if you could be friends."
                            brennan "I'm not very good at being 'just friends' with women, [her_name]."
                            her "Well, you and I are just friends, right?"
                            brennan "... Of course."
                            her "Just like that, then."
                            brennan "Sure. Just like that."
                        "No, you should date Dr. Lily":
                            her "No, I was just kidding. Actually, I think you should reconsider Dr. Lily."
                            brennan "Really? You don't think twenty years age difference is too much?"
                            her "No way! I mean, she's young enough to still be good-looking, right?"
                            brennan "Yeah, I suppose she does have a sort of distracted-librarian sort of beauty..."
                            her "And, you're not the type to be intimidated by a smart woman, right?"
                            brennan "You know I'm not."
                            her "Well, then what do you have to lose?"
                            brennan "I just - she's old enough to be my mother, you know!"
                            her "She doesn't act like your mother!"
                            brennan "No, you're right... I should talk to her. There's no harm in trying, right?"
                            her "The worst thing that could happen is she says she's not interested, and then it's awkward every time you see her for a while, and then you both forget about it."
                        "No, there's no hope for you":
                            her "Of course not. But I didn't want to tell you to just give up."
                            brennan "You never know, perhaps we'll find some beautiful blue alien women out here somewhere. I could be Earth's ambassador, to teach them all about the strange and wonderful ways of the human species..."
                            her "Keep dreaming, Brennan!"
                "I'm not so sure":
                    her "I used to think so, but I'm not so sure."
                    brennan "Why not?"
                    her "Things just aren't as exciting as they were when we were dating. I mean, we say 'I love you', but I don't feel it anymore. I don't think he does, either."
                    brennan "Bollocks. That's completely normal in a long-term relationship."
                    her "Is it?"
                    brennan "Of course! But that doesn't mean you can't have any sparks of excitement. You just have to work a little harder."
                    her "Got any ideas?"
                    brennan "Hundreds! Like, when you're at dinner, play a little footsie under the table, or give him a little spank when he walks by, or go to bed naked, or--"
                    her "OK! That's enough!"
                    brennan "I've got plenty more..."
                    her "It's kind of weird to have you telling me to get naked for my husband..."
                    brennan "Well, no one else is telling you, and you need to hear it!"
                    her "Brennan, you really don't have to-"
                    brennan "Also, you should wake him up once in a while with steamy hot kisses, nevermind how bad your breath may smell in the morning."
                    brennan "And you should work together! When you've got a job to do, ask him to help you, or help him out. Find something he likes and surprise him with it. Make his favorite food!"
                    brennan "I mean, for crying out loud, [her_name], don't you realize how lucky you are just to have someone?!"
                    her "..."
                        
                "He doesn't love me." if (loved <= -5):
                    her "I don't think he loves me at all."
                    brennan "What?! Why do you say that?"
                    menu:
                        "What should I say?"
                        "He doesn't tell me":
                            her "He never says 'I love you'"
                            brennan "Well, he should. How could he look at you every single day and not say 'I love you'? I'm sure I would."
                            her "Would what?"
                            brennan "I, ah, well-- He's an arse, that's all I'm saying."
                        "We never make love":
                            her "It seems like we never make love anymore..."
                            brennan "Is he gay? Impotent?"
                            her "What?! No!"
                            brennan "Well, then, what's his problem?! Who could be married to you, and not want to show you some love every day?"
                            her "I don't know; it just seems like we're always too tired or too busy by the time we go to bed."
                            brennan "Well, how about first thing in the morning? Or right before dinner? Or when you come home for a quick lunch break?"
                            her "Ha ha, that's not a bad idea. We'd probably feel like it more, then."
                            brennan "I mean, don't you two realize how lucky you are to have each other?!"
                            her "..."
                        "I'm not good enough":
                            her "I'm no good at living here; I'm not tough or hard-working enough."
                            brennan "What?! That's not true at all; we'd be totally lost without you as our [profession]."
                            her "But I'm no farmer. I hate farm food; I don't want to work hard all day; I don't want to have to do without. I just want to go to a store and buy food and soap and have hot water!"
                            brennan "It sounds like [his_name] isn't the problem."
                            her "Maybe not. But he loves it here. I just... don't."
                            brennan "Do you love him enough to stay here with him?"
                            her "I don't know..."
                            brennan "If you want out, we could leave the planet on the next colony ship. It'll be a few months, but you don't have to stay here if you're miserable."
                            her "Brennan..."
                        "Things aren't exciting":
                            her "I don't know; it's just not the same as it was when we first got married."
                            brennan "Of course not. Nothing exciting can last forever, or it wouldn't be exciting any more, would it?"
                            her "But if I don't feel the love, then..."
                            brennan "That's not the only way to feel love, right? You care about each other, want the other person to be happy?"
                            her "I used to..."
                            brennan "Do you love him enough to try and make things better?"
                            her "I don't know..."
                            brennan "Because if you want out, we could leave the planet on the next colony ship. It'll be a few months, but you don't have to stay here if you're miserable."
                            her "Brennan..."

            "Suddenly I noticed an acrid smell..."
            brennan "The hash!"
            "Luckily, it wasn't burned too badly, and we ate it together as the conversation turned to other topics."
            brennan "You know that I'm always here for you, right?"
            her "Yeah, thanks for listening."
            if (brennan_relationship >= 1):
                brennan "You helped me when I was feeling worthless; I'd do the same for you."
                her "I--"
                brennan "I don't want you to ever feel trapped, like no one loves you or you have nowhere to go, because it's not true."
                her "Thanks, Brennan..."
            $ brennan_relationship += 1

        "No":
            her "No, thank you. But if you would cover for me in case I get back late, I'd appreciate that."
            brennan "Of course."
            "I had to rush at home, and only had time to eat some raw vegetables before it was time to walk back."
            "But I didn't mind too much, as I got to see [his_name] while I was at home."
            him "I'll walk halfway with you; I don't usually get to see you during the day."
            her "Sure!"
            "We talked and laughed together. [his_name] was going way out of his way, using up the energy he needed for farming...just to be with me."
            "I held his hand tight, and he squeezed back. We didn't need to say anything; he knew I appreciated him, and I knew he appreciated me, too."
            $ loved += 5
            return
        "{i}Let's join Sara{/i}" if (skill_social >= 30):
            her "Hey, do you mind if I invite Sara, too? Sometimes we like to have lunch together."
            brennan "No, that's - that would be fine. I'll cook up something for the three of us."
            "We all went over to the Grayson's house where Brennan lived. He fried up some potatoes and cabbage and eggs for us, and we talked and laughed all together."
            her "Oh! It's been almost an hour; we have to get back to work!"
            sara "Thanks for lunch, Brennan. We should do this again sometime."
            brennan "It was my pleasure to entertain you."
    return

# MONTH 21
# Brennan is government spy looking for lucrative resources. 
# People find out about past crimes; chance for redemption or execution?
# has quantum entanglement communicator for instantaneous communication with Earth
label work_7:
    $ times_worked += 1
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade


    $ has_batteries = False
    $ questioned_brennan = False
    $ searched_room = False

    "One day while we were cleaning up after work, Brennan came up to me."
    brennan "[her_name], can I ask a favor of you?"
    her "You can ask..."
    brennan "I need batteries."
    her "Can't you just get them from the storehouse?"
    brennan "Normally I would, but... I've used my quota already. It's been so cloudly lately, you know, the solar panels just haven't been keeping up."
    her "What do you need them for?"
    brennan "Just some electronics in my room."
    menu:
        "What should I say?"
        "Sure.":
            her "Sure, Brennan, I'll get some for you."
            brennan "Thanks so much. And, ah, I'd appreciate it if you didn't mention to Ilian that they're for me."
            menu investigate_brennan:
                "What should I do?"
                "Question Brennan further" if (not questioned_brennan):
                    $ questioned_brennan = True
                    her "So, what kind of electronics do you have that are using so much power?"
                    brennan "You know, razor, computer pad, blow dryer, that sort of thing."
                    if ((skill_technical >= 60) or (profession == "mechanic")):
                        her "Blow dryers don't even work here, they draw too much current."
                    elif ((skill_spiritual >= 60) or (skill_social >= 60)):
                        her "You aren't being completely honest with me."
                    else:
                        her "Really? That's strange..."

                    if (brennan_relationship >= 2):
                        brennan "Oh, [her_name], I should have known I couldn't hide anything from you."
                        brennan "It's easier if I just show you. Come with me."
                        "We walked over to his room at the Graysons'. He pointed to an electronics box under the table."
                        jump brennan_confess
                    else:
                        brennan "You're right, of course, but I can't tell you what they're really for. Can you just trust me?"
                        jump investigate_brennan
                "Go to the store house" if (not has_batteries):
                    #scene bg storehouse
                    "I headed over to the store house and asked Ilian for the batteries. I hadn't gone over quota, so there was no problem."
                    $ has_batteries = True
                    menu:
                        "What should I do?"
                        "Question Ilian":
                            her "Hey, Ilian, do you know what Brennan needs all these batteries for?"
                            ilian "Wait, these are for Brennan?!"
                            her "Yeah, he asked me to get them for him."
                            ilian "He's already five sets over his quota! He needs to learn to do without!"
                            her "Do you know what they are for?"
                            ilian "What does everyone use batteries for? Lights, computers, things around the house. They're not supposed to wear out so fast when they're charged properly."
                            her "Hmmm, okay, thanks."
                            ilian "What about the batteries?!"
                            her "I might need them."
                            ilian "Gahhh..."
                        "Leave":
                            "I left with the batteries."
                                                        
                    jump investigate_brennan
                "Search Brennan's room" if (not searched_room):
                    $ searched_room = True
                    "Something wasn't right here. I sensed Brennan was hiding something important from me, and I was determined to find out what it was."
                    "Since he said he needed the batteries for his room, I thought I would check there."
                    scene bg bedroom
                    "No one was home at the Grayson's house, but there were also no locks on the doors, so I just walked in."
                    her "(Brennan will be at work for a little bit longer, if he's waiting for me to bring him the batteries...)"
                    "His room had the same few pieces of shuttle furniture we had, with a sleeping bag on the floor and a seat and table in the corner. The walls were bare; there were no photos or posters or decorations at all."
                    "The table had a mess kit, a few books, and a cable for charging a computer pad. There was another cable, too, though, and when I followed it, it went underneath the table where there was a strange device."
                    "It looked a little bit like a computer, with a metal case and some LEDs lighting up every now and then. But there was no writing or labels on the case at all. It made a low humming noise."
                    her "What is it?"
                    "Suddenly, I heard footsteps and I jumped. Brennan was in the doorway, watching me. He seemed amused."
                    jump brennan_confess
                    
                "Give him the batteries" if has_batteries:
                    "I brought the batteries back to Brennan."
                    brennan "Thank you so much, [her_name]. I'm completely in your debt."
                    her "You're welcome..."
                    return

        "No, sorry.":
            her "I'm sorry; I can't do that for you, Brennan."
            brennan "Oh...well, I'll just make do without, then, I suppose."
            her "Yeah, that's something we've all had to do, isn't it?"
            return
    return

label brennan_confess:
    brennan "It's a quantum entanglement communicator."
    her "Okay, but what does it do and why do you have one?"
    "He sighed and entered the room, closing the door behind him."
    brennan "I use it to send messages with Earth, instantly."
    her "Instantly?! Faster than light speed - I thought that was impossible!"
    brennan "The technology's quite new and expensive - this is a prototype, actually. Part of my job here was to test it."
    her "And the other part?"
    "He looked away and paused for a second before answering."
    brennan "I'm to report on any resources this planet has that my employer might find profitable."
    her "Who is your employer?"
    brennan "Rare Earth Tech. Well, technically I'm an independent contractor for Senator Martinez, who happens to be both on the board of R.E.T. and on the Senate Energy Committee."
    her "So you're a spy, basically."
    brennan "You could look at it that way."
    her "Since you've kept your employment a secret, I don't see any other way I can look at it."
    her "How could you hide this technology? People could have been using this to talk to their families back on Earth!"
    brennan "That's just it - there's not enough bandwidth for that. I can only send small bits of text at a time - like a telegraph. And besides, when I first came here we weren't even sure it would work."
    her "So why did you need the extra batteries?"
    brennan "If it ever turns off, even for a second, the connection will be broken and I'll completely lose contact."
    if (brennan_relationship >= 1):
        her "You were never a salesman on Earth, were you?"
        brennan "Actually, I was. I never lied to you, [her_name] - though I hope you'll understand why there's some topics I haven't brought up."

    her "So, is this the part where you turn into an evil villain and kill me because I know too much?"
    brennan "Kill you?! Of course not. This is the part where I beg for mercy and ask you not to tell anyone else about my device here."
    menu:
        "What should I say?"
        "I won't tell":
            her "I won't tell anyone. You're not hurting anyone, and..."
            brennan "And what?"
            if (brennan_relationship >= 2):
                her "I'm afraid of what they'd do to you."
                brennan "That's much too sweet of you, [her_name]."
            else:
                her "I'm not sure if everyone else would be as understanding as I am."
                brennan "That's true. Well, I trust you to keep it a secret. Thank you."
        "They have a right to know":
            her "The colony has a right to know, and a right to be able to use the device. Like you said, we'll need some kind of priority system and limits on messages, etc, but it's not fair for only one person to be able to communicate with Earth like that."
            brennan "Do you think they'll forgive me?"
            her "We'll see."
            "Brennan and I worked out a proposed system where he would send one message a month under a certain length for each family. Then we told the colony about the device."
            "At first they were upset with Brennan (and with me for siding with him), but they were so excited at the ability to send telegrams to Earth that they forgave him pretty quickly."
            $ exposed_brennan = True
        "I won't tell if...":
            her "I won't tell if you promise to-"
            menu:
                "What should I say?"
                "Get me off this planet":
                    her "Promise to get me off this planet with the next colony ship. I know I promised to stay forever, but you have connections, you could help me."
                    brennan "Of course I'll help you. Just leave it to me."
                "Send a message for me":
                    her "Promise to send some messages to Earth for me."
                    brennan "Of course, I'll do what I can."
                    brennan "Thank you, [her_name]. I trust you to keep it a secret."
                    return
                "Kiss me" if ((brennan_relationship >= 2) and (loved <= -10)):
                    her "Kiss me. Now."
                    "What was I saying? What was I doing? I thought he was going to laugh, and I could pretend it was a joke, but then he stepped closer."
                    "My heart raced and my mind shut down as there were no more words, just flesh melting into flesh with all the passion we had been holding back."
                    "I didn't think, didn't analyze, didn't worry about [his_name]; I just existed, in that eternal moment of pleasure and mutual acceptance."
                    $ cheated_on_him = True

# MONTH 24 Resolve things at work?
label work_8:
    $ times_worked += 1

    "Month 24"
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade

    return
