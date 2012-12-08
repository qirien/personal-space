# Afternoon Events
# Physical

# Intro Event and the default
label physical_0:
    "I went for a run around the farm."
    $ skill_physical += 10

    return

label physical_1:
    "I decided to do some exploring. Here I was, living on a completely new planet, and all I had ever seen was the town and my own little farm. There was a ridge to the south, so I decided to hike over the top and see what was there."
    "The ridge was steeper than it looked, but I was able to scramble up to the top. From the top of the ridge I could see all the way to town to the north, and to the south was a vast expanse of wild rolling hills with sparse shrubs, a few of the taller plants we called trees, and over all the ground the blue-green lichen that seemed to live everywhere on Talaam."
    "And, as the ridge descended before me, at its base I could see a grove of trees that looked out-of-place, telling me there was wa"
    her "There must be water there!"
    "Sure enough, the stream that ran through the valley formed a pond that the trees drew water from. As I descended the slope, the fragrant smell of new plants reached me. At the bottom, the shade and cool water looked inviting and calm."
    her "Whew...I've been hiking for almost two hours now -- time for a break!"
    "I took off my shoes and socks and dipped my feet in the water. The rocks at the bottom were a little slimy with a strange magenta substance that I assumed was algae, but it still felt good.  I sat down on a rock and took a long drink from the water I brought."
    if (skill_creative >= 20):
        "The pond was so familiar, and yet so distinct from anything I'd seen on Earth, I felt like I had to draw it, so I took out my sketchpad and got to work."
    if (skill_domestic >= 40):
        "I decided to bring some of the sweet-smelling herbs back to the house and see if the scientists had tested their edibility."

    "When I had rested long enough, I started to bring my legs out of the water. However, they were completely numb! They weren't just cold; and they weren't tingly like they had fallen asleep - it felt more like some kind of anaesthesia."
    "I had to use my hands to pull my legs out of the water. I noticed some black spots on them, but when I tried to wipe off the spots..."
    her "It's not mud...are these some kind of leech?!"
    "I was able to pry it off, and, sure enough, they were attached to my skin with little jaws just like leeches. They must secrete some kind of anesthetic..."
    if (skill_knowledge >= 40):
        "I thought I would bring one back for the scientists to analyze, so after removing it I stuck it in my now-empty water bottle."
    "There must have been twenty or thirty on my legs, and by the time I had removed them all, the sun was setting. When I tried to stand up, my legs wobbled and I splashed back in the pond."
    her "My legs are too numb to walk..."

    if (skill_technical >= 20):
        "Luckily, I brought my radio with me and was able to call for help."
    elif (profession == "doctor"):
        "An adrenaline rush might help counteract the leeches' natural anesthetic..."
        "I don't have any medications with me, but I might be able to get my body to release adrenaline on its own."
        "I imagined all the scariest creatures that had been documented to live on this planet, all converging on the water hole for an evening drink, and I, unable to move, helpless...I breathed quickly to try to bring on my body's natural fight-or-flight response."
        her "HRRRRGH!"
        "I stumbled up the hill, heading north. The sun was setting, but I couldn't enjoy it."
    else:
        "I kept trying to move my legs, and I finally managed a slow sort of crawl away from the pond. It was impossible for me to enjoy the glowing sunset; all I could think of was getting out of there."

    him "[her_name]! [her_name]!"
    her "I'm here!"
    him "Keep talking to me, I'm coming!"
    her "I can't move very well."
    him "It's okay, I'll get you home."
    "I saw [his_name] appear on the top of the ridge. He was riding Lettie, his eyes scanning the landscape fiercely, until he finally saw me."
    "Before I could even explain what had happened, he had picked me up and was holding me close. I rested my head on his chest."
    him "You're safe..."
    her "Thanks for coming for me. I was worried some vicious alien animal was going to come gobble me up, and I've already been nibbled on one too many times this evening."
    him "Don't worry, [her_name], I'm the only one that will be gobbling you up now."
    "He nibbled on my ear playfully, and set me on Lettie. He held my hand all the way home."

    "After I had cleaned up and my legs were functioning again, I fell asleep. But [his_name] wanted to talk."
    menu:
        him "I don't think it's a good idea for you to go hiking by yourself."
        "Don't tell me what to do.":
            her "Don't tell me what to do."
            him "I'm just saying, who knows what's out there? We don't even know half the creatures on this planet. It's too dangerous."
            her "That's not for you to decide."
            him "Promise me you won't go off by yourself again."
            her "I'm not promising anything!"
            him "Dammit, [her_name], I need you! I need you alive, here with me, not as a carcass torn apart by some alien beast!"
            her "I need you to trust me to make my own decisions."
            him "I...do trust you. Please, be more careful, [her_name]"
        "Want to come next time?":
            her "Want to come with me next time? We can take a picnic."
            him "Sure, just as long as I don't have to share you with the pond creatures."
            her "Yeah, that would suck."
            him "Ohhhhhhh."
            her "Sorry, that was a bad joke."
        "I'll be more careful.":
            her "I'll be more careful next time."
            him "Next time?! Are you planning on doing that again?!"
            her "Of course. I want to know what's out there, just a few miles from our house. Who knows, maybe I'll find something useful?"
            him "Maybe you'll find something lethal!"
            menu:
                him "Maybe you'll find something lethal!"
                "That's the fun":
                    her "That's the fun of it! It wouldn't be an adventure if it wasn't just a little bit dangerous, would it?"
                    him "You're not indestructible, like some action hero. If you die out there, you can't just load your game and try again."
                    her ""
                "Come with me, then.":
                    her "Why don't you come with me next time, then? You can protect me from all the scary monsters out there."
                    him "I...sure. That's a good idea. Just, don't go alone, okay?"
                    her "All right. But neither should you."
                    him "I won't."
                    her "Do we need to pinkie promise?"
                    him "I can think of a better way to seal this promise."
                    "The argument melted away into kisses."
                "Whatever.":
                    her "Whatever. It's not that bad."
                    him "I guess there's no point in trying to convince you, is there? You're never going to listen."
                    $ loved -= 10
        "Maybe you're right.":
            her "Maybe you're right. Don't worry, I'm not planning on any more blood-donation excursions anytime soon."
            him "Thank you, [her_name]. I...need you."
            
    jump events_skip_period
    $ loved += 5
    $ skill_physical += 10
    return

label physical_2:
    $ skill_physical += 10

    return

label physical_3:
    $ skill_physical += 10

    return

label physical_4:

    $ skill_physical += 10
    return

label physical_5:

    $ skill_physical += 10
    return

label physical_6:

    $ skill_physical += 10
    return

label physical_7:

    $ skill_physical += 10
    return

label physical_8:

    $ skill_physical += 10
    return

label physical_9:

    $ skill_physical += 10
    return

label physical_master:

    $ skill_physical += 10
    return
