# Afternoon Events
# Knowledge

# Default
label knowledge_def:
    scene bg library with fade
    "I read up on the latest science research. Dr. Lily had posted some articles about Talaam's geology and biology."
    $ skill_knowledge += 10

# Intro Event
label knowledge_0:
    scene bg library with fade
    show pete at midright with dissolve
    "I knew there was a library here, so I decided to check it out. I sent Pete a message and he agreed to meet me there and show me around. When I arrived, he was lounging in a chair reading on his computer pad. He stood up to greet me."
    show her normal at midleft with moveinleft
    if (profession == "doctor"):
        pete happy "Howdy, Doc! What can I help you with?"
    else:
        pete happy "Howdy! [her_name], right? Well, what can I help you with?"
    her normal "I had a few minutes and I thought I'd see what sort of stuff you have here in the library."
    pete normal "Well, most books you can just borrow from our online library, but we do have some high-res maps of the planet and a few printed reference books.  We've also got some tools and equipment people can borrow, like if you want to build something."
    her serious "Okay, that makes sense. We didn't have room to bring drills and wrenches for everyone, huh?"
    pete happy "Yup. This is also where you can get new data from the extranet connection to Earth, though  it'll take a couple of years to arrive."
    her surprised "What are those machines over there?"
    pete normal "Those are our printers. You can print on paper, of course, and we have a 3D printer if you need to print something out of metal or plastic. But we don't have a ton of either material, so you can't just print anything, and recycling's real important."
    her normal "That makes sense. Thanks for the tour, Pete."
    pete normal "You're welcome."
    her surprised "By the way, what are you reading?"
    pete "Aw, just a book, nothing special."
    her normal "What's it about?"
    pete happy "It's sort of a historical book about some settlers in Australia. New place, unfamiliar terrain, crazy people - sort of like us."
    her serious "Hopefully without the crazy people part."
    pete normal "Well, most folks are alright, but that Julia... man, she's tough as a wolfslug and twice as mean. Don't know how she passed the psych test to come up here."
    her flirt "Same way you passed it, probably."
    pete happy "By havin' more guts than you could hang on a fence? I guess we do have that in common."
    her normal "Maybe so. See you around, Pete."
    pete "Bye."
    $ skill_knowledge += 10

    return

# Learning about edible plants
label knowledge_1:
    scene bg lab with fade
    "I went to a workshop at the laboratory about how to use a spectrometer to determine whether or not a food is edible." 
    show lily at quarterright 
    show pete at left
    show brennan at midleft
    show her normal at center
    with dissolve
    with dissolve
    lily "And in some cases, you'll just have to test a little on an Earth creature. If you spectrize something new and want to make sure it's safe, bring it into the lab and I will have one of our rats try it."
    her surprised "Do you have a list of plants you've already tested?" 
    lily "Yes. Of course there's the ones you're planting, but in addition to those we've discovered a few that contain relevant nutrients. I'll have my assistant send out a guide." 
    "I was excited to try out some of the edible plants here."
    $ skill_knowledge  += 10 
    return 

# Volunteering to do research at library
label knowledge_2:
    scene bg library with fade
    "I went to town and helped out at the library."
    "They didn't need me to shelve books or anything, but sometimes people put in data requests for librarians to research or print out."
    "Pete was working on printing out some plastic tools, so he asked me to help with something else."
    "There were some research requests the colonists had posted, so I read some recently published research papers to answer their questions."
    $ skill_knowledge += 10

    return

# Finding fiber crops
label knowledge_3:
    scene bg path with fade
    "I studied the guide to edible plants the scientists sent out. It included information about other uses for plants. Some plants, called fiber crops, have the potential to be made into cloth or paper."
    show her normal at midright
    show him normal at midleft
    with dissolve
    her "I'm looking for plants to make into cloth, have you seen any plants that are fluffy-looking?"
    him "Hmm, not fluffy-looking, but I have seen some really tall grasses out past the riverbed. I can bring you some tomorrow if you'd like."
    her "Sure, it's worth a shot."
    scene black with fade
    "The next day he brought me a pile of these tall grasses. I brought some to the laboratory to see how we could process them."
    scene bg lab with fade
    show lily happy at midright with dissolve
    show her normal at midleft with moveinleft
    lily "It looks like if you pull apart the fiber strands, you can get something that looks like hair. It's not very soft, but it's strong, so it would make good food sacks or rope. I'll make a note in the guide about this plant."
    "I told her it grew near our riverbed, and she promised to update the useful plants list."
    define has_grass = True
    $ skill_knowledge += 10
    $ community_level += 2
    
    return

# Nature hike for edible plants
label knowledge_4:
    scene bg path with fade
    show lily at right
    show pete at midright
    show brennan at left
    show julia at quarterleft
    show her normal at center
    with dissolve
    "Lily, our resident xenobiologist, organized a nature hike to tell us more about the local plants, and I went along."
    lily "As far as I can tell, this plant, which I call Bulbosa, isn't edible. But its bright orange flowers make a good dye."
    lily "Scrutinize this next plant and its surroundings. What can you tell me about it?"
    "Lily pointed to a tall flower with what looked like a tongue sticking out of its flower. Its leaves looked furry like ferns, but were hairier than an Earth fern. There were no other plants around it, besides a few trees."
    menu:
        lily "What can you tell me about it?"
        "Is it poisonous?":
            her surprised "Is it poisonous?"
            lily "It's poisonous to certain kinds of seeds. Its roots make the soil around it very acidic, so new flowers won't germinate near it. But it is dangerous in another way."
        "Is it carnivorous?":
            her surprised "Is it carnivorous?"
            lily happy "Yes!"
        "Is it very old?":
            her surprised "Is it very old?"
            lily "I don't think it's much older than the other plants here. But it's actually carnivorous!"
    lily normal "The tongue-like projection both attracts and detains nearby flying insects. While the insect is stuck on its tongue, the plant sucks out its innards, much like an Earth spider. If you look closely at the tongue-like area, it has multiple spikey projections for this purpose."
    lily "On Earth, the secretions from carnivorous plants had antifungal properties. I'm in the process of testing this plant's goo to see if I can find a good use for it."
    her concerned "Hopefully athlete's foot didn't make it onto the shuttle."
    lily upset "A good example. There are also a lot of plants around here that release spores, and if they make us sick, I want to have a medicine to give out."
    lily normal "That reminds me, while we don't have any mushrooms here, we do have these cute edible plants I call ringlets..."
    "The other hikers and I learned more about nearby plants."
    $ skill_knowledge += 10
    return

# Research geology, geography of planet
label knowledge_5:
    scene bg library with fade
    "I wanted to know why Talaam's climate was the way it was, and why they chose to settle here on this particular spot."
    "I read a few research papers from astronomers and looked at maps of the planet. I could see that it was colder near the poles; we were closer to the equator, which made for milder temperatures and made year-round agriculture possible."
    "Obviously the river was very useful to our settlement for irrigation, and I also noticed that the mountains I had seen to the west made a barrier between our fertile colony and a desert."
    "I wondered why they didn't put us near the ocean, but then I read that hurricanes were very common close to shore."
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
    show her normal at midright with dissolve
    show lily at midleft with moveinleft
    lily "[her_name]. I want to talk to you. I am writing an article about the edible, native plants we've found for an Earth science journal. Will you co-author it with me?"
    menu:
        "What should I say?"
        "Sounds fun.":
            her normal "Sure, that sounds like a good way to get our knowledge out to the scientific community."
            lily happy "Good. I'll send you what I have so far, and we can discuss it in the lab tomorrow."
            show lily normal
            "Lily's paper was very technical, getting down to how the enzymes in these plants could still be broken down by human digestion, even though they were slightly different than Earth's."
            "She also wrote about how humans wouldn't be able to live off of Talaam's plants alone, since they were missing vital nutrients."
            "I felt a little out of my league when I went in to talk to Lily."
            her concerned "I'm not much of a chemist, so I can't really help with checking most of your paper. I found a few typos, but you can easily fix those. Why did you want my help?"
            lily "I have a hard time seeing the big picture with plants. I know a lot of scientists are interested in their classification, but I think my knowledge of Earth plants might be tainting how I attempt to classify them. I'm interested in a more plebian perspective."
            her annoyed "Well, I'm not completely ignorant of biology, but I see what you're getting at and I'll give it shot."
            "I spent some time gathering the edible plants Lily talked about in her paper. At first, I tried to sort them into categories based on their venation, but there were only two plants where that made a difference."
            "I decided to write down all the ways the plants were different, and then I ranked them by order of usefulness. The flowers were the easiest to tell apart, but were only present for part of the time."
            "I realized that Talaam's plants' leaves didn't vary in size within a species. Leaf size ranged from tiny to umbrella-sized. Since I was halfway to making an identification key, I made one."
            lily happy "This is excellent. I had overlooked leaf size in my previous categorization attempts."
            her "I'm glad I could help. Maybe we can distribute the key to the colonists too."
            lily "Yes, that would be helpful. You can use the photos I already have."
            "Lily sent the paper off to Earth and I sent out an updated edible plant guide to the colonists, with guidelines on which earth foods were essential for supplementing a Talaam-based diet."
            $ community_level += 1
            
        "I want to write my own paper to publish here on Talaam.":
            her "Actually, I was thinking of writing my own paper. I'd like to make a more detailed and accessible chart of edible plants with explanations my neighbors could understand."
            lily normal "Oh. I see. After you finish it, may I reference it in my paper?"
            her "Yes, that's fine."
            scene black with fade
            "I worked hard over the next week to make a digital plant reference I could send out to the other colonists. In some ways, it was more difficult than making a complete encyclopedia. I wanted a succinct, but smart way of teaching about plants."
            "I left out all the plants that were technically edible, but weren't nutritious. I also included some poisonous plants that might otherwise be mistaken for an edible one."
            "I made an identification key to put in the back, which helped me organize the plants into chapters."
            "At first I tried drawing the plants, but I quickly gave up and took several photos of each instead."
            "After I sent out the link to the guide on our intranet, [his_name] pointed out a few typos, but I was able to fix them fairly quickly."
            "I saw Lily again that weekend."
            scene bg lab
            show lily at midright
            show her normal at midleft
            with dissolve
            lily happy "Thank you for making the guide and identification key. I would not have thought to look at leaf size first, but given the plants you described that was the quickest way to do it. I shall definitely cite this."
            her happy "Well, I'm glad it ended up being useful to you too."
            $ community_level += 1
            
        "I don't want to write anything down.":
            her concerned "I don't know, that sounds like a lot of work. I've seen these plants so many times that I don't think writing down will help my memory at all. I can pass my knowledge on by you know, actually {b}talking{/b} to my neighbors."
            lily upset "Writing is a lot of work, but what if your neighbor doesn't remember what you told her correctly?"
            her annoyed "That's your job."
            lily normal "Perhaps you could tell me what you know, and I could write it down?"
            her serious "Well, if it's that important to you, I can tell you what I know."
            "I spent the afternoon with Lily in the lab, discussing which plants were most useful to eat. She told me that she was fascinated by how a human could almost live off of Talaam's plants alone, except for a few missing nutrients."
            "We both learned a lot, and I didn't have to spend any time writing aimlessly."

    $ skill_knowledge += 10
    return

# Turn the community center into an art museum!
label knowledge_7:
    scene black with fade
    "One of the things I missed about Earth was all the cultural events and places. We didn't have any museums or galleries or concerts here."
    "But we did have digital copies of lots of famous paintings and music...."
    "I couldn't be the only one yearning for a night of culture and art."
    scene bg community_center with fade
    show pavel at midright, behind her with dissolve
    show her normal at midleft with moveinleft
    her surprised "Is it okay if I use the community center for a night next week?"
    pavel "What for?"
    her happy "I want to turn it into a museum for a night!"
    pavel "That sounds marvelous. I would certainly like to see it."
    her normal "I'll be sure to invite everyone."
    scene black with fade
    "I would need a lot of computer pads to be setup like paintings, so I posted on the colony message board asking for volunteers."
    "I sent each person a different artist, and asked them to have their computer pad ready to slideshow that art on our museum night."
    "I also asked them to play music from a playlist that I picked to go with that artist."
    "Soon, the museum night arrived."
    scene bg community_center with fade
    play music "music/RondoAMinor.ogg" fadeout 1.0

    show greatwave at Position(xpos=170,ypos=250)
    show pearlearring at Position(xpos=900,ypos=300)
    show starrynight at Position(xpos=400,ypos=250)
    show viewfromkremlin at Position(xpos=665,ypos=250)

    "It seemed like the whole colony had turned out for the event."
    show her normal at center
    "Some people contemplated and discussed the paintings, while others just chatted, and the little kids started playing under the stacks of chairs."
    "[his_name] came, too."
    show her normal at midright
    show him normal at midleft with moveinleft
    him annoyed "All right, so, tell me about this painting."
    her surprised "Which one?"
    him serious "The one with the wave. I've seen it before, but why's it so famous?"
    her normal "Well, it's a woodblock print from Japan around 1830."
    him surprised "What's a woodblock print?"
    her normal "Basically they would take a painting with simple colors and make stamps out of it, so they could just stamp each color onto a new piece of paper to make copies."
    him serious "Okay, why did you choose this one?"
    her concerned "Well, I like the power of the wave, and how helpless all the little people in boats are against its raw power."
    him concerned "Hmmm..."
    him happy "Yeah, I see what you mean. I like it."
    show her happy
    "It felt good to share some of what I loved with [his_name], and the colony."
    $ skill_knowledge += 10
    $ community_level += 1
    return

# Find bacteria that produce plastic
label knowledge_8:
    scene black with fade
    "I had been working with Dr. Lily on a lot of things - not just the edible plants, but also cataloguing animal species and their behavior."
    "We were trying to build a food web based on what the animals here ate, but we knew it was woefully incomplete."
    scene bg pond with fade
    "I decided to spend the day observing animals near the pond to see if I could discover any new species or record new behavior."
    "I was able to find two new predators, as well as several migratory species that sometimes visited the pond. Later in the afternoon, though, a sheen on the far side of the pond caught my eye."
    show her normal at center with dissolve
    her surprised "What could that be?"
    "I hiked over to the other side of the pond, and found a smooth, glossy crust forming on one part of the pond."
    her "It feels like plastic!"
    scene black with fade
    "I took a sample back to Dr. Lily for analysis."
    scene bg lab with fade
    show lily at midright with dissolve
    show her normal at midleft with moveinleft
    lily "It is plastic."
    her surprised "How is that possible?! This doesn't look like anything we brought from Earth..."
    lily "That's because it is not from Earth. This is a naturally formed plastic."
    her serious "Naturally formed?"
    lily upset "On the sample you gave me were some local bacteria. These bacteria eat organic material in the pond and excrete a chemical used to make plastic."
    her surprised "But how did the plastic form?"
    lily normal "There must be some sort of chemical reaction... We should study it more. Will you show me where you found it?"
    scene bg pond with fade
    show lily at center
    "I showed her the spot at the pond."
    lily "Hmm, I'll need samples of this, and this...it could be due to dehydration, or high acidic content..."
    "She took a lot of samples back to the lab."
    lily "I'll let you know what I find out."
    "A few weeks later, I asked her about it again."
    scene bg lab with fade
    show lily at midright with dissolve
    show her normal at midleft with moveinleft
    her happy "So, did you ever find out what was making that plastic at the pond?"
    lily happy "Oh! Yes. In fact, I am attempting to replicate the conditions of the pond in that tank over there to grow plastic."
    her surprised "It looks like it's working!"
    lily normal "Yes, I believe I have managed to replicate the necessary conditions."
    her happy "Great! If we can produce our own plastic, we can 3D print more things that we need."
    lily "It will require recalibration due to the higher melting point of this plastic, but, yes."
    "How cool is that?! We could now make our own plastic with bacteria..."
    $ community_level += 2

    $ skill_knowledge += 10
    return

# Write a book about Talaam? Collect essays from everyone?
label knowledge_master:
    scene bg lab with fade
    show lily at midright
    show her normal at midleft
    with dissolve
    
    lily normal "[her_name], we've learned so much about this planet, but I'm worried that all our research will be for naught if it is not shared properly."
    her normal "Well, we did work on that information on edible plants..."
    lily normal "Yes, but that is not enough. What about the bacteria you found, and the creatures we found at the ocean, and the maps we've made? There's not one place to find all those things."
    her flirt "We could just ask you."
    lily upset "I will not live forever. And neither will you. Our knowledge needs to outlive us."
    her concerned "I see what you mean..."

    scene bg library with fade
    show pete at midright with dissolve
    show her normal at midleft with moveinleft

    her normal "Pete, do we have any referece materials about our planet?"
    pete "About Talaam? Well, there's Dr. Lily's initial reports, and the probe's data..."
    her surprised "But nothing since we arrived here?"
    pete "Nah, everyone's been too busy just tryin' to survive."
    her serious "That's going to change, starting now."
    pete "You writin' a book or something?"
    her "An encyclopedia."
    pete happy "Ha ha, sure, no point in starting simple, is there?"
    her normal "Don't worry; I'll have help."
    pete "Who has time to write for an encyclopedia?"
    her flirt "You do."
    pete normal "Whoa, whoa, hold your horses! I don't know anything worth puttin' on paper!"
    her "Of course you do! We all do. Just think about what you know better than anyone else. What knowledge about Talaam would be lost if you died right now?"
    pete "Well, when you put it that way... but I ain't the only one who's learned a thing or two."
    her normal "I'll be asking everyone to contribute."

    scene bg farm_interior with fade
    "It wasn't enough to have a whole bunch of information in one place, though - it needed to be organized properly."
    "I spent a few nights sketching out a knowledge tree of things we ought to have in our encyclopedia."
    if (loved >= 0):
        "[his_name] helped me with some of the agricultural categories."

    "I started making articles for things I knew about, linking in existing information, like the database of edible and useful plants, the bacteria we found, the animals we'd observed, and crops that had done well or not."
    if (skill_physical >= 60):
        "I included a map to the hot spring I had found and the things we had found there."
    if (skill_domestic >= 70):
        "I talked about how to preserve the meat of different animals and native plants."
    if (profession == "doctor"):
        "I wrote about what we knew about local bacteria that were dangerous to humans, and other medical issues specific to this planet."
    if ((profession == "carpenter") or (skill_creative >= 50)):
        "I wrote about what plants were useful for making rope and furniture and how to treat them to last longer."
        
    "Then I sent a message out asking for everyone to help fill in the blank sections of the encyclopedia."
    "I waited for a few days... but the only person who had posted anything was Pete, who had written one article about what plants were good for cattle to graze on and which could be dangerous."
    "This was no good! I needed everyone's help for this encyclopedia!"
    menu:
        "What should I do?"
        "Ask people individually.":
            "I decided to talk to or e-mail each member of the colony individually and request them to write about a specific topic."
            scene bg wedding with fade
            "I asked Naomi to write about the psychological issues of a small colony isolated from Earth."
            scene bg fields with fade
            "I asked [his_name] to write about soil properties and how they affected the plants he had tried to grow."
            scene bg storehouse with fade
            "I asked Ilian to write about what things from Earth were in short supply, and what future colony ships could do better."
            
        "Write a passionate plea for help.":
            scene black with fade
            "I decided to write another message that would get my point across better."
            her_c "We need your knowledge! With what you know, future colony ships can be better prepared, and other colonists in the community can learn from your mistakes instead of repeating them!"
            her_c "I know each of you has learned something about this planet that no one else knows - with this encyclopedia we can preserve that information not just for future generations, but for your neighbors right here and now!"
            her_c "Don't wait until your knowledge is perfect or until someone makes a costly mistake your knowledge could have prevented - share it with us now!"
            her_c "If you don't know where your information goes, or there's not a place for it yet, just send it to me and I will add it in the right place."
            "I hoped that would encourage people to add to our planet encyclopedia."
            nvl clear
        "Get the Mayor's help.":
            scene bg community_center with fade
            show pavel at midright, behind her with dissolve
            show her normal at midleft with moveinleft
            her surprised "Mayor Grayson, is there a way you could encourage people to add to the planet encyclopedia?"
            pavel "There's a planet encyclopedia?"
            her annoyed "Yes, I just started one! Didn't you see my message?!"
            pavel sad "Well, I remember something like that..."
            her concerned "(No wonder no one's added anything...)"
            pavel normal "But that sounds like a great idea! I know there's been times when I wanted to know something, like Talaam's weather patterns."
            her surprised "So can you encourage everyone to write articles for it?"
            pavel "Yes, I will! I might just write an article myself..."
            her happy "That would be wonderful!"
            "With the mayor's encouragement, more people wrote about what they knew for the encyclopedia."

    scene bg lab with fade
    show lily happy at midright with dissolve
    show her normal at midleft with moveinleft

    her happy "Well, we have twenty articles about Talaam now! Are you going to write one, too, Dr. Lily?"
    lily "Yes, I'll post the initial geographical surveys and maps, as well as our more recent research. I'm simply trying to condense them into a more readable format."
    her normal "Great! I'll continue to add what I learn, too."
    "I added an article whenever we learned something new, and I kept all the articles well-organized and edited so they were easy to find and read."
    "I was proud of this legacy I could pass on to future colonists."

    $ skill_knowledge += 10
    $ community_level += 10
    return
