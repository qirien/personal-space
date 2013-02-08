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
                
    $ skill_creative += 10

    return

# Crochet something new using goat's hair?
label creative_3:
    scene bg farm_interior with fade
    "One of the villagers was able to spin yarn out of goat hair. I took a skein and promised I'd try to make something with it."
    "Luckily, I was able to borrow a crochet needle from the library. I looked up how to crochet on my computer pad, and started making a simple potholder."
    her "Oh no! Each row is just getting more and more narrow."
    "Luckily I figured out that I needed to add an extra stitch at the end of each row before I finished, but I ended up with an hourglass-shaped potholder."
    him "Wow, you made an abnormally-shaped potholder on your first try crocheting? I would have just stuck with something safe; you're really ambitious!"
    her "Yes, it's so it won't flop around in your hand as much when you go to pick something up!"
    $ skill_creative += 10
    return

# Woodworking - make vegetable crate/barrel or clothes drying rack out of local wood 
label creative_4:
    "Our harvests were staying fairly fresh in the cellar, but I needed a way to organize which vegetables were the oldest."
    "I wanted to make some crates out of wood, but I wasn't sure how I'd manage without nails."
    "I went to the storehouse to get the wood I needed."
    #TODO find a character to be the storehouse/workshop manager, or make one
    menu:
        "Notch the planks log-cabin style.":
            "I tried notching the planks to help them stay in place as I stacked them into a box shape. There were some wide gaps between planks, but luckily they weren't wide enough for the vegetables to fall out."
            $ community_level += 2
        "{i}Ask the store manager about how to put planks together without nails.{/i}" if (skill_social > 10):
            "The store manager told me about how he had been making pegs out of wood to help hold furniture together. Before I left, he gave me some pegs and we drilled holes in the right spots while I had access to the drill."
            "It was tricky to make it so I didn't pull up on the pegs when I lifted the crate, but with the store manager's help, I made something that would keep a few vegetables separate from the rest."
            $ community_level += 5
        "{i} Learn from a woodworking manual.{/i}" if skill_technical > 20:
            "I read up on carpentry techniques that didn't use metal. I found out that I could use wood pegs in the place of nails, or that I could cut the wood to fit together like a tight jigsaw puzzle."
            "I was up for a challenge. I made a design that would use pegs to hold planks together, but the puzzle-piece technique on the corners."
            "After I designed the crate, I took my plans to the workshop to use their equipment. The store manager was pretty impressed at my finished crate."   
            $ community_level += 5

    $ skill_creative += 10
    
    return

label creative_5:
    "[his_name] asked me if we had any rope to make a rope to get up into the loft of our barn and pull carts around. I told him I'd look at the supply center next time I went into town."
    her "Do you have any rope?"
    manager "It looks like they didn't send much along with us. I guess they thought we'd be making our own by now."
    if (has_grass == True):
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

# Re-cover space shuttle seats to make a couch?
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

# Make a documentary about the colony and send it to Earth
label creative_master:

    $ skill_creative += 10
    return
