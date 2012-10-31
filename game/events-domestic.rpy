# Afternoon Events
# Domestic

# Intro Event and the default
label domestic_0:
    "I did some extra cleaning and organizing, and put in some extra work for a great dinner."
    $ skill_domestic += 10

    return

# Cellar Event
# TODO: Right now this has an infinite loop -- why?
label domestic_1:
    show him normal at left
    him "It'll sure be nice when we have some fresh food to eat."
    show her normal at center
    her "I know; I'm so tired of MREs!"
    him "It won't take too long until the radishes, spinach, and maybe even carrots are ready."
    #show her worried at center
    her "We don't have a refrigerator..."
    him "No, I was thinking of digging a cellar, but I just haven't had time...preparing the fields has taken longer than I thought."
    menu:
        "The cellar...?"
        "I'll do it!":
            her "Don't worry about the cellar; I'll take care of it!"
            him "Whoa, whoa, that's a big job - why don't we work on it together?"
            "We dug and hauled out dirt and dug and hauled until finally we had a small cellar to store food in! We were exhausted, but it felt good to get it done together."
            $ loved += 5
            $ skill_domestic += 10

        "I'll surprise him...":
            her "We have time; don't worry about it yet."
            "I started digging after work, thinking I could get a lot dug before he came home, but..."
            him "Nice hole. Are you going to plant something in it?"
            her "No, it's going to be our cellar."
            him "Oh."
            her "..."
            him "Why don't we work on it together?"
            "We dug and hauled out dirt and dug and hauled until finally we had a small cellar to store food in! We were exhausted, but it felt good to get it done together."
            $ loved += 5
            $ skill_domestic += 10

        "I want to help, but...":
            her "Why don't you let me take care of the farm while you dig it?"
            him "Well...That could work. There's a lot of weeds that need pulling; I'll show you how to do the watering with the irrigation ditches I have set up."
            her "I can do that."
            him "You can even...you can take Lettie if you want to."
            #show her laughing at center
            her "Wow, you're trusting me with your favorite horse? I'm touched."
            him "I wouldn't trust anyone else."
            "I rode Lettie around, scouting the fields for weeds. I had never noticed how big the farm was before -- [his_name] takes care of a lot of plants!"
            "It took longer than I thought, and I ended up helping him haul out a lot of the dirt, but then we had our very own cellar!"
            $ skill_domestic += 10
            $ loved += 5

        "I don't want to help.":
            her "I'm sure you'll find the time."
    return


label domestic_2:
    show her normal
    her "I've got to do something about these windows. They are too bright when the sun is low. But it's not as if I can just buy some cloth..."
    if (skill_social >= 10):
        her "I'll ask around for everyone's scraps of cloth, and sew them together to make some curtains"
    else:
        her "I could probably sew these old dishtowels together to make some curtains..."
    her "There! That's better."
    $ skill_domestic += 10
    return

label domestic_3:
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
    $ skill_domestic += 10

    return

label domestic_4:
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
            $ have_goat = True
        "No, thanks.":
            her "(I don't think I have time to take care of goats right now!)"
            her "Thanks for offering, but I don't think we want to do that right now."
            "Thuc Nguyen" "I understand."
            "But [his_name] wasn't so understanding."
            him "Free goats? Why did you turn him down!"
            her "I don't know anything about goats! I have enough to do as it is!"
            her "Besides, goat milk tastes gross."
            menu:
                him "I would have appreciated you asking me about it first."
                "You're right.":
                    her "You're right, I'm sorry."
                    him "Sorry for yelling at you - it's not worth getting upset over."
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
    show him at left
    him "Here's some more radishes, love"
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
    elif (skill_social >= 20):
        her "I bet I could trade these with the Peron's for some eggs from their chickens..."
        "Sure enough, Natalia was delighted to have some fresh vegetables, and I made a souffle instead."
    else:
        "I sliced them really thin and spread them with cheese and some herbs from the garden."
        her "They hardly taste like radishes anymore...much better!"

    return

label domestic_6:

    return

label domestic_7:

    return

label domestic_8:
    return

label domestic_9:
    return

label domestic_master:
    return

return
