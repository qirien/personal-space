# Afternoon Events
# Creative

# Default Event
label creative_def:
    scene bg farm_interior with fade
    "I worked on a quilt for our bedroom using scraps of fabric we didn't need. It was pretty tedious cutting out tiny squares of exactly the right size and sewing them together by hand, so I just worked on it a little at a time."
    $ skill_creative += 10

# Intro Event
label creative_0:
    scene bg farm_interior with fade
    "Looking around our tiny, bare house, we had only the barest necessities. A towel, sturdy blankets and clothing, a plate, spork and knife for each of us, and a rough table and two convertible seats from the shuttle that also doubled as our bed."
    "It was enough to survive on, but I wanted to do more than just survive."
    "But if we wanted more, we would have to make things ourselves."

    "I wanted to do something to make our one room pre-fab house seem unique."
    show her serious at right with dissolve
    "So I took a knife and carved our names in calligraphy above the door."
    "I had so much fun that I started carving designs on the wall posts near the ceiling. [his_name] came in and watched me for a while."
    show him normal at center with moveinleft
    him serious "Hmm, this is a nice house, here. Hand-carved moldings, even! I wonder who it belongs to?"
    him happy "Oh, look, it's written right here above the door, [his_name] and [her_name]. One of them must be very creative."
    her flirting "I hear the other one's hard-working and handsome."
    him flirting "Really? We should go meet them sometime."

    "I was a little worried he wouldn't like it, but I guess he doesn't mind."
    "Now it felt like {b}our{/b} house."

    $ skill_creative += 10

    return

# Scarecrow
label creative_1:
    scene bg farm_interior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    him angry "Those flying crab things are eating all the squash!"
    her annoyed "Ohhh, I hate those! I've never been pinched, but, still - something that flies should not be allowed to have claws."
    him annoyed "I've got to do something about them. I shoo them away when I'm there, but I can't be out there all the time."
    her surprised "Hmmm, how about a scarecrow?"
    him surprised "A scarecrow? I don't think they're instinctively scared of people; we just barely got here."
    her normal "We'll make it shaped like something they are scared of, then! Like those wolfslugs that hunt near the river."
    him normal "Do you think you could do that?"
    scene bg fields with fade
    "He placed some different scents near some of the plants, while I got to work on our 'scarecrow'."
    "I started with bunches of sticks for the body and legs, held together with twine.  Then I covered them with algae from a pond to give it that slimy look."
    "I rummaged through our trash pile and found some bottlecaps for eyes, and stuck in some old bones for teeth."
    show her concerned at midleft
    show him serious at midright
    her "What do you think?"
    him normal "I'm scared of that thing. The crabirds definitely will be."
    her surprised "Oh, is that their name?"
    him normal "I'm sure they have a boring scientific name, but I'm calling them 'crabirds'."
    hide him
    hide her
    with dissolve
    "We put the fake wolf slug near one section of squash plants - he had sprayed strong smells near some of the others."
    "The scarecrow seemed to work pretty well for a while, but then they figured out that it was fake and started nibbling on the squash again. We had to move it around every few days to try and fool them, so it was kind of a pain, but it was worth it when we finally got to eat the squash."

    $ skill_creative += 10

    return

# Crochet something new using goat's hair?
label creative_2:
    scene bg farm_interior with fade
    "One of the villagers was able to spin yarn out of goat hair. I took a skein and promised I'd try to make something with it."
    "Luckily, I was able to borrow a crochet needle from the library. I looked up how to crochet on my computer pad, and started making a simple potholder."
    show her surprised at midright
    her "Oh no! Each row is just getting more and more narrow."
    "Luckily I figured out that I needed to add an extra stitch at the end of each row before I finished, but I ended up with an hourglass-shaped potholder."
    show him normal at midleft
    him flirting "Wow, you made an abnormally-shaped potholder on your first try crocheting? I would have just stuck with something boring like a square. You're really ambitious!"
    her annoyed "Yes, I did that on purpose. It's so it won't flop around in your hand as much when you go to pick something up."
    him normal "It'll work just fine, [her_nickname]."
    show her normal
    "My next attempt turned out much more even. But I kept that first one around anyway - for some reason I liked it."
    $ skill_creative += 10
    return

# Woodworking - make vegetable crate/barrel or clothes drying rack out of local wood 
label creative_3:
    scene bg farm_interior with fade
    "Our harvests were staying fairly fresh in the cellar, but I needed a way to organize which vegetables were the oldest."
    "I wanted to make some crates out of wood, but I wasn't sure how I'd manage without nails."
    "I got some wood from the storehouse, and tried to figure out how to put it together."
    menu:
        "What should I do?"
        "Notch the planks log-cabin style.":
            "I tried notching the planks to help them stay in place as I stacked them into a box shape. There were some wide gaps between planks, but luckily they weren't wide enough for the vegetables to fall out."
            $ community_level += 2
        "{i}Ask around for ideas.{/i}" if (skill_social > 10):
            scene bg storehouse with fade
            "I asked the storehouse manager, Ilian, if he had any ideas."
            "He told me about how he had been making pegs out of wood to help hold furniture together. Before I left, he gave me some pegs and we drilled holes in the right spots while I had access to the drill."
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
            show him at midright with dissolve
            show her at midleft with moveinleft
            her surprised "Hey, [his_nickname], do you have any ideas for how to make a crate out of these pieces of wood? We don't have any nails..."
            him serious "Any screws?"
            her serious "Nope. No nuts and bolts, either."
            him surprised "Hmmm... how about lashing them together with some string?"
            her normal "Well, I have that yarn I was using to practice crocheting with. Maybe that would work?"
            him normal "Sure, let's try it."
            "We worked together to lash the slats together and made some serviceable crates. They wouldn't hold up well to transporting vegetables, but that was okay, since they were just going to sit in our cellar."
            $ community_level += 2
            $ loved += 2

    $ skill_creative += 10
    
    return

# Make rope
label creative_4:
    scene bg farm_interior with fade
    "[his_name] asked me if we had any rope to make a rope to get up into the loft of our barn and pull carts around. I told him I'd look at the supply center next time I went into town."
    scene bg storehouse with fade
    show ilian at midright with dissolve
    show her normal at midleft
    with moveinleft
    her surprised "Do you have any rope?"
    ilian "It looks like they didn't send much along with us. I guess they thought we'd be making our own by now."
    her normal "So you have some?"
    ilian "Yes, but it's only for approved projects."
    her annoyed "(I don't want to go through that red tape unless I have to!)"
    her concerned "I guess I'll figure something else out..."

    scene bg farm_interior with fade
    if (has_grass == True):
        "I took a look at the long grasses I found earlier and pulled it apart to get fibers, which I twisted into string. Rope is basically a bunch of strings, right? So I twisted the strings together to make a thin rope. It wasn't very long, but I made enough of them to pull a wagon with."
        show him normal at midright
        show her normal at midleft
        with dissolve
        him happy "This is great! It's amazing what you can make with the right resources."
        her normal "Yeah! I can think of a few things I'd like to use it for too, like giving some of our livestock a leash or making a backpack."
        him flirting "Oh, are you going to make a leash for me too?"
        her flirting "Only if you want one."
        $ loved += 2
    else:
        "I tried to make rope out of my own hair but it didn't work very well, since I wasn't willing to chop off all my hair to make a tiny amount of rope. I tried using some hair from brushing Lettie, but I only had enough hair to make a short, thin rope."
        show him normal at midright
        show her normal at midleft
        with dissolve
        him surprised "Oh, you made rope with horsehair? I think I've heard of that before. It won't be strong enough for a ladder, but we can make some reins out of it."
        her concerned "Well, I'm glad we can use it for something."

    $ skill_creative += 10
    return

# Re-cover space shuttle seats to make a couch?
label creative_5:
#month 5 is what to do with trash, so I'm assuming this will have to come after it (though it may be several months after it)
    scene bg storehouse with fade
    "Ever since the push to recycle or compost all our trash, I had been trying to think of other uses for shuttle parts."
    "I went down to the storehouse to ask about how the shuttle parts were being distrubuted. I thought maybe I could make a sofa out of them."
    show ilian at midright with dissolve
    show her normal at midleft with moveinleft
    ilian "We already gave you your seat for your bed... I don't have that many extras!"
    her happy "So there are extras?"
    ilian "... yes. But there's not enough for every family to have an extra, so we've been keeping them here."
    menu:
        "What should I say?"
        "I'll make one for you, too.":
            her surprised "What if I make one for you and Sara, too?"
            ilian "Are you trying to bribe me?!"
            her normal "Of course not! We'd just be helping each other out. Isn't that what we're supposed to do to get along as a colony?"
            ilian "I guess it's kind of a waste for them to just be sitting there in storage..."
            her happy "Exactly! I'll come back later with [his_name] to pick up the seats on our wagon."

        "No one else has asked for them, right?":
            her serious "No one else has come asking for extra seats, right?"
            ilian "No, no one else has."
            her "So, I'm probably the one in the whole colony who cares the most about them, and giving them to me would be the most efficient."
            ilian "I guess it's kind of a waste for them to just be sitting there in storage..."
            her happy "Exactly! I'll come back later with [his_name] to pick up the seats on our wagon."

        "Why not have a lottery to decide who gets them?":
            her serious "Maybe you could post a message asking who wants them, and have a lottery to distribute them? Some people probably don't even want them cluttering up their house."
            ilian "All right, I'll do that."
            "There ended up being enough for everyone that wanted one."

    scene bg farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    "That night I told [his_name] about my plan."
    him surprised "You want a sofa? Do we really have room for that?"
    menu:
        "What should I say?"
        "Yeah.":
            her concerned "Yeah, I kind of miss have a sofa. Don't you?"
            him normal "I do sometimes miss it. Would it have reclining seats?"
            her normal "Well, considering it will be two bed-seats from the shuttle, yes."
            him surprised "That means it could be a sofabed too."
            her flirting "Our bed isn't good enough?"
            him normal "Well, I'm not sure which I'd prefer. But it will be nice to have an extra bed in case someone else is stranded here."

        "We could sit on it to watch movies.":
            her normal "Watching movies on our kitchen chairs is great, but wouldn't it be nice if we had somewhere to snuggle up?"
            him annoyed "We don't watch that many movies. Besides, we can just watch them in bed if want to do that."
            her serious "It doesn't have to be movies. When you're planning the crops, you might want to read somewhere comfortable."
            him normal "Okay, okay. I just want to make sure we'll actually use a piece of furniture before bringing it into our tiny dwelling."

        "It would increase our seating capacity.":
            her normal "When we have guests over, wouldn't it be nice if we could all sit inside?"
            him annoyed "When the weather is bad, I think people will want to be visiting, and otherwise we can sit outside."
            her normal "But sometimes it might just be dark or cold, not necessarily raining."
            him normal "You have a point. Plus it would be nice for reading on."

    her happy "Then let's go!"
    scene black with fade
    "[his_name] brought the seats back with Lettie and our wagon. The next day, I set to work on making a loveseat."
    "I wanted to upholster it with some fabric. I ended up weaving together long grasses into patches, which I sewed together with some goat-hair yarn. "
    "I used more grass as extra padding between the seats. It ended up being a bit scratchy, but better than nothing."
    "A sofa was a little thing, but it made our little cabin seem so much more homey."

    $ skill_creative += 10
    return

# Photography
label creative_6:
    scene bg sunset with fade
    "I hadn't done any photography in a long time, but the way the light was coming through the clouds really inspired me."
    "As I set up shots- some simple landscapes, others focusing on an alien plant or insect with the clouds in the background- I felt awed. Here was this entire planet full of wonders, and only the few of us who lived here got to experience it."
    "I decided to send some of my pictures to magazines on Earth; maybe they would be interested in doing an article on Talaam and would want to use them. I just wanted to show everyone on Earth what a beautiful planet we had."
    scene bg community_center with fade
    show pavel at midright, behind her with dissolve
    show her normal at midleft with moveinleft
    boss "So, you want special permission to exceed your allotted Earth-upload bandwidth to send photographs?"
    her "Yes, they need to be large so that they will look good in print. Is that okay?"
    boss "I think that is a worthy use of our resources. The pictures look great, [her_name], I hope people on Earth get to see them."
    "It would take years for the photos to reach Earth, and even more years before I heard anything back, but I felt like it was worth it, anyway. I felt like an ancient explorer like Magellan, writing in his journal, not knowing if anyone from the homeland would ever read it..."
    $ skill_creative += 10
    return

# Make some dishes out of local clay, fire them
label creative_7:
    scene bg pond with fade
    "A rainy night made the banks of the river swell. When I was checking to make sure our plants were okay, I noticed that some of the upturned soil had a clay-like texture."
    "I did a little digging on the other side of the river, where I found some clay."
    "It had lots of rocks and leaves in it, so I dried it and broke it into pieces, which were easier to sort from the leaves. Then I let it sit in a bucket of water."

    scene bg farm_exterior with fade
    "The next day, I put the clay through a piece of fabric to further purify it."
    "I didn't have a potter's wheel, so I tried to make a cup without one."
    show her normal at midright with dissolve
    show him normal at midleft with moveinleft
    him happy "This clay looks great. If you want, I could turn the wagon over, and you could use one of the wheels while I spin it."
    her normal "Thanks, that would help a lot."
    "Together we made a few more cups and water jug. We didn't have a kiln, so we went down to the research station to see if they had an oven we could use."
    scene bg lab with fade
    show lily at midright with dissolve
    show him normal at quarterleft
    show her normal at midleft
    with moveinleft
    lily "I'll check your clay for toxins, and then if it's safe I'll bake your pottery. Our oven doesn't get as hot as some kilns, but it's better than not firing it at all."
    "I came by later and picked up the pottery, which Lily said was safe to drink from."
    hide lily with moveoutright
    him happy "Wow, our own water jug! We're getting fancy around here."
    her normal "If I ever figure out how to make a glaze, I could paint them too."
    him normal "I think they look great as is."
    her happy "I'm proud of our work too."
    $ skill_creative += 10
    return

#build a bridge out of braided grass rope
label creative_8:
    scene bg pond with fade
    "It was a nice day out and I went for a walk. I wanted to cross the river and continue walking, but I didn't want to get wet."
    "I know a few other people said they would like to get more familiar with the land past the river, but they didn't want to go to the trouble of getting their boats out just for a walk."
    "Since I already had some experience making rope, I thought I could give it a try."
    "I found some dry grasses near the mountain and took some home with me, where I started twisting them into rope."
    scene bg farm_interior with fade
    "I tried to find the part in the documentary that showed how they incoporated new strands of grass, but they didn't show it very closely. I had to kind of twist them in on my own."
    show her normal at midright
    show him normal at midleft
    with dissolve
    him surprised "Have you finally found a way to make rope?"
    her normal "I hope so. I'd like to make a bridge over the river that anyone can access in any weather."
    him normal "Can you spare some rope for me?"
    her happy "Let me teach you how; it's not too hard."
    "We spent the evening winding grasses into rope."
    scene bg pond with fade
    "The next day I walked along the river bank. I was hoping to find the narrowest place to build my bridge. I also had to find a place where a suspension bridge would fit in with the geography."
    "I found the perfect spot just as I was about to give up and go home. Near the Engel's, the river split a large knoll into two. Water had worn away the dirt into smooth mounds on either side of the river."
    if (skill_social >= 30) or (skill_knowledge >= 30):
        "I talked to the Engels about building the bridge and they were excited to help. Helen especially seemed grateful for a chore she could do at home, and Jed said he'd try to spin rope during downtime at the library."
        "After a few days we had enough rope to start making stronger rope."
    else:     
        if (loved >= 20):
            "[his_name] helped me twist tons of rope every evening."
            "After a few days I had enough rope to start making stronger rope."
        else:
            "I worked on the rope every night for weeks."
            "Finally, I had enough to start making stronger rope."
    "I twisted and tied the large rope around a tree. [his_name] helped me get it to the other side using a small rope to guide it."
    "We tied two more ropes higher up for hand rails. At first the hand rails were too close together, so we had to tie them to some of the tree's branches."
    "The next day, I tied the handrails to the main rope using small ropes. At first it was a little scary to be on the bridge before it was done, but it wasn't very high up."
    "When I crossed the finished bridge, I felt a thrill of accomplishment. We did this, all on our own..."
    
    $ skill_creative += 10
    return

# Make a documentary about the colony and send it to Earth
label creative_master:
    scene bg sunset with fade
    "One day, as I was taking pictures of a flock of crabirds, I suddenly realized that no one on Earth had any idea what Talaam was like. They had never seen a wolfslug, or the shimmering rocks by the hot springs, or the rise of twin moons at twilight."
    "I had sent a few pictures, but they alone couldn't communicate enough."
    "I couldn't bear it - I had to share the wild, alien beauty of this planet with everyone I had left behind back home."
    "I wrote down all the things I wanted to show everyone, and then sorted them and connected the ideas."
    "I made a list of footage to shoot, and wrote a script for the narrator."
    
    if (skill_spiritual >= 20):
        "The film had a lot of meaning - I wanted viewers to be able to ponder their own place in the universe and be delighted at the new things we experienced here."
    if (skill_technical >= 20):
        "I was able to put in great transitions and professional-looking text, and I made sure to use non-lossy compression algorithms to keep the video quality high."
    if (skill_knowledge >= 20):
        "I included details about the planet's geology, biology, and chemistry that I had been studying the whole time we'd been living here."
    if (skill_social >= 20):
        "The film had a great human element - I interviewed some of the families and they told of their struggles and triumphs."

    "It wasn't the most professional or polished film ever. But it was the only film about this planet I had come to call home."
    "Before I sent it to Earth, I invited the whole colony to come and see it."
    scene bg community_center with fade
    "They watched quietly, and laughed at the fumbling baby crab spiders, and cried at the photos of infested crops, and shouted out when they saw someone from the colony they knew."
    "They all applauded at the end. I felt relieved, and also satisfied - I had been able to express something we had all felt."
    "It would be a few years before the transmission would reach Earth, but it was worth the wait for us to be able to share our beautiful new home with those we loved."

    $ skill_creative += 10
    return
