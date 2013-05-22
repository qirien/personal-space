# Event content for all the events that can happen in the evening,
# where we relax together

# Relationship Focus Events

label relax_together_0:
    scene bg stars with fade
    play music "music/Will.ogg" fadeout 2.0
    "We went for a walk together under the stars. I brought my computer pad so we could find which one was our old Sun. I didn't see any constellations I recognized, so it was hard to find any reference points, but we finally found which one we thought it was."
    her "It looks so small..."
    him "Remember how small Talam's sun looked from Earth?"
    her "That seems so long ago..."
    $ relaxed += 5
    return

label relax_together_1:
    scene bg farm_interior with fade
    play music "music/Will.ogg" fadeout 2.0
        
    "One of the things I missed most about Earth was having my own shower and bath. While we washed up well enough with water from the well, we still enjoyed going to the community bath once a week or so to really get clean."
    her "I really need a bath."
    him "Really? You smell great to me."
    her "Ick, you need a bath, too! Let's go tonight."
    him "Sure, after dinner and...dessert."
    her "You made dessert?! What kind?"
    him "I was thinking we'd make some dessert...together."
    her "Ohhh, {b}that{/b} kind of dessert."
    him "Yes...though we could have dessert first, you know. Sometimes it's fun to break the rules."
    menu:
        "\"Dessert\" first?"
        "Dinner first.":
            her "How about dinner first? You can think of it as an appetizer..."
            him "Hmmm, you're very appetizing."
            "We played footsie under the table while we ate and gave each other suggestive looks. Dinner didn't last very long..."
            $ loved += 5
            $ made_love += 1
        "Dessert first.":
            her "Life is short; eat dessert first!"
            "And what a dessert it was..."
            $ loved += 5
            $ made_love += 1
        "No dessert tonight.":
            her "I think I'd rather skip dessert tonight..."
            him "Oh...okay. Sure, let's just eat dinner."
            $ loved -= 5
    "Afterwards, we packed up our towels and toiletries and headed down to the bathhouse."
    "We built a fire to heat up one of the tubs of water, and took turns washing off and then soaking in the small tub."
    "It felt so good to soak and relax together."
    if (relaxed < 0):
        $ relaxed = 0
    else:
        $ relaxed += 5
    return

label relax_together_2:
    "We went on a moonlight walk to the river. We found a spot where the water was deeper and slower, and sat down. I put my head on his shoulder, breathing in the cool night air."
    him "Want to go for a swim?"
    her "Are you nuts?!"
    him "Yes!"
    "He took off his clothes - all of them - and cannonballed in, splashing me."
    menu:
        her "Hey!"
        "Join him":
            "I took of my clothes slowly. There was enough moonlight that I knew he could see me."
            him "Whoo! Alright, [her_name]! Come on in!"
            "I decided to get back at him by jumping in right next to him with a big splash, but he didn't seem to mind."
            "The water was cold, but somehow that just made everything more exciting."
            $ loved += 5
        "Watch him":
            her "I don't really want to get wet; I'll just watch you."
            him "Oh yeah? I better give you a good show, then."
            "He flexed his muscles and then tried to do a handstand on the bottom of the river."
            her "Ha ha, not bad!"
            "Soon he got tired of swimming and we headed home together."
            $ loved += 5
        "Leave":
            her "Ugh, now I'm all wet and cold!"
            him "I'll warm you up, [her_nickname]!"
            her "No thanks, I'm going home."
            $ loved -= 5
    return

label relax_together_3:
    scene bg library with fade
    "The library had a huge collection of Earth media that colonists could check out. They only had enough space for the most popular things, but it was still more media than anyone could experience in a lifetime."
    "One day I noticed they had a movie about space colonists. I was curious to see how people on Earth saw people like us, so I checked it out."
    scene bg farm_interior with fade
    her "What do you want to do tonight? I checked out a movie that looks fun..."
    him "Oh, sorry, I told Thuc I'd help him build a fence tonight. He helped me build ours to keep the animals out of the crops, so I said I'd help with his."
    menu:
        "I was disappointed, but..."

        "Can't you do it another night?":
            her "Can't you help him another night? I was really looking forward to watching this with you."
            him "No, sorry, it has to be tonight."
            her "Okay, see you later."
            him "Bye, [her_nickname]."
            "The house suddenly seemed so quiet. I usually didn't mind being alone, but I had really been looking forward to this. The wind whistled mournfully through the cracks in the walls."
            menu:
                "What should I do?"
                "Watch it without him":
                    her "Forget it, I'm watching it without him!"
                    "It was full of drama, comedy, and funny inaccuracies about space colonies, but I didn't really enjoy it..."
                    $ relaxed -= 5
                "Do something else":
                    "I tried to distract myself with a book, but I wasn't really having fun."
                    $ relaxed -= 5
                "...":
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something fun with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    $ relaxed -= 10
            "Finally, I just went to bed."
            scene black with fade
            "Everything seemed fine the next day, but I still felt insecure."

        "I'll help, too.":
            her "I'll help too!"
            him "Do you really want to?"
            her "Yes, we all need to work together to succeed. Plus, I'll get to be with you."
            him "All right, let's go!"
            "Thuc had already cut some logs and branches for us to tie up, but we still had to dig holes for posts."
            if (skill_physical >= 20):
                "It was a good thing I came, because there was a lot of hard work to do."
            elif (skill_technical >= 20):
                "It was a good thing I came, because I pointed out a better way we could make the fence that would be really sturdy."
            else:
                "I'm not sure I was much help, but I worked hard and did my best."
            "We worked hard in the gathering darkness, until the moons rose and gave us their wan light. We worked on and on, until finally it was done."
            thuc "Thank you so much, both of you."
            him "Glad we could help. I hope this fence holds up for you."
            thuc "Well, you can count on my help anytime, if you need it."
            her "Thanks, I'm sure we will."
            "We walked home by moonlight.  The two moons cast opposing shadows from the shrubs and trees, making a maze of light for us to follow. [his_name] reached for my hand."
            him "Thanks for coming. Everything's better with you."
            her "Even putting up fences is not too bad when we're together."
            $ loved += 5
            $ skill_physical += 5
            $ community_level += 5
            scene black with fade
  
        "Want to watch it another night?":
            her "No problem, we'll just watch it another night."
            him "Thanks for understanding. I'll see you later, [her_nickname]."
            "It was a little lonely, especially since I was really looking forward to watching the movie with him, but I soon was absorbed in a good book and then went to bed."
            scene black with fade
            "We watched the movie the next night. Even though they got a lot of things wrong about space colonization, we really got into the drama and tension. We both cried a little at the end."
            $ relaxed += 5
            $ loved += 5
  
        "You're never here when I need you!":
            her "You're never here when I need you!"
            him "What are you talking about? I'm home almost every night."
            her "But you're always on your computer; I wanted to do something together tonight."
            him "Well, I can't. I promised Thuc I'd come tonight."
            her "I'm not really important to you, am I?"
            him "What?! Of course you are!"
            her "Then stay home with me!"
            him "No, I'm not going to break my promise. Now I have to go, we want to get this done before the moons set."
            menu:
                "He's leaving..."
                "Fine, just leave me here.":
                    her "Fine, just leave me here."
                    "He didn't say anything, just shook his head. I watched him leave, feeling hurt and lonely."
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something fun with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    scene black with fade
                    "I forgave him the next day, but I still felt insecure."
                    $ relaxed -= 5
                    "Finally, I just went to bed."
                "...":
                    "I didn't say anything; just watched him leave, feeling hurt and lonely."
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something fun with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    $ relaxed -= 5
                    "Finally, I just went to bed."
                    scene black with fade
                    "I forgave him the next day, but I still felt insecure."
                "Sorry":
                    her "Sorry, [his_name]. I'm being selfish."
                    him "It's all right, [her_nickname]. Let's do something together tomorrow night, okay?"
                    her "Okay, [his_name]."
                    "We watched the movie the next night. Even though they got a lot of things wrong about space colonization, we really got into the drama and tension. We both cried a little at the end."
                    $ relaxed += 5
                    $ loved += 5
    return

# Did he only marry [her_name] so he could be a colonist?
label relax_together_4:
    scene bg farm_interior with fade
    play music "music/Prelude02.ogg" fadeout 2.0
    "One day [his_name] came in from the fields with a big smile on his face."
    him "Ah, [her_nickname], you're such a great part of my life. You've brought me love, joy, and laughter. You've even brought me to new worlds, literally! There's no way I could have come here without you."
    her "What do you mean?"
    him "Well, I mean, it's a colony, right? They want couples, people that are going to have kids, so they can build up the colony."
    her "You mean, you wouldn't have been able to come unless we were married."
    him "Probably not. Farmers aren't that hard to find."
    her "You never told me that... So part of the reason you married me was so that you could come to Talam."
    him "No! I mean, that was part of the timing, I guess, but I would have asked you to marry me anyway! That just sort of, made it happen sooner, I guess."
    menu:
        her "That..."
        "Makes sense.":
            her "That makes sense, I guess. What would it have taken to get you to propose to me, barring extra-terrestrial colonies?"
            him "A tax break, maybe?"
            her "You're terrible!"
            him "I'm kidding, I'm kidding! I guess I was waiting for everything to be just right."
            her "Well, I'm glad you did propose, finally. I was wondering if I was going to have to do it."
            him "Sorry it took so long - change is hard, you know?"
            her "Speaking of which, you should change."
            him "What? What don't you like?"
            her "Change out of those clothes! You smell like Lettie."
            him "What's wrong with Lettie?!"
            her "Nothing, but I don't invite Lettie to share my bed."
            him "I see your point."
            $ loved += 5
            $ made_love += 1
            $ relaxed += 2

        "Bothers me.":
            her "That bothers me. Why didn't you tell me that was one of the factors?"
            him "Because it's not romantic? It doesn't really sound good to say, 'Hey, I want to be a colonist, and I have to be married, and you're the person I like the most, so want to get married?'."
            her "Wow, it sounds even worse when you put it like that."
            him "Exactly! I wanted to get married either way; the whole colony thing just made me quit stalling and ask you."
            her "I still wish you had told me about that earlier."
            him "I'm sorry, [her_nickname]. But I do love you, no matter what."
            her "I love you, too, [his_nickname]. But I still wish you had told me."

            $ loved += 2

        "Is deceitful.":
            her "That's deceitful. I feel used."
            him "Why? It's not like I only married you so I could come be a colonist."
            her "Really? It kind of feels like that."
            if (not want_kids):
                her "Also, we're not ready for kids, and who knows when we will be? You didn't promise them we'd have kids, did you?"
                him "No! I mean, it's sort of expected, but-"
                her "And you didn't think that was something I should know?!"
                him "I thought it was obvious! And, anyway, who cares what they think?!"
                her "I do! Now I feel like, if we don't have kids soon, we're not keeping up our side of the agreement. Even though it was an agreement I knew nothing about!"
                him "Sorry, I guess I just assumed we'd have kids eventually and it wouldn't really be a big deal."
                her "..."
            him "I don't know what you want me to say. I just told you that I love you and everything you've brought into my life, and somehow you've turned it into a big argument."
            her "I've turned it into an argument?! You're the one that didn't tell me this earlier!"
            him "I'm sorry, okay?! What more can I say?!"
            her "Nothing. Just- don't say anything more right now."
            $ loved -= 5
            $ relaxed -= 2
        
    return

# Massage time!
label relax_together_5:
    scene bg bedroom with fade
    play music "music/Will.ogg" fadeout 2.0
    "One day after dinner I noticed [his_name] rubbing his shoulders and grimacing."
    show him normal at center
    show her normal at right
    her "Are you okay?"
    him "Yeah, I'm just really sore from all the digging I've been doing lately."
    if ((relaxed < 0) or (loved < 0)):
        her "Yeah, I feel pretty tense, too."
        "I could have rubbed his shoulders, I guess, but I was just too tired."

    else:
        her "Want me to rub your shoulders?"
        him "I would love that!"
        "I started off gently. His muscles were so tight, I was amazed he could move at all. I gradually kneaded harder, trying to tell what sorts of massage he liked."
        him "Ohhh, that feels so good."
        "Sometimes he would make sort of painful grunt that let me know he didn't like what I was doing. But he would also sigh with content when I hit a particularly tense spot."
        if (relaxed >= 5 and skill_physical >= 10):
            "After his shoulders, I massaged his arms and hands. It made me think of how hard he had been working all day."
            
            if (skill_physical >= 30):
                "My hands were starting to get a little tired, but I didn't want to stop yet, so I rubbed his legs and feet, too."

        "To finish off I massaged his neck and head. I could tell he really enjoyed it."

        if (loved >= 5):
            him "Now it's your turn to get massaged."
            her "Mmmm, really? Are you talking about shoulders, or...?"
            him "I'll massage anything you like."
            her "Why don't you start with the shoulders, and then we'll see what happens?"
            "He copied what I had done earlier, and gave me quite the massage, too. It was so relaxing to just sit and do nothing while he took care of all my tense muscles. He takes such good care of me..."
            $ made_love += 1
            $ relaxed += 5

        $ loved += 5

    return

# go "out" to eat on a picnic
label relax_together_6:
    scene bg farm_interior with fade
    him "Put on your fancy clothes, [her_nickname], because we are going OUT tonight!"
    her "Out where? And I don't have any fancy clothes..."
    him "Any clothes look fancy on you! But I can't tell you where we're going; it's a suprise."
    her "Okay, let me get ready, then. I can at least brush my hair."
    "(Where can we be going?)"
    him "Now put this blindfold on."
    her "You're not serious, are you?!"
    him "I'm totally serious!"
    scene black with fade
    "I let him blindfold me and we left the house.  He spun me around so I couldn't tell which direction we were going, and then we hiked for about twenty minutes or so. He held my hand so I didn't trip."
    her "It's a good thing I didn't actually put on fancy clothes, since this isn't exactly level terrain."
    him "We're almost there."
    "Finally, he took off the blindfold."
    scene bg sunset with fade
    "He had setup a small table and two chairs with dishes and utensils. I sat down at the table and he lit the candles.  Then he got some food out of his backpack."
    menu:
        "It's..."
        "So cool!":
            her "It's...so romantic! Wow, I didn't know you were planning this!"
            him "I'm glad you like it! I just really missed taking you out to eat, so I thought this would be as close as we could get."
        "A lot of trouble.":
            her "Wow, you went to a lot of trouble to set this all up. I feel bad..."
            him "Don't feel bad; just enjoy it!"
        "A waste.":
            her "This is really pretty, but isn't it kind of a waste?"
            him "My time is never wasted when it's spent on you."
    "We ate our candlelight dinner and watched the sun setting over the hills. I couldn't even see our house or the town or anything."
    her "It's like we're the only two people in the whole universe."
    him "Then we have quite a job ahead of us, don't we?"
    her "A job?"
    him "Repopulating the entire universe. We better get started now, don't you think?"
    menu:
        "He's so..."
        "Funny":
            her "Oh, you...! You always make me laugh."
            him "I like it when you laugh."
            her "It's too bad there's so many rocks here..."
        "Sexy":
            her "Should we get started like this...?"
            him "Maybe a little bit of this?"
            her "It's too bad there's so many rocks here..."
        "Exasperating":
            her "Is everything about sex to you?!"
            him "Ha ha, I'm just kidding. And, anyway, it's hard to think of anything else when I'm with you."
            her "..."
            $ loved -= 2

    him "Come sit down over here, it's softer."
    her "Is this our mattress?! You were planning this all along!"
    him "It never hurts to be prepared..."
    menu:
        "That's..."
        "Romantic":
            her "You're so romantic. You thought of everything."
            him "I love you, [her_name]."
            $ made_love += 1
        "Logical":
            her "Yeah, that makes sense. You really planned this out, didn't you?"
            him "I love you, [her_name]."
            $ made_love += 1
        "Presumptuous":
            her "That's pretty presumptuous. You think that just because you setup a fancy dinner that you're automatically going to get some?"
            him "No! I mean, I was thinking it would be a nice end to the evening, but we don't have to. I just thought it might be romantic."
            her "Well, it's not. You can't just assume things like that."
            him "Sorry for assuming my own wife would want to make love to me."
            "I tried to storm off, but I didn't know which way was home."
            her "Which way back home?"
            him "That way."
            "I stomped off towards home, leaving him to carry everything back to the house himself. It wasn't that I didn't appreciate what he did; I just didn't like feeling manipulated."
            $ loved -= 5
            return

    $ relaxed += 5
    $ loved += 5
    scene black with fade
    "We lay there for a long time...In the morning, it felt so good to wake up next to him, watching the sky lighten. With one final kiss, we got up and carried everything back to the house together."
    return

label relax_together_7:
    scene bg fields with fade
    "I was weeding in the backyard when I found some wildflowers. They reminded me of clover, so I made a daisy-chain circlet out of them. It was fun."
    menu:
        "Make one for [his_name] too.":
            him "It looks like you had some fun this afternoon."
            her "I made one for you too!"
            him "What am I, king of the faeries?"
            her "And I'm the queen! All the insects will obey our orders!"
            him "Maybe if those orders include eating everything in sight!"
            $loved += 5
            
        "Make matching flower bracelets.":
            him "Glad to see those weeds are getting some practical use!"
            her "Well, jewelry isn't exactly practical, but it is fun."
            him "Shall I address you as Queen Mab from now on?"
            her "Yes. I'll fulfill all your wishes... in your dreams."
            him "Ooo, harsh. But being with you is like a dream come true, so does that mean you'll fulfill my wishes here?"
            "You get in a tickle fight, and one of your flower bracelets falls off. It was fun while it lasted."
            $loved += 5
            $ made_love += 1
                
    $ skill_creative += 5
    return

# He wants to go to church services, you can go with him or not.
label relax_together_8:
    scene bg farm_interior with fade
    him "Hey, [her_nickname], I was going to go to church services today... do you want to come?"
    menu:
        "Do I want to go to church with him?"
        "Sure":
            if (skill_spiritual >= 30):
                her "Yeah, I usually go anyway, but it will be nice to go with you."
            else:
                her "Yeah, I'll go with you."
            jump goto_church
        "Why?":
            her "Why are you going?"
            him "I thought I'd check it out. It's been a long time since I've been to church; maybe it'd be good for me."
            menu:
                "What do I think?"
                "I'll go with you.":
                    her "I'll go with you."
                    jump goto_church
                "What do you think about spirituality, anyway?":
                    her "What's your position on spirituality?"
                    him "Well, you know I used to go with my family a lot back on Earth... I went more to be with them, though, than because I really wanted to. I'm not sure what's true and what's human tradition, but if there is someone out there watching out for us, we sure could use some blessings."
                    menu:
                        "How do I feel?"
                        "I agree with you":
                            her "I feel kind of the same way... I know a lot of people that religion has helped, but sometimes God feels so far away."
                            him "Let's go together, then, and we can talk about it afterwards."
                            her "Sure."
                            jump goto_church
                        "I have no doubt God exists":
                            her "I know someone's watching out for us."
                            him "Maybe so. We can talk about it more after church, if you want to come with me."
                            her "Sure."
                            jump goto_church
                        "I don't think about it much":
                            her "I don't know. It's not something I think about a lot. I'd rather stay here, I guess."
                            him "Okay, well, I'll let you know how it goes."
                            her "Bye."
                        "I don't think there's a God, but if it helps you, go ahead":
                            her "God is just an idea people made up to explain things they don't understand. But you don't have to agree with me."
                            him "Alright, well, I'll see you later, then."
                            her "Bye."
                            return
                "I'm not going.":
                    her "I'm not going."
                    him "Alright, well, I'll see you later, then."
                    her "Bye."
                    return.
        "No, thanks":
            her "No, I'm staying here."
            him "Okay. Are you not interested today, or would you pretty much never want to come?"
            menu:
                "I don't feel like it today.":
                    her "I just don't feel like it today. Thanks for inviting me; I'm going to enjoy some peace and quiet here."
                    him "Okay, maybe next time. I'll see you later, my sweet [her_nickname]."
                "Church isn't my thing.":
                    her "I probably would never go."
                    him "Okay, no problem. I'll see you in a bit."
                    return
    "When he came home, he seemed thoughtful and quiet."
    her "How was it?"
    him "It was interesting- Sister Naomi is not like any other preacher I've listened to."
    her "How's that?"
    him "Well, she tries to speak to everyone, even though people here have a lot of different beliefs. So she uses a lot of stories and asks a lot of questions."
    him "Like today, she told us the story of some seeds that fell out of a merchant's pack where there weren't any other plants like them. In most places the soil was dry and rocky."
    him "But in one spot a gardener had cleared some soft earth, and the seeds that landed there sprouted and grew. The gardener at first thought they were weeds, but he decided to wait."
    him "Eventually, after years and years, some of them grew to beautiful trees that gave delicious fruit."
    her "What does that mean to you?"
    him "A couple of things. In one way, our colony is kind of like the seeds that fell onto strange soil. Looking at the story another way, however, sometimes the strange things and opportunities that come into our lives are like the seeds. While at first they seem strange, they can sometimes become something great."
    her "Was it helpful?"
    him "It made me think about things, which is good... I feel a little more peaceful, optimistic... but also motivated to keep working hard. So, yeah, I guess it was helpful."
    her "That's good."
    return

label goto_church:
    "We didn't dress up or anything - nobody here owned nice clothes. We held hands as we walked to town and entered the community center."
    scene bg wedding with fade
    "Probably about half the people of the colony were there. Some people were coming in from smaller rooms on the side; some denominations held their own meetings before Sister Naomi's sermon."
    "We sang a hymn of thankfulness for blessings, and Mrs. Peron gave a prayer."
    naomi "Today I want to share a story with you."
    naomi "Once there was a merchant travelling to a far-off land. He carried fruits and other foods. While he was travelling, one of the fruits fell out of his pack and rolled down the hill to a gardener's house."
    naomi "No fruit trees grew in this area; everyone thought it was too dry and rocky."
    naomi "But this fruit landed in some soft earth that had been cleared by a man who lived nearby. Wild animals came and ate away the fruit, but the seeds nestled into the soft dirt."
    naomi "When they sprouted, the man who lived nearby didn't know what they were. He thought about pulling them up so they wouldn't bother his garden. But he decided to wait and see what they were."
    naomi "He waited for years and years, until a great tree grew there, and every summer it gave bushels and bushels of delicious fruit to the man, who shared it with his friends and neighbors with a heart of thanksgiving, and humility."
    "Sister Naomi was quiet for a minute, letting us think about what she said. I wondered if we were supposed to be the merchant, or the gardener, or maybe the seeds?"
    "She told a few more stories, but I kept thinking about those seeds."
    "She ended with a few moments of silence for us to ponder or pray."
    "Then there was a potluck lunch, where everyone brought some food to share, and we talked and mingled with the other colonists."

    "Then we walked home."

    her "What did you think about it, [his_name]?"
    him "Oh, it was alright. Sister Naomi seems really nice."
    her "Yeah... I keep thinking about that story about the seeds."
    him "Yeah, me too... Like, what kind of seeds are we planting for those who will come after us?"
    her "It made me think about how I came here, even though I had no idea what it would be like. I'm still waiting to see what sort of tree this colony will grow into..."
    "We walked in thoughtful silence together all the way home."

    return

# People probably won't even see these last ones unless they always choose "Do something with [his_name]", so don't put a ton of effort into them.

# walk around the farm together looking at what you've created together.
label relax_together_9:
    "We walked around the farm together. [his_name] showed me where all the different crops were, and told me about what kind of soil they liked and what the weeds were like."
    her "This is like your baby, isn't it?"
    him "Yeah, it is."
    him "Who's the cutest widdle farm on the planet, huh? You are!"
    "I could tell it meant a lot to him to show me everything he had been working on."

    return

label relax_together_10:
    "We started talking, and somehow I ended up telling him all about my job. Who was hard to work with, things that seemed impossible, the people I helped... it felt good to have him know what I had been working on."
    return

label relax_together_11:
    scene bg farm_interior with fade
    "We watched a movie together. It was pretty good, but the ending was terrible."
    him "See, what they needed was to have the girlfriend show back up at the end--"
    her "--leading a horde of zombie warriors! Oh, that would have been so much better!"
    him "And what about the pterodactyl? They didn't do anything with that."
    her "I know, I kept thinking someone was going to ride it."
    him "I thought it was going to turn out to be a cyborg pterodactyl."
    her "That would have been awesome!"
    "Sometimes talking about the movie is more fun than the actual movie itself..."
    $ relaxed += 5
    $ loved += 5
    return

label relax_together_12:
    him "I'm so glad we do things together all the time."
    her "Me, too. You're not just my [his_nickname]; you're also my best friend."
    return

# Random events that can happen multiple times

label relax_together_a:
    scene bg bedroom with fade
    "We cuddled together while we watched an episode of an old TV show."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_b:
    scene bg bedroom with fade
    "We snuggled together in bed and talked softly together."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_c:
    "We played card games and flirted shamelessly. Sometimes I even let him win."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_d:
    scene bg farm_interior with fade
    "We were both reading on our computer pads, sitting near each other. We didn't talk much, but everyone once in a while we would look up and smile at each other."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_e:
    scene bg farm_interior with fade
    "We played video games together on our computer pads. We liked to play on the same team."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_f:
    scene bg farm_interior with fade
    "We made a nice dinner together, and talked while we ate slowly, watching the sun go down."
    $ relaxed += 5
    $ loved += 2
    return
