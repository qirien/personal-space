# Event content for all the events that can happen in the morning,
# either at work or skipping work.

# Default work event if there's no special event
label act_work:
    # TODO: mention that the mayor's favorite song is "It's the End of the World"

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
        $ relaxed += 2

    $ slacked_off += 1
    return

# Special Morning Events
label work_0:
    $ times_worked += 1

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
    if (profession == "doctor"):
        scene bg clinic with fade
        boss "All right! This is the clinic where people will come in if they get sick. I don't just want us to react to injuries and illness, though - we need to be proactive, and help promote good health."
        her "I helped some people out on the ship on the way here, so this should be similar. I will need some more supplies, though."
        boss "That's fine, just write up a list and give it to me to approve. Then you can go on over to the storehouse and take what you need."
    elif (profession == "crafter"):
        scene bg workshop with fade
        boss "All right! This is the shop where people will come in if they need something made they can't make themselves. We don't have a lot of materials yet, but you can requisition some from the storehouse for important projects, and there are some materials, like wood, right here on the planet."
        her "I can see that this job is going to take a lot of creativity!"
        boss "Yes, it will! Perhaps you can start by helping me out - one of the roof pieces from the Nguyen's house broke when we were unpacking it, so they are going to need a replacement."
        her "Sure, I'll take a look at the standard roofs and see if I can make something out of the wood around here."

    elif (profession == "auto mechanic"):
        scene bg machine_shop with fade
        boss "All right! This is the shop where people will bring machines that need to be fixed. You'll be responsible for any kind of machine people have, from datapads to tractors. We don't have many replacement parts, so do what you can to fix things up when they break."
        her "I can see that this will take a lot of creativity."
        boss "Yes, it will! Perhaps you can start by helping me with my datapad? It always freezes up when I try to access my calendar..."
        her "Sure, let me take a look at it..."
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
    elif (profession == "auto mechanic"):
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
    elif (profession == "auto mechanic"):
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
    "He winked at me playfully. Was he...flirting with me?! I didn't have time to think about it; there was too much work to do."
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
    if (profession == "doctor"):
        scene bg clinic with fade
        "I worked hard all month. A new baby was born, a kid got his finger chopped off, and it looked like Mr. Peron might have cancer. In addition, we were monitoring the colonist's radiation and nutrient levels to try to keep them healthy."
        "Brennan worked hard, too - he didn't have any formal medical training, but he learned to take vitals and organize blood samples and fetch equipment for me."
        "It would have been impossible to do it all by myself."
    elif (profession == "crafter"):
        scene bg workshop with fade
        "I worked hard all month. Now that everyone was settling in, people had a lot of things they wanted. We made towels and spoons and a cradle and pots and other things."
        "Brennan worked hard, too - he had some woodworking skills, so he did a lot of that work so I could concentrate on other things."
        "Together we accomplished way more than I could have on my own. Our task list never seemed to get any shorter."
    elif (profession == "auto mechanic"):
        scene bg machine_shop with fade
        "I worked hard all month. People's datapads would get corrupted if they were left out during solar flares, the farm equipment needed maintenance, and sometimes homes' solar panels or stoves would break down."
        "Some critter kept chewing through the wires at the Engels' farm, and so we were always going out there to replace those."
        "Brennan worked hard, too - he didn't know much about electronics, but he could run wires and use ordinary tools to care of the easier things."
        "We accomplished a lot more together than I could have on my own."
    elif (profession == "teacher"):
        scene bg classroom with fade
        "I worked hard all month. We had to be a lot more flexible than at a regular school, as sometimes kids were absent if they were needed at home on the farm. I wrote up an entirely new curriculum customized for teaching all ages at once, so that all the kids could be studying the same topic but at their own level."
        "Some of my lessons were not as interesting to the kids as I hoped they'd be, but usually they went over pretty well. I felt like the kids were learning a lot."
        "Brennan worked hard, too - he didn't have any experience with teaching, but he was good with kids and helped keep them on task."
        "There were times when just having another adult around was so important."

    her "Good work today, Brennan. It's nice to have you around."
    brennan "Thanks, [her_name]. I really enjoy working with you."
    menu:
        "What should I say?"
        "So do I":
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
    brennan "On a whim I applied to be a colonist, and I suppose there was something about it they liked, because I was accepted."
    her "That's strange..."
    brennan "What, you think it's strange they found something about me they liked?"
    her "No, it's just - well, no offense, but we don't really need any salesmen here, especially ones with no family, and.... I'm sorry, that was rude of me--"
    brennan "And absolutely true. It feels lonely here, sometimes. There's no bars or even any other single people to hang out with. I don't even have my own pad or anything; they put me up in the Mayor's house."
    her "That sounds awkward."
    brennan "He's a nice enough fellow, and his wife doesn't seem to mind having me around, but they're not family."
    menu:
        "What should I say?"
        "Want to come over for dinner?":
            her "Not family, no, but you have friends here! Why don't you come have dinner with [his_name] and me tonight? I'm sure he'd like to meet you."
            brennan "Not bloody likely! You haven't seen the dirty looks he's been giving me?"
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
# Something bad happens - she can't fix an illness, thing, or kid - Brennan helps out.
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
        "We stayed up all night with the kids, and the next day, the child was shaking, and her hand was starting to turn white around the cut. And now her brother was in the clinic with similar symptoms on his knee."
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

    # problems with 3d printer, running out of plastic
    elif (profession == "crafter"):
        scene bg workshop with fade
        
    # running out of metal, need new parts
    elif (profession == "auto mechanic"):
        scene bg machine_shop with fade
    # a kid claims teacher hit them?
    elif (profession == "teacher"):
        scene bg classroom with fade                

    return

label work_5:
    $ times_worked += 1

    "Month 15"
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "auto mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade

    return

# Solar flare while at work?
label work_6:
    $ times_worked += 1

    "Month 18"
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "auto mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade

    return

# Brennan is government spy looking for lucrative resources. 
# People find out about past crimes; chance for redemption or execution?
# has quantum entanglement communicator for instantaneous communication with Earth
label work_7:
    $ times_worked += 1

    "Month 21"
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "auto mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade

    return

label work_8:
    $ times_worked += 1

    "Month 24"
    if (profession == "doctor"):
        scene bg clinic with fade
    elif (profession == "crafter"):
        scene bg workshop with fade
    elif (profession == "auto mechanic"):
        scene bg machine_shop with fade
    elif (profession == "teacher"):
        scene bg classroom with fade

    return
