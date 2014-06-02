label msg_01:
    boss_c "Mandatory all-colony meeting tomorrow at 10, followed by a farmer's meeting at 11!"
    him_c msg "Hey, a few people asked me about the attachment system on these tractors; so here's a how-to."
    
label msg_02:
    naomi_c "Please let me know if you would be interested in a weekly yoga and meditation session."
    lily_c "I am looking for a volunteer to come to the ocean and gather guano. No experience necessary."
    sven_c "Doubt you'll get many takers on that one, Lily."
    
label msg_03:
    sven_c "Hey, uh, I forgot who checked out the chisel set, but could you please return them?"
    her_c "Happy Birthday, [his_name]!"
    him_c "Thanks, [her_name]..."
    sara_c "It's your birthday? How old are you?"
    him_c "In Earth time, or relative time as experienced by me?"
    sara_c "Oh, never mind, it doesn't really matter, I guess."

label msg_04:
    brennan_c ""
    
label msg_05:
    boss_c "I've had a few questions about what to do with trash - let me remind everyone that our plastic and metal supplies are very limited, so make sure you recycle these items at the community center. Other trash can be burned or composted; see pages 126-128 of the Colonist's Guide."
    
label msg_06:
    thuc_c "Hey, my corn was doing fine, but the ears don't seem to be growing any bigger - anyone else having this problem?"
    martin_c "Yeah, mine, too. I noticed some tiny white dots under the leaves - maybe insect eggs?"
    
label msg_07:
    #message from her based on highest_skill
    $ highest_skill = highest_stat()
    if (highest_skill == "Domestic"):
        her_c "I've got some extra mint if anyone needs some - it grows really well here!"
    elif (highest_skill == "Creative"):
        her_c "Moonrise over the south hills, pic attached."
    elif (highest_skill == "Technical"):
        her_c "Finally got our new antenna installed. Everyone sounds much clearer now!"
    elif (highest_skill == "Spiritual"):
        her_c "Sister Naomi gave a great sermon yesterday..."
        natalia_c "Yes, it even kept Martin awake!"
    elif (highest_skill == "Social"):
        her_c "Free advice: never play Pictionary against Helen! She draws like da Vinci on speed..."
        him_c "I thought we did pretty good!"
        her_c "You draw more like Picasso..."
        him_c "Well, he's a pretty good artist, right?"
        her_c "Not for Pictionary!"
        
    elif (highest_skill == "Knowledge"):
        her_c "I took a picture of this plant; does anyone know if you can eat it? It smells good, but I'm not sure..."
        lily_c "It's not in our database; bring it by the lab and I'll run it through the spectrometer."
    elif (highest_skill == "Physical"):
        her_c "Ran 10k today; it feels good!"
        
label msg_24:
    boss_c "I know we're all looking forward to a few new supplies from the new ship, but let's remember to take only what we need."
    