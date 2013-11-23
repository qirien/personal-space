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
    "We held hands and walked together, and though I felt so small in the universe, I knew [his_name] and I had a place with each other."
    $ relaxed += 5
    $ loved += 1
    return

# Onsen
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
            $ loved += 3
            $ made_love += 1
        "Dessert first.":
            her "Life is short; eat dessert first!"
            "And what a dessert it was..."
            $ loved += 3
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

# Skinny dipping!
label relax_together_2:
    scene bg pond with fade
    "We went on a moonlight walk to the river. We found a spot where the water was deeper and slower, and sat down. I put my head on his shoulder, breathing in the cool night air."
    show her normal at midleft
    show him normal at center
    him "Want to go for a swim?"
    her "Are you nuts?!"
    him "Yes!"
    show him normal at quarterright
    "He took off his clothes - all of them - and cannonballed in, splashing me."
    menu:
        her "Hey!"
        "Join him":
            "I undressed slowly. There was enough moonlight that I knew he could see me."
            him "Whoo! Alright, [her_name]! Come on in!"
            show her normal at center
            "I decided to get back at him by jumping in right next to him with a big splash, but he didn't seem to mind."
            "The water was cold, but somehow that just made everything more exciting."
            "When we were done, we got dressed and raced each other home, laughing all the way."
            $ loved += 5
            $ made_love += 1
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

    scene black with fade
    return

# Did he only marry [her_name] so he could be a colonist?
label relax_together_3:
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
label relax_together_4:
    scene bg bedroom with fade
    play music "music/Will.ogg" fadeout 2.0
    "One day after dinner I noticed [his_name] rubbing his shoulders and grimacing."
    show him normal at center
    show her normal at right
    her "Are you okay?"
    him "Yeah, I'm just really sore from all the digging I've been doing lately."
    if (relaxed < 0):
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
label relax_together_5:
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

    "The food wasn't anything special, but somehow it tasted better combined with a beautiful sunset. Afterwards he gathered up the dishes and walked a little ways away."
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

# Baby names
label relax_together_6:
    scene bg farm_interior with fade
    if (is_pregnant or want_kids):
        "We were talking about what it would be like when we did have a baby, and soon we started talking about baby names."
    else:
        "Somehow, we started talking about baby names."

    him "You don't like the name Ringo?"
    her "No! It sounds like a circus master, or a cowboy, or..."
    him "Or a totally awesome musician?"
    her "No! It just sounds dumb!"
    him "Well, not as dumb as Alistair. 'Hello, my name is Alistair, I'm a tap-dancing pansy who can't even button his own waistcoat."
    her "It's refined and elegant! And there's nothing wrong with tap dancing, is there?"
    him "No, but do you really think a kid of ours is going to be a tap dancer?"
    her "Probably not.\nAnyway, we'll just keep looking, I bet we can find a name we both like."

    $ relaxed += 5
    $ loved += 2

    return

# generic; maybe add a specific movie?
label relax_together_7:
    scene bg bedroom with fade
    "We cuddled together while we watched a movie."
    $ relaxed += 5
    $ loved += 2
    return

# walk around the farm together looking at what you've created together.
label relax_together_8 :
    scene bg fields with fade
    "We walked around the farm together. [his_name] showed me where all the different crops were, and told me about what kind of soil they liked and what the weeds were like."
    her "This is like your baby, isn't it?"
    him "Yeah, it is."
    him "Who's the cutest widdle farm on the planet, huh? You are!"
    "I could tell it meant a lot to him to show me everything he had been working on."

    return


# He wants to go to church services, you can go with him or not.
label relax_together_9:
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
                        "I don't think there's a God":
                            her "God is just an idea people made up to explain things they don't understand. But if it helps you, go ahead and go by yourself."
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
    him "Like today, she told us the story of some seeds that fell out of a merchant's pack where there weren't any other plants like them."
    him "A gardener let them grow and they grew into beautiful trees with delicious fruit."
    her "What does that mean to you?"
    him "Hmm, well it made me think of how our colony is kind of like the seeds that fell onto strange soil. I hope we will grow into something great."
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
label relax_together_10:
    scene bg farm_interior with fade
    "We did the dishes together, and then sat together and talked while we worked on little projects."
    him "I'm so glad we do things together all the time."
    her "Me, too. You're not just my [his_nickname]; you're also my best friend."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_11:
    scene bg bedroom with fade
    "We started talking, and somehow I ended up telling him all about my job. Who was hard to work with, things that seemed impossible, the people I helped... it felt good to have him know what I had been working on."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_12:
    scene bg bedroom with fade
    "We snuggled together in bed and talked softly together."
    $ relaxed += 5
    $ loved += 2
    return


# Events that can happen in any order. 
# TODO: Add more of these.

# Play games with Ilian and Sara
label relax_together_a:
    scene bg farm_exterior with fade
    him "Hey, [her_name], want to go into town with me?"
    her "You're going to town? That's a rare occasion..."
    him "I'm taking a load of extra food to the storehouse."
    her "Sure, I'll go with you."

    scene bg path with fade
    "We walked beside Lettie, who was pulling the wagon. We talked and laughed, and when we dropped off the food we saw Ilian and Sara."

    scene bg storehouse with fade
    her "Hey, Sara!"
    sara "Wow, you got [his_name] to come to town? Did you pretend to be sick or something?"
    her "No, he came on his own, believe it or not."
    him "Hey, I'm working hard on the farm, I don't have time to come to town all the time."
    ilian "Well, since you're here, why don't you come over and see our house?"
    sara "Yeah, because it's SOO different from all the other prefab houses..."
    ilian "I was trying to be nice..."
    sara "Our house is totally boring, but maybe we can play a game or something?"
    her "Thanks, that'd be fun! Right, [his_name]?"
    him "..."
    if (loved >= 0):
        him "Sure, let's go."
        scene bg farm_interior
        "The four of us played Robot Turtles and Machine of Death."
        ilian "...which is why you never saw it coming when the piano crashed down ten stories onto your head."
        him "Ohhh! You got me! That was awesome."
        sara "That was way better than [her_name]'s poison-in-the-toothpaste attempt."
        her "Those were just the cards I had!"
        $ relaxed += 5
        $ loved += 2
        $ community_level += 2
    else:
        him "Sorry, I've got to do some things at home."
        menu:
            "What should I do?"
            "Go with [his_name]":
                her "Yeah, I should probably get going, too. Maybe another time, Sara?"
                sara "Yeah, I'll see you at lunch or something."
                "We both worked hard on our projects at home, but at least we were together."
                $ relaxed -= 2
                $ loved += 2
            "Hang out with Ilian and Sara":
                her "Well, I'll come over, if you don't mind."
                sara "Sure, we can play with three people."
                her "Bye, [his_name]."
                him "Bye..."
                "We played some games together, but I felt a little out of place without [his_name]."
                $ loved -= 2
                $ relaxed += 2
    return
    

label relax_together_b:
    scene bg farm_interior with fade
    "We watched a sports game together. It was hard to get too excited about it, since it happened on Earth four years ago, and I didn't feel as loyal to any of the teams now that I wasn't even on the same planet as them."
    "But it was still fun to see their skill and see how they played so hard."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_c:
    scene bg farm_interior with fade
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

# Midnight lovin'
label relax_together_g:
    scene bg bedroom with fade
    show her normal at quarterright
    with dissolve

    "I decided to surprise [his_name] with a few candles lit near our bed and some soft music playing, and I wore the sexiest thing I owned. But it didn't go how I had planned..."
    show him normal at midleft with moveinleft
    him flirt "Oh! Wow, you look really hot..."
    him sad "...but I'm kind of in a hurry, I gotta go fix something before the wind totally breaks it apart."
    her concerned "You don't have fifteen minutes for me?"
    him normal "Well, yeah, if you can wait until I get this done. You don't mind, do you?"
    her angry "Yes I mind! I've been sitting here waiting for you for hour! Aren't you going to do anything about it?"
    him angry "Look, I just can't right now! I'll be back in after I fix this!"
    hide him
    "He left."
    show her concerned at center
    "I waited."
    show her annoyed at center
    "And waited."
    show her angry at center
    "And waited."
    scene black with fade
    "Finally, I just went to sleep."
    scene bg bedroom with fade
    show her normal at midleft
    show him normal at center
    with dissolve
    show overlay night
    "I half awoke in the middle of the night to [his_name] snuggling up to me and nuzzling my ear."
    her concerned "Wha-huh?"
    him annoyed "I'm home..."
    her "Welcome home...and good night."
    him flirt "You don't want to stay up for just fifteen more minutes?"
    her annoyed "I'm not up to begin with. I'm still asleep. Zzzzzz..."
    him normal "Mmm, you're so sexy..."
    menu:
        "What should I do?"
        "Wake up for some action":
            her flirt "I just can't say no to you..."
            him flirt "Why would you want to?"
            her surprised "Did you get everything fixed up outside?"
            him sad "Yeah, sorry it took so long; that wind is awful."
            her flirt "You're awful, to keep me waiting so long."
            him flirt "I know, I better be extra good to you."
            her happy "Ohhh, you are good..."
            "[his_name] was definitely worth waking up for."
            $ made_love += 1
            $ loved += 2
            $ relaxed += 5
        "Go back to sleep":
            her concerned "I'm so sleepy..."
            him sad "..."
            her normal "But I love you."
            him normal "I love you too, [her_name]."
            "He kissed me one last time, and then held me close as I fell back asleep."
            $ loved += 1
            $ relaxed -= 2
        "Tell him off":
            her angry "You had your chance, but you missed it. Sorry, I can't just wait around all day for you to finally decide to show up and get some action."
            him concerned "C'mon, my [her_nickname]..."
            her annoyed "Just leave me alone."
            show him angry at midright with dissolve
            him "Fine."
            "We lay there, both angry, not saying anything, for a long time, before I finally got back to sleep."
            $ loved -= 2
            $ relaxed -= 2
    return

# Zombie Dinosaur Movie
label relax_together_h:
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
    $ loved += 2
    return

# Daisy-chain circlet of wildflowers
label relax_together_i:
    scene bg fields with fade
    "I was weeding in the backyard when I found some wildflowers. They reminded me of clover, so I made a daisy-chain circlet out of them. It was fun."
    menu:
        "Make one for [his_name] too.":
            him "It looks like you had some fun this afternoon."
            her "I made one for you too!"
            him "What am I, king of the faeries?"
            her "And I'm the queen! All the insects will obey our orders!"
            him "Maybe if those orders include eating everything in sight!"
            $ loved += 2
            
        "Make matching flower bracelets.":
            him "Glad to see those weeds are getting some practical use!"
            her "Well, jewelry isn't exactly practical, but it is fun."
            him "Shall I address you as Queen Mab from now on?"
            her "Yes. I'll fulfill all your wishes... in your dreams."
            him "Ooo, harsh. But being with you is like a dream come true, so does that mean you'll fulfill my wishes here?"
            "You get in a tickle fight, and one of your flower bracelets falls off. It was fun while it lasted."
            $ loved += 2
            $ made_love += 1
                
    $ skill_creative += 5
    return

# Messages on the computer
label relax_together_j:
    scene bg farm_interior with fade
    "I was sitting at the table, reading on my computer pad, when I got a message from [his_name]."
    "(Why is he sending me a message? He's right there...)"
    "I opened it."
    him "Right now I am sitting five feet away from the hottest chick in the universe."
    menu:
        "What should I write back?"
        "I'm jealous":
            her "I'm so jealous, who is she?!"
            him "Her name's [her_name]; you've probably heard of her. She's famous for her quick wit and good looks."
            her "Tell me more about her."
            him "Well, she's not conceited at all, that's one thing I like about her, and she's funny and creative, and she's got these lips that just beg to be kissed."
            her "So kiss them already!"
            "He sauntered over with a grin, leaned down, and kissed me like we had never kissed before."
            $ made_love += 1
            $ loved += 2
        "I'm next to a hot guy":
            her "Oh yeah, well I'm sitting right next to the sexiest man alive, or dead!"
            him "Sexier than Clark Gable and Abraham Lincoln?!"
            her "Definitely. He's funny, and hard-working, and when he looks at me, he's got these intense eyes-- I just melt."
            him "What a lucky guy..."
            "He looked over at me with what I'm sure he thought was a melting gaze, but instead it just made me laugh."
            "Soon he was laughing, too, and we were kissing, and everything seemed just about perfect."
            $ loved += 2
        "Nothing":
            "I didn't write him back. He's just being silly, to send me a message when I'm right here. I don't have time for that."
            $ loved -= 2
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_k:

    $ relaxed += 5
    $ loved += 2
    return

# Horror puzzle game
label relax_together_l:
    scene bg farm_interior with fade
    "We played a horror puzzle game together. We were both good at different kinds of puzzles, so we made a good team."
    "...plus I think he liked to see me jump at all the scary parts."
    her "AHHHHHHH!"
    him "You didn't know that was going to happen?"
    her "Well, I knew {b}something{/b} was going to happen, but no! Clowns don't usually have fangs!"
    him "Hehe, it's okay, we'll beat him. If we can figure out what to type on the typewriter..."
    her "Oh, try the first letter of each word in the clue!"
    him "Yeah!"
    "The game was fun, but I don't think I would have played it on my own. The best part was being with [his_name]."

    $ relaxed += 5
    $ loved += 2
    return
