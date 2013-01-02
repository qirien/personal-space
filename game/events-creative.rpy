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

    $ skill_creative += 10

    return

label creative_3:

    $ skill_creative += 10
    return

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
    else:
        "I tried to make rope out of my own hair but it didn't work very well, since I wasn't willing to chop off all my hair to make a tiny amount of rope. I tried using some hair from brushing Lettie, but I only had enough hair to make a short, thin rope."
        him "Oh, you made rope with horsehair? I think I've heard of that before. It won't be strong enough for a ladder, but we can make some reins out of it."
        her "Well, I'm glad we can use it for something."

    $ skill_creative += 10
    return

label creative_6:

    $ skill_creative += 10
    return

label creative_7:

    $ skill_creative += 10
    return

label creative_8:

    $ skill_creative += 10
    return

label creative_9:

    $ skill_creative += 10
    return

label creative_master:

    $ skill_creative += 10
    return
