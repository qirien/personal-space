# Afternoon Events
# Knowledge

# Intro Event and the default
label knowledge_0:
    scene bg library
    if (skill_knowledge <= 10):
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
        
    else:
        "I read up on the latest science research."
    $ skill_knowledge += 10

    return

# Learning about edible plants
label knowledge_1:
    "I went to a workshop at the laboratory about how to use a spectrometer to determine whether or not a food is edible." 
    lily "And in some cases, you'll just have to test a little on an Earth creature. If you spectrize something and can't tell if it's safe, bring it into the lab."
    her "Do you have a list of plants you've already tested?" 
    lily "Oh, right. Well, of course there's the ones you're planting, but in addition to those we've discovered a few that contain relevant nutrients. I'll have my assistant send out a guide." 
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
    "You and the other hikers learned more about nearby plants."
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
            "Lily's paper was very technical, getting down to how the enzymes in these plants could still be broken down by human digestion, even though they were slightly different than earth's. She also wrote about how humans wouldn't be able to live off of Telanian plants alone, since they were missing vital nutrients."
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
            
            #possibly add community points in here, if it doesn't throw things off balance.
            
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
            
            #possibly add community points in here, if it doesn't throw things off balance.
            
        "I don't want to write anything down.":
            her "I don't know, that sounds like a lot of work. I've seen these plants so many times that I don't think writing down will help my memory at all. I can pass my knowledge on by you know, actually talking to my neighbors."
            lily "Writing is a lot of work, but what if your neighbor doesn't remember what you told her correctly?"
            her "That's your job."
            lily "How about you tell me what you know, and I can write it down?"
            her "Well, if it's that important to you, I can tell you what I know."
            "I spent the afternoon with Lily in the lab, discussing which plants were most useful to eat. She told me that she was fascinated by how a human could almost live off of Talam's plants alone, except for a few missing nutrients."
            "We both learned a lot, and I didn't have to spend any time writing aimlessly."
            
            #this option would not have community points added
        
    $ skill_knowledge += 10
    return

# Research psychology of the frontier, gain insight into something?
label knowledge_7:

    $ skill_knowledge += 10
    return

# Learn about new medical treatment for skin cancer, can help Mr. Peron? 
label knowledge_8:

    $ skill_knowledge += 10
    return

label knowledge_9:

    $ skill_knowledge += 10
    return

label knowledge_master:

    $ skill_knowledge += 10
    return
