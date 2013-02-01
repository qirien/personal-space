# Event content for all the events that can happen in the evening,
# where we relax together

# Relationship Focus Events
# TODO; Have them talk about missing (or not) families on Earth.
# TODO: Have them tour the farm and talk about progress/problems
# TODO: Sunset on the new planet


label relax_together_0:
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

label relax_together_1:
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
    scene bg stars with fade
    play music "music/Will.ogg" fadeout 2.0
    "We went for a walk together under the stars. I brought my computer pad so we could find which one was our old Sun. I didn't see any constellations I recognized, so it was hard to find any reference points, but we finally found which one we thought it was."
    her "It looks so small..."
    him "Remember how small Talam's sun looked from Earth?"
    her "That seems so long ago..."
    $ relaxed += 5
    return

label relax_together_3:
    scene bg farm_interior with fade
    "The library had a huge collection of Earth media that colonists could check out. They even received new things from Earth sometimes, though they only had enough bandwidth to receive the most popular things."
    "One day I noticed they had a new movie about space colonists. I was curious to see how people on Earth saw people like us, so I checked it out."
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
            her "Even putting up fences is not too bad when it's with you."
            $ loved += 5
            $ skill_physical += 5
            $ community_level += 5
            scene black with fade
  
        "Want to watch it another night?":
            her "No problem, we'll just watch it another night."
            him "Thanks for understanding. I'll see you later, [her_nickname]."
            "It was a little lonely, especially since I was really looking forward to watching the movie with him, but I soon was absorbed in a good book and then went to bed."
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
                    $ relaxed -= 5
                    "Finally, I just went to bed."
                "...":
                    "I didn't say anything; just watched him leave, feeling hurt and lonely."
                    "All I could think about was how he abandoned me. It wasn't every night I asked him to do something fun with me; why couldn't he put me first instead of his other plans?"
                    "I worried that maybe I was not good enough - not pretty enough, not smart enough, not strong enough - not just for him, but for this planet. What was I even doing here?"
                    "I trudged in circles through these depressing thoughts for hours."
                    $ relaxed -= 5
                    "Finally, I just went to bed."
                "Sorry":
                    her "Sorry, [his_name]. I'm being selfish."
                    him "It's all right, [her_nickname]. Let's do something together tomorrow night, okay?"
                    her "Okay, [his_name]."
                    "We watched the movie the next night. Even though they got a lot of things wrong about space colonization, we really got into the drama and tension. We both cried a little at the end."
                    $ relaxed += 5
                    $ loved += 5
    return

label relax_together_4:
    return

label relax_together_5:
    scene bg farm_interior with fade
    play music "music/Will.ogg" fadeout 2.0
    "One day after dinner I noticed [his_name] rubbing his shoulders and grimacing."
    show him normal at center
    show her normal at right
    her "Are you okay?"
    him "Yeah, I'm just really sore from all the digging I've been doing lately."
    if (relaxed < 0):
        her "Yeah, I feel pretty tense, too."
        "I could have rubbed his shoulders, I guess, but I was just too tired."

    elif (loved >= 0):
        her "Want me to rub your shoulders?"
        him "I would love that!"
        "I started off gently. His muscles were so tight, I was amazed he could move at all. I gradually kneaded harder, trying to tell what sorts of massage he liked."
        him "Ohhh, that feels so good."
        "Sometimes he would make sort of painful grunt that let me know he didn't like what I was doing. But he would also sigh with content when I hit a particularly tense spot."
        if (relaxed >= 5 && skill_physical >= 10):
            "After his shoulders, I massaged his arms and hands. It made me think of how hard he had been working all day."
            
            if (skill_physical >= 30):
                "My hands were starting to get a little tired, but I didn't want to stop yet, so I rubbed his legs and feet, too."

        "To finish off I massaged his neck and head. I could tell he really enjoyed it."

        if (loved >= 5):
            him "Now it's your turn to get massaged."
            her "Mmmm, really? Are you talking about shoulders, or...?"
            him "I'll massage anything you like."
            her "Why don't you start with the shoulders, and then we'll see what happens?"
            "He copied what I had done earlier, and gave me quite the massage, too. It was so relaxing to just sit and do nothing while he took care of all my tense muscles."
            $ made_love += 1
            $ relaxed += 5

        $ loved += 5

    return

# go "out" to eat on a picnic
label relax_together_6:
    him "Put on your fancy clothes, [her_nickname], because we are going OUT tonight!"
    her "Out where? And I don't have any fancy clothes..."
    him "Any clothes look fancy on you! But I can't tell you where we're going; it's a suprise."
    her "Okay, let me get ready, then. I can at least brush my hair."
    "(Where can we be going?)"
    him "Now put this blindfold on"
    her "You're not serious, are you?!"
    him "I'm totally serious!"
    "I let him blindfold me and we left the house.  He spun me around so I couldn't tell which direction we were going, and then we hiked for about twenty minutes or so. He held my hand so I didn't trip."
    her "It's a good thing I didn't actually put on fancy clothes, since this isn't exactly level terrain."
    him "We're almost there."
    "Finally, he took off the blindfold."
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
        "Sexy":
            her "Should we get started like this...?"
            him "Maybe a little bit of this?"
        "Exasperating":
            her "Oh, you...!"
            him "Ha ha, I'm just kidding."

    her "It's too bad there's so many rocks here..."
    him "Come over here, it's softer."
    her "Is this our mattress?! You were planning this all along!"
    him "It never hurts to be prepared..."
    menu:
        "That's..."
        "Romantic":
            her "You're so romantic."
            him "I love you, [her_name]."
            $ made_love += 1
        "Logical":
            her "Yeah, that makes sense."
            him "I love you, [her_name]."
            $ made_love += 1
        "Presumptuous":
            her "That's pretty presumptuous. You think that just because you setup some fancy dinner that you're automatically going to get some?"
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
    scene bg black with fade
    "We lay there for a long time...In the morning, it felt so good to wake up next to him, watching the sky lighten. With one final kiss, we got up and carried everything back to the house together."
    return

label relax_together_7:
    return

label relax_together_8:
    return

label relax_together_9:
    return

label relax_together_10:
    return

label relax_together_11:
    return

label relax_together_12:
    return


# Random events that can happen multiple times

label relax_together_a:
    "Random A"
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_b:
    "Random B"
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_c:
    "Random C"
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_d:
    "We were both reading on our computer pads, sitting near each other. We didn't talk much, but everyone once in a while we would look up and smile at each other."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_e:
    "We played video games together on our computer pads. We liked to play on the same team."
    $ relaxed += 5
    $ loved += 2
    return

label relax_together_f:
    "We made a nice dinner together, and talked while we ate slowly, watching the sun go down."
    $ relaxed += 5
    $ loved += 2
    return
