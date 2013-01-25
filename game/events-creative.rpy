# Afternoon Events
# Creative

# Intro Event and the default
label creative_0:
    "I worked on a quilt for our bedroom."
    $ skill_creative += 10

    return

label creative_1:
    "On my way back from work, I found some tall, wide weeds that had grown very quickly. I wanted to work on some weaving, so I took some home and made two placemats with it."
    $ skill_creative += 10
    return

label creative_2:
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
                
    $ skill_creative += 10

    return

# Crochet something new using goat's hair?
label creative_3:
    "One of the villagers was able to spin yarn out of goat hair. I took a skein and promised I'd try to make something with it."
    "Luckily, I was able to borrow a crochet needle from the library. I looked up how to crochet on my computer pad, and started making a simple potholder."
    her "Oh no! Each row is just getting more and more narrow."
    "Luckily I figured out that I needed to add an extra stitch at the end of each row before I finished, but I ended up with an hourglass-shaped potholder."
    him "Wow, you made an abnormally-shaped potholder on your first try crocheting? I would have just stuck with something safe, you're really ambitious!"
    her "Yes, it's so it won't flop around in your hand as much when you go to pick something up!"
    $ skill_creative += 10
    return

# Woodworking - make vegetable crate/barrel or clothes drying rack out of local wood 
label creative_4:

    $ skill_creative += 10
    return

label creative_5:
    "[his_name] asked me if we had any rope to make a rope to get up into the loft of our barn and pull carts around. I told him I'd look at the supply center next time I went into town."
    her "Do you have any rope?"
    manager "It looks like they didn't send much along with us. I guess they thought we'd be making our own by now."
    if (has_grass = True):
        "I took a look at the long grasses I found and pulled it apart to get fibers, which I twisted into string. Rope is basically a bunch of strings, right? So I twisted the strings together to make a thin rope. It wasn't very long, but I made enough of them to pull a wagon with."
        him "This is great! It's amazing what you can make with the right resources."
        her "Yeah! I can think of a few things I'd like to use it for too, like giving some of our livestock a leash or making a backpack."
        him "Oh, are you going to make a leash for me too?"
        her "Only if you want one."
        $ loved += 2
    else:
        "I tried to make rope out of my own hair but it didn't work very well, since I wasn't willing to chop off all my hair to make a tiny amount of rope. I tried using some hair from brushing Lettie, but I only had enough hair to make a short, thin rope."
        him "Oh, you made rope with horsehair? I think I've heard of that before. It won't be strong enough for a ladder, but we can make some reins out of it."
        her "Well, I'm glad we can use it for something."

    $ skill_creative += 10
    return

# Patch his favorite jeans with fabric from space shuttle seats
label creative_6:

    $ skill_creative += 10
    return

# Play some music (on the recorder?)
label creative_7:

    $ skill_creative += 10
    return

# Make some dishes out of local clay, fire them
label creative_8:

    $ skill_creative += 10
    return

label creative_9:

    $ skill_creative += 10
    return

label creative_master:

    $ skill_creative += 10
    return
