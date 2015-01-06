# Afternoon Events
# Domestic

# Default Event
label domestic_def:
    scene bg farm_interior with fade
    "I did some deep cleaning and organizing, and put in some extra work for a great dinner."
    $ skill_domestic += 10
    return

# Intro Event
label domestic_0:
    scene bg farm_interior with fade
    show her serious at center with dissolve
    her "There's a lot of work to do be done around the house... should I plan it, or just dive in?"
    menu:
        "What should I do?"
        "Make a cleaning schedule.":
            "I setup a system for cleaning the house, with different tasks for each day of the week."
            "Mondays I would plan meals for the week based on what food we had; Tuesdays I would do laundry; Wednesdays I would dust and wipe down the walls and furniture; Thursdays I would clean the outhouse; and Fridays I reserved for special projects."
            "Chores like sweeping and dishes would be done every day."
            "Having a system made it easier, because I didn't have to decide each day what I should do (though I didn't follow it every day)."
            $ community_level += 2
        "Get started and clean whatever looks dirtiest.":
            "I didn't want to be restricted by a schedule. I saw the sink was dirty, so I cleaned it. When the floors got too messy, I swept them. When our clothes got too dirty, I did laundry."
            "You could never tell when things would need to be cleaned, anyway."
            "When I wanted to make something, I'd look at the ingredients we had and throw something together."
            "It worked out pretty good most of the time."
    
    $ skill_domestic += 10

    return

# Laundry by hand is tough?
label domestic_1:
    scene bg laundry with fade
    show her normal
    her "Time for laundry!"
    "I put all the clothes in a big bucket with water and soap, and scrubbed them. Usually that worked fine, but some of the clothes were really dirty."
    her annoyed "Washing these clothes by hand is taking forever."
    her surprised "I wonder how I could speed it up?"
    menu:
        "What should I do?"
        "Leave the clothes soaking while you finish doing the dishes.":
            her "Maybe I just need to let the soap do my work for me."
            "Twenty minutes later..."
            her "That helped a bit! I should leave clothes soaking more often."
            $ relaxed +=2

        "Use hot water instead of cold water.":
            "It took about half an hour to go fetch enough water for the wash bin, heat it up on the stove, and pour it in the wash tub."
            "But the hot water did seem to get dirt out faster."
        
    $ skill_domestic += 10
    return

# fence to keep out herb garden pests
label domestic_2:
    scene bg fields with fade
    show her normal at center
    "I planted an herb garden when we first arrived, and the plants are just starting to get big enough for me to use. I think I'll make some tea..."
    her surprised "Something's been nibbling at my herbs...!"
    "I peeked out the window every time I passed, trying to see what it was. Finally, I saw a strange small animal that looked kind of like a cross between a frog and a rabbit."
    her annoyed "(I chased it away, but what about next time?)"
    her serious "I know!  I'll make a fence!"
    "I gathered some sticks from some of the local plants, and tied them together with vines. When I tried to pound in the corners, the sticks broke in the hard dirt."
    "I took a break for a snack and thought about it. I decided to soften the dirt with water first.  Then I was able to pound in the corners and finish my fence."
    her happy "Whew! It's done!"
    "I watched, and sure enough, my fence kept out the creature.  Good to know my herbs were safe."
    $ skill_domestic += 10

    return

# Who wants a goat?
label domestic_3:
    scene bg farm_exterior with fade
    show her normal at midright with dissolve
    show thuc at midleft with moveinleft
    thuc "Hello? [his_name]?"
    her normal "Thuc! Good to see you! [his_name] is out in the fields, working, if you want to go find him."
    thuc "Maybe I'll just ask you, then. You heard about the baby goats born at our farm, right?"
    her surprised "Yeah, how are they doing? Are they hard to take care of?"
    thuc "Not at all! They can eat almost any plants, and are pretty hardy. Are you interested in taking care of some goats?"
    menu:
        "What should I say?"
        "Yes!":
            her normal "I would love to! But I've never taken care of goats before, so would you help me if I run into trouble?"
            thuc "Of course! Why don't you let me know when you have a spot fenced off for them? They are able to eat the native vegetation here, so you could even use them to help clear space for fields."
            "[his_name] and I talked it over, and we decided to fence in a part of the wild area not too far from the house for the goats."
            scene bg fields with fade
            show lettie at right with dissolve            
            show goat_flip at left
            show goat at center
            show goat_small at quarterright
            "There were three of them, two males and a female, and I became remarkably attached to them. [his_name] used the manure for fertilizer, and they worked hard eating the strange plants from this planet."
            "They even kept Lettie company - she seemed to like grazing near them."
            $ skill_domestic += 10
            $ community_level += 5
            $ have_goat = True
        "No, thanks.":
            her annoyed "(I don't think I have time to take care of goats right now!)"
            her serious "Thanks for offering, but I don't think we want to do that right now."
            thuc "I understand."
            "But [his_name] wasn't so understanding."
            scene bg farm_interior with fade
            show her normal at midleft
            show him angry at midright
            with dissolve
            play music "music/Prelude02.ogg" fadeout 1.0
            him "Free goats? Why did you turn him down?!"
            her angry "I don't know anything about goats! I have enough to do as it is!"
            her annoyed "Besides, goat milk tastes gross."
            him annoyed "You should have asked me about it first."
            menu:
                "What should I say?"
                "{i}You're right.{/i}" if (relaxed >= 0):
                    her sad "You're right, I'm sorry."
                    him sad "Sorry for yelling at you - it's not worth getting upset over."
                    menu:
                        "What should I say?"
                        "I hate it when we fight.":
                            her concerned "I hate it when we fight."
                            "He came over and held me close."
                            him serious "I'm sorry, [her_nickname]. You do a lot around here that I don't always see or appreciate."
                            her serious "I know you work hard every day, too. I don't want to ask you to do any more than you already do."
                            "We didn't need to say anything more."
                        "I have to get out of here.":
                            her angry "I'm going out."
                            "I went on a walk until I had cooled off. When I came back, we didn't talk about it anymore, and eventually we were back to normal."
                        "(Give him a hug.)":
                            "I hugged him. It took a few seconds for him to hug me back, but then I knew that everything would be all right."
                            
                "What's the point?":
                    her annoyed "What would be the point of asking you? You don't have time to take care of goats, either."
                    him serious "The point is that we're a team. We need to make big decisions like this as a team."
                    her serious "I didn't think it was even worth considering."
                    him annoyed "Well, I do. I guess now you know for next time."
                    her annoyed "(Yeah, next time I won't even tell you about it.)"
                    $ loved -= 10
                "Forget it.":
                    her concerned "It's not worth fighting over; let's just forget about it."
                    him serious "Yeah, I can think of much better things to fight over."
                    her surprised "Such as?"
                    him flirting "Who's going to get the last strawberry."
                    her annoyed "Ohhh! I was saving that for something special!"
                    him serious "I was saving it for something special, too."
                    her flirting "Like what?"
                    him serious "Like you."
        "Let me ask [his_name].":
            her concerned "I don't know... maybe I'll ask [his_name]."
            thuc "Sure, just let me know. See you later, [her_name]."
            her normal "Bye!"
            scene bg farm_interior with fade
            show her normal at midleft
            show him normal at midright
            with dissolve
            him surprised "Free goats?! Of course we want those!"
            her surprised "Are they really that useful?"
            him happy "Yeah! They can clear land by eating weeds, they leave fertilizer wherever they go, and you can get goat's milk from them."
            him normal "And they can keep Lettie company."
            her concerned "That's true... but I don't know anything about how to take care of them."
            him normal "Don't worry about it; I'll take care of them."
            her normal "Okay, great. I'll tell Thuc tomorrow."
            scene bg fields with fade
            show lettie at right with dissolve            
            show goat_flip at left
            show goat at center
            show goat_small at quarterright
            "[his_name] and I talked it over, and we decided to fence in a part of the wild area not too far from the house for the goats."            
            "There were three of them, two males and a female, and I became remarkably attached to them. They worked hard eating the strange plants from this planet."            

            $ skill_domestic += 10
            $ community_level += 3
            $ have_goat = True
            
    return

# Too many radishes!
label domestic_4:
    scene bg farm_interior with fade
    show her normal at midright with dissolve
    show him normal at midleft with moveinleft
    him "Here's some more radishes from the fields, love."
    her happy "Thanks, they look great!"
    hide him
    show her concerned at center with move
    her "(More radishes? I don't know what else to do with these besides salad...We can't waste any food, so I better think of something!)"
    if (skill_knowledge >= 20):
        "I decided to do some research about radishes..."
        her happy "Radish pickles?! That sounds fun!"
        "They had plenty of vinegar and salt at the storehouse, and I used some of the herbs and spices from the garden to make a few batches of pickled radishes."
    elif (skill_social >= 20):
        her normal "I bet I could trade these with the Perón's for some eggs from their chickens..."
        "Sure enough, Natalia was delighted to have some fresh vegetables, and I made a souffle instead."
        $ community_level += 5
    elif have_goat:
        "I sliced them really thin and spread them with goat cheese and some herbs from the garden."
        her happy "They hardly taste like radishes anymore...much better!"
    else:
        "I couldn't think of anything else, so I cut them into pretty rose shapes and drizzled oil and vinegar on them. They still tasted like radishes, but at least it was something a little different."

    $ skill_domestic += 10
    return

# Pumpkins and Halloween!
label domestic_5:
    scene bg farm_interior with fade
    show her normal at midright with dissolve
    "One day, [his_name] brought home some pumpkins he had planted."
    show him normal at midleft with moveinleft
    him "Look how well these pumpkins turned out!"
    menu:
        "What should I say?"
        "They look good!":
            her happy "They look good! What a deep orange color. But...are they supposed to be so bumpy?"
            him normal "Yeah, they grew bumps to protect themselves from the critters here."
            $ loved += 2
        "They look deformed...":
            her normal "They look a little strange- are they supposed to be so bumpy?"
            him normal "Yeah, they grew bumps to protect themselves from the critters here."
        "They look useless.":
            her annoyed "Pumpkins? What am I supposed to do with those?"
            him annoyed "I don't know; make pumpkin pie?"
            $ loved -= 2
     
    hide him
    show her normal at center with move
    her surprised "(I wonder what I should do with them...?"
    menu:
        "What should I do?"
        "Make pumpkin pie.":
            "I made pumpkin pie. I didn't have much sugar to put in it, but it tasted pretty good, anyway."
        "Make pumpkin goulash.":
            "I made a pumpkin goulash with other vegetables and baked it inside the pumpkin. It tasted pretty good!"
        "Make jack-o-lanterns.":
            "I made some jack-o-lanterns and put candles in them. They grinned saucily at us at night, until they started rotting and I had to throw them away."

    hide her
    play music "music/Prelude22.ogg" fadeout 1.0
    "Even though it wasn't anywhere near Halloween going by the Earth calendar, the colonists all thought that if we had pumpkins, we should have a harvest festival!"
    "They announced that there would be a costume party at the community center, and everyone could bring sweets to give out to the kids."
    menu:
        "I thought:"
        "How fun!":
            "We didn't have any candy, of course, but I decided to try to make some. The main problem was that we didn't have any sugar left."
            if (skill_knowledge >= 40):
                "In my studies with Lily, we had found a plant whose sap had a high sugar content. I boiled it, and then dipped sticks into it. After two days, small crystals started to form on the sticks, and after a week, each stick had a nice cluster of rock candy crystals on it."
            else:
                "I made some cookies using smashed fruit as a sweetener.  They weren't very sweet, but I added some spices and nuts so they had lots of interesting flavors."
            scene bg community_center
            "The kids made costumes out of scraps and household items, and they went around trick-or-treating to all the farms and houses."
            if (want_kids):
                "I wondered what it would be like to have our own child and take them trick-or-treating and celebrate holidays together. What will our kids be like?"
            else:
                "They were cute, but I was kind of glad when the party was over. I'm not used to being around kids so much."
            $ community_level += 1
        "How annoying.":
            "I thought that sounded loud and annoying. How was I supposed to make candy, anyway?! We just stayed home."

    $ skill_domestic += 10
    return

# what to do with local meat
label domestic_6:
    scene bg farm_interior with fade
    "One day, I came home from work to find a dead monster on the kitchen table."
    show her surprised at midleft with moveinleft
    her "What is THAT?!"
    show him normal at midright with moveinright
    him "There was a herd of them eating some of the vegetables on the north side. I was watching them, because they're so strange, you know, and I just thought they looked really tasty."
    her surprised "Tasty?! They look like fish with long legs!"
    him serious "It's been a really long time since we had any fresh meat! They made me think of salmon... so I lassoed one."
    her serious "What happened next?"
    him normal "Well, it started to run. Luckily I was on Lettie at the time, so she started running, too. We had quite a chase through the woods before the creature tired out."
    him serious "When it finally slowed down, I jumped off and attacked it."
    menu:
        "What should I say?"
        "That's barbaric.":
            her angry "That's barbaric! What did that poor creature ever to do you?"
            him annoyed "Ate my plants, that's what. Well, you don't have to have any; I guess I'll just cook it myself."
            her annoyed "Yeah, please get that thing out of here."
            "He roasted it outside over a fire. He didn't tell me how it tasted, which was fine - I didn't want to know, anyway."
            $loved -= 5
            return
        "That's awesome.":
            her happy "That's awesome! You're like my very own mountain man."
            $loved += 5
        "That's weird!":
            her concerned "That's...not something I'm used to. Can you really eat it?"
            him serious "The scientists here haven't detected anything toxic or unusual in the animal life here - I think as long as we cook it well and don't eat the organs it should be fine."
    
    her concerned "This is going to be a lot of meat..."
    him surprised "Yes, any ideas what we should do with it?"
    
    menu:
        "What should I say?"
        "Let's give some away.":
            her normal "We could give some away to our neighbors."
            him normal "Yeah, there's plenty here, if they'd want some."
            if skill_technical >= 20:
                her "I'll ask around."
                "I got on the radio and asked around town -- turns out a lot of people felt like [his_name] and thought some fresh meat would be delicious, even if it was alien meat."
                "It felt good to share with our neighbors."
                $ community_level += 5
            elif skill_social >= 20:
                her normal "I know just who would want some."
                "The Nguyen family had ten kids and I knew some of their crops hadn't made it. There were plenty of rations in the storehouse, so they weren't starving or anything, but I thought they'd like some real food."
                "When I took it to them, they didn't care that it came from an alien monster; they just thanked me and gave me some butter from their goats to take home with me."
                $ community_level += 5
            else:
                "I wanted to share, but I didn't really know who to ask. I gave some to the Mayor, and some to Sara, but there was still a fair amount left over."
                $ community_level += 2
        "Let's dry it.":
            her normal "We could dehydrate it and make jerky."
            him surprised "Do you know how to do that?"
            her serious "Theoretically...we'll need to smoke and salt it...We can adapt a recipe for fish jerky, I think."
            him normal "OK, I'll skin and cut up this sucker while you're figuring that out."
            if (skill_technical >= 30):
                "I rigged up a smoker with some old scrap metal and put some screens above it for the meat"
            else:
                "We soaked the meat in brine, and then I setup some racks where the fish could dry in the sun and wind."
                her concerned "If it rains we'll need to bring everything inside..."
                him normal "Let's hope it doesn't rain, then!"
                "It took several days longer to dry than I had planned, and we did have to bring it the house once, but when we were done we had some jerky that would last a long time, and actually tasted pretty good."
        "Let's compost it.":
            her concerned "Should we just compost what we can't eat?"
            him concerned "I guess..."
            "We cooked and ate quite a bit, but we didn't have a way to freeze or refrigerate so we just tossed the leftovers into the compost pile. Probably some scavenging animals will enjoy a nice feast..."
            $ community_level -= 5

        "Let's have a meat party.":
            her normal "Let's cook it all up, invite our friends over, and have a meat party!"
            him happy "All right! We can try cooking it several different ways and see what tastes best!"
            her happy "A meat-tasting party!"

            scene bg farm_exterior with fade
            if skill_social >= 90:
                "We invited the whole town for a giant potluck celebration. People brought salads and fresh bread and rice and spicy beans and there was even a little fruit for everyone."
                "Our little colony didn't have many celebrations; even though there wasn't really enough meat for everyone to have much, since we all brought something it worked out. We felt like a real community."
                $ community_level += 10
            elif skill_social >=30:
                "We invited a large group of friends and we ate almost all of it. I think they appreciated that we shared it with them. It felt good to help out our friends."
                $ community_level += 5
            else:
                "We invited a few friends over and we ate and ate and ate as much as we could. I wondered if we might get sick, but other than feeling full all the next day (and having a little trouble going to the bathroom), nothing bad happened."
                $ community_level += 2
            
    $ skill_domestic += 10
    return

# running out of soap; must make own soap with ash, fat, etc
label domestic_7:
    scene bg community_center with fade
    show pavel at center with dissolve
    pavel "One last item of business for the community meeting-"
    pavel "Our soap supply is running low. If anyone can make some soap and put the extra in the storehouse, that will help everyone to stay clean and healthy."
    hide pavel
    show him normal at midright
    show her normal at midleft 
    with dissolve
    him "I bet you could make some soap, [her_nickname]."
    her flirting "I bet I could. But I bet we could make even better soap together."
    if (loved >= 5):
        him flirting "Everything we make together is good."
    else:
        him concerned "Sorry, [her_nickname], I don't have time right now."
    
    scene black with fade
    "Making soap from scratch wasn't something I had ever done before. On Earth soap was so cheap there was not much reason to make your own. But I used my computer pad to look up instructions."
    scene bg laundry with fade
    show her serious at center with dissolve
    her "It looks like it will take at least a month to make the soap...better start on it now!"
    "First, I put on gloves and goggles. We needed to make lye, which is very caustic. I got some ashes from our stove and added boiling water, and let it sit overnight."
    "Meanwhile, I needed to get some fat."
    if (loved >= 5):
        scene bg farm_interior with fade
        show him normal at midright with dissolve
        show her normal at midleft with moveinleft
        her surprised "Hey, [his_nickname], we need some fat for the soap. Any ideas?"
        him "I could hunt down another one of those creatures that are always nosing around the farm."
        menu:
            "What should I say?"
            "Yes.":
                her normal "That would work. We could use the meat and hide, too, for other things."
                him happy "All right, I'll bring home the bacon for you, [her_nickname]."
                "It was a lot of work separating the fat from the meat, and rendering and cleaning the fat, but I was glad we could make it using only things we found on this planet."
                him normal "It feels good to be more independent from Earth."
                her happy "Yeah, who needs Earth, anyway!"
                him serious "Doesn't mean I won't be glad to see the supply ships, though."
            "No.":
                her serious "No, why don't you just see if the storehouse still has oil?"
                him serious "Okay, but we should start saving fat for next time."
                her normal "Good idea."
        scene bg laundry with fade
        show her normal at center
    else:
        "I got some shortening from the storehouse."
        "At first Ilian didn't want to give me so much, but when I told him it was for soap he relented."
   
    "I heated the grease in one pot, and heated the lye in another pot to the right temperatures. Then I added a little of each to another pot several times until I had the right amount."
    if (loved >= 5):
        show her normal at midright with move
        show him normal at midleft with moveinleft
        her "Would you stir that for me, please?"
        him "No problem."
        "It helped to have him stirring while I added the lye and grease."
    else:
        "I stirred it and stirred it."
    "I tried to balance the amount of lye and grease to make a soap that was not too greasy and not too caustic. Then I let it cool."
    "I poured off some of it for liquid soap that we could use right away, and saved the rest for hard soap. Adding salt and skimming off the foam on top helped dry the hard soap out."
    if (skill_creative >= 40):
        "I melted it again and added some flowers for scent and color."
    if (skill_technical >= 40):
        "I used some of the cans and boxes to make soap molds and poured it in."
    else:
        "I poured all the soap in a box and let it cool."
    "After the hard soap cooled, I cut it up and set it out to dry and air out. After a few weeks, it was ready to use!"
    "My first batch was very drying and hard on the skin, but it did get things clean. I decided to start saving ashes and fat to use so I could get better at making soap."
    her surprised "Now, after all this hard work, should I share some with everyone else? I do have some extra..."
    menu:
        "What should I do?"
        "Share it.":
            "I took what we couldn't use right away to the storehouse."
            scene bg storehouse with fade
            show ilian at right
            show pavel at midright, behind ilian
            with dissolve
            show her normal at midleft with moveinleft
            her "I was able to make some soap; here's some extra. You might want to warn anyone using it that it's pretty strong."
            pavel "This looks wonderful! Thank you, [her_name]."
            ilian "Huh. You actually did it."
            her "I can make more, if it's useful."
            pavel "Definitely! No one else has tried soapmaking yet."
            $ community_level += 2
        "Keep it.":
            "I worked so hard on this soap, I couldn't bear to give it away to just anyone."

    "I would never take soap for granted again."
    
    $ skill_domestic += 10
    return

# Canning
label domestic_8:
    scene bg farm_interior with fade
    "[his_name] was harvesting a lot of vegetables and fruits, and while the cellar kept some things cool and dry, other produce didn't last very long."
    "We had so many tomatoes and zucchinis there was no way we could possibly eat them all before they went bad. We took a bunch to the storehouse, but they told us that everyone else had all they could eat, too."
    "I didn't want them to go to waste, and I knew we would be wishing we had some more later, so I decided to preserve them. But what should I turn them into?"
    menu:
        "What should I do?"
        "Make tomato sauce.":
            if (skill_technical >= 60):
                "I used the blender I had made to puree a bunch of vegetables in a nice sauce."
            else:
                "I chopped up the tomatoes and zuchinis."
            "Then I cooked the sauce and ladled it into clean glass jars. I let the jars sit in boiling water to kill any bacteria."
            "It took all day, but looking at the rows of jars full of food we had grown and made ourselves was very satisfying."
        "Make salsa.":
            if (skill_technical >= 60):
                "I used the blender I had made to puree a bunch of vegetables in a nice salsa."
            else:
                "I chopped up the tomatoes and zuchinis and onions and peppers."
            "I ladled the salsa into clean glass jars. I let the jars sit in boiling water to kill any bacteria."
            "It took all day, but looking at the rows of jars full of food we had grown and made ourselves was very satisfying."
        "Dehydrate them.":
            "I sliced up the vegetables and set them on screens outside to dry."
            "The texture wasn't very good, but they would be fine rehydrated in sauces and things."
            "I sealed them up and put them in the cellar. The sight of all that food that we had grown and made ourselves was very satisfying!"

    $ skill_domestic += 10
    return

# Start a 'No Space Like Home' blog about domestic life!
label domestic_master:
    scene bg farm_interior with fade
    "I had learned so much about how to keep things clean and comfortable around our house."
    "So many people had asked me for advice that I decided to write a blog with entries relevant to domestic life on Talaam."
    "I was surprised at the huge response. It seemed everyone in the colony was reading my 'No Space like Home' blog."
    pete_c "[her_name], your jerky recipe's the best thing I ever tasted."
    ilian_c "It has a long shelf life, too, if properly sealed."
    naomi_c "Will you hold another canning class anytime soon? I'm afraid I had to miss the last one."
    her_c "Sure, let me see who else is interested and I can teach another class."
    nvl clear
    
    "I got a lot of e-mails with questions on preserving and cooking different kinds of foods, cleaning furniture, pest control."
    "Lots of people were struggling with these things, especially since we didn't have the luxury of just going to a store and buying a bottle of some new product every week."
    "It seems I would always have something to write about."
    $ skill_domestic += 10
    $ community_level += 10
    return

return
