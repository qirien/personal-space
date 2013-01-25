# Afternoon Events
# Domestic

# Intro Event and the default
label domestic_0:
    scene bg farm_interior with fade
    "I did some extra cleaning and organizing, and put in some extra work for a great dinner."
    $ skill_domestic += 10

    return

# Laundry by hand is tough?
label domestic_1:
    scene bg laundry with fade
    show her normal
    her "Washing these clothes by hand is taking forever. I wonder how I could speed it up."
    "Currently you're agitating the clothes in soapy water to clean them."
    menu:
        "Leave the clothes soaking while you finish doing the dishes.":
                her "Maybe I just need to let the soap do my work for me."
                "Twenty minutes later..."
                her "That helped a bit! I should leave clothes soaking more often."
                $relaxed +=5

        "Just keep doing it the same way.":
                her "Well, I guess there's no getting around hard work."
        
    $ skill_domestic += 10
    return

# make curtains for windows
label domestic_2:
    scene bg farm_interior with fade
    show her normal
    her "I've got to do something about these windows. They are too bright when the sun is low. But it's not as if I can just buy some cloth..."
    if (skill_social >= 10):
        her "I'll ask around for everyone's scraps of cloth, and sew them together to make some curtains"
    else:
        her "I could probably sew these old dishtowels together to make some curtains..."
    her "There! That's better."
    $ skill_domestic += 10
    return

# fence to keep out herb garden pests
label domestic_3:
    scene bg fields with fade
    show her normal at center
    "I planted an herb garden when we first arrived, and the plants are just starting to get big enough for me to use. I think I'll make some tea..."
    #show her worried at center
    her "Something's been nibbling at my herbs...!"
    "I peeked out the window every time I passed, trying to see what it was. Finally, I saw a strange small animal that looked kind of like a cross between a frog and a rabbit. I chased it away, but what about next time?"
    her "I know!  I'll make a fence!"
    "I gathered some sticks from some of the local plants, and tied them together with vines. When I tried to pound in the corners, the sticks broke in the hard dirt."
    #show her angry at center
    "I took a break for a snack and thought about it. I decided to try wetting the dirt first.  Then I was able to pound in the corners and finish my fence."
    #show her happy
    her "Whew! It's done!"
    "I watched, and sure enough, my fence kept out the creature.  Good to know my herbs were safe."
    $ skill_domestic += 10

    return

# Who wants a goat?
label domestic_4:
    scene bg farm_exterior with fade
    "Thuc Nguyen" "Hello? Anybody home?"
    her "Thuc! Good to see you! How are the baby goats?"
    "Thuc Nguyen" "Doing well!  There's so many of them, though, I don't think we'll have room for them all!"
    her "Are they hard to take care of?"
    "Thuc Nguyen" "Not at all! They can eat almost any plants, and are pretty hardy. Are you interested in taking care of some goats?"
    menu:
        "Goats...?"
        "Yes!":
            her "I would love to! But I've never taken care of goats before, so would you help me if I run into trouble?"
            "Thuc Nguyen" "Of course! Why don't you let me know when you have a spot fenced off for them? They are able to eat the native vegetation here, so you could even use them to help clear space for fields."
            "[his_name] and I talked it over, and we decided to fence in a part of the wild area not too far from the house for the goats."
            "There were three of them, two males and a female, and I became remarkably attached to them. [his_name] used the manure for fertilizer, and they worked hard eating the strange plants from this planet."
            $ skill_domestic += 10
            $ community_level += 5
            $ have_goat = True
        "No, thanks.":
            her "(I don't think I have time to take care of goats right now!)"
            her "Thanks for offering, but I don't think we want to do that right now."
            "Thuc Nguyen" "I understand."
            "But [his_name] wasn't so understanding."
            scene bg farm_interior with fade
            show her normal at left
            #show him angry at center
            show him normal at center 
            him "Free goats? Why did you turn him down!"
            her "I don't know anything about goats! I have enough to do as it is!"
            her "Besides, goat milk tastes gross."
            menu:
                him "I would have appreciated you asking me about it first."
                "You're right.":
                    her "You're right, I'm sorry."
                    him "Sorry for yelling at you - it's not worth getting upset over."
                    menu:
                        "I hate it when we fight":
                            her "I hate it when we fight."
                            "He came over and held me close."
                            him "I'm sorry, [her_name]. You do a lot around here that I don't always see or appreciate."
                            her "I know you work hard every day, too. I don't want to ask you to do any more than you already do."
                            "We didn't need to say anything more."
                        "I have to get out of here":
                            her "I'm going out."
                            "I went on a walk until I had cooled off. When I came back, we didn't talk about it anymore, and eventually we were back to normal."
                        "(Give him a hug)":
                            "I hugged him. It took a few seconds for him to hug me back, but then I knew that everything would be all right."
                            
                "What's the point?":
                    her "What would be the point of asking you? You don't have time to take care of goats, either."
                    him "The point is that we're a team. We need to make big decisions like this as a team."
                    her "I didn't think it was even worth considering."
                    him "Well, I do. I guess now you know for next time."
                    her "(Yeah, next time I won't even tell you about it.)"
                    $ loved -= 10
                "Forget it.":
                    her "It's not worth fighting over; just forget about it."
                    him "Yeah, I can think of much better things to fight over."
                    her "Such as?"
                    him "Who's going to get the last strawberry."
                    her "Ohhh! I was saving that for something special!"
                    him "I was saving it for something special, too."
                    her "Like what?"
                    him "Like you."
            
    return

label domestic_5:
    scene bg farm_interior with fade
    show him at left
    him "Here's some more radishes from the fields, love."
    show her at center
    her "Thanks, they look great!"
    hide him
    #show her worried at center
    her "(More radishes? I don't know what else to do with these besides salad...We can't waste any food, so I better think of something!)"
    if (skill_knowledge >= 20):
        "I decided to do some research about radishes..."
        #show her excited at center
        her "Radish pickles?! That sounds fun!"
        "They had plenty of vinegar and salt at the storehouse, and I used some of the herbs and spices from the garden to make a few batches of pickled radishes."
        $ skill_knowledge += 5
    elif (skill_social >= 20):
        her "I bet I could trade these with the Peron's for some eggs from their chickens..."
        "Sure enough, Natalia was delighted to have some fresh vegetables, and I made a souffle instead."
        $ community_level += 5
        $ skill_social += 5
    elif have_goat:
        "I sliced them really thin and spread them with goat cheese and some herbs from the garden."
        her "They hardly taste like radishes anymore...much better!"
    else:
        "I couldn't think of anything else, so I cut them into pretty rose shapes and drizzled oil and vinegar on them. They still tasted like radishes, but at least it was something a little different."

    $ skill_domestic += 10
    return

label domestic_6:
    "Domestic 6"
    $ skill_domestic += 10
    return

label domestic_7:
    "Domestic 7"
    $ skill_domestic += 10
    return

label domestic_8:
    scene bg farm_interior with fade
    "One day, I came home from work to find a dead monster on the kitchen table."
    #show her surprised at center
    show her normal at center
    her "What is THAT?!"
    show him normal at left
    him "There was a herd of them eating some of the vegetables on the north side. I was watching them, because they're so strange, you know, and I just thought they looked really tasty."
    her "Tasty?! They look like fish with long legs!"
    him "It's been a really long time since we had any fresh meat! They made me think of salmon... so I lassoed one."
    her "What happened next?"
    him "Well, it started to run. Luckily I was on Lettie at the time, so she started running, too. We had quite a chase through the woods before the creature tired out."
    him "When it finally slowed down, I jumped off and attacked it."
    menu:
        her "That's..."
        "Barbaric":
            her "Barbaric! What did that monster ever to do you?"
            him "Ate my plants, that's what. Well, you don't have to have any; I guess I'll just cook it myself."
            her "Yeah, please get that thing out of here."
            "He roasted it outside over a fire. He didn't tell me how it tasted, which was fine - I didn't want to know, anyway."
            $loved -= 10
            return
        "Awesome":
            her "That's awesome! You're like my very own mountain man."
            $loved += 10
        "Strange":
            her "That's...not something I'm used to. Can you really eat it?"
            him "The scientists here haven't detected anything toxic or unusual in the animal life here - I think as long as we cook it well and don't eat the organs it should be fine."
    
    her "This is going to be a lot of meat..."
    him "Yes, any ideas what we should do with it?"
    
    menu:
        her "How about..."
        "Giving it away":
            her "We could give some away to our neighbors."
            him "Yeah, there's plenty here, if they'd want some."
            if skill_technical >= 20:
                her "I'll ask around."
                "I got on the radio and asked around town -- turns out a lot of people felt like [his_name] and thought some fresh meat would be delicious, even if it was alien meat."
                "It felt good to share with our neighbors."
                $ skill_social += 5
                $ community_level += 5
            elif skill_social >= 20:
                "I know just who would want some."
                "The Blair family had seven kids and I knew some of their crops hadn't made it. There were plenty of rations in the storehouse, so they weren't starving or anything, but I thought they'd like some real food."
                "When I took it to them, they didn't care that it came from an alien monster; they just thanked me and gave me some eggs from their chickens to take home with me."
                $ community_level += 5
                $ skill_social += 5
        "Drying it":
            her "We could dehydrate it and make jerky."
            him "Do you know how to do that?"
            her "Theoretically...we'll need to smoke and salt it...We can adapt a recipe for fish jerky, I think."
            him "OK, I'll skin and cut up this sucker while you're figuring that out."
            if (skill_technical >= 40):
                "I rigged up a smoker with some old scrap metal and put some screens above it for the meat"
                $ skill_technical += 5
            else:
                "We soaked the meat in brine, and then I setup some racks where the fish could dry in the sun and wind."
                her "If it rains we'll need to bring everything inside..."
                him "Let's hope it doesn't rain, then!"
                her "It took several days longer to dry than I had planned, and we did have to bring it the house once, but when we were done we had some jerky that would last a long time, and actually tasted pretty good."
        "Composting it":
            her "Should we just compost what we can't eat?"
            him "I guess..."
            "We cooked and ate quite a bit, but we didn't have a way to freeze or refrigerate so we just tossed the leftovers into the compost pile. Probably some scavenging animals will enjoy a nice feast..."

        "Having a meat party":
            her "Let's cook it all up, invite our friends over, and have a meat party!"
            him "All right! We can try cooking it several different ways and see what tastes best!"
            her "A meat-tasting party!"
            if skill_social >= 90:
                "We invited the whole town for a giant potluck celebration. People brought salads and fresh bread and rice and spicy beans and there was even a little fruit for everyone."
                "Our little colony didn't have many celebrations; even though there wasn't really enough meat for everyone to have much, since we all brought something it worked out. We felt like a real community."
                $ skill_social += 5
                $ community_level += 10
            elif skill_social >=30:
                "We invited a large group of friends and we ate almost all of it. I think they appreciated that we shared it with them. It felt good to help out our friends."
                $ community_level += 5
            else:
                "We invited a few friends over and we ate and ate and ate as much as we could. I wondered if we might get sick, but other than feeling full all the next day, nothing bad happened."
            
    $ skill_domestic += 10
    return

label domestic_9:
    "Domestic 9"
    return

label domestic_master:
    "I AM A DOMESTIC GODDESS!!!"
    return

return
