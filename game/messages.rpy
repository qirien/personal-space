label msg_01:
    boss_c "Mandatory all-colony meeting tomorrow at 10, followed by a farmer's meeting at 11!"
    note " "
    him_c msg "Hey, a few people asked me about the attachment system on these tractors; so here's a how-to."
    
label msg_02:
    naomi_c "Please let me know if you would be interested in a weekly yoga and meditation session."
    note " "
    lily_c "I am looking for a volunteer to come to the ocean and gather guano. No experience necessary."
    sven_c "Doubt you'll get many takers on that one, Lily."
    
label msg_03:
    sven_c "Hey, uh, I forgot who checked out the chisel set, but could you please return them?"
    note " "
    her_c "Happy Birthday, [his_name]!"
    him_c "Thanks, [her_name]..."
    sara_c "It's your birthday? How old are you?"
    him_c "In Earth time, or relative time as experienced by me?"
    sara_c "Oh, never mind, it doesn't really matter, I guess."

label msg_04:
    brennan_c ""
    
label msg_05:
    boss_c "I've had a few questions about what to do with trash - let me remind everyone that our plastic and metal supplies are very limited, so make sure you recycle these items at the community center. Other trash can be burned or composted; see pages 126-128 of the Colonist's Guide."
    
label msg_06:
    thuc_c "Hey, my corn was doing fine, but the ears don't seem to be growing any bigger - anyone else having this problem?"
    martin_c "Yeah, mine, too. I noticed some tiny white dots under the leaves - maybe insect eggs?"
    
label msg_07:
    #message from her based on highest_skill
    $ highest_skill = highest_stat()
    if (highest_skill == "Domestic"):
        her_c "I've got some extra mint if anyone needs some - it grows really well here!"
    elif (highest_skill == "Creative"):
        her_c "Moonrise over the south hills, pic attached."
    elif (highest_skill == "Technical"):
        her_c "Finally got our new antenna installed. Everyone sounds much clearer now!"
    elif (highest_skill == "Spiritual"):
        her_c "Sister Naomi gave a great sermon yesterday..."
        natalia_c "Yes, it even kept Martin awake!"
    elif (highest_skill == "Social"):
        her_c "Free advice: never play Pictionary against Helen! She draws like da Vinci on speed..."
        him_c "I thought we did pretty good!"
        her_c "You draw more like Picasso..."
        him_c "Well, he's a pretty good artist, right?"
        her_c "Not for Pictionary!"
        
    elif (highest_skill == "Knowledge"):
        her_c "I took a picture of this plant; does anyone know if you can eat it? It smells good, but I'm not sure..."
        lily_c "It's not in our database; bring it by the lab and I'll run it through the spectrometer."
    elif (highest_skill == "Physical"):
        her_c "Ran 10k today; it feels good!"
        
label msg_8:
    if (profession == "teacher"):
        natalia_c "I'm so grateful for [her_name]; my kids love going to school! Josephina's so jealous of her brothers and sisters, but they've been trying to teach her on their own."
        her_c "That's great! You know, if she's ready, she could come to school some days, or maybe just in the mornings."
        natalia_c "Yes, that would be so good for her. I'll bring her by in a few days and we'll see how she does."
    elif (profession == "doctor"):
        julia_c "I'm so grateful for [her_name]; if it wasn't for her, my dear little Van wouldn't be with us anymore."
        her_c "I'm glad he's okay! His breathing isn't noisy, is it?"
        julia_c "No, he's completely recovered."
        sven_c "She fixed my leg up good, too. Thanks, Doc."
        her_c "No problem. But, next time you go up against a mill roller, get some backup first, okay?"
        sven_c "Sure thing, Doc."
    elif (profession == "carpenter"):
        martin_c "The new roof works great, [her_name]. The craftsmanship is excellent; I can tell  it will last."
        her_c "Glad to hear it!."
    elif (profession == "mechanic"):
        helen_c "[her_name], I heard you fixed the clinic's radio, could you take a look at ours, too? The volume control is broken..."
        her_c "Sure, bring it by sometime."

label msg_9:
    sara_c "Anyone seen \"Pioneer of the Stars\"? Is it any good?"
    her_c "Yeah, I just saw it! The romance was good, but the science was terrible. If you can ignore that, you might be able to enjoy it."
    sara_c "All right! Ilian, date night!!"
    ilian_c "I'm not watching it."
    her_c "I'll watch it with you, Sara, Ilian won't enjoy it anyway. He'll just spend the whole movie talking about how space ships don't really work like that."
    lily_c "They don't. The scenario in that movie is physically impossible."
    her_c "That's why it's a movie, not a documentary."
    
label msg_10:
    boss_c "Who grew the strawberries? These are delicious!"
    sven_c "They taste even better with some cream, Mayor G."
    boss_c "I'm sure they do - do you have any to spare?"
    sven_c "Sure, we can work out a trade."
    
label msg_11:
    thuc_c "[his_name], is Lettie better yet?"
    him_c "Yeah, she's fine. Still haven't figured out exactly what it was, though."
    nvl " "
    

label msg_15:
    if (is_pregnant):
        natalia_c "So, [his_name], what are you going to name the baby?"
        sara_c "Baby?! What baby? Why am I always the last to hear about these things?!"
        him_c "Haven't decided on a name yet; we just barely found out ourselves!"
        boss_c "Congratulations!"
        sven_c "About time!"
        ilian_c "[his_name], come by sometime, I have something for the baby..."
        lily_c "Congratulations may be premature. Approximately 15% of pregancies end in a miscarriage during the first trimester."
        helen "Even so, it's something to celebrate."
        brennan_c "Congratulations, [her_name]."
        nvl " "
    boss_c "Just a reminder - please don't let kids play in the community center when no one else is there. I wouldn't want anyone to get hurt by falling chairs or anything."
    natalia_c "Falling chairs? We're on an alien planet full of unknown perils and you're worried about falling chairs?"
    boss_c "I would feel responsible if something bad happened at the community center."
    natalia_c "Well, you wouldn't be. Let the kids be responsible for themselves, or else they won't learn how."
    boss_c "Well, I-"
    naomi_c "The truth is... there was a mess of mud and sticks on the corner. It seems some children were building a fort?"
    natalia_c "Oh, that. Well, sure, I'll have them clean it up. No need to restrict the whole area, right?"
    boss_c "I suppose not. But we can't have messes in there, we hold meetings there."
    natalia_c "Of course not. I'll let them know."
    
label msg_19:
    him_c "Hey, is there someone that wants our tomatoes and peppers? I'm not allowed to use my burned hands for another week..."
    thuc_c "You're not going to pick them with your teeth? You're such a slacker, [his_name]."
    him_c "Yeah, I know."
    thuc_c "I'm just kidding! I'll help you tomorrow night, okay?"
    sara_c "I'll help, too, as long as I get to eat some. Now I'm craving salsa! Ilian, do we have any chips?"
    ilian_c "No."
    natalia_c "I'll teach you how to make some, if you want."
    sara_c "Yes! Ohhh, chips and salsa..."
    brennan_c "Sara, have I mentioned lately how beautiful you are? And how generous, and kind to poor hungry souls like myself?"
    sara_c "Yes, actually you have. Make your own chips and salsa, Brennan."

label msg_22:
    natalia_c "I have good news - our son Tomas is engaged to Joanna Ngyuen!"
    julia_c "They can't keep their hands off each other, so I suppose it's for the best."
    thuc_c "Now, Julia, is that any way to talk about your daughter and her true love?"
    julia_c "True love! You're probably where she got such a ridiculous romantic notions."
    thuc_c "That, or it could be your old love letters that I let her read. I knew there was a reason I kept them all."
    julia_c "Thuc!!"
    nvl " "
    brennan "Ahhh, Tomas, you're a lucky man."
    martin_c "Man?! He's still a boy... Though if he's old enough to get married..."
    
label msg_24:
    boss_c "I know we're all looking forward to a few new supplies from the new ship, but let's remember to take only what we need."
