# Afternoon Events
# Creative

# Intro Event and the default
label creative_0:
    "I worked on a quilt for our bedroom using scraps of fabric we didn't need. It was pretty tedious cutting out tiny squares of exactly the right size and sewing them together by hand, so I just worked on it a little at a time."
    $ skill_creative += 10

    return

# Weave Placemats
label creative_1:
    scene bg path with fade
    "On my way back from work, I found some tall, wide weeds that had grown very quickly. I wanted to work on some weaving, so I took some home and made two placemats with it."
    $ skill_creative += 10
    return

# Scarecrow
label creative_2:
    scene bg farm_interior with fade
    him "Those flying crab things are eating all the squash!"
    her "Ohhh, I hate those! I've never been pinched, but, still - something that flies should not be allowed to have claws."
    him "I've got to do something about them. I shoo them away when I'm there, but I can't be out there all the time."
    her "Hmmm, how about a scarecrow?"
    him "A scarecrow? I don't think they're instinctively scared of people; we just barely got here."
    her "We'll make it shaped like something they are scared of, then! Like those wolfslugs that hunt near the river."
    him "Do you think you could do that?"
    her "Let me give it a try. You could also experiment with different strong scents that they might not like, like coffee grounds or vinegar."
    "He placed some different scents near some of the plants, while I got to work on our 'scarecrow'."
    "I started with bunches of sticks for the body and legs, held together with twine.  Then I covered them with algae from a pond to give it that slimy look."
    "I rummaged through our trash pile and found some bottlecaps for eyes, and stuck in some old bones for teeth."
    her "What do you think?"
    him "I'm scared of that thing. The crabirds definitely will be."
    her "Oh, is that their name?"
    him "I'm sure they have a boring scientific name, but I'm calling them 'crabirds'."
    "We put the fake wolf slug near one section of squash plants - he had sprayed strong smells near some of the others."
    "The scarecrow seemed to work pretty well for a while, but then they figured out that it was fake and started nibbling on the squash again. We had to move it around every few days to try and fool them, so it was kind of a pain, but it was worth it when we finally got to eat the squash."

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
    her "Yes, I did that on purpose. It's so it won't flop around in your hand as much when you go to pick something up."
    $ skill_creative += 10
    return

# Woodworking - make vegetable crate/barrel or clothes drying rack out of local wood 
label creative_4:
    scene bg farm_interior with fade
    "Our harvests were staying fairly fresh in the cellar, but I needed a way to organize which vegetables were the oldest."
    "I wanted to make some crates out of wood, but I wasn't sure how I'd manage without nails."
    "I went to the storehouse to get the wood I needed."
    #scene bg storehouse with fade
#TODO Ilian Andrevski is the manager dude. Still need to go through other events and make sure it's the same, if I mentioned him.
    menu:
        "Notch the planks log-cabin style.":
            "I tried notching the planks to help them stay in place as I stacked them into a box shape. There were some wide gaps between planks, but luckily they weren't wide enough for the vegetables to fall out."
            $ community_level += 2
        "{i}Ask the storehouse manager, Ilian about how to put planks together without nails.{/i}" if (skill_social > 10):
            "Ilian told me about how he had been making pegs out of wood to help hold furniture together. Before I left, he gave me some pegs and we drilled holes in the right spots while I had access to the drill."
            "It was tricky to make it so I didn't pull up on the pegs when I lifted the crate, but with the Ilian's help, I made something that would keep a few vegetables separate from the rest."
            $ community_level += 5
        "{i} Learn from a woodworking manual.{/i}" if skill_technical > 20:
            "I read up on carpentry techniques that didn't use metal. I found out that I could use wood pegs in the place of nails, or that I could cut the wood to fit together like a tight jigsaw puzzle."
            "I was up for a challenge. I made a design that would use pegs to hold planks together, but the puzzle-piece technique on the corners."
            "After I designed the crate, I took my plans to the workshop to use their equipment. Ilian was pretty impressed at my finished crate."   
            $ community_level += 5
        "Forage nails from trash.":
            "I looked in the village trash heap, and I found a few nails in things people had thrown away. They didn't hold the wood together as tightly as I would have liked, but it was sturdy enough to hold some lightweight vegetables, anyway."
            $ community_level += 2
        "Ask [his_name] for help.":
            her "Hey, [his_nickname], do you have any ideas for how to make a crate out of these pieces of wood? We don't have any nails..."
            him "Any screws?"
            her "Nope. No nuts and bolts, either."
            him "Hmmm... how about lashing them together with some string?"
            her "Well, I have that yarn I was using to practice crocheting with. Maybe that would work?"
            him "Sure, let's try it."
            "We worked together to lash the slats together and made some serviceable crates. They wouldn't hold up well to transporting vegetables, but that was okay, since they were just going to sit in our cellar."
            $ community_level += 2
            $ loved += 2

    $ skill_creative += 10
    
    return

label creative_5:
    #scene bg storehouse with fade
    "[his_name] asked me if we had any rope to make a rope to get up into the loft of our barn and pull carts around. I told him I'd look at the supply center next time I went into town."
    her "Do you have any rope?"
    ilian "It looks like they didn't send much along with us. I guess they thought we'd be making our own by now."
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
#month 5 is what to do with trash, so I'm assuming this will have to come after it (though it may be several months after it)
    #scene bg storehouse with fade
    "Ever since the push to recycle or compost all our trash, I had been trying to think of other uses for shuttle parts."
    "I went down to the storehouse to ask about how the shuttle parts were being distrubuted. I thought maybe I could make a sofa out of them"
    ilian "There was a seat for everyone on the shuttle, and as far as I'm concerned, that seat is still yours."
    her "Great! I'll come back later with [his_name] to pick up the seats on our wagon."
    "That night I told [his_name] about my plan."
    him "You want a sofa?"
    menu:
        "Yeah.":
            her "Yeah, I kind of miss have a sofa. Don't you?"
            him "I do sometimes miss it. Would it have reclining seats?"
            her "Well, considering it will be two bed-seats from the shuttle, yes."
            him "That means it could be a sofabed too."
            her "Our bed isn't good enough?"
            him "Well, I'm not sure which I'd prefer. But it will be nice to have an extra bed in case someone else is stranded here."

        "It would let us have somewhere to sit other than our bed when we watch movies.":
            her "Watching movies from our kitchen chairs is great, but wouldn't it be nice if we had somewhere to snuggle up?"
            him "We don't watch that many movies."
            her "It doesn't have to be movies. When you're planning the crops, you might want to read somewhere comfortable."
            him "Okay, okay. I just want to make sure we'll actually use a piece of furniture before bringing it into our tiny dwelling."

        "It would increase our seating capacity.":
            her "When we have guests over, wouldn't it be nice if we could all sit inside?"
            him "When the weather is bad, I think people will want to be visiting, and otherwise we can sit outside."
            her "But sometimes it might just be dark or cold, not necessarily raining."
            him "You have a point. Plus it would be nice for reading on."
            her "Then let's go!"
            "[his_name] brought the seats back with Lettie and our wagon. The next day, I set to work on making a loveseat."
            "I wanted to upolster it with some fabric. I ended up weaving together long grasses into patches, which I sewed together with some goat-hair yarn. "
            "I used more grass as extra padding between the seats. It ended up being a bit scratchy, but better than nothing."

    $ skill_creative += 10
    return

# Photography
label creative_7:
    scene bg sunset with fade
    "I hadn't done any photography in a long time, but the way the light was coming through the clouds really inspired me."
    "As I set up shots- some simple landscapes, others focusing on an alien plant or insect with the clouds in the background- I felt awed. Here was this entire planet full of wonders, and only the few of us who lived here got to experience it."
    "I decided to send some of my pictures to magazines on Earth; maybe they would be interested in doing an article on Talam and would want to use them. I just wanted to show everyone on Earth what a beautiful planet we had."
    boss "So, you want special permission to exceed your alloted Earth-upload bandwidth to send photographs?"
    her "Yes, they need to be large so that they will look good in print. Is that okay?"
    boss "I think that is a worthy use of our resources. The pictures look great, [her_name], I hope people on Earth get to see them."
    "It would take years for the photos to reach Earth, and even more years before I heard anything back, but I felt like it was worth it, anyway. I felt like an ancient explorer like Magellan, writing in his journal, not knowing if anyone from the homeland would ever read it..."
    $ skill_creative += 10
    return

# Make some dishes out of local clay, fire them
label creative_8:
    scene bg pond with fade
    "A rainy night made the banks of the river swell. When I was checking to make sure our plants were okay, I noticed that some of the upturned banks had a clay-like texture."
    "I did a little digging on the other side of the river, where I found some clay."
    "It had lots of rocks and leaves in it, so I dried it and broke it into pieces, which were easier to sort from the leaves. Then I let it sit in a bucket of water."
    #source: http://www.kitcornellpottery.com/teaching/clay.html
    "The next day, I put the clay through a piece of fabric to further purify it."
    "I didn't have a potter's wheel, so I tried to make a cup without one."
    him "This clay looks great. If you want, I could turn the wagon over, and you could use one of the wheels while I spin it."
    her "Thanks, that would help a lot."
    "Together we made a few more cups and water jug. We didn't have a kiln, so we went down to the research station to see if they had an oven we could use."
    lily "I'll check your clay for toxins, and then if it's safe I'll bake your pottery. Our oven doesn't get as hot as some kilns, but it's better than not firing it at all."
    "I came by later and picked up the pottery, which Lily said was safe to drink from."
    him "Wow, our own water jug! We're getting fancy around here."
    her "If I ever figure out how to make a glaze, I could paint them too."
    him "I think they look great as is."
    her "I'm proud of our work too."
    $ skill_creative += 10
    return

#build a bridge out of braided grass rope
#source: http://www.pbs.org/wgbh/nova/education/ancient/grass-bridge.html
label creative_9:
    "It was a nice day out and I went for a walk. I wanted to cross the river and continue walking, but I didn't want to get wet."
    "I know a few other people said they would like to get more familiar with the land past the river, but they didn't want to go to the trouble of getting their boats out just for a walk."
    "I knew that some ancient Earth civilizations used grass to form rope bridges, and I wondered if I could do the same."
    "I found some dry grasses near the mountain and took some home with me, where I started twisting them into rope."
    "I tried to find the part in the documentary that showed how they incoporated new strands of grass, but they didn't show it very closely. I had to kind of twist them in on my own."
    him "Have you finally found a way to make rope?"
    her "I hope so. I'd like to make a bridge over the river that anyone can access in any weather."
    him "Can you spare some rope for me?"
    her "Let me teach you how; it's not too hard."
    "We spent the evening winding grasses into rope."
    "The next day I walked along the river bank. I was hoping to find the narrowest place to build my bridge. I also had to find a place where a suspension bridge would fit in with the geography."
    "I found the perfect spot just as I was about to give up and go home. Near the Engel's, the river split a large knoll into two. Water had worn away the dirt into smooth mounds on either side of the river."
    if (skill_social >= 30) or (skill_knowledge >= 30):
        "I talked to the Engels about building the bridge and they were excited to help. Helen especially seemed grateful for a chore she could do at home, and Sven said he'd try to spin rope during downtime at the library."
        "After a few days we had enough rope to start making stronger rope."
    else:     
        if (loved >= 30):
            "[his_name] helped me twist tons of rope every evening."
        else:
            "I spent a lot of time at home making the rope."
        "After a few days I had enough rope to start making stronger rope."
    "I twisted and tied the large rope around a tree. [his_name] helped me get it to the other side using a small rope to guide it."
    "We tied two more ropes higher up for hand rails. At first the hand rails were too close together, so we had to tie them to some of the tree's branches."
    "The next day, I tied the handrails to the main rope using small ropes. At first it was a little scary to be on the bridge before it was done, but it wasn't very high up."
    "When I crossed the finished bridge, I felt a thrill of accomplishment."
    
    $ skill_creative += 10
    return

# Make a documentary about the colony and send it to Earth
label creative_master:

    $ skill_creative += 10
    return
