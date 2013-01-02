# Afternoon Events
# Knowledge

# Intro Event and the default
label knowledge_0:
    "I read up on the latest science research."
    $ skill_knowledge += 10

    return

label knowledge_1:
    "I went to a workshop at the laboratory about how to use a spectrometer to determine whether or not a food is edible." 
    teacher "And in some cases, you'll just have to test a little on an Earth creature. If you spectrize something and can't tell if it's safe, bring it into the lab."
    her "Do you have a list of plants you've already tested?" 
    teacher "Oh, right. Well, of course there's the ones you're planting, but in addition to those we've discovered a few that contain relevant nutrients. I'll have my assistant send out a guide." 
    $ skill_knowledge  += 10 
    return 

label knowledge_2:
    "I went to town and helped out at the library."
    "They don't have a lot of physical books there, but there are printouts of Talam and pad computers people can use if they don't have one of their own. Even though there's not lots of shelving to do, people can also put in data requests for librarians to research and things still need to be organized."
    "I was able to help with some obscure requests the colonists had posted by reading some recently published research papers."    

    $ skill_knowledge += 10

    return

label knowledge_3:
    "I studied the guide to edible plants the scientists sent out. It included information about other uses for plants. Some plants, called fiber crops, have the potential to be made into cloth or paper."
    her "I'm looking for plants to make into cloth, have you seen any plants that are fluffy-looking?"
    him "Hmm, not fluffy-looking, but I have seen some really tall grasses out past the riverbed. I can bring you some tomorrow if you'd like."
    her "Sure, it's worth a shot."
    "The next day he brought me a pile of these tall grasses. I brought some to the laboratory to see how we could process them."
    teacher "It looks like if you pull apart the fiber strands, you can get something that looks like hair. It's not very soft, but it's strong, so it would make good food sacks or rope. I'll make a note in the guide about this plant."
    "I told him it grew near our riverbed, and he promised to update the useful plants list."
    define has_grass = True
    $ skill_knowledge += 10
    
    return

label knowledge_4:

    $ skill_knowledge += 10
    return

label knowledge_5:

    $ skill_knowledge += 10
    return

label knowledge_6:

    $ skill_knowledge += 10
    return

label knowledge_7:

    $ skill_knowledge += 10
    return

label knowledge_8:

    $ skill_knowledge += 10
    return

label knowledge_9:

    $ skill_knowledge += 10
    return

label knowledge_master:

    $ skill_knowledge += 10
    return
