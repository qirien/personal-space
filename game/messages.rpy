# These are messages that appear on the colony message board each month

# TODO: have tiny avatars appear with each person's name

screen message_board:
    default side_image = None
    
    add "bg/silk-gray.jpg"
    add "bg/computer-pad.png"
    window:
        style "nvl_window"
        xpadding 50
        ypadding 50

        yfill True
        xfill True

        has vbox:
            style "nvl_vbox"
        $ num_messages = len(dialogue)
        text "{b}Colony Messages{/b}"

        # This is kind of cool, but it is distracting when there are not many messages.
        # TODO: Is there a way to only display this when the text is big enough?
        if (num_messages >= 10):
            viewport:
                mousewheel True
                yinitial 0
                scrollbars "vertical"
                has vbox
                for who, what, who_id, what_id, window_id in dialogue:
                    window:
                        id window_id
                    
                        has hbox:
                            spacing 10

                        if who is not None:
                            text who id who_id

                        text what id what_id                
        else:
            vbox:
                # Display dialogue.
                for who, what, who_id, what_id, window_id in dialogue:
                    window:
                        id window_id
                    
                        has hbox:
                            spacing 10

                        if who is not None:
                            text who id who_id

                        text what id what_id
            
# NVL mode characters for chat rooms, etc
define her_c = DynamicCharacter("her_name", color="#8864d5", image="her", kind=nvl)
define him_c = DynamicCharacter("his_name",  who_suffix = " {image=sprites/him-icon.png}",color="#c80000", image="him", kind=nvl) #red 
define naomi_c = Character("Naomi", color="#ededed", image="naomi", kind=nvl)  #light gray
define boss_c = Character("Pavel", who_suffix = " {image=sprites/pavel-icon.png}", color="#cccccc", image="pavel_c", kind=nvl)   #dark gray
define lily_c = Character("Lily", color="#8655bd", image="lily", kind=nvl)  #purple
define sara_c = Character("Sara", color="#c64e89", image="sara", kind=nvl)  # dark pink
define thuc_c = Character("Thuc", color="a9ff22", image="thuc", kind=nvl)  #lime green
define ilian_c = Character("Ilian", color="ffa922", image="ilian", kind=nvl) #tangerine
define brennan_c = Character("Brennan", color="33b533", image="brennan", kind=nvl)  #irish green
define jed_c = Character("Jed", color="cb5500", image="jed", kind=nvl)  #rusty brown
define natalia_c = Character("Natalia", color="ffe74a", image="natalia", kind=nvl)  #yellow
define helen_c = Character("Helen", color="cdcfb2", image="helen", kind=nvl) #tan
define julia_c = Character("Julia", color="#4b54cd", image="julia", kind=nvl) #icy blue
define martin_c = Character("Martín", color="#990011", image="martin", kind=nvl)  #dark red

define computer = Character(None, kind=nvl)

label msg_0:
    boss_c "We'll be arriving in a few days, so please review the attached housing setup document that explains how we will be setting up the colony."
    return

label msg_1:
    boss_c "Mandatory all-colony meeting tomorrow at 10, followed by a farmer's meeting at 11!\n"
    
    him_c "Hey, a few people asked me about the attachment system on these tractors; so here's a how-to."
    return
    
label msg_2:
    naomi_c "Please let me know if you would be interested in a weekly yoga and meditation session.\n"

    lily_c "I am looking for a volunteer to come to the ocean and gather guano. No experience necessary."
    jed_c "Doubt you'll get many takers on that one, Lily."
    return
    
label msg_3:
    jed_c "Hey, uh, I forgot who checked out the chisel set, but could you please return them?\n"

    her_c "Happy Birthday, [his_name]!"
    him_c "Thanks, [her_name]..."
    sara_c "It's your birthday? How old are you? ;-)"
    him_c "In Earth time, or relative time as experienced by me?"
    sara_c "Oh, never mind, it doesn't really matter. Happy Birthday, anyway! :-D"
    return

label msg_4:
    julia_c "I don't mean to be rude, but whoever is using our front yard as a shortcut to the community center is being extremely inconsiderate. They're trampling my oregano."
    natalia_c "Oh, is that your front yard? I didn't see a fence, so I just thought they were weeds. Sorry!"
    julia_c "I didn't think fences were necessary among trusting, sensible neighbors."
    sara_c "You have oregano?! :-o Can I have some?"
    julia_c "Of course, dear. Bring me some soap from the storehouse when you come, please."
    sara_c "Sure. :-)"
    ilian_c "Make sure you log it, Sara."
    sara_c "I always do."
    ilian_c "Except for that one time with the chocolate."
    sara_c "That was three months ago! Can you just let it go already?!"
    ilian_c "It's my job to see that everything is accounted for."
    return
    
label msg_5:
    boss_c "I've had a few people ask questions about what to do with trash - let me remind everyone that our plastic and metal supplies are very limited, so make sure you recycle these items at the community center. Other trash can be burned or composted; see pages 126-128 of the Colonist's Guide."
    lily_c "You can save combustible trash for your hybrid stoves for days of precipitation or cloud cover."
    him_c "Yeah, just make sure it's well-covered. There's some gigantic scavengers here who would love to become your pets."
    return
    
label msg_6:
    thuc_c "Hey, my corn was doing fine, but the ears don't seem to be growing any bigger - anyone else having this problem?"
    martin_c "Mine as well. I noticed some tiny white dots under the leaves - maybe insect eggs?\n"
   
    #message from her based on highest_skill
    $ highest_skill = highest_stat()
    if (highest_skill == "Domestic"):
        her_c "I've got some extra mint if anyone needs some - it grows really well here!"
        sara_c "Ooh, I'll take some! :-D"
        thuc_c "Me, too. You could dry some, too."
        her_c "Yeah, I think I will."
    elif (highest_skill == "Creative"):
        her_c "Moonrise over the south hills, pic attached."
        julia_c "Beautiful! You're quite the photographer!"
        natalia_c "Do you do family pictures? I want to send one back to Earth with a Christmas card."
        her_c "Sure! Let me know when and where."
    elif (highest_skill == "Technical"):
        her_c "Finally got our new antenna installed. Everyone sounds much clearer now!"
        sara_c "Yay, call me sometime! :-)"
    elif (highest_skill == "Spiritual"):
        her_c "Sister Naomi gave a great sermon yesterday..."
        natalia_c "Yes, it even kept Martín awake!"
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
        her_c "Ran 10k today; I feel tired but so good!"
        sara_c "Yay! You go, [her_name]! \o/"
    return
    
label msg_7:
    boss_c "Congratulations, everyone, at the end of the month we'll have been here for one whole Talaam year!"
    boss_c "We wanted to give everyone a time to celebrate their winter holidays, so at the end of the month we'll take a week off for those, and also to make plans for the new year."
    brennan_c "Hopefully there are plans for celebration!"
    naomi_c "Yes, I'll post a list of events for all the winter holidays, including a New Year's Eve party at the community center."
    brennan_c "Hey, Jed, any chance you could bring some strong beverages?"
    jed_c "I don't think you could handle my latest batch, Brennan."
    brennan_c "I can't back down from that sort of challenge. Bring it on!\n"
    
    sara_c "It'll be strange to have Christmas without snow... :-/"
    martin_c "When I lived in Chile we'd always go to the beach for Christmas..."
    brennan_c "Too bad it's not warm enough for that here!"
    return
        
label msg_8:
    if (profession == "teacher"):
        natalia_c "I'm so grateful for [her_name]; my kids love going to school! Josephina's so jealous of her brothers and sisters, but they've been trying to teach her on their own."
        her_c "That's great! You know, if she's ready, she could come to school some days, or maybe just in the mornings."
        natalia_c "Yes, that would be so good for her. I'll bring her by in a few days and we'll see how she does."
    elif (profession == "doctor"):
        julia_c "I'm so grateful for [her_name]; if it wasn't for her, my dear little Van wouldn't be with us anymore."
        her_c "I'm glad he's okay! His breathing isn't noisy, is it?"
        julia_c "No, he's completely recovered."
        jed_c "She fixed my leg up good, too. Thanks, Doc."
        her_c "No problem. But, next time you go up against a mill roller, get some backup first, okay?"
        jed_c "Sure thing, Doc."
    elif (profession == "carpenter"):
        martin_c "The new roof works great, [her_name]. Two storms and no leaks yet."
        her_c "Glad to hear it!."
    elif (profession == "mechanic"):
        helen_c "[her_name], I heard you fixed the clinic's radio, could you take a look at ours, too? The volume control is broken..."
        her_c "Sure, bring it by sometime."
        
    naomi_c "I'm sorry to have to bring this up, but some candles are missing from the chapel. If you borrowed them, please return them."
    natalia_c "I was wondering where those came from! I'll send Raúl over to give them back."
    naomi_c "Thank you."
    return

label msg_9:
    sara_c "Anyone seen \"Pioneer of the Stars\"? Is it any good?"
    her_c "Yeah, I just saw it! The romance was good, but the science was terrible. If you can ignore that, you might be able to enjoy it."
    sara_c "All right! Ilian, date night!! :-D"
    ilian_c "I'm not watching it."
    sara_c ":'-("
    her_c "I'll watch it with you, Sara, Ilian won't enjoy it anyway. He'll just spend the whole movie talking about how space ships don't really work like that."
    lily_c "They don't. The scenario in that movie is physically impossible."
    her_c "That's why it's a movie, not a documentary."
    return
    
label msg_10:
    boss_c "Who grew the strawberries? These are delicious!"
    jed_c "They taste even better with some cream, Mayor G."
    boss_c "I'm sure they do - do you have any to spare?"
    jed_c "Sure, we can work out a trade."
    return
    
label msg_11:
    thuc_c "[his_name], is Lettie better yet?"
    him_c "Yeah, she's fine. Still haven't figured out exactly what it was, though.\n"
    julia_c "I just fed someone else's ill-mannered children again... Ilian, would it be possible for me to pick up a little extra flour the next time I'm there?"
    ilian_c "Uhhh, yeah, that's probably fine..."
    natalia_c "Why are you getting all passive-aggressive, Julia? Just send them all over here next time. They know to listen to adults."
    julia_c "I'm terribly sorry, but I only let my children play at houses where there is proper adult supervision."
    natalia_c "You're not still mad about the mud, are you?"
    julia_c "They threw mudballs at my children!"
    natalia_c "They were all throwing mudballs! It was fun!"
    julia_c "I will not subject my children to that sort of mean-spirited \"play\"."
    natalia_c "Just mean-spirited parenting."
    return
    
    
label msg_12:
    if (ocean_character == "Jed"):
        jed_c "For the small price of shoveling guano, you too can see the beauties of the ocean! Ask Dr. Lily for details."
        her_c "Purple jelly encounter included at no additional cost!"
        jed_c "Yeah, that critter was downright strange. Almost seemed like it knew we were there."
    elif (ocean_character == "Brennan"):
        brennan_c "Dr. Lily, I wanted to thank you for that charming excursion to the ocean."
        her_c "Yeah, it was a nice break from the routine, and such beautiful scenery!"
        lily_c "You are welcome. If I need to go in the future, I may ask you to assist me again."
        brennan_c "You can count on me. Just, don't ask me to do anything with those purple jellies."
        lily_c "You... do not like them?"
        brennan_c "They made you fall asleep and act a bit loony."
        lily_c "Yes... I may have to retrieve one for study next time I go."
    else:
        sara_c "If you haven't been to the ocean yet, you should totally go sometime! Just watch out for those purple jellies. :-o"
        lily_c "They did not harm me."
        sara_c "They made you fall asleep!"
        lily_c "An effect that could have medicinal applications. I cannot afford not to look into it further."
                            
    return

label msg_13:
    natalia_c "Has anyone seen Josephina?! I put her to bed last night, and now she's gone!"
    thuc_c "She hasn't been to our farm all day."
    sara_c "I haven't seen her in town... :-("
    her_c "I saw her walking home from school with her siblings yesterday, but not this morning."
    boss_c "How long has she been missing?"
    natalia_c "I don't know! She could've been gone all night! I thought I saw her when I went to bed, but she's so small, it could've just been her blankets..."
    boss_c "She's awfully young to be out on her own for so long. Anyone who can, please meet at the Perón's and we'll organize a search."
    natalia_c "Thank you, Mayor."
    return
    
label msg_14:
    jed_c "Sure has been quiet around here lately..."
    martin_c "It's even quieter over here, without Josephina..."
    jed_c "Sorry, Martín..."
    helen_c "How's Natalia holding up?"
    natalia_c "I'm fine."
    #TODO: brennan_c posts pic of sad kitten, everyone calls him insensitive.
    return

label msgs_pregnant:
    natalia_c "So, [his_name] and [her_name], what are you going to name the baby?"
    sara_c "Baby?! :-o What baby? Why am I always the last to hear about these things?!"
    him_c "Haven't decided on a name yet; we just barely found out ourselves!"
    boss_c "Congratulations!"
    naomi_c "That's wonderful!"
    jed_c "About time!"
    ilian_c "[his_name], come by sometime, I have something for the baby..."
    lily_c "Congratulations may be premature. Approximately 15\% of pregancies end in a miscarriage during the first trimester."
    helen_c "Even so, it's something to celebrate."
    brennan_c "Congratulations, [her_name]."
    thuc_c "And [his_name]! People are always forgetting about the father."
    brennan_c "...Yes, of course."
    nvl clear
    return

label msg_15:
    boss_c "Just a reminder - please don't let kids play in the community center when no one else is there. I wouldn't want anyone to get hurt by falling chairs or anything."
    natalia_c "Falling chairs? We're on an alien planet full of unknown perils and you're worried about falling chairs?"
    boss_c "I would feel responsible if something bad happened at the community center."
    natalia_c "Well, you wouldn't be. Let the kids be responsible for themselves, or else they won't learn how."
    boss_c "Well, I-"
    naomi_c "The truth is... there was a mess of mud and sticks on the corner. It seems some children were building a fort?"
    natalia_c "Oh, that. Well, sure, I'll have them clean it up. No need to restrict the whole area, right?"
    boss_c "I suppose not. But we can't have messes in there; that area is for meetings and other colony business."
    natalia_c "Of course. I'll let them know."
    return
    
label msg_16:
    if (is_pregnant):
        call msgs_pregnant
    helen_c "Has anyone seen Jed?! He didn't come home last night!"
    naomi_c "He and Brennan got rather intoxicated last night, testing Jed's latest brew - I'll check at the community center for you."
    helen_c "Thanks, Naomi. Hopefully that's all it is.\n"
    jed_c "hey baby be home soon sorry you were worried."
    helen_c "We can talk about it when you get home, dear."
    brennan_c "Whatever she has to say, it was completely worth it, Jed. That was your best creation yet."
    naomi_c "I'm sure I don't have to remind you gentlemen to make sure the community center is ready for the meeting this afternoon."
    brennan_c "No problem, we got it covered."
    brennan_c "Ha ha, get it, man?! We got it \"covered\"?! Because the floor is covered in, in--"
    jed_c "your hilarious."
    return
    
label msg_17:
    sara_c "Hey, is there a schedule somewhere for the bathhouse?"
    boss_c "No, right now it's first come, first served. Has there been a problem?"
    sara_c "No, I just wanted to like, reserve it for tomorrow night."
    boss_c "Well, then, consider it reserved!"
    sara_c "Okay, great! :-D"
    return
    
label msg_18:
    him_c "Anyone else have any problems with a tractor battery going dead?"
    thuc_c "Mine doesn't hold the charge it used to; I have to come home at lunch and charge it off the house battery."
    julia_c "And then there's no power left for the stove!"
    lily_c "The overcast meteorological conditions of late also reduce the efficiency of the solar chargers."
    him_c "Anyone tried using the biofuel system?"
    jed_c "Yeah, if you use wood you gotta refill it every hour or so. Not too efficient. If we had some liquid fuel it'd probably last longer."
    ilian_c "That fuel is only for emergencies."
    him_c "Alright, I'll just charge it off the house for now."
    return
    
label msg_19:
    him_c "Hey, is there someone that wants some tomatoes and peppers? I'm not allowed to use my burned hands for another week..."
    thuc_c "You're not going to pick them with your teeth? You're such a slacker, [his_name]."
    him_c "Yeah, I know."
    thuc_c "I'm just kidding! I'll help you tomorrow night, okay?"
    sara_c "I'll help, too, as long as I get to eat some. Now I'm craving salsa! Ilian, do we have any chips?"
    ilian_c "No."
    natalia_c "I'll teach you how to make some, if you want."
    sara_c "Yes! Ohhh, chips and salsa..."
    brennan_c "Sara, have I mentioned lately how beautiful you are? And how generous, and kind to poor hungry souls like myself?"
    sara_c "Yes, actually you have. Make your own chips and salsa, Brennan. :-P"
    return
    
label msg_20:
    her_c "Does anyone have any protein foods they could spare? Meat, nuts, eggs, dairy...? I can trade vegetables..."    
    if (community_level < COMMUNITY_LEVEL_OK):
        natalia_c "No extra, sorry."
        jed_c "Nope."
        thuc_c "No."
        ilian_c "The storehouse still has some protein powder."
        her_c "I was hoping to avoid that, but I guess that'll have to do."
    else:
        natalia_c "You want some eggs? Bring some of those bell peppers and tomatoes and we'll trade!"
        jed_c "We've got milk or cheese we could trade for quinoa. I found a way to cook it so it almost tastes like grits."
        julia_c "I'll drop something by your house this evening."
        if (is_pregnant or is_pregnant_later):
            julia_c "You especially need the protein, since you're expecting."
        her_c "Thanks everyone... I just hope I can repay your kindness."
        
    return

label msg_21:
    ilian_c "COLONISTS: Please try to conserve rechargeable batteries. We are running out. They should last for at least ten years if treated properly."
    natalia_c "What does \"treated properly\" mean?"
    ilian_c "Try to charge them when they are halfway full instead of waiting until they are empty, and don't let them overcharge."
    lily_c "Also, don't let them get too hot. They should not be kept in the sun, or especially solar flares, if possible."
    natalia_c "OK, can do."
    
    return

label msg_22:
    # Can I have Tomas and Joanna post here w/o making characters for them?
    natalia_c "I have good news - our son Tomás is engaged to Joanna Ngyuen!"
    julia_c "They can't keep their hands off each other, so I suppose it's for the best."
    thuc_c "Now, Julia, is that any way to talk about your daughter and her true love?"
    julia_c "True love! You're probably where she got such a ridiculous romantic notion."
    thuc_c "That, or it could be your old love letters that I let her read."
    julia_c "Thuc!!\n"

    brennan_c "Ahhh, Tomás, you're a lucky man. Though I don't envy you having Julia for a mother-in-law...."
    martin_c "Man?! He's still a boy... Though if he's old enough to get married..."
    julia_c "A man is as a man does. Tomás is more of a man than some here, at least."
    brennan_c "I stand by what I said."
    
    return
    
label msg_23:
    helen_c "Hey, [her_name] you haven't had your baby yet, right? I hardly ever see you..."
    her_c "Not yet... I'm not due for another month."
    him_c "She's been sleeping a lot, trying to store it up for the nights ahead."
    helen_c "Ohhh, if only it worked that way!\n"
    nvl clear

    naomi_c "I wanted to announce that I will be asking each person to come in for a visit with me, just to make sure everyone is doing okay. I'm asking everyone, so please don't assume something's wrong when I contact you."
    natalia_c "This doesn't have anything to do with the shampoo incident, does it?"
    naomi_c "Not at all. Just that it's been almost two years since we arrived."
    natalia_c "After your honesty sermon yesterday I just wanted to make sure."
    julia_c "Hit you a little hard, did it?"
    natalia_c "Not a bit. But I noticed you looking quite uncomfortable."
    julia_c "I was just bored."
    ilian_c "I suggest you both stop arguing, since right after the sermon you both returned items you had \"borrowed\" from the storehouse."
    brennan_c "Ilian! Shame on you!"
    ilian_c "What? It stopped their argument, didn't it?"
    nvl clear
    brennan_c "You stopped it just as it was getting good!"
    julia_c "This is none of your business, Mr. Callahan."
    natalia_c "Shut up, Brennan."
    brennan_c "There, did you see how I sacrificed myself to get them to agree on something?"
    jed_c "Downright noble of you."
    return
             
label msg_24:
    boss_c "I know we're all looking forward to a few new supplies from the new ship, but let's still remember to conserve our resources."
        
    return
    
label msg_25:
    if (is_pregnant):
        julia_c "Congratulations to [his_name] and [her_name] on the birth of their new baby, [baby_name]!"
        sara_c "She's adorable! Yay! :-D"
        martin_c "Congratulations!"
        natalia_c "You'll be wonderful parents! I'd be happy to watch her for you if you need to get some things done. I miss babies..."
        thuc_c "She looks just like you, [his_name]!"
        him_c "I hope not!"
        helen_c "I think she looks more like [her_name]."
        lily_c "Congratulations on successfully breeding."
        ilian_c "I can bring some things by from the storehouse, so you don't have to leave the house for a bit, if you want."
        her_c "Thanks, everyone!! We're just taking it easy for a week or two, but I'll be bringing her to work with me as soon as I can manage it."
    elif (is_pregnant_later):
        call msgs_pregnant
    else:
        sara_c "Great news everyone!! We're going to have a baby!! :-)"
        her_c "Way to go! That's great!"
        naomi_c "That's wonderful!"
        helen_c "I'm so happy for you!"
        thuc_c "Congratulations!"
        julia_c "Congratulations. I can serve as midwife when the time comes, if you would like."
        sara_c "Thanks, everyone! I'm sure Ilian appreciates your well-wishes, too... :-/"
        ilian_c "Yeah, thanks."
        
    nvl clear
    if (((community_level < COMMUNITY_LEVEL_OK) and (loved < 0)) or wants_to_leave):
        sara_c "I'm going to miss you, [her_name]!!! :-("
        helen_c "What? [his_name] and [her_name] are leaving?"
        him_c "No, I'm staying."
        helen_c "Ohhh... I'm sorry."
        him_c "Yeah, well, it's okay."
        nvl clear
        
    brennan_c "I'm leaving, in case anyone cared."
    him_c "Not likely."
    lily_c "That is a shame."
    brennan_c "Thanks, Lily."
    lily_c "With you gone, the ratio of people capable of producing useful capital to dependents will decrease substantially."
    brennan_c "Awww, stop, you're making me blush."
    lily_c "Also, the variation of our genetic pool will decrease."
    brennan_c "You should have said something sooner, maybe we could have contributed to the gene pool together!"
    julia_c "That's enough; sometimes my kids read these messages!"
    lily_c "I will continue this conversation with you in private, Brennan."
    sara_c ":-o Ummm, wow, did one of Brennan's pickup lines actually work?!"
    jed_c "It's about time."
        
    return