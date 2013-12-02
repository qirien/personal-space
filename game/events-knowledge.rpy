# Afternoon Events
# Knowledge

# Default
label knowledge_def:
    scene bg library
    "I read up on the latest science research."
    $ skill_knowledge += 5

# Intro Event
label knowledge_0:
    scene bg library
    "I knew there was a library here, so I decided to check it out. A young man was intently reading from his computer pad at the desk when I walked in."
    her "Hello there, your name's Sven, right?"
    sven "Oh! Hi there! Yes, I'm Sven, but I forgot your name."
    her "It's okay, there's a lot of people here on the colony.  I'm [her_name]."
    sven "That's right. Uh...what can I help you with?"
    her "Well, I had a few minutes and I thought I'd see what sort of stuff you have here in the library."
    sven "Well, most books you can just borrow from our online library, but we do have some high-res maps of the planet and a few printed reference books as well. We have also some tools and equipment people can borrow, like if you want to build something."
    her "Okay, that makes sense. We didn't have room to bring drills and wrenches for everyone, huh?"
    sven "Exactly. This is also where you can request new data from the extranet connection to Earth, though we have limited bandwidth and it will take several years to get here."
    her "What are those machines over there?"
    sven "Those are our printers. You can print on paper, of course, and we have a 3D printer if you need to print something out of plastic. We have limited quantities of paper and plastic, though, so please keep that in mind."
    her "I will. Thanks for the tour, Sven."
    sven "You're welcome."
    $ skill_knowledge += 10

    return

# Learning about edible plants
label knowledge_1:
    "I went to a workshop at the laboratory about how to use a spectrometer to determine whether or not a food is edible." 
    lily "And in some cases, you'll just have to test a little on an Earth creature. If you spectrize something and can't tell if it's safe, bring it into the lab."
    her "Do you have a list of plants you've already tested?" 
    lily "Oh, right. Well, of course there's the ones you're planting, but in addition to those we've discovered a few that contain relevant nutrients. I'll have my assistant send out a guide." 
    "I was excited to try out some of the edible plants here."
    $ skill_knowledge  += 10 
    $ met_Lily = True
    return 

# Volunteering to do research at library
label knowledge_2:
    scene bg library with fade
    "I went to town and helped out at the library."
    "They didn't need me to shelve books or anything, but sometimes people put in data requests for librarians to research or print out."
    "Sven was working on printing out some plastic tools, so I was able to help with some obscure requests the colonists had posted by reading some recently published research papers."
    $ skill_knowledge += 10

    return

# Finding fiber crops
label knowledge_3:
    scene bg path with fade
    "I studied the guide to edible plants the scientists sent out. It included information about other uses for plants. Some plants, called fiber crops, have the potential to be made into cloth or paper."
    her "I'm looking for plants to make into cloth, have you seen any plants that are fluffy-looking?"
    him "Hmm, not fluffy-looking, but I have seen some really tall grasses out past the riverbed. I can bring you some tomorrow if you'd like."
    her "Sure, it's worth a shot."
    "The next day he brought me a pile of these tall grasses. I brought some to the laboratory to see how we could process them."
    lily "It looks like if you pull apart the fiber strands, you can get something that looks like hair. It's not very soft, but it's strong, so it would make good food sacks or rope. I'll make a note in the guide about this plant."
    "I told her it grew near our riverbed, and she promised to update the useful plants list."
    define has_grass = True
    $ skill_knowledge += 10
    $ community_level += 5
    
    return

# Nature hike for edible plants
label knowledge_4:
    scene bg path with fade
    "Lily, our resident xenobiologist, organized a nature hike to tell us more about the local plants, and I went along."
    lily "As far as I can tell, this plant, which I call Bulbosa, isn't edible. Its bright orange flowers make a good dye though."
    lily "Alright, take a good look at this next plant and its surroundings. What can you tell me about it?"
    "Lily pointed to a tall flower with what looked like a tongue sticking out of its flower. Its leaves looked furry like ferns, but were hairier than an Earth fern. There no other plants around it, besides a few trees."
    menu:
        lily "Do you have any questions?"
        "Is it poisonous?":
            lily "It's poisonous to certain kinds of seeds. Its roots make the soil around it very acidic, so new flowers won't germinate near it. The tongue-like projection both attracts and detains nearby flying insects. While the insect is stuck on its tongue, the plant sucks out its innards, much like an Earth spider. If you look closely at the tongue-like area, it has multiple spikey projections for this purpose."
        "Is it carnivorous?":
            lily "Yes! The tongue-like projection both attracts and detains nearby flying insects. While the insect is stuck on its tongue, the plant sucks out its innards, much like an Earth spider. If you look closely at the tongue-like area, it has multiple spikey projections for this purpose."
        "Is it very old?":
            lily "I don't think it's much older than the other plants here. It's actually carniverous! The tongue-like projection both attracts and detains nearby flying insects. While the insect is stuck on its tongue, the plant sucks out its innards, much like an Earth spider. If you look closely at the tongue-like area, it has multiple spikey projections for this purpose."
    lily "On Earth, the secretions from carnivorous plants had antifungal properties. I'm in the process of testing this plant's goo to see if I can find a good use for it."
    her "Hopefully athlete's foot didn't make it onto the shuttle."
    lily "Seriously. There are also a lot of plants around here that release spores, and if they make us sick, I want to have a medicine to give out. That reminds me, while we don't have any mushrooms here, we do have these cute edible plants I call ringlets..."
    "The other hikers and I learned more about nearby plants."
    $ skill_knowledge += 10
    return

# Research geology, geography of planet
label knowledge_5:
    scene bg library with fade
    "I wanted to know why Talam's climate was the way it was, and why they chose to settle here on this spot, out of the whole planet."
    "I read a few research papers from astronomers and looked at maps of the planet. I could see that it was colder near the poles; we were closer to the equator, which made for milder temperatures and made year-round agriculture possible."
    "Obviously the river was very useful to our settlement for irrigation, and I also noticed some mountains further to the west. I had seen them in the distance. There was much more precipitation on this side of the mountain than on the other side, which also made this area ideal for colonization."
    "I wondered why they didn't put us near the ocean, but then I read that hurricanes were very common here. Those same mountains acted as a hurricane barrier as well."
    "There were plans to mine the mountains later for valuable metals and minerals, but for now they mainly wanted to see if it was even possible for us to live here. Apparently they were not as confident in our chances for survival as [his_name] was."
    "Last, I learned that the mountains were also a region of previous volcanic activity, and there might be hot springs in the area."
    if (skill_physical >= 60):
        "Of course, I had already found these while hiking, but it was good to know there might be more."
    else:
        "I might have to go check those out sometime."

    $ skill_knowledge += 10
    return

# Research nutrition theories for colonization, write article about nutritional value of native plants
#I wasn't sure what the nutrition theory was, so feel free to add that in.
label knowledge_6:
    scene bg library with fade
    lily "Hi [her_name]. I was hoping I'd run into you this week. I'm writing an article about the edible, native plants we've found for an Earth science journal, but I'm worried that I'll miss something if I write it alone. Would you like to co-author it with me?"
    menu:
        "Do I want to co-author a paper on plants?"
        "Sounds fun":
            her "Sure, that sounds like a good way to get our knowledge out to the scientific community."
            lily "Great! I'll send you what I have so far, and we can discuss it in the lab tomorrow."
            "Lily's paper was very technical, getting down to how the enzymes in these plants could still be broken down by human digestion, even though they were slightly different than earth's."
            "She also wrote about how humans wouldn't be able to live off of Telanian plants alone, since they were missing vital nutrients."
            "I felt a little out of my league when I went in to talk to Lily."
            her "I'm not much of a chemist, so I can't really help with checking most of your paper. I found a few typos, but you can easily fix those. Why did you want my help?"
            lily "Oh, I have a hard time seeing the big picture with plants. I know a lot of scientists are interested in their classification, but I'm not sure where to start."
            lily "In some ways, I think my knowledge of Earth plants might be tainting how I attempt to classify them, so I'd be interested to see how you would do that."
            her "Well, I'm not COMPLETELY ignorant of biology, but I see what you're getting at and I'll give it shot."
            "I spent some time gathering the edible plants Lily talked about in her paper. At first, I tried to sort them into categories based on their venation, but there were only two plants where that made a difference."
            "I decided to write down all the ways the plants were different, and then I ranked them by order of usefulness. The flowers were the easiest to tell apart, but were only present for part of the time."
            "I realized that Talam's plants' leaves didn't vary in size within a species. Leaf size ranged from tiny to umbrella-sized. Since I was halfway to making an identification key, I made one."
            lily "This is perfect! For some reason whenever I tried to categorize these plants I could only think of things like leaf shape and number of petals. This is an excellent addition."
            her "I'm glad I could help. Maybe we can distribute the key to the colonists too."
            lily "That's a wonderful idea. You can use the photos I already have if that will help."
            "Lily sent the paper off to Earth and I sent out an updated edible plant guide to the colonists, with guidelines on which earth plants were essential for supplementing a Talam-based diet."
            $ community_level += 1
            
        "I want to write my own paper to publish here on Talam":
            her "Actually, I was thinking of writing my own paper. I'd like to make a more detailed and accessible chart of edible plants with explanations my neighbors could understand."
            lily "Oh, well, after you finish it, is it okay if I reference it in my paper?"
            her "Yes, that's fine."
            "I worked hard over the next week to make a digital plant reference I could send out to the other colonists. In some ways, it was more difficult than making a complete encyclopedia. I wanted a succinct, but smart way of teaching about plants."
            "I left out all the plants that were technically edible, but weren't nutritious. I also included some poisonous plants that might otherwise be mistaken for an edible one."
            "I made an identification key to put in the back, which helped me organize the plants into chapters."
            "At first I tried drawing the plants, but I quickly gave up and took several photos of each instead."
            "After I sent out the link to the guide on our intranet, [his_name] pointed out a few typos, but I was able to fix them fairly quickly."
            "I saw Lily again that weekend."
            lily "Thank you for making the guide and identification key! I'm not sure if I would have thought to look at leaf size first, but given the plants you described that was the quickest way to do it! I'm definitely citing this!"
            her "Well, I'm glad it ended up being useful to you too."
            $ community_level += 1
            
        "I don't want to write anything down.":
            her "I don't know, that sounds like a lot of work. I've seen these plants so many times that I don't think writing down will help my memory at all. I can pass my knowledge on by you know, actually talking to my neighbors."
            lily "Writing is a lot of work, but what if your neighbor doesn't remember what you told her correctly?"
            her "That's your job."
            lily "How about you tell me what you know, and I can write it down?"
            her "Well, if it's that important to you, I can tell you what I know."
            "I spent the afternoon with Lily in the lab, discussing which plants were most useful to eat. She told me that she was fascinated by how a human could almost live off of Talam's plants alone, except for a few missing nutrients."
            "We both learned a lot, and I didn't have to spend any time writing aimlessly."
            $ community_level -= 1

    $ skill_knowledge += 10
    return

# Research psychology of the frontier, gain insight into something?
label knowledge_7:
    scene bg library with fade    
    "I had been doing a lot of reading lately. I read about the lives of pioneers who settled in new places, whether it was the Pilgrims in the 17th century, homesteaders in the 19th century, or refugees fleeing war and discord to start a new life in a totally unfamiliar place."
    "I could really relate to these pioneers. While it was exciting to be experiencing new areas, it was also scary. They couldn't rely on past experience, other people, or traditional society - they could only rely on themselves."
    "I realized how much trust we had all placed in each other, on our new colony here."
    "Not just the lazy trust of suburban neighbors, where you trust that your neighbor is not a killer, but the trust of pioneers, where you have to believe everyone is working hard and will help each other out of otherwise hopeless situations."
    her "What will living on a different planet do to our culture...?"
    
    $ skill_knowledge += 10
    return

# Turn the community center into an art museum!
label knowledge_8:
    "One of the things I missed about Earth was all the cultural events and places. We didn't have any museums or galleries or concerts here."
    her "But we do have digital copies of lots of famous paintings and music...."
    "I couldn't be the only one yearning for a night of culture and art."
    scene bg community_center with fade
    her "Is it okay if I use the community center for a night next week?"
    boss "What for?"
    her "I want to turn it into a museum for a night!"
    boss "That sounds marvelous. I would certainly like to see it."
    her "I'll be sure to invite everyone."
    "I would need a lot of computer pads to be setup like paintings, so I posted on the colony message board asking for volunteers."
    "I sent each person a different artist, and asked them to have their computer pad ready to slideshow that art on our museum night."
    "I also asked them to play music from a playlist that I picked to go with that artist."
    "Soon, the museum night arrived."
    scene bg community_center with fade
    image greatwave = "sprites/art-greatwave.png"
    image pearlearring = "sprites/art-girlpearlearring.png"
    image starrynight = "sprites/art-starrynight.png"
    image viewfromkremlin = "sprites/art-viewfromkremlin.png"

    show greatwave at Position(xpos=100,ypos=150)
    show pearlearring at Position(xpos=950,ypos=250)
    show starrynight at Position(xpos=500,ypos=150)
    show viewfromkremlin at Position(xpos=800,ypos=150)

    "It seemed like the whole colony had turned out for the event."
    show her normal at center
    "Some people contemplated and discussed the paintings, while others just chatted, and the little kids started playing under the stacks of chairs."
    "[his_name] came, too."
    show her normal at right
    show him normal at quarterright with moveinleft
    him annoyed "All right, so, tell me about this painting."
    her surprised "Which one?"
    him annoyed "The one with the wave. I've seen it before, but what's the big deal about it?"
    her normal "Well, it's a pretty famous woodblock print from Japan around 1830."
    him surprised "What's a woodblock print?"
    her normal "Basically they would take a painting with simple colors and make stamps out of it, so they could just stamp each color onto a new piece of paper to make copies."
    him annoyed "Okay, why did you choose this one?"
    her concerned "Well, I like the power of the wave, and how helpless all the little people in boats are against its raw power."
    him concerned "Hmmm."
    him happy "Yeah, I see what you mean. I like it."

    "It felt good to share some of what I loved with [his_name], and the colony."
    $ skill_knowledge += 10
    return

# Find bacteria that produce plastic, sort of like:
# http://www.scientificamerican.com/article.cfm?id=turning-bacteria-into-plastic-factories-replacing-fossil-fuels
label knowledge_9:
    "I had been working with Dr. Lily on a lot of things - not just the edible plants, but also cataloguing animal species and their behavior."
    "We were trying to build a food web based on what the animals here ate, but we knew it was woefully incomplete."
    scene bg pond with fade
    show her normal at center with dissolve
    "I decided to spend the day observing animals near the pond to see if I could discover any new species or record new behavior."
    "I was able to find some new predators, as well as several migratory species that sometimes visited the pond. Later in the afternoon, though, a sheen on the far side of the pond caught my eye."
    her surprised "What could that be?"
    "I hiked over to the other side of the pond, and found a smooth, glossy crust forming on one part of the pond."
    her "It feels like plastic!"
    scene black with fade
    "I took a sample back to Dr. Lily for analysis."
    scene bg lab with fade
    lily "It is plastic."
    her "How is that possible?! This doesn't look like anything we brought from Earth..."
    lily "That's because it is not from Earth. This is a naturally-formed plastic."
    her "Naturally formed?"
    lily "On the sample you gave me were some local bacteria. These bacteria eat organic material in the pond and excrete a chemical used to make plastic."
    her "But how did the plastic form?"
    lily "There must be some sort of chemical reaction... We should study it more. Will you show me where you found it?"
    scene bg pond with fade
    "I showed her the spot at the pond."
    lily "Hmm, I'll need samples of this, and this...it could be due to dehydration, or high acidic content..."
    "She took a lot of samples back to the lab."
    lily "I'll let you know what I find out."
    "A few weeks later, I asked her about it again."
    her "So, did you ever find out what was making that plastic at the pond?"
    lily "Oh! Yes. In fact, I am attempting to replicate the conditions of the pond in that tank over there to grow plastic."
    her "It looks like it's working!"
    lily "Yes, I believe I have managed to replicate the necessary conditions."
    her "Great! If we can produce our own plastic, we can 3D print more things that we need."
    lily "That's true; It would normally be at least 25 years before we could have our own plastic manufacturing facilities."
    "How cool is that?! We could now make our own plastic with bacteria..."
    $ community_level += 2

    $ skill_knowledge += 10
    return

# Learn about new medical treatment for skin cancer, can help Mr. Peron? 
label knowledge_master:

    $ skill_knowledge += 10
    return
