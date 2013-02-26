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
    "Lily organized a nature hike to tell us more about the local plants, and I went along."
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
    $ skill_knowledge += 10
    return

# Research nutrition theories for colonization, write article about nutritional value of native plants
label knowledge_6:

    $ skill_knowledge += 10
    return

# Research psychology of the frontier, gain insight into something?
label knowledge_7:

    $ skill_knowledge += 10
    return

# Learn about new medical treatment for skin cancer, can help one of the colonists?
label knowledge_8:

    $ skill_knowledge += 10
    return

label knowledge_9:

    $ skill_knowledge += 10
    return

label knowledge_master:

    $ skill_knowledge += 10
    return
