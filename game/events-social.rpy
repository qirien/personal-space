# Afternoon Events
# Social

# Default Event
label social_def:
    "I met up with my friend Sara and we talked together. She is a great listener and understands me so well."
    $ skill_social += 5

# Intro Event
label social_0:
    "Aside from [his_name], I had one other person I felt close to - Sara."
    "We had met on the ship when [his_name] was meeting with the other farmers."
    scene bg community_center with fade
    show her normal at midright
    show sara at midleft
    with dissolve
    sara "I guess you're not a farmer, either, huh?"
    her "Not really. I'm a [profession]."
    sara "Really? That's pretty cool."
    "We talked about my job for a while, and then she admitted,"
    menu:
        sara "I'm not sure why I'm here...I'm not really good at anything."
        "That's not true!":
            her concerned "That's not true! I mean, I don't know you very well yet, but I can tell you're a good listener."
            sara "Thanks..."
        "Why are you here?":
            her "Why {b}are{/b} you here?"
            sara "Well..."
        "(Change the subject)":
            her surprised "(I don't know what to say!)"
            her normal "Well, uh, what do you like to do?"
            sara "I like to read...I read a lot. I'm a pretty good photographer, too."
            her "That sounds fun. Who's in your family??"
    show her normal
    sara "My husband is Ilian Andrevski - he's not a farmer, either. He's a food scientist."
    her surprised "Really? There are food scientists?"
    sara "Yes, they study things like nutrition and shelf-life and ways to preserve foods while maintaining lots of nutrients - things like that. I think he'll also do a lot of the inventory and distribution of food once we get there."
    her normal "What about you? What's your job?"
    sara "Breeding stock."
    her surprised "!"
    sara "Ha ha ha, I'm just kidding! Though it does seem like we'll be expected to have lots of kids quickly to increase the population...but I'll be helping Ilian in the storehouse, and also helping the mayor stay organized."
    her normal "Good! I bet we'll see each other a lot, then."
    sara "Probably so. It's nice to have met you, [her_name]."
    "Sara and I talked almost every day after that. We had a lot in common as newlywed colonists, and she had an easy laugh and an understanding smile that made her fun to be around."
    $ skill_social += 10

    return

label social_1:
    scene bg farm_exterior flip with fade
    "One day I was at the Peron's house. Natalia had found some fruits while hiking that the scientists deemed edible. She had picked so many; her table was covered with them."
    show natalia at midright
    show her normal at midleft
    with dissolve
    her happy "These look really good!"
    natalia "Here, try one."
    her surprised "Thanks...Oh!"
    "They tasted sweet and juicy, but they were full of hard, bitter seeds."
    show her normal
    natalia "I'm going to cut them in half, and then scrape out the seeds and dry them. Want to help? You can take some home with you."
    her happy "Sure!"
    "We cut and scraped and talked together all afternoon."
    $ skill_social += 10
    $ community_level += 2
    return

# Start a weekly game night at the community center
label social_2:
    scene bg community_center with fade
    "Soon after we arrived, the main shuttle bay was converted into a community center. It was the only building large enough for everyone to gather in at once."
    "But other than official colony meetings, it wasn't used very much."
    show pavel at midright with dissolve
    show her normal at midleft with moveinleft

    her serious "Excuse me, Mayor Grayson?"
    boss "Yes, [her_name]?"
    her surprised "Can anyone use the community center?"
    boss "Well, of course, for anything that's open to the entire colony."
    her normal "Good, that's what I wanted to know..."
    hide pavel
    hide her
    "I sent out a message inviting everyone to come to a once-a-week party. People could bring games and snacks to share, and just chat and be together."
    "I wasn't sure anyone would show up..."
    "But [his_name] agreed to come, and Sara and Ilian and the mayor were coming, so we could at least hang out."
    show him normal at midleft
    show her normal at center
    with dissolve
    show brennan at quarterright behind her, him
    show pavel at right behind her, him
    with moveinleft
    show ilian at quarterleft behind her, him
    show sara at left behind her, him
    with moveinright
    play sound "sfx/people.mp3" loop
    "I was surprised when a lot of people showed up! I guess there's not much else to do here yet..."
    hide pavel with moveoutleft
    hide brennan with moveoutright
    show natalia at left behind her, him
    show martin at quarterleft behind her, him
    with moveinright
    show sara at quarterright behind her, him
    show ilian at right behind her, him
    with move
    natalia "Great idea, [her_name]!"
    sara "Yeah, it feels good to get out of the house!"
    "Our snacks were not very tasty (mostly vegetables), and the games were not always fun, but joining together informally once a week helped us feel closer together."
    stop sound fadeout 2.0
    
    $ skill_social += 10
    $ community_level += 2
    return

# Invite family over for dinner
label social_3:
    scene bg farm_interior with fade
    "Even though we had all lived together for months, there were some people in the community we didn't know very well."
    show her normal at midright
    show him normal at midleft
    with dissolve
    her "I invited the Nguyens over for dinner tomorrow night."
    him surprised "Oh yeah, I know Thuc pretty well. Don't they have, like, ten kids?"
    her surprised "Yes..."
    him serious "Okay, that will be interesting...where are we all going to sit?"
    her serious "I thought we'd just sit outside. I guess I should make some food that kids like, too."
    him normal "Maybe some fruit?"
    her normal "Yeah, I'll figure it out, don't worry."
    "I worked hard on the food, and spread out some blankets to sit on, even though it meant I'd have more laundry to do to get all the dust out."
    scene bg farm_exterior with fade
    show him normal at right
    show her normal at quarterright
    with dissolve
    show julia at center
    show thuc at midleft
    show kid at left
    with moveinleft
    julia "Thank you so much for having us over for dinner. I only hope we don't wear out your generosity by the end of the evening."
    her happy "Well, hopefully I made enough food! Let's eat!"
    if (skill_domestic >= 10):
        "I served make-your-own-wraps, where you could put in beans or cheese or vegetables or whatever you wanted. I had some salsa or salad dressing that people could put on, too. They were delicious, and the kids liked them too."
    else:
        "I just put out a bunch of beans, crackers, fruit, and vegetables, and let people choose what they wanted. It tasted a little bland, but the kids seemed to like it."
    "Then the kids all played hide-and-seek around the farm while we talked with the Nguyens."
    hide kid
    if (profession == "teacher"):
        her normal "The kids are doing great in school."
        julia "I'm glad to hear that! They look forward to it; they say you are a wonderful teacher."
        her serious "That's nice to hear. Joanna is about ready to graduate, I think. She knows way more than I do about geology and physics already. And Miranda is not far behind."
        thuc "It's too bad there's no university here, but I think she will do fine studying with Dr. Lily."
    if (is_pregnant):
        thuc "I hear you are expecting a baby, congratulations!"
        her happy "Thank you! So many new things keep happening; sometimes it's a little overwhelming."
        julia "Yes, that's true. But mostly babies just need love. Everything else you can figure out as you go."
        her concerned "But...what if I don't love the baby right away?"
        julia "You want to love the baby, don't you?"
        her serious "Yes, of course!"
        julia "Well, that's enough love to start with. Do you have someone to deliver the baby yet?"
        her surprised "I guess I assumed someone at the clinic would do it?"
        julia "Let me help you, too. Call me on the radio when it's time, and I'll meet you at the clinic or wherever you are."
        her happy "Really? That would be great; you seem to be an expert on having kids, but I'm not sure if anyone at the clinic knows much about babies."
        julia "I'd be happy to help."
    elif (want_kids):
        her flirting "So...Mrs. Nguyen, you seem like an expert on kids."
        julia "Please, call me Julia. I do have a lot of experience with children - besides my own ten, I've been at twenty deliveries or so, helping the mother through labor."
        her surprised "Really? We want to have kids, sometime..."
        julia "Well, I hope you'll let me help you. There's a lot that the doctors don't know about babies and new mothers."
        if (profession == "doctor"):
            her serious "Yes, I know about all the medical conditions and treatments, but not very much about the actual babies themselves."
        else:
            her surprised "That's probably true..."
    else:
        "[his_name] and I talked to the Nguyens about our farms and crops, and what things seemed to help the crops grow better, and what the kids were doing."

    "We talked and talked, until finally, it got dark. One of the moons was shining brightly; the other was dark."
    show overlay night with dissolve
    julia "Thanks so much for having us over, [her_name]. I'm glad we got to know you a little better."
    thuc "Yes, the food was delicious!"
    her normal "Thanks for coming, we enjoyed your company."
    "[his_name] and I watched them start walking for home."
    hide natalia
    hide martin
    with moveoutleft
    him "I wonder what our family will look like in a few years?"
    if (want_kids or is_pregnant):
        her concerned "It will be different, won't it?"
    elif (loved >= 0):
        her flirting "As long as you and me are in it, it will be just fine."
    else:
        her surprised "Who knows?"

    $ skill_social += 10
    $ community_level += 2
    return

#organize lunch group
label social_4:
    "Sara and I met for lunch every week to chat and take a break."
    scene bg community_center with fade
    show sara at midright
    show her normal at midleft
    sara "How are your neighbors doing?"
    her happy "We ate with the Nguyens a while back and they were all doing well! We're all starting to live off the land; it's kind of exciting."
    sara "I know! Hopefully we won't starve or anything."
    her laughing "Yeah, really!"
    sara "Sometimes it seems like the physical needs are actually the easiest... it's making social connections that's hard."
    menu:
        "I should get out more.":
            her normal "Yeah, we should see if we can get a lunch group going! Lots of people are on break now; let's ask around."
            "We found a few other people who seemed interested in gathering at the community center for lunch every Friday."
        "I'm not worried.":
            her serious "I feel pretty socially healthy now. I see you, my boss, and my husband pretty regularly."
            sara "But we're going to be here the rest of our lives! Shouldn't we get to know everyone?"
            menu:
                "I don't want to meet everyone.":
                    her concerned "Sometimes I feel like it's easier to like people when I don't know them."
                    sara "True. And if everyone knew each other we'd be more likely to gossip and get all drama-y."
                    her normal "Maybe I could stand to meet a few new people though."
                    sara "Look, there's someone else on her lunch break, let's introduce ourselves."
                    show lily at quarterright with dissolve
                    show her at center
                    show sara at quarterleft
                    with move
                    if (not met_Lily):
                        "We met Lily, one of the workers in the science lab. She invited us to come visit her to learn more about alien botany."
                    elif (met_Lily):
                        "I had already met Lily, but I introduced her to Sara and we had an enjoyable lunch together."
                "I guess.":
                    her serious "Well, if I'm going to meet them all eventually I might as well get to know them sooner rather than later."
                    sara "Exactly. Look, some other people are taking their breaks now too, let's ask them if they want to have lunch with us."
                    "We interrupted a few conversations, but luckily everyone was in a good mood and seemed happy to meet us. We decided to meet every Friday for lunch in the community center."
            
    $ skill_social += 10
    $ community_level += 2
    return

# Organize community movie night!
# Watch a neighbor's kids; think about having own kids
label social_5:
    scene bg community_center with fade
    "One week at Friday lunch group, we were all complaining about our lack of excitement."
    show lily at quarterright
    show sven at quarterleft
    show sara at midleft
    show her normal at midright
    with dissolve
    lily "We all live so close to each other, but it seems like in the evening everyone just wants to go to bed early."
    her concerned "Well, people who aren't working in town are farming all day, which is pretty tiring."
    sven "That's true, but don't you get tired of sitting at home all the time? I'm in the library all day for work and the last thing I want to do when I get home is sit around by myself some more."
    her normal "I'm pretty busy, but I agree that it'd be fun to do something together as a community."
    lily "I was just reading on how we could use a magnifying glass with our tablets to make a projector. Perhaps we could have a movie night?"
    sven "Yes, this sounds perfect. A movie is low-key enough that even if you're super tired from farming you should be able to sit through it."
    sara "And kids like to watch movies too, so we could include everyone."
    her happy "I know the perfect movie!"
    menu:
        "What should we watch?"
        "A sci-fi drama":
            her laughing "There's a space opera movie about finding the strength to persist through hardships that I think would be highly entertaining!"
            sara "Oh no, is it one of those Star Wars remakes?"
            her normal "Well, yes, but isn't it interesting to think about what space travel will be like in the future?"
            sara "You just like watching it for the cute guys."
            her happy "I think everyone enjoys watching good-looking people do stupid things. Plus I already know we have it in the archives!"
            sven "We do have lots of Star Wars remakes in the archives, but maybe you didn't know that we have some rarer sci-fi movies here too."
            her surprised "Like what?"
            sven "So, {i}Time for No Man{/i} was originally a tellanovella, but when set in space, it suddenly became a sleeper cult hit in the 2030s!"
            her flirting "'No man', huh? Does it have any guys in it?"
            sven "I think it has a few. It's not just lesbians if that's what you're asking."
            sara "Is it appropriate for children?"
            sven "Sure. There's some innuendo but that goes right over their heads."
            scene black with fade
            "We decided to watch {i}Time for no man{/i} the next day in the evening. I sent out a message to the colony message board, and tried to remind everyone I saw to come."
            "The movie was kind of ridiculous. At one point two cousins realized they were actually sisters, and that their evil uncle was actually their father. Then it turned out he wasn't evil at all, but had been infected with an alien virus that caused him brain damage that made him act rudely."
            "A feminist organization let the cousins/sisters travel the galaxy at light speed to administer vaccines to the rest of civilization, but by the time they got anywhere, everyone else had been infected by the virus which made them act rudely."
            scene bg community_center with fade
            show him normal at sitting, midleft
            show her normal at sitting, midright
            show overlay night
            with dissolve
            him annoyed "This movie is ridiculous."
            her annoyed "Yeah, there's no way a virus would only affect men. It's not like our immune systems are all that different."
            him surprised "What would you do if I turned into a jerk overnight?"
            menu:
                "Take you to the doctor.":
                    her normal "I would take you in to have your head examined."
                    him happy "Because the only way I would be mean to you is if I had brain damage, right?"
                    her annoyed "And if you were mean to me you might get brain damage, if you know what I mean."
                    him flirting "Oh, you're so feisty."
                    menu:
                        "You'd better believe it.":
                            her flirting "I know you like it like that."
                            him "Let's take this indoors!"
                            $ made_love += 1
                        "Ugh, stop it.":
                            her annoyed "Stop being so patronizing. It's like you don't take my threats seriously."
                            him annoyed "I'm pretty sure that if we got in a fight I could win. Besides, it's not like you're doing physical labor all day like I am. I'm a lot stronger."
                            her angry "Well you don't have to talk down to me like that just because you're stronger."
                            him concerned "Geez, sorry."
                            $ loved -= 2
                "You already are a jerk.":
                    her annoyed "Too late, you're already a jerk."
                    him surprised "Hey, I know I tease you a lot, but that doesn't mean I'm a jerk."
                    her angry "Then I guess I wouldn't notice anything was wrong!"
                    $ loved -= 2
            "It seemed like the other families enjoyed the movie too, even though it was pretty ridiculous."
        "A historical mystery action flick":
            her happy "Sherlock Holmes would be perfect! It has mystery, suspense, romance, action, and would help educate children about the 1890s."
            sara "Yeah, and it would encourage kids to try smoking alien weeds."
            her annoyed "Oh come on. We grew up watching films with people drinking all the time and it didn't turn us into alcoholics."
            sara "The plot of a Sherlock Holmes mystery is also difficult to understand, so it might not hold their interest."
            sven "Wait, I can think of a historical film with plenty of mystery that kids and adults might like."
            her normal "Tell us about it."
            sven "It's a mini-series called {i}The Adventures of Emily Thompson{/i} about a young girl living in a small town in England during the 1900s. She solves various mysteries including finding missing shoes and pets, culminating in her finding the culprit of a livestock theft."
            her surprised "Well, that does sound a little more child-friendly than murder mysteries."
            sara "Let's do it."
            scene black with fade
            "I sent out a message to the colony e-mail list, and tried to remind everyone I saw to come."
            scene bg community_center with fade
            show her normal at midright
            show him normal at midleft
            show overlay night
            with dissolve
            "We had a pretty good turnout, and the kids and adults both found things to laugh at."
            him surprised "So, the part where the sadistic child was killing sheep with bread-encrusted coins was a little hard for me to believe."
            her flirting "It could have been worse. The sadistic child could have been a werewolf who was eating them."
            him happy "Yeah, but making coins out of copper is a waste of metal!"
            her happy "Seriously, they should be making teapots out of them."
            him normal "Or you know, wires."
        "An animated art film":
            her normal "Let's put on an old cartoon movie so that the kids will enjoy it too."
            lily "Oh, let's watch {i}Wall-E{/i}, I always thought that one was cute."
            her surprised "I was thinking more along the lines of {i}The Old Man and the Sea{/i}."
            sven "I think that movie would put everyone to sleep."
            her normal "It's only forty minutes long!"
            sven "Let's watch {i}Wall-E{/i}. I haven't seen it in a while and it could start some interesting conversations about what our colony should be like."
            sara "I agree! Some of the younger kids have never seen it, and I think they would like it."
            scene black with fade
            "We decided to watch {i}Wall-E{/i}. I sent out a message to the colony e-mail list, and tried to remind everyone I saw to come."
            scene bg community_center with fade
            show her normal at midright
            show him normal at midleft
            show overlay night
            with dissolve            
            "The kids enjoyed watching the robot's antics, and the trash-filled city reminded me of some of the things we were trying to do differently in our colony."
            her concerned "I'm so glad the green revolution happened before the whole earth turned into a landfill."
            him concerned "Yeah, and then no one could make anything because the regulations on materials were so strict."
            her normal "Aren't you glad we're here where we can decide those things for ourselves?"
            him normal "Yes, I am glad. Are you?"
            menu:
                "What should I say?"
                "I love it here!" if (loved > 0):
                    her normal "Of course I miss my family, but I love our community and working with you to make a place for ourselves."
                    him laughing "Good, because we're stuck here!"
                "I don't really like it here" if (loved <= 0): 
                    her sad "I think about going home all the time. I wish I hadn't come."
                    him surprised "Really? I thought you were getting used to it."
                    her annoyed "No, I'm not."
                    him concerned "Maybe you just need time."
                    her surprised "You don't wish we could go home?"
                    him happy "I love it here! I love that we're going to be able to live off the fruits of our labors and have contact with the land we live on."
                    her concerned "But we might not survive! And I keep messing things up."
                    him normal "Making mistakes is how we'll learn! And even if we end up dying young together... isn't that kind of romantic?"
                    menu:
                        "What should I say?"
                        "No, it's not romantic":
                            her annoyed "It's not romantic. We'll be too dead to appreciate how cute our sacrifice is."
                            him normal "Well, I'm happy as long as we're together."
                        "It could be romantic":
                            her flirting "If they find our skeletons embracing each other, I guess that could be romantic."
                            him flirting "That's the spirit!"
                            $ loved += 5
                "Most of the time":
                    her normal "Most of the time I'm happy to be here. There are lots of things I miss, of course. But it's also exciting to start something new."
                    him happy "We're living off the land! We can make our own futures!"
                    her flirting "Yeah, as long as that future involves farming of some kind."
                    him annoyed "Well, you're not farming."
                    her annoyed "True. But it's going to be a big part of our lives for the foreseeable future, is what I meant."
                    him normal "That's the way I like it. There's nothing like farm-fresh food to make you healthy."
        
    "The families went home as we talked. Sven and Sara and Lily and I congratulated each other for a movie well-watched, and I went home feeling like I helped everyone feel a little closer."
    $ skill_social += 10
    $ community_level += 2
    return

#TODO finish adding emotions
# Someone's house burns down; will you help?
label social_6:
    scene bg bedroom with fade
    show overlay night
    show him serious at midright
    show her serious at midleft
    with dissolve
    #TODO add images
    "One good thing about being such a small community was that we all helped out when someone needed it."
    "Like when Sara's house burned down..."
    "It was the middle of the night when the radio crackled on."
    "Sara on the radio" "Is anyone awake? Please, help! Our house is on fire!!!"
    him "Let's go!"
    scene bg sunset with fade
    show overlay night
    show ilian at quarterright
    show sara at midright
    with dissolve
    show him serious at midleft
    show her serious at quarterleft
    with moveinleft
    "We brought buckets of water, but by the time we got there, the whole house had already burned to the ground."
    sara "Oh, [her_name], I'm so glad you came! It's... awful."
    menu:
        "What should I say?"
        "At least you and Ilian are okay.":
            her concerned "At least you two got out safely..."
            sara "Yeah, that's good. We didn't have time to bring anything with us, though...It's a good thing we weren't sleeping naked."
            her normal "Yeah, that's true."
        "Did you lose much?":
            her surprised "Did you lose much?"
            sara "Everything...which actually isn't that much. A few things from Earth, our computers, clothes, some tools."
            her sad "That's terrible..."
        "How did the fire start?":
            her surprised "How did your house catch fire?"
            sara "I don't know! We just woke up and there was this huge fire over by the oven."
            her "Maybe there was something wrong with the stove?"
            sara "What does it matter?! Either way, our house just burned down! Not just the house, but our clothes, tools, computers..."
            her concerned "I'm so sorry..."
    sara "I don't know where we'll stay; what we'll wear; how we'll eat..."
    menu:
        "Come stay at our house.":
            her serious"You and Ilian are welcome to stay at our house if you want..."
            sara "Really? I know your house is pretty small..."
            her normal "It's no trouble. C'mon, it'll be fun! We can hang out every night like it's a weekend!"
            him normal "Yeah, and don't worry; [her_name] doesn't snore too loudly."
            show her annoyed
            ilian "Thanks; we really appreciate it."
            sara "Yes, honestly, I'd rather stay with you guys than anywhere else."
            scene bg farm_interior with fade
            "It was a little crowded and stressful having so many people in our one-room house"
            "And sometimes I overheard things I really didn't want to know..."
            show ilian at quarterright
            show sara at midright
            ilian "I don't want to go anywhere tonight; I have a headache."
            sara "But I told Helen and Sven we'd both come over! How come you only have a headache when it's time to do something I want to do?!"
            ilian "It's not like I can just turn them on or off! You think I like my head pounding?"
            sara "Yeah, I think you like having a headache more than you like doing something with me."
            ilian "That's ridiculous!"
            sara "You're ridiculous! No wonder you don't have any friends..."
            show her serious at left with moveinleft
            ilian "..."
            sara "..."
            her concerned "Ah... I was just going to make some dinner, but maybe I'll just take a walk outside instead."
            sara "I'll go with you."
            scene farm_exterior with fade
            show her serious at midleft
            show sara at midright
            with moveinright
            sara "Sorry you had to hear that."
            her "No, it's okay, everyone has disagreements."
            sara "I just feel so trapped sometimes! I hate staying at home in the evenings and doing nothing!"
            her "I guess that's Ilian's favorite thing to do?"
            sara "Yeah..."
            her "Well, why don't I go with you to Helen's, and we can have a girl's night? We haven't done that for a while..."
            sara "Okay...thanks, [her_name]."
            scene black with fade
            "Luckily, they had materials for an extra house on the shuttle, so the whole community worked together one day to put it together for them."
            "The Nguyens donated one of their computer pads for them to share, and everyone pitched in some cookware and tools to replace those that had burned."
            scene bg farm_interior with fade
            show him normal at midright
            show her normal at midleft
            him "It wasn't as bad as I thought, having Ilian and Sara stay with us for a week..."
            her flirting "Yeah. But now that we have the house to ourselves, we can do whatever we want, whenever we want..."
            him flirting "I like the way you think."
            $ community_level += 5
            $ relaxed -= 2
            $ made_love += 1
        "You can stay at the community center.":
            her serious "You should be able to stay at the community center; there's some comfortable sleeping areas from the shuttle, and a little kitchen."
            sara "Yeah, I guess that will work."
            "They settled in on the floor of the community center."
            "Luckily, there were extra materials for building another house on the shuttle, but it took Ilian and Sara a few weeks to build it by themselves."
            "We didn't have time to help out; we were all too busy."
            "I hoped that something like that would never happen to us."
            $ skill_social += 5
            return
        "You could stay at the clinic." if (profession == "doctor"):
            her "You could stay at the clinic; there's extra beds we're not using."
            sara "That could work..."
            "It was a little awkward, coming to work at the clinic when they were using it for a house. But it was good in some ways, too."
            "Sara started watching me work and I was able to teach her more about health and medicine."
            "Even so, we were happy to find out that there were extra materials for building another house, and we got right to work helping Ilian and Sara build it."
            $ community_level += 2
        "I hope you find a place to stay.":
            her serious "Yeah, I hope you can work something out."
            "They settled in on the floor of the community center."
            "Luckily, there were extra materials for building another house on the shuttle, but it took Ilian and Sara a few weeks to build it by themselves."
            "We didn't have time to help out; we were all too busy."
            "I hoped that something like that would never happen to us."
    "The fire was a tragedy, but it also drew us closer together."
    $ skill_social += 10
    return


# Teach 'enrichment' class on [profession]
label social_7:

    $ skill_social += 10
    return


# Community Shindig
label social_8:
    scene bg path with fade
    play music "music/Prelude22.ogg" fadeout 3.0

    "One day Sara and I took a walk together."
    sara "I think this town needs something special."
    her "Like what? Indoor plumbing?"
    sara "No, silly, I mean a special event! Like a festival, a party, a shindig! Something to cheer everyone up, give them hope."
    her "Yeah, I know what you mean. We've all been working pretty hard..."
    sara "So let's plan one!"
    her "If we got Mayor Grayson in on it, he might have some special food or something we could use."
    sara "Good idea."
    "We asked him about it, and he thought it sounded great."
    boss "It's about time we had a celebration of some kind. Earth Day is in two weeks - we could have it then. But I don't know who to ask to plan it - everyone is so busy..."
    sara "Just leave it to us. We'll have a party ready in two weeks!"
    
    $ party_music = ""
    $ party_entertainment = ""
    $ party_decorations = ""

    "We decided to make it a potluck, so everyone could share the different foods they had grown. We also obtained some goodies from the dwindling rations in the storehouse."
    sara "Look! Potato chips! And fruit punch mix!"
    her "Wow, I haven't had those in months!"
    sara "OK, I think we have the food down. What else should we have?"
    menu party_menu:
        "What does the party still need?"
        "Music" if (party_music == ""):
            her "We need some music."
            sara "Yeah...should we use recorded music, or see if we can get someone to play live?"
            menu:
                "What kind of music?"
                "Recorded music":
                    her "Recorded music is fine; then we we have more control over it, and it's better for dancing."
                    sara "Let's get a good playlist setup of lots of different kinds of dance music."
                    her "Good point; everyone here probably likes different things, so I will send out an e-mail asking everyone to send me their favorite dance song."
                    $ party_music = "recorded"
                "Live music":
                    her "Live music is better because it's people you actually know playing the music."
                    if (skill_creative >= 50):
                        her "I can play, you know."
                        sara "Of course! Can you get a group together to play some songs?"
                    else:
                        sara "Yes! That would be so cool. Can you be in charge of that?"
                    her "Sure, I'll send out an e-mail. Maybe some people will want to play or sing solos, too."
                    $ party_music = "live"
                    
            sara "OK, we've got the music!"
            jump party_menu
                                    
        "Entertainment" if (party_entertainment == ""):
            her "We should have some kind of entertainment."
            sara "Yeah, something everyone would like..."
            menu:
                "How about:"                
                "Party games":
                    her "Maybe some party games? Like musical chairs or something? Is that dumb?"
                    sara "Not if we play it right..."
                    her "There are also a lot of people. We might need to split them up into small groups."
                    sara "I have some ideas; leave it to me!"
                    $ party_entertainment = "games"
                "Talent show":
                    her "How about a talent show? I'm sure lots of people have things they can do, even if it's just jokes or a skit or something."
                    sara "Sure! We'll just organize the performances and be the announcers."
                    $ party_entertainment = "talent show"
                "Contests":
                    her "Maybe some kind of contests?"
                    sara "Okay, this is totally redneck, but what about a wood chopping contest?"
                    her "Ha ha, that actually could be fun. We'd need some other contests, too, though..."
                    sara "Leave it to me! I'll have a bunch of fun contests."
                    $ party_entertainment = "contests"
            jump party_menu

        "Decorations" if (party_decorations == ""):
            her "Some kind of decorations would be fun..."
            sara "Yeah, it's not like we can just go to the party store and get some balloons or something, though."
            her "How about wildflowers?"
            sara "Oh, yeah, we could just have a vase of wildflowers on each table."
            her "I'll see if I can get some old jars or bottles to use as vases."
            if (skill_creative >= 20):
                her "Maybe we could glue old papers or scraps of cloth on them to make them look nice? I'll figure something out."
                sara "Sounds good! We don't need a lot of decorations; just enough to show that it's a party. I'll see if I can make the lights in the new community room change color."
            $ party_decorations = "flowers"
            jump party_menu

        "Nothing else":
            her "I think that's enough."
            jump done_party_menu

label done_party_menu:
    "Sara and I worked hard for two weeks getting everything ready. Finally, the night of the party came..."
    scene black with fade
    "As people started to arrive, they seemed to brighten when they saw the community center ready for a party."
    if (party_decorations == "flowers"):
        "The flowers we picked looked nice. Even though they were nothing like Earth flowers, they had their own beauty. And Sara had programmed some of the lights to glow softly blue and green, like an ocean."

    if (party_music == "recorded"):
        "We played some great dance music, and some people really got into dancing! It was really interesting to hear the variety of songs everyone sent us. There was pop music, ballads, slow love songs, techno, rap... Even though some of it was in languages we didn't all know, it was still good for dancing."
    elif (party_music == "live"):
        if (skill_creative >= 50):
            "I was a little nervous about playing music for everyone, but as soon as I started playing I lost myself in the songs."

        "It turned out we had a lot of musicians in our little community. Some of them played together - we had some great Irish dancing music with a fiddle and flute - but there were a lot of solos, too."

        "Everyone brought some food from their farm to share. There were lots of different soups and salads, some strange fruits that Natalia found while hiking, some local game meat, some hearty rolls, and an egg casserole."
    if (have_goat == True):
        "We brought some cheese we had made from our goat's milk, along with a few vegetables."
    else:
        "We brought some fresh vegetables and some salsa."

    if (party_entertainment == "games"):
        "After we ate, Sara broke us up into small groups for games."
        "The first one was 'Two Truths and a Lie' where we each had to tell three things about ourselves, and the group would try to guess which one wasn't true."
        her "Hi, I'm [her_name]. I met my husband [his_name] only six months before coming to Talam, I helped organize this party, and I used to-"
        menu:
            "Used to what? (I need to tell a plausible lie...)"
            "Eat bacon ice cream":
                her "-eat bacon ice cream."
            "Work as a roller-skating carhop":
                her "-work as a roller-skating carhop."
            "Hate looking at the stars":
                her "-hate looking at the stars."
        "Everyone guessed my lie right away, but that's okay. I was more interested in hearing what everyone else had to say."
        him "Hi, my name's [his_name]. I like to write poetry, I won a sheep-riding rodeo when I was five years old, and in high school I was known as The Candid Bandit."
        "(Well, I know he likes to write poetry...but I have no idea which of the other things is true!"
        him "No one has a guess which one of those is a lie?"
        menu:
            "What should I guess?"
            "The sheep-riding is a lie.":
                her "I'll guess the sheep-riding."
                him "Nope!"
            "The Candid Bandit nickname is a lie.":
                her "Nobody called you 'The Candid Bandit'."
                him "You're right. But maybe they should..."
            "I'm not going to guess.":
                "I had no clue."
        him "I really did win a sheep-riding rodeo when I was five. Just held on forever. I wouldn't let go even when they told me it was over. Nobody has called me 'The Candid Bandit' yet, but you can if you want to."
        her "(I'm not going to call him that!)"
                 
        "We also played a game called 'Mafia' where we had to guess who in our group was secretly a bad guy, and also a game called 'Unfortunately' where each person told one sentence of a story, starting with the words 'Fortunately' or 'Unfortunately'."
        "It was fun to get to know our neighbors better and relax for a bit."

    elif (party_entertainment == "talent show"):
        "We had a few entries in the talent show, but not a lot. The Mayor got up and told jokes, some of which were even funny. Some of the Peron children sang a silly song about a goat, and Thuc juggled knives. We had no idea he could do that!"
        "But I was even more surprised when [his_name] took the stage. I whispered to Sara,"
        her "You didn't tell me he had an act!"
        sara "I thought you'd like being surprised!  Shhh, watch."
        him "I just have a poem for you all, and then I'll leave you alone."
        "I was apprehensive. His previous 'poems' were not that impressive."
        him "Here on this lonely planet\nFar from that of our birth,"
        him "We're trying to make our own\nNew planet, just like Earth."
        him "The skies aren't really blue here,\nA red sun flares above,"
        him "But we've got what's most important:\nFriends, family, and love."
        him "So though we often struggle\nIn our small community,"
        him "We'd better work and get along,\nOr we'll be extrasolar history."

        menu:
            "That was..."
            "Touching":
                "...actually sort of touching. It wouldn't win any poetry contests, but I think it described how we all felt. Everyone applauded, including myself."
            "Funny":
                "...kind of funny. 'Extrasolar history', hee hee. Everyone seemed to agree with me; they laughed and applauded."
            "Embarrassing":
                "...embarrassing. Poetry should be a private thing, shouldn't it? But the other people seemed to like it, and they applauded politely."
                $ loved -= 5
        "We all felt closer together after enjoying the performances together."

    elif (party_entertainment == "contests"):
        "Next came the contests. Sara was in charge of those."
        sara "All right, listen up! We've got four contests tonight, and I need participants to make these a success! So I hope you will all consider taking part in a contest, even if it's just for fun! The contests are: Wood Chopping, Space Ship Construction, Colony Trivia, and Adamantium Chef."
        menu:
            "Which contest should I enter?"
            "Wood Chopping":
                "I decided to enter the wood chopping contest."
                sara "Line up, everyone! Now, the goal is to see who can chop the most wood in one minute! Ready, set...GO!"
                "I raised the axe and let it fall to split the wood, barely taking time to aim. I was concentrating so hard, I didn't even notice what anyone else was doing."
                him "Go, [her_name]!"
                sara "Time's up!"
                if (skill_physical >= 70):
                    "They counted the wood in each person's pile, and I managed to chop more wood than anyone else! I guess all the exercise I'd been doing really paid off."
                else:
                    "They counted the wood in each person's pile, but I hadn't really chopped very much. My arms were sore and I was sweating all over, but it was still fun."
            "Space Ship Construction":
                "I decided to enter the Space Ship Construction contest."
                sara "This is a game for teams of two, so find a partner!"
                him "Let's do it."
                her "Yeah, you and me, right now."
                sara "I have a box of materials for each team. Your goal is to build the sturdiest and coolest-looking cardboard spaceship you can in five minutes! Then we will launch them from the roof and see whose has the best landing."
                sara "Ready, set...GO!"
                "[his_name] and I rummaged through the box. Sara had gathered trash from everyone and cleaned it off so we could use it on our creation."
                him "Let's make the box the body of the spaceship."
                her "OK, we'll also need some wings..."
                if (loved <= 0):
                    him "Why are you putting that tin foil there?"
                    her "It's reflective, like a solar panel."
                    him "Solar panels aren't reflective."
                    her "We don't have a lot of time! I'm just doing the best I can!"
                else:
                    "We worked together fluidly, like dancers, attaching a piece here and wrapping a piece there, not needing to talk much."
                "We finished just as the time was up."
                if (loved > 0):
                    if (skill_creative >= 70):
                        "Ours didn't have the best landing, but it looked so artistic and sleek that they gave it the best score anyway. We won the contest!"
                    elif (skill_technical >= 70):
                        "Ours didn't look the best, but it actually kind flew off the roof and glided for a bit before landing gracefully on the ground. We won the contest!"
                else:
                    "Ours was kind of a disaster. We felt relieved when the contest was over."
            "Colony Trivia":
                "I decided to enter the triva contest. They had questions about the shuttle, the colony, and the people on the colony."
                if (skill_knowledge >= 70):
                    "Because of all my research, I was able to answer a lot of the questions about the shuttle and the colony."
                elif (skill_spiritual >= 70):
                    "Because of my connections in the community, I was able to answer a lot of the questions about the people in the colony."
                sara "And for the last question, which will determine the winner of the trivia contest:"
                sara "What is Mayor Grayson's favorite song?"
                menu:
                    "The mayor's favorite song?"
                    "\"Walkin' on the Sun\"":
                        her "\"Walkin' on the Sun\" is his favorite song."
                        sara "Sorry, that's not it."
                        "I didn't win, but I had fun anyway."
                    "\"It Came Out of the Sky\"":
                        her "\"It Came Out of the Sky\" is his favorite song."
                        sara "Sorry, that's not it."
                        "I didn't win, but I had fun anyway."
                    "\"Jupiter\", from 'The Planets'":
                        her "\"Jupiter\", from 'The Planets' is his favorite song."
                        sara "Sorry, that's not it."
                        "I didn't win, but I had fun anyway."
                    "\"It's the End of the World\"":
                        her "\"It's the End of the World\" is his favorite song."
                        sara "That's right! [her_name], you are the winner!"
                        "It was fun to win, and also to learn more about everyone."
            "Adamantium Chef":
                "I decided to enter the Adamantium Chef contest."
                $ party_meat = False
                $ party_gravy = False
                $ party_strawberries = False
                $ party_potato_chips = False
                $ party_onions = False
                $ party_cheese = False
                sara "All right, listen up contestants! You have five minutes to make the tastiest concoction you can out of the leftover food on the tables! Ready, set...GO!"
                "We all scanned through the leftovers. We each had a bowl for mixing, and a dish for serving."
                menu party_chef:
                    "I scooped up some:"
                    "Meat" if (not party_meat):
                        "meat. I looked around for the next ingredient."
                        $ party_meat = True
                        jump party_chef
                    "Gravy" if (not party_gravy):
                        "gravy. I looked around for the next ingredient."
                        $ party_gravy = True
                        jump party_chef
                    "Strawberries" if (not party_strawberries):
                        "strawberries. I looked around for the next ingredient."
                        $ party_strawberries = True
                        jump party_chef
                    "Potato Chips" if (not party_potato_chips):
                        "potato chips. I looked around for the next ingredient."
                        $ party_potato_chips = True
                        jump party_chef
                    "Onions" if (not party_onions):
                        "onions. I looked around for the next ingredient."
                        $ party_onions = True
                        jump party_chef
                    "Cheese" if (not party_cheese):
                        "cheese. I looked around for the next ingredient."
                        $ party_cheese = True
                        jump party_chef
                    "Nothing else":
                        "...and I mixed them all together as best as I could."
                if (skill_domestic >= 70):
                    "Despite the strange ingredients, I melded them together into a mouthwatering concoction. The judges picked mine to be the winner!"
                elif (skill_domestic >= 30):
                    "Despite the strange ingredients, I managed to make something that didn't taste terrible, but it certainly wasn't the best."
                else:
                    "I tasted my concotion, and it was pretty terrible. Still, it was fun to play the game."

    sara "Well, the party's almost over, guess it's time to clean up."
    her "Yeah, is that going to be just you and me?"
    boss "Thank you, Sara and [her_name], for organizing such a wonderful celebration for us. I know you've put a lot of work into it."
    boss "But, folks, I see quite a mess here in our community center. I don't think it's fair that these two ladies should have to do all the work, so I'd like to ask one person from each family to stay and help clean up."
    "I was relieved to hear that, and even more relieved to see that a lot of people stayed to help clean up. Not just one person from each family, either - entire families got to work clearing plates, putting away chairs, mopping up spills, and doing dishes."
    her "Thanks, Mayor Grayson."
    boss "Thank you! I think the party was a success."

    $ skill_social += 10
    $ community_level += 5
    return

# Family (appears to be?) slacking off and mooching off everyone else;
# mayor asks [her_name] to see if she can determine what to do
label social_9:
    "I didn't see the other colonists much during the day, but I assumed they were working hard like we were."
    "But not everyone thought that..."
    scene bg farm_exterior
    sara "Have you seen the Nguyen's farm lately?"
    her "No, I don't really get over there."
    sara "Well, there's nothing on it! They haven't planted anything this season!"
    her "I'm sure there's a good reason..."
    sara "I don't know; I see Mrs. Nguyen at the storehouse all the time, picking up food for their family... but it's not really fair for them to always be taking, and not contributing!"
    her "I see your point... but is it really any of our business?"
    sara "I'm going to tell the Mayor about it."
    "I followed Sara over to the storehouse, where the Mayor was talking to Ilian."
    scene bg storehouse
    boss "Hello, Sara, what can I do for you?"
    sara "Mayor, it's not fair for the Nguyens to always be taking food from the storehouse but not contributing anything. Their job is to be farmers, right?!"
    boss "Yes, it is - you have reason to believe they are not doing their job?"
    sara "Their fields are completely empty!"
    boss "I see... [her_name], would you please go and speak to the Nguyens and see if you can determine the problem?"
    her "(Me?! Well, I guess Sara might be too upset about it, and I am on friendly terms with the Nguyens...)"
    her "Yes, I'll do that."
    scene black with fade
    "I headed over to their farm, and found Mrs. Nguyen hanging up the clothes to dry. She smiled when she saw me coming."
    scene bg laundry
    julia "Hello, [her_name], what can I do for you?"
    menu:
        "What should I say?"
        "Ask if she is okay":
            her "Is...everything all right with your family?"
            "Mrs. Nguyen stiffened, and she suddenly became very interested in her laundry."
            julia "Of course. Everything's fine."
            her "I mean, if there's any problems, we're all here to help each other..."
            julia "I will ask if we need anything."
            "I could tell something was bothering her, but she didn't want to talk about it with me."
            julia "Thank you for stopping by, [her_name], but I have a lot to do and shouldn't waste time chit-chatting."
            her "I just want to help."
            julia "Then please, leave us alone!"
            "All I could do was leave...it was clear something was wrong, but she wouldn't tell me what it was."
            "I sent her an apology message later that day, and she wrote me back."
            julia "Thanks for stopping by...If you really want to help, perhaps someone could help Thuc with a flooding system for the rice he wants to plant."
            
        "Ask why they haven't planted anything":
            her "Why haven't you planted anything this season?"
            julia "You think you know all about our farm, just by looking at it?"
            her "No, but it just looks empty, so I wondered-"
            julia "You wondered?! If you have time to waste with wondering, then perhaps you should put it to better use than bothering people who are trying to get some work done!"
            her "I'm sure you have a good reason--"
            julia "Yes, but I see no reason to share our troubles with you. Thank you for stopping by, but I don't have any more time to share with you."
            "She pinned clothes furiously, and I thought I'd better leave."
            "I sent her an apology message later that day, and she wrote me back."
            julia "If you really want to help, perhaps someone could help Thuc with a flooding system for the rice he wants to plant."

        "Chat for a while":
            her "I just came by to say hi. We don't get to see each other very often, do we?"
            julia "No, we don't! How are things going at your farm?"
            her "Pretty well, though we lost a lot of corn a while back to some nasty bugs here. There's so many things you can't control on a farm, aren't there?"
            julia "Yes, that's true."
            "She paused for a minute. It looked like she was trying to decide whether to tell me something."
            her "Your laundry looks so clean; how are you getting all the stains out? We don't have very good soap here..."
            julia "Ah, you noticed! The trick is fermented urine."
            her "Really?"
            julia "Yes, it's a trick they used in ancient Rome. It's also good for fertilizer."
            her "Wow! You might want to post that on the community message board; I bet everyone would like to know about it."
            julia "Oh, I usually don't have time to go on there."
            her "Well, if you don't mind, then, maybe I will post it on there with a note that you taught me how."
            julia "Well, if you think it will help people."
            her "Yes, we all need to help each other, don't you think?"
            julia "Yes... I suppose you're right."
            her "..."
            julia "You know, we lost a lot of our corn to those bugs, too. All of it, in fact."
            her "Oh, no! Did you have any other crops?"
            julia "We have our vegetable garden, of course, but one day the goats got out and ate most of our plants..."
            her "That's awful!"
            julia "We wanted to plant rice, but we are still working on a system to flood and irrigate the fields properly. Well, Thuc {b}was{/b} working on it, but after the corn..."
            her "It seems fruitless, doesn't it?"
            julia "Yes! What's the point of digging and planning and planting, if some crazy critter is just going to come destroy everything we've done?!"
            her "I know what you mean. I felt the same way, too, after the corn."
            julia "Thuc's not one to complain about his troubles, but I can see he's taken this hard. I suppose I haven't been very encouraging, either."
            her "It is hard... but maybe if you had some help, it'd be easier to get started?"
            julia "Do you think people would help?"
            her "Sure! Not only would they want rice to eat, but we all are going to need help at some point."
            if (has_goat):
                her "Your family has been so kind to us, giving us one of your goats, and Thuc is a good friend to [his_name]."
            else:
                her "Thuc is a good friend to [his_name], so I'm sure he at least would be willing to help!"
            julia "Oh, thank you. I've fretted about this long enough, it's time we did something about it!"
            
    "I told the mayor what I had found out, and he agreed to find some people to help Thuc get his flooding system setup before the start of the next planting season."
    "[his_name] and some other farmers helped, and they managed to get most of it done in a few days. I hoped their rice wouldn't face the same fate as the corn..."
    
    $ skill_social += 10
    return

# Propose and fill seat on Community Council
label social_master:
    her "Mayor Grayson, can I talk to you for a moment?"
    boss "I'd like to, [her_name], but there's too much to do. I have to decide where the new farm should be, and how to allocate the latest harvest, and which supply requests to approve, and-"
    her "That's what I want to talk to you about."
    boss "Oh?"
    her "There's too much here for just one person. You need some help."
    boss "Isn't that what I told you when we first arrived here?"
    her "Yes, and I listened to you, so I hope you will listen to me."
    her "You've done a great job, but the truth is there's just too much for one person. There's a lot of decisions to be made, and some of them would be made easier by someone just specializing in that one thing."
    boss "What do you propose?"
    menu:
        "What do I propose?"
        "Have a committee":
            her "Why not have a committee? One person could be in charge of the store house, one person could be in charge of the land, one person in charge of the services like the school and library, and one person in charge of laws and safety."
            boss "Hmmm..."
            her "Of course, you would be on the committee as well"
            boss "Will you serve as one of the committee members?"
            her "If you like, though I think it would be better if they were elected."
            boss "Very well. I am sure you will be voted on the committee."
            "Sure enough, they voted me to be in charge of the libraries."

        "I could assist you":
            her "Maybe I could help you out with some of the more mundane things."
            boss "Hmm, sort of like a deputy mayor?"
            her "Yeah, you need a deputy! That would also help in case you got sick or something."
            boss "Splendid! But... I believe our charter states that any additional officers must be elected by the adults of the colony."
            her "That's fine; everyone will support me more if they feel like they have chosen me."
            boss "We'll see if anyone else wants the job."
            "The mayor announced a vacancy in the post of deputy mayor, and asked for nominations."
            "Sara nominated me, and [his_name] nominated Ilian, but he didn't want to run. Sven nominated Sister Naomi, but she declined the position as well. Nobody else wanted to run, but we held a vote anyway."
            boss "I guess you've got the job, [her_name]! Now, about those supply requests..."
        
    "It was quite a lot of work to help be in charge of the colony, but the Mayor seemed much less stressed out. It felt good to be trusted, and to help everyone work together here on Talam."

    $ skill_social += 10
    $ community_level += 10
    return
