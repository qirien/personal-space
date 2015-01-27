# Afternoon Events
# Social

# Default Event
label social_def:
    "I met up with my friend Sara and we talked together. She is a great listener and understands me so well."
    $ skill_social += 10
    return

#
# SOCIAL 0
# Intro Event
# Community message board flame war
#
label social_0:
    
    scene bg farm_interior with fade
    show her normal at center with dissolve
    play music "music/Prelude02.ogg" fadeout 1.0
    nvl clear
    
    "We had a community message board online where we could talk to anyone else in the colony easily."
    "But people weren't always as polite online as they were in person..."
    julia_c "Can everyone please make an effort to attend the next farmer's meeting? We can't get your input if you do not attend."
    natalia_c "Some of us are busy farming."
    pete_c "Why're the meetings always held in the community center? That's a long ways for some of us."
    natalia_c "Not such a tough cowboy now, are you? It's only two kilometers!"
    pete_c "Well, it ain't fair for the meetings to always be close for some folks, and far for others. We oughta meet here sometime."
    nvl clear
    julia_c "The community center is centrally located. The meeting will be there."
    pete_c "Who died and made you queen of the colony?"
    "I decided to step in and try and keep the peace."
    
    her_c "Hey, let's all support Julia and the farmers! She's working hard to help everyone be organized and have the food they need."
    pete_c "She's working hard knowin' everyone's business."
    julia_c "We will all have to cooperate to survive!"
    nvl clear
    pete_c "Speak for yourself, we're doin' just fine up here."
    natalia_c "I'll remember that the next time Helen asks me for some eggs!"
    helen_c "Hey, hey, don't drag me into this!"
    pete_c "Yeah, well, see how you like going without milk for your kids. They're runty enough as it is."
    show her concerned
    "Uh-oh. Things were getting personal. Was there anything I could do?"
    nvl clear
    
    menu:
        "What should I do?"
        "Side with Natalia and Julia.":
            her_c "Pete, that's going to far! We all need to help each other!"
            pete_c "Of course you'd side with the other women. Where's all the men around here, anyway?  Back me up, guys!"
            thuc_c "Don't look at me!"
            him_c "..."
            pete_c "[his_name]? C'mon..."
            him_c "I don't care where we meet; let me know when you have it all straightened out."
            nvl clear
            pete_c "You guys are all whipped..."
            natalia_c "Oh please. You had a dumb idea, get over it."
            her_c "I think it's time we all got over ourselves and stopped arguing."
            natalia_c "No one asked you."
            pete_c "Yeah, you don't even come to these meetings."               
        "Side with Pete.":
            her_c "I'm sure Pete wouldn't make a big deal out of it unless it was really important to him. Would it be that terrible to have a meeting at his house?"
            natalia_c "I'm not letting that bully have anything he wants."
            pete_c "[her_name], stay out of this. I don't need you to make my case for me."
            her_c "Fine, forget it."
        "Stay neutral.":
            her_c "Hey, hey, calm down everyone. We don't have to agree about everything, but let's try and be polite, okay? We need each other."
            natalia_c "Tell that to Mr. Lone Ranger, who thinks he can do it all alone. Well, if he keeps this up, he may just get his wish!"
            her_c "I'm telling that to everyone. It takes two to argue, right?"
            natalia_c "..."
            pete_c "..."
            $ community_level += 2
        "Say nothing.":
            natalia_c "You leave my kids out of this!!!"
            pete_c "Hey, it's just an observation."
            natalia_c "Why, you...!"
            him_c "Are we going to have a meeting or not?"
            julia_c "Yes!"
    
    
    julia_c "Anyway, you are all free to choose whether to attend or not, but we hope to get everyone's input at the next meeting."
    her "(Whew! They would never say things like that in person! Hopefully everyone can think a little more before they type...)"
    nvl clear
    
    "Later, Natalia sent me a message."
    play music "music/OceansApart.ogg" fadeout 1.0
    natalia_c "I'm sorry I was so rude; Pete just really gets under my skin!"
    her_c "Oh, I understand. I think everyone's a little frustrated."
    natalia_c "Why don't you come over and we can chat in person? I found a fruit you might want to try..."
    her_c "Sure, I'll be right over."
    nvl clear

    scene bg farm_exterior flip with fade
    "When I got to the Perón's house, I saw Natalia's table was covered with some small, spiny fruits she had found while hiking."
    show natalia at midright
    show her normal at midleft
    with dissolve
    her happy "These look really good!"
    natalia "Here, try one. Dr. Lily says they should be fine, and I haven't had any problems with them."
    her surprised "Thanks...Oh!"
    "They tasted sweet and juicy, but they were full of hard, bitter seeds."
    show her normal
    natalia "I'm going to cut them in half, and then scrape out the seeds and dry them. Want to help? You can take some home with you."
    her happy "Sure!"
    "We cut and scraped and talked together all afternoon."
    $ skill_social += 10
    $ community_level += 1
    return

#
# SOCIAL 1
# Start a weekly game night at the community center
#
label social_1:
    scene bg community_center with fade
    "Soon after we arrived, the main shuttle bay was converted into a community center. It was the only building large enough for everyone to gather in at once."
    "But other than official colony meetings, it wasn't used very much."
    show pavel at midright, behind her with dissolve
    show her normal at midleft with moveinleft

    her serious "Excuse me, Mayor Grayson?"
    pavel "Yes, [her_name]?"
    her surprised "Can anyone use the community center?"
    pavel "Well, of course, for anything that's open to the entire colony."
    her normal "Good, that's what I wanted to know..."
    hide pavel
    hide her
    "I sent out a message inviting everyone to come to a once-a-week party. People could bring snacks to share, and just chat and be together."
    "I wasn't sure anyone would show up..."
    "But [his_name] agreed to come, and Sara and Ilian and the mayor were coming, so we could at least hang out."
    play bg_sfx "sfx/people.mp3" loop
    play music "music/Sojourn.ogg" fadeout 1.0
    show him normal at midleft
    show her normal at center
    with dissolve
    show brennan at quarterright behind her, him
    show pavel at right behind her, him
    with moveinleft
    show ilian at quarterleft behind her, him
    show sara at left behind her, him
    with moveinright

    "I was surprised when a lot of people showed up! I guess there's not much else to do here yet..."
    "Martín and Natalia brought a board game to play, and one of the Nguyen's teenagers brought dice and computer pads to play a role-playing game. I overheard [his_name] talking to Pete about tractor racing, which sounded weird, but I was glad he was having a good time."
    "The little kids seemed to playing some kind of spying game, as they would peek around a corner at us and then run away giggling whenever they were spotted."
    hide pavel with moveoutleft
    hide brennan with moveoutright
    show martin happy at left behind her, him
    show natalia at quarterleft behind her, him
    with moveinright
    show sara at quarterright behind her, him
    show ilian happy at right behind her, him
    with move
    natalia "Great idea, [her_name]!"
    sara "Yeah, it feels good to get out of the house!"
    "Our snacks were not very tasty (mostly vegetables), and the games were not always fun, but joining together informally once a week helped us feel closer together."
    stop bg_sfx fadeout 1.0
    
    $ skill_social += 10
    $ community_level += 2
    return

#
# SOCIAL 2
# Invite Nguyens over for dinner
#
label social_2:
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
    her normal "Yeah, we'll figure it out, don't worry."
    "I worked hard on the food, and spread out some blankets to sit on, even though it meant I'd have more laundry to do to get all the dust out."
    scene bg farm_exterior with fade
    show him normal at quarterright
    show her normal at midright
    with dissolve
    show julia at midleft
    show thuc at quarterleft
    show kid at center
    show van at left
    with moveinleft
    play bg_sfx "sfx/kids.mp3" loop
    julia "Thank you so much for having us over for dinner. I only hope we don't wear out your generosity by the end of the evening."
    her happy "Well, hopefully I made enough food! Let's eat!"
    if (skill_domestic >= 10):
        "I served make-your-own-wraps, where you could put in beans or cheese or vegetables or whatever you wanted. I had some salsa or salad dressing that people could put on, too. They were delicious, and the kids liked them too."
    else:
        "I just put out a bunch of beans, crackers, fruit, and vegetables, and let people choose what they wanted. It tasted a little bland, but the kids seemed to like it."
    "Then the kids all played hide-and-seek around the farm while we talked with the Nguyens."
    hide kid 
    hide van
    with moveoutleft
    stop bg_sfx fadeout 20.0
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
        julia "Well, that's enough love to start with. You know I'm a midwife, right?"
        her normal "Yes, I was sort of planning on you helping me out?"
        julia "Of course. Call me on the radio when it's time, and I'll meet you at the clinic or wherever you are."
        her happy "I'll do that; I could definitely use an expert's help!"
    elif (want_kids):
        her normal "So...Mrs. Nguyen, you seem like an expert on kids."
        julia "Please, call me Julia. I do have a lot of experience with children - besides my own ten, I've been at twenty deliveries or so, helping the mother through labor."
        her surprised "Really? We want to have kids, sometime..."
        julia "Well, I hope you'll let me help you. There's a lot that the doctors don't know about babies and new mothers."
        if (profession == "doctor"):
            her serious "Yes, I know about all the medical conditions and treatments, but not very much about the actual babies themselves."
        else:
            her surprised "That's probably true..."
    else:
        "[his_name] and I talked to the Nguyens about our farms and crops, and what things seemed to help the crops grow better, and what the kids were doing."
        
    him surprised "So, I'm curious, how did you two meet?"
    thuc "Well, we were both-"
    julia "Oh no, don't let him tell it, he'll get everything wrong."
    show him normal
    her happy "Well, why don't you tell it and then we'll ask for Thuc's version afterwards?"
    julia "Hmph. Well, we were both serving in the Peace Corps in Cambodia. I was working as a sanitation educator, and he was working on a sustainable farming project."
    him surprised "You're not Cambodian, are you Thuc?"
    thuc "No, my great-grandparents immigrated from Vietnam. My grandpa thought it was crazy that I knew how to speak Khmer but not Vietnamese."
    julia "Eventually we worked together on a bio-gas system to transform sewage into fertilizer. I didn't think anything of it at the time, but later it turned out he had specifically requested this opportunity so that he could see me more often."
    thuc "That wasn't the only reason!"
    julia "And soon every night he's hanging around my host family's house after dinner, and wants my opinion on every little detail of the project."
    thuc "That was just for work!"
    julia "Well, anyway, we got to be good friends. After we returned from our service, he looked me up and we started dating."
    thuc "No, no, no. She's the one who looked me up! Any time I'd post something online, she'd comment on it. She practically stalked me."
    julia "I was just tring to keep up our friendship! You were the one who wanted to meet in person!"
    thuc "She's the one that proposed to me, just so you know."
    him happy "Did she really?"
    julia "It was a joke!"
    thuc "I think our ten kids prove otherwise, {i}oun somlanh{/i}."
    julia "Well, that's not to say it didn't turn out to be a good idea after all."
    "That's what she said, but she blushed and smiled. I wasn't sure exactly how they had ended up together, but they were clearly just right for each other."

    "We talked and talked, until finally, it got dark. One of the moons was shining brightly; the other was dark."
    show night with dissolve
    julia "Thanks so much for having us over, [her_name]. I'm glad we got to know you a little better."
    thuc "Yes, the food was delicious!"
    her normal "Thanks for coming, we enjoyed your company."
    "[his_name] and I watched them start walking for home."
    hide julia
    hide thuc
    with moveoutleft
    him "I wonder what our family will look like in a few years?"
    if (want_kids or is_pregnant):
        her concerned "It will be different, won't it?"
    elif (loved >= 0):
        her flirt "As long as you and me are in it, it will be just fine."
    else:
        her surprised "Who knows?"

    $ skill_social += 10
    $ community_level += 2
    return

#
# SOCIAL 3
# organize lunch group
#
label social_3:
    play music "music/Sojourn.ogg" fadeout 1.0
    play bg_sfx "sfx/people.mp3" loop
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
        "What should I say?"
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
                    show her normal at center
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
            
    stop bg_sfx
    $ skill_social += 10
    $ community_level += 2
    return

#
# SOCIAL 4
# Organize community movie night!
#
label social_4:
    scene bg community_center with fade
    play music "music/Sojourn.ogg" fadeout 1.0
    play bg_sfx "sfx/people.mp3" loop
    "One week at Friday lunch group, we were all complaining about our lack of excitement."
    show lily at quarterright
    show pete at left
    show sara at midleft
    show her normal at midright
    with dissolve
    lily upset "We all live so close to each other, but in the evenings everyone just wants to go to bed early."
    her concerned "Well, people who aren't working in town are farming all day, which is pretty tiring."
    pete "That's true, but don't you get tired of sitting at home all the time? I get up early to milk the cows, and I'm in the library all day, so the last thing I want to do when I get home is sit around by myself some more."
    her normal "I'm pretty busy, but I agree that it'd be fun to do something together as a community."
    lily normal "I was just reading on how we could use a magnifying glass with our tablets to make a projector. Perhaps we could have a movie night?"
    pete "Yeah, a movie is low-key enough that even if you're all tuckered out from farming you should be able to sit through it."
    sara "And kids like to watch movies too, so we could include everyone."
    her happy "I know the perfect movie!"
    menu:
        "What should we watch?"
        "A sci-fi drama.":
            her laughing "There's a space opera movie about finding the strength to persist through hardships that I think would be highly entertaining!"
            sara "Oh no, is it one of those Star Wars remakes?"
            her normal "Well, yes, but isn't it interesting to think about what space travel will be like in the future?"
            sara "You just like watching it for the cute guys."
            her happy "I think everyone enjoys watching good-looking people do stupid things. Plus I already know we have it in the archives!"
            pete "We've got lots of Star Wars remakes in the archives, but maybe you didn't know that we have some rarer sci-fi movies here too."
            her surprised "Like what?"
            pete "{i}Time For No Man{/i} was originally a tellanovella, but when set in space, it suddenly became a sleeper cult hit in the 2030s!"
            her flirt "'No man', huh? Does it have any guys in it?"
            pete "I think it has a few. It's not just lesbians if that's what you're asking."
            sara "Is it appropriate for children?"
            pete "Sure. There's some innuendo, but that goes right over their heads."
            stop bg_sfx fadeout 1.0
            scene black with fade
            "We decided to watch {i}Time For No Man{/i} the next day in the evening. I sent out a message to the colony message board, and tried to remind everyone I saw to come."
            "The movie was kind of ridiculous. At one point two cousins realized they were actually sisters, and that their evil uncle was actually their father. Then it turned out he wasn't evil at all, but had been infected with an alien virus that caused him brain damage that made him act rudely."
            "A feminist organization let the cousins/sisters travel the galaxy at light speed to administer vaccines to the rest of civilization, but by the time they got anywhere, everyone else had been infected by the virus which made them act rudely."
            scene bg community_center with fade
            show him normal at sitting, midleft
            show her normal at sitting, midright
            show night
            with dissolve
            him annoyed "This movie is ridiculous."
            her annoyed "Yeah, there's no way a virus would only affect men. It's not like our immune systems are all that different."
            him surprised "What would you do if I turned into a jerk overnight?"
            menu:
                "What should I say?"
                "Take you to the doctor.":
                    her normal "I would take you in to have your head examined."
                    him happy "Because the only way I would be mean to you is if I had brain damage, right?"
                    her annoyed "And if you were mean to me you might get brain damage, if you know what I mean."
                    him flirting "Oh, you're so feisty."
                    menu:
                        "What should I say?"
                        "You'd better believe it.":
                            her flirt "I know you like it like that."
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
        "A historical mystery action flick.":
            her happy "Sherlock Holmes would be perfect! It has mystery, suspense, romance, action, and would help educate children about the 1890s."
            sara "Yeah, and it would encourage kids to try smoking alien weeds."
            her annoyed "Oh come on. We grew up watching films with people drinking all the time and it didn't turn us into alcoholics."
            sara "The plot of a Sherlock Holmes mystery is also difficult to understand, so it might not hold their interest."
            pete "Well, I can think of a historical film with plenty of mystery that kids and adults might like."
            her normal "Tell us about it."
            pete "It's a mini-series called {i}The Adventures of Emily Thompson{/i}, about a young girl living in a small town in England during the 1900s. She solves various mysteries like finding missing shoes and pets, and she ends up finding the culprit of a livestock theft."
            her surprised "Well, that does sound a little more child-friendly than murder mysteries."
            sara "Let's do it."
            stop bg_sfx fadeout 1.0
            scene black with fade
            "I sent out a message to the colony e-mail list, and tried to remind everyone I saw to come."
            scene bg community_center with fade
            show her normal at midright
            show him normal at midleft
            show night
            with dissolve
            "We had a pretty good turnout, and the kids and adults both found things to laugh at."
            him surprised "So, the part where the sadistic child was killing sheep with bread-encrusted coins was a little hard for me to believe."
            her flirt "It could have been worse. The sadistic child could have been a werewolf who was eating them."
            him happy "Yeah, but making coins out of copper is a waste of metal!"
            her happy "Seriously, they should be making teapots out of them."
            him normal "Or you know, wires."
        "An animated art film.":
            her normal "Let's put on an old cartoon movie so that the kids will enjoy it too."
            lily normal "{i}Wall-E{/i} is one that might be both relevant and entertaining."
            her surprised "I was thinking more along the lines of {i}The Old Man and the Sea{/i}."
            pete "I think that movie would put everyone to sleep."
            her normal "It's only forty minutes long!"
            pete "I haven't seen {i}Wall-E{/i} in a while, and it could start some conversations about the colony, and what it oughta be like."
            sara "I agree! Some of the people have never seen it, and I think they would like it."
            stop bg_sfx fadeout 1.0
            scene black with fade
            "We decided to watch {i}Wall-E{/i}. I sent out a message to the colony e-mail list, and tried to remind everyone I saw to come."
            scene bg community_center with fade
            show her normal at midright
            show him normal at midleft
            show night
            with dissolve            
            "The kids enjoyed watching the robot's antics, and the trash-filled city reminded me of some of the things we were trying to do differently in our colony."
            her concerned "I'm so glad the green revolution happened before the whole earth turned into a landfill."
            him concerned "Yeah, and then no one could make anything because the regulations on materials were so strict."
            her normal "Aren't you glad we're here where we can decide those things for ourselves?"
            him normal "Yes, I am glad. Are you?"
            menu:
                "What should I say?"
                "{i}I love it here!{/i}" if (loved > 0):
                    her normal "Of course I miss my family, but I love our community and working with you to make a place for ourselves."
                    him laughing "Good, because we're stuck here!"
                "{i}I don't really like it here.{/i}" if (loved < 0): 
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
                        "No, it's not romantic.":
                            her annoyed "It's not romantic. We'll be too dead to appreciate how cute our sacrifice is."
                            him normal "Well, I'm happy as long as we're together."
                        "It could be romantic.":
                            her flirt "If they find our skeletons embracing each other, I guess that could be romantic."
                            him flirting "That's the spirit!"
                            $ loved += 5
                "Most of the time.":
                    her normal "Most of the time I'm happy to be here. There are lots of things I miss, of course. But it's also exciting to start something new."
                    him happy "We're living off the land! We can make our own futures!"
                    her flirt "Yeah, as long as that future involves farming of some kind."
                    him annoyed "Well, you're not farming."
                    her annoyed "True. But it's going to be a big part of our lives for the foreseeable future, is what I meant."
                    him normal "That's the way I like it. There's nothing like farm-fresh food to make you healthy."
        
    "The families went home as we talked. Pete and Sara and Lily and I congratulated each other for a movie well-watched, and I went home feeling like I helped everyone feel a little closer."
    $ skill_social += 10
    $ community_level += 2
    return

#
# SOCIAL 5
# Someone's house burns down; will you help?
#
label social_5:
    scene bg bedroom with fade  
    $ is_nude = True
    show him sleeping at midleft, squatting
    show her sleeping at midright, squatting
    show bedroom_covers    
    show night    
    with dissolve
    
    play music "music/NoOneWillKnow.ogg" fadeout 1.0
    "One good thing about being such a small community was that we all helped out when someone needed it."
    "Like when Sara's house burned down..."
    "It was the middle of the night when the radio crackled on."
    play bg_sfx "sfx/radio.mp3"
    "Sara on the radio" "Is anyone awake? Please, help! Our house is on fire!!!"
    show her surprised
    him nude surprised "Let's go!"
    scene bg farm_exterior flip burned with fade
    $ is_nude = False
    show night
    show ilian at quarterright
    show sara sad at midright
    with dissolve
    show him serious at midleft
    show her serious at quarterleft
    with moveinleft
    play bg_sfx "sfx/fire-2.mp3" fadein 1.0
    "We brought buckets of water, but by the time we got there, the whole house had already burned to the ground."
    sara "Oh, [her_name], I'm so glad you came! It's... awful."
    show her serious at center with move
    show him serious at midleft with move
    menu:
        "What should I say?"
        "At least you and Ilian are okay.":
            her concerned "At least you two got out safely..."
            sara "Yeah, that's good. We didn't have time to bring anything with us, though...It's a good thing we weren't sleeping naked."
            her normal "Yeah, that's true."
        "Did you lose much?":
            her surprised "Did you lose much?"
            sara "Everything...which actually isn't that much, I guess. A few things from Earth, our computers, clothes, some tools."
            her sad "That's terrible..."
        "How did the fire start?":
            her surprised "How did your house catch fire?"
            sara "I don't know! We just woke up and there was this huge fire over by the oven."
            her "Maybe there was something wrong with the stove?"
            sara "What does it matter?! Either way, our house just burned down! Not just the house, but our clothes, tools, computers..."
            her concerned "I'm so sorry..."
    sara "I don't know where we'll stay; what we'll wear; how we'll eat..."
    stop bg_sfx
    menu:
        "What should I say?"
        "Come stay at our house.":
            her serious "You and Ilian are welcome to stay at our house if you want..."
            sara "Really? I know your house is pretty small..."
            her normal "It's no trouble. C'mon, it'll be fun! We can hang out every night like it's a weekend!"
            him happy "Yeah, and don't worry; [her_name] doesn't snore too loudly."
            show her annoyed
            ilian happy "Thanks; we really appreciate it."
            show her normal
            sara normal "Yes, honestly, I'd rather stay with you guys than anywhere else."
            scene bg farm_interior with fade
            "It was a little crowded and stressful having so many people in our one-room house."
            "And sometimes I overheard things I really didn't want to know..."
            show ilian at quarterright
            show sara at midright
            ilian "I don't want to go anywhere tonight; I have a headache."
            sara sad "But I told Helen and Pete we'd both come over! How come you only have a headache when it's time to do something I want to do?!"
            ilian "It's not like I can just turn them on or off! You think I like my head pounding?"
            sara "Yeah, I think you like having a headache more than you like doing something with me."
            ilian "That's ridiculous!"
            sara "You're ridiculous! No wonder you don't have any friends..."
            show her serious at left with moveinleft
            ilian "..."
            sara "..."
            her concerned "Ah... I was just going to make some dinner, but maybe I'll just take a walk outside instead."
            sara "I'll go with you."
            hide her
            hide sara
            with moveoutleft
            scene bg farm_exterior with fade
            show her serious at midleft
            show sara sad at midright
            with moveinright
            sara "Sorry you had to hear that."
            her serious "No, it's okay, everyone has disagreements."
            sara "I just feel so trapped sometimes! I hate staying at home in the evenings and doing nothing!"
            her surprised "I guess that's Ilian's favorite thing to do?"
            sara "Yeah..."
            her normal "Well, why don't I go with you to Helen's after dinner, and we can have a girl's night? We haven't done that for a while..."
            sara normal "Okay...thanks, [her_name]."
            scene black with fade
            "When we came back, the mood had definitely changed."            
            scene bg farm_interior with fade
            show ilian happy at quarterright with dissolve
            show him normal at midleft with dissolve
            show sara at midright with moveinleft
            show her normal at quarterleft with moveinleft
            ilian "Did you have a good time?"
            sara "We did, actually."
            ilian "Good."
            sara sad "..."
            ilian normal "..."
            sara sad "Hey, sorry I got mad at you. I know you don't like stuff like that; I shouldn't try to make you do things you don't like."
            ilian "I could do more, I'm just lazy..."
            show sara normal
            "She came up and hugged him and whispered something in his ear. He laughed and squeezed her close."
            ilian happy "I'm not going to let a headache stop me from--"
            her laughing "Hey! [his_name], come outside, I want to show you something."
            him surprised "Huh? What is it?"
            her happy "Just come outside with me for twenty minutes."
            sara "Thank you, [her_name]!"
            hide him
            hide her
            with moveoutleft
            scene bg farm_exterior flip with fade
            "Luckily, they had materials for an extra house on the shuttle, so the whole community worked together one day to put it together for them."
            "The Nguyens donated one of their computer pads for them to share, and everyone pitched in some cookware and tools to replace those that had burned."
            scene bg farm_interior with fade
            show him normal at midright
            show her normal at midleft
            him "It wasn't as bad as I thought, having Ilian and Sara stay with us for a week..."
            her flirt "Yeah. But now that we have the house to ourselves, we can do whatever we want, whenever we want..."
            him flirting "You're right! Now I can finally let out all the gas I've been saving up..."
            her annoyed "Is that the best thing you can think of?!"
            if (loved <= 0):
                him flirting "You're the best thing I can think of."
                her happy "That's more like it!"
            else:
                him flirting "Isn't my comfort important to you? It's important to me!"
                her flirt "I'll show you some comfort..."
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
            $ skill_social += 10
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

#
# SOCIAL 6
# Teach 'enrichment' class on [profession]
#
label social_6:
    call set_work_bg
    show her normal at quarterright with dissolve
    "As the colony's [profession], I knew a lot more than most about my job. I decided to hold a class to teach anyone who was interested in learning more.  It wasn't smart for me to be the only [profession] around."
    show brennan at quarterleft
    show natalia at center
    show naomi at left      
    show thuc at midleft

    with moveinleft
    if (profession == "doctor"):
        "I taught about basic first aid and health, and when to come into the clinic."
        her normal "...and that's how to recognize a stroke. Can anyone review the symptoms for us?"
        naomi "You mentioned sudden headache, numbness, trouble speaking, trouble walking, and vision problems, sometimes just on one side."
        her serious "Yes, thank you. If you see any of these, please bring the person to the clinic right away, or radio me if it's after hours. There are some treatments that must be applied immediately to be effective."
        "They were little things, really, but they could make a big difference in saving someone's life."
    elif (profession == "carpenter"):
        "I taught everyone how to make a simple basket out of one of the local plants that had long, flexible branches."
        her normal "So, you weave the horizontal branches in and out of the skeleton you've already made..."
        brennan "Like this?"
        her concerned "Yes, your first row is good, but the second row needs to alternate which ones it goes over and under."
        brennan "Ah, I see."
        show her normal
        "Maybe if I taught them how to make some of the easier things, they wouldn't come to me with every little thing they wanted."
    elif (profession == "mechanic"):
        "I taught everyone about basic tractor repair and maintenance. Even though a lot of the farmers were already experienced with this, the hybrid tractors we used had some different parts and needed different servicing."
        her serious "So you see, if there's an electrical problem, you need to check both the alternator, the solar panels, and the transformers to make sure they are hooked up properly. The shop has a multimeter you are welcome to borrow anytime to check connections."
        "I hoped that this would help them to maintain their own tractors so I could focus on other things."
        
    elif (profession == "teacher"):
        "I held an open house for all the parents to come and see their kids' work. I also talked a little bit about my teaching philosophy, and how we handled having kids of all different ages in one classroom."
        natalia "Yes, that's very well, but could you please not give the older kids so much homework? We need them to have time to work on the farm, too."
        thuc sad "That kind of training is vital to the success of our farms."
        her concerned "I try to give all the kids time to complete their assignments at school. So if they are bringing work home, it is because they have not completed what they were supposed to at school."
        her normal "Sometimes they are more interested in each other than the material."
        show thuc normal
        natalia "Well, then maybe they ought to do their work at home some days! They'd probably get more done without their friends to distract them!"
        her concerned "We could try that if you like, though I think their coming to school and mentoring the younger students has greatly benefited them, both in academic and social areas."
        natalia "Hmmm. Well, I'll think about it."
        show her normal
        "I think I helped the parents to understand a little bit better how our school system worked."

    $ skill_social += 10
    return

#
# SOCIAL 7
# Family (appears to be?) slacking off and mooching off everyone else;
# mayor asks [her_name] to see if she can determine what to do
#
label social_7:
    "I didn't see the other colonists much during the day, but I assumed they were working hard like we were."
    "But not everyone thought that..."
    scene bg community_center with fade
    show her normal at midright
    show sara at midleft
    with dissolve
    sara sad "Have you seen the Nguyen's farm lately?"
    her serious "No, I don't really get over there."
    sara "Well, there's nothing on it! They haven't planted anything this season!"
    her surprised "Really? I wonder why?"
    sara "I don't know; I see Mrs. Nguyen at the storehouse all the time, picking up food for their family... but it's not really fair for them to always be taking, and not contributing!"
    her concerned "I see your point... but is it really any of our business?"
    sara "I'm going to tell the Mayor about it."
    "I followed Sara over to the storehouse, where the Mayor was talking to Ilian."
    scene bg storehouse
    show pavel at midright with dissolve
    show her normal at left
    show sara at midleft
    with moveinleft
    pavel "Hello, Sara, what can I do for you?"
    sara sad "Mayor, it's not fair for the Nguyens to always be taking food from the storehouse but not contributing anything. Their job is to be farmers, right?!"
    pavel "Yes, it is - do you have reason to believe they are not doing their job?"
    sara "Their fields are completely empty!"
    pavel sad "I see..."
    pavel normal "[her_name], would you please go and speak to the Nguyens and see if you can determine the problem?"
    her surprised "(Me?! Well, I guess Sara might be too upset about it, and I am on friendly terms with Julia and Thuc...)"
    her serious "Yes, I'll do that."
    scene bg laundry with fade
    show julia at midright with dissolve
    show her normal at midleft with moveinleft
    "I headed over to their farm, and found Mrs. Nguyen hanging up the clothes to dry. She smiled when she saw me coming."
    julia "Hello, [her_name], what brings you over for a visit?"
    menu:
        "What should I do?"
        "Ask if she is okay.":
            her concerned "Is...everything all right with your family?"
            "Mrs. Nguyen stiffened, and she suddenly became very interested in her laundry."
            julia mad "Of course. Everything's fine."
            her serious "I mean, if there's any problems, we're all here to help each other..."
            julia "I will ask if we need anything."
            "I could tell something was bothering her, but she didn't want to talk about it with me."
            julia normal "Thank you for stopping by, [her_name], but I have a lot to do and shouldn't waste time chit-chatting."
            her concerned "I just want to help."
            julia mad "Then please, leave us alone!"
            show her sad
            "All I could do was leave...it was clear something was wrong, but she wouldn't tell me what it was."
            scene black with fade
            "I sent her an apology message later that day, and she wrote me back."
            julia_c "Thanks for stopping by...If you really want to help, perhaps someone could help Thuc with a flooding system for the rice he wants to plant."
            nvl clear
            
        "Ask why they haven't planted anything.":
            her surprised "Why haven't you planted anything this season?"
            julia "You think you know all about our farm, just by looking at it?"
            her serious "No, but it just looks empty, so I wondered-"
            julia mad "You wondered?! If you have time to waste with wondering, then perhaps you should put it to better use than bothering people who are trying to get some work done!"
            her concerned "I'm sure you have a good reason--"
            julia "Yes, but I see no reason to share our troubles with you. Thank you for stopping by, but I don't have any more time to waste today."
            "She pinned clothes furiously, and I thought I'd better leave."
            scene black with fade
            "I sent her an apology message later that day, and she wrote me back."
            julia_c "If you really want to help, perhaps someone could help Thuc with a flooding system for the rice he wants to plant."
            nvl clear

        "Chat for a while.":
            her normal "I just came by to say hi. We don't get to see each other very often, do we?"
            julia "No, we don't! How are things going at your farm?"
            her serious "Pretty well, though we lost a lot of corn a while back to some nasty bugs here. There's so many things you can't control on a farm, aren't there?"
            julia "Yes, that's true."
            "She paused for a minute. It looked like she was trying to decide whether to tell me something."
            her normal "Your laundry looks so clean; how are you getting all the stains out? We don't have very good soap here..."
            julia "Ah, you noticed! The trick is fermented urine."
            her surprised "Really?"
            julia "Yes, it has ammonia in it. They used to use in ancient Rome."
            her surprised "You might want to post that on the community message board; I bet everyone would like to know about it."
            julia "Oh, I usually don't have time to go on there."
            her normal "Well, if you don't mind, then, maybe you could help me write up some instructions and I will post it from both of us."
            julia "Well, if you think it will help people."
            her serious "Yes, we all need to help each other, don't you think?"
            julia "Yes... I suppose you're right."
            her concerned "..."
            julia "You know, we lost a lot of our corn to those bugs, too. All of it, in fact."
            her surprised "Oh, no! Did you have any other crops?"
            julia "We have our vegetable garden, of course, but one day the goats got out and ate most of our plants..."
            her sad "That's awful!"
            julia "We wanted to plant rice, but we are still working on a system to flood and irrigate the fields properly. Well, Thuc {b}was{/b} working on it, but after the corn..."
            her serious "It seems fruitless, doesn't it?"
            julia "Yes! What's the point of digging and planning and planting, if some alien creature is just going to come destroy everything we've done?!"
            her concerned "I know what you mean. I felt the same way, too, after the corn."
            julia "Thuc's not one to complain about his troubles, but I can see he's taken this hard. I suppose I haven't been very encouraging, either."
            her serious "It is hard... but maybe if you had some help, it'd be easier to get started?"
            julia mad "Who would want to help us? Perhaps you've noticed that I'm not the most friendly person around..."
            her normal "I think a lot of people would help! Not only would they want rice to eat, but we all are going to need help at some point."
            if (have_goat):
                her "Your family has been so kind to us, giving us one of your goats, and Thuc is a good friend to [his_name]. Of course we will help you."
            else:
                her "Thuc is a good friend to [his_name], so I'm sure he at least would be willing to help!"
            julia normal "Oh, thank you. I've fretted about this long enough, it's time we did something about it!"
            
    scene black with fade
    "I told the mayor what I had found out, and he agreed to find some people to help Thuc get his flooding system setup before the start of the next planting season."
    "[his_name] and some other farmers helped, and they managed to get most of it done in a few days. I hoped their rice wouldn't face the same fate as the corn... but at least now Julia and Thuc knew they weren't alone."
    
    $ skill_social += 10
    return

#
# SOCIAL 8
# Help the Mayor - how much role should government play?
#
label social_8:
    scene bg path with fade
    "One day I was walking through town when I heard loud music from inside the community center."
    her surprised "I wonder if some kids are playing with the sound system?"
    
    scene bg community_center with fade
    show pavel at right with dissolve
    show her normal at quarterleft with moveinleft
    "But to my surprise, the only one inside was the Mayor. He was facing away from me, dancing, and...singing?"
    show pavel at midright with move    
    pavel "\"It's the end of the world, as we know it\nIt's the end of the world as we know it\nAnd I feel fine!\""
    show pavel at right with move
    "Either I giggled, or he sensed my presence, because he turned around looking sheepish."
    show pavel at center with move
    pavel sad "[her_name]! Sorry about that."
    her happy "Not at all! You should be in a talent show or something, that was great."
    pavel normal "Well, it wouldn't be a talent show if I was in it. My skills lie in other areas, I'm afraid."
    her flirt "Like keeping space colonies running?"
    pavel sad "I used to think so, but..."
    her surprised "What's wrong?"
    pavel "There's just been... a really difficult situation, lately. I'm not sure I know what to do."
    her serious "Do you want to talk about it?"
    pavel "I probably shouldn't, but..."
    her concerned "I'll keep it confidential."
    pavel "Well... have you heard of fire grass?"
    if (skill_knowledge >= 40):
        her normal "Yeah, that's on the edible plants list with a warning not to eat it raw. I guess it's kind of spicy?"
    else:
        her concerned "No..."
        
    pavel "It grows wild all over here, and someone found out that if you smoke it, it is a powerful stimulant."
    her surprised "Like caffeine?"
    pavel normal "Yes, but more powerful. Some of the colonists say they can get a lot more done and have more energy when they use it."
    her serious "Is it dangerous?"
    pavel "We haven't studied it enough yet to know what long term effects it may have. It does seem to make the user more tired afterwards, but that's the only reported side effect."
    her surprised "Has someone been abusing it?"
    pavel sad "One woman wants to make smoking fire grass illegal. Apparently her kids play at the house of someone who smokes it, and she says the secondhand smoke makes them jittery and cranky."
    menu:
        "What should I say?"
        "You should make it illegal.":
            her concerned "That sounds really unhealthy; people shouldn't be using things like that."
            pavel "Hmmm, I had been thinking that it wasn't our job to tell people what they should and shouldn't consume."
            her annoyed "Yes, but it doesn't just affect the people that smoke it - it affects their kids, and apparently other people's kids, too.  That's not fair for them."
            pavel normal "You're right. And I wouldn't be surprised if some of the older kids start smoking it to copy their parents, if we don't do something about it now."
            her serious "But it grows everywhere... enforcing a law like that would be difficult."
            pavel "Well, my job is not to make sure no one ever breaks any laws. My job is just to mediate disputes."
            her surprised "So... if someone breaks a law, but nobody cares, nothing will happen?"
            pavel "Yes, exactly. So if we made smoking illegal, it would hopefully still allow people to smoke it in ways that don't bother anyone."
            her concerned "That kind of makes the law meaningless."
            pavel "The law is not a set of dos and don'ts to control people's lives. The law is a way to resolve conflicts in a way that's fair for everyone."
            her serious "I hadn't thought about it like that before..."
        "You should not make it illegal.":
            her annoyed "That's too bad, but I think our community will function better without too many  laws."
            pavel "Really? I'm worried about the smoke's effects on the children..."
            her serious "Well, there are other ways to help them. Maybe this woman could just talk to the person she has a problem with, or not let her kids play over there."
            pavel "That's true..."
            her annoyed "People don't need laws to tell them how to live; people only need laws to stop those that want to harm others. Too many laws just get in the way."
            her flirt "Besides, do you really want to have to enforce a law like that?"
            pavel normal "Good point. I'll see if there's a solution to this problem aside from making a new law."
            her normal "I'm sure there is."
        "The colony should vote on it.":
            her concerned "Don't we vote on all new laws?"
            pavel "Yes, of course, but I don't want to encourage the woman to propose a new law if there's another solution to this problem."
            her normal "Well, if she has enough support, then maybe we should let everyone vote on it. That puts the burden off you a little bit and onto everyone else."
            pavel normal "That might work... if people don't vote for it, then she will have to find another solution to her problem."
            her serious "And if they do vote for it?"
            pavel "Then hopefully people that want to smoke fire grass will be more discreet about it."
            her concerned "Just because there's a law against something doesn't mean people will stop doing it."
            pavel "But if their smoking is so discreet that it doesn't bother anyone else, then I don't think there's a problem."
            her serious "Maybe so..."
            
    pavel "Anyway, I appreciate your insight into this dilemma, [her_name]. It helps to be able to talk to someone that I trust."
    her normal "Anytime, Mayor."
    
    $ skill_social += 10
    $ community_level += 2
    return

# Propose and fill seat on Community Council
label social_master:
    scene bg community_center with fade
    show pavel at midright, behind her with dissolve
    show her normal at midleft with moveinleft
    her surprised "Mayor Grayson, can I talk to you for a moment?"
    pavel sad "I'd like to, [her_name], but there's too much to do. I have to decide where the new farm should be, and how to allocate the latest harvest, and which supply requests to approve, and-"
    her normal "That's what I want to talk to you about."
    pavel normal "Oh?"
    her serious "There's too much here for just one person. You need some help."
    pavel "Isn't that what I told you about your job when we first arrived here?"
    her normal "Yes, and I listened to you, so I hope you will listen to me."
    her serious "You've done a great job, but the truth is there's just too much for one person."
    her normal "There's a lot of decisions to be made, and some of them would be made easier by someone just specializing in that one thing."
    pavel "What do you propose?"
    menu:
        "What do I propose?"
        "Form a committee.":
            her normal "Why not have a committee? One person could be in charge of the store house, one person could be in charge of the land, one person in charge of the services like the school and library, and one person in charge of laws and safety."
            pavel "Hmmm..."
            her "Of course, you would be welcome on the committees."
            pavel "Will you serve as one of the committee members?"
            her serious "If you like, though I think it would be better if they were elected."
            pavel "Very well. I am sure you will be voted to be in charge of something."
            "Sure enough, they voted me to be in charge of services."

        "I could assist you.":
            her happy "Maybe I could help you out with some of the more mundane things."
            pavel "Hmm, sort of like a deputy mayor?"
            her normal "Yeah, you need a deputy! That would also help in case you got sick or something."
            pavel "Splendid! But... I believe our charter states that any additional officers must be elected by the adults of the colony."
            her happy "That's fine; everyone will support me more if they feel like they have chosen me."
            pavel "We'll see if anyone else wants the job."
            "The mayor announced a vacancy in the post of deputy mayor, and asked for nominations."
            "Sara nominated me, and [his_name] nominated Thuc, but he didn't want to run. Pete nominated Sister Naomi, but she declined the position as well. Nobody else wanted to run, but we held a vote anyway."
            pavel "I guess you've got the job, [her_name]! Now, about those supply requests..."
        
    "It was quite a lot of work to help be in charge of the colony, but the Mayor seemed much less stressed out. It felt good to be trusted, and to help everyone work together here on Talaam."

    $ skill_social += 10
    $ community_level += 10
    return
