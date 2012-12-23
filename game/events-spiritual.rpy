# Afternoon Events
# Spiritual

# Intro Event and the default
label spiritual_0:
    "I took a walk and spent some time just thinking."
    $ skill_spiritual += 10

    return

label spiritual_1:
    "I went to the colony's spiritual leader, just to talk. I'd been thinking a lot about what makes us human, and what there may be that we cannot see."
    "Naomi Takahara" "Welcome, [her_name]. How can I help you?"
    her "Hi...uh, What should I call you, anyway? Pastor? Reverend?"
    naomi "Why don't you call me \"Sister\"? While I'm not a nun of any religion, I like to emphasize that we are all like children when it comes to matters of the spirit."
    her "OK, Sister Naomi...what exactly do you do here?"
    naomi "When people have questions about what they should do, or what to believe, sometimes it is helpful for them to have a guide. Since there are people of many different faiths here on Talam, I try and guide them in a way that is helpful for their religious background."
    her "But what do you believe?"
    naomi "Is that really the question you should be asking?"
    her "Huh?"
    naomi "Shouldn't you be asking yourself that question?"
    her "What do *I* believe?"

    menu:
        "What do *I* believe?"
        "I don't know.":
            her "I don't really know what I believe. My parents didn't talk about spiritual things much."
        "I have firm beliefs, but I still want to learn from others.":
            her "I've thought a lot about religion and spirituality, and I have my own reasons for my beliefs, but I still want to learn from others and their experiences."
        "I don't think it matters.":
            her "What does it matter what I believe? I'm only interested in what's true."

    naomi "It is good to want to learn. May I suggest learning about several of the main religions people believe in here on Talam, and let your experiences there guide you further?"
    her "I would like to learn more, yes."
    naomi "I have several books you can borrow, if you would like. But as you study, listen with your heart as well as your mind. Read as if the writer is speaking to you, about your own life, and perhaps you will find some truth that you need."
    $ skill_spiritual += 10
    return

label spiritual_2:
    "One of the books Naomi loaned me was the Dhammapada, a collection of sayings of the Buddha. A lot of it seemed pretty obvious, but I was struck by one part in particular..."
    her "\"For hatred does not cease by hatred at any time: hatred ceases by love, this is an eternal rule.\""
    her "..."
    her "I don't really *hate* anyone, but I think the same thing could be said for disagreements, or times when I feel mad. You don't stop arguing by arguing; you stop arguing with love and seeing the other person's point of view."
    her "Now can I actually *do* that?"

    $ skill_spiritual += 10

    return

label spiritual_3:
    "Sister Naomi also leads worship services once a week. I decided to go see what it was like."
    naomi "...and all are alike unto God. He invites all to come unto him and partake of his goodness. Do you think it matters what planet we are on?  Of course it doesn't. We all have the same access to divine inspiration and guidance, no matter where we are. Now let us pray."
    "We had a few minutes of silence where everyone could pray on their own."
    menu:
        "I..."
        "Didn't know what to say.":
            "I didn't know what to say, so I just kind of sat there. I guess it was peaceful?"
        "Poured out my heart to God.":
            "I poured out my heart to God. I told Him everything that was bothering me, everything that made me happy, and asked for His help. Praying about all that helped me feel at peace."
        "Prayed for peace and understanding.":
            "I wished for an increase in love, peace, and understanding in the  people of Talam -- and Earth. I also prayed for peace in my own heart, and began to feel it even as the services ended."

    "Every week she had different things to say, but she always ended with about ten minutes of just quiet, where people could pray or meditate or just think. I didn't always make time for quiet moments in my everyday life, so I enjoyed this bit of peace."
    $ skill_spiritual += 10

    return


label spiritual_4:
    "Another book Naomi loaned me was the Hindu Upanishads."
    her "\"That one, who is able to visualize the presence of Atma [the Soul] in all other moving things and even creatures and is able to visualize the presence of all such things within the Atma, never gets angry and he never hates anything in life.\""
    her "So...I should try to visualize the souls of all the living things?"
    her "Ugh, even those nasty bugs that sneak in the cracks of our house to drink out of our wash basin?!"
    her "I guess even they have a soul of sorts...they are just thirsty, aren't they? They're not *trying* to scare the crap out of me in the morning. Poor things..."
    her "...and I guess I should try to visualize the souls of other people, too."
    #TODO give example?
    
    $ skill_spiritual += 10
    return

label spiritual_5:
    "I decided to take a break from reading for a while...I wanted to experience some of the things I read about for myself."
    menu:
        "I decided to:"
        "Meditate":
            "I found a quiet place and sat down, emptying my thoughts. I tried to be like the ocean, letting thoughts drift away like bits of kelp. Without my thoughts, what was I?"
            "Without any distractions, without any worldly cares, I could just...*be*. The boundary between myself and other living things seemed smaller, somehow, and I floated in a sea of stars and souls."
        "Pray":
            "I prayed to God to help me find the truth I had been looking for. I prayed that our little colony would make it. I prayed that [his_name] and I would make it. I prayed for forgiveness and comfort and peace and something to fill the emptiness that I felt sometimes even when I was happy."
            "And...I felt something. It was like the feeling you get when you know someone far away is thinking about you, or the feeling you get when someone looks in your eyes and sees your soul, or the feeling of belonging and being loved and knowing everything will be okay."
        "Ponder":
            "As I walked I pondered. I thought about the stars; how many trillions of stars were there, and how small our one little planet was. I marvelled at how many living things there were, just on our own little farm, not to mention in the universe."
            "I was just one of those little lives. Could I make a difference? What was the point of my life, unless I made things better for at least some other little lives near mine?"

    $ relaxed += 5
    $ skill_spiritual += 10
    return

label spiritual_6:
    "In the Koran I read:"
    "\"You will not attain piety until you expend of what you love; and whatever thing you expend, God knows of it.\""
    $ skill_spiritual += 10
    return

label spiritual_7:
    "Naomi sure sent me a lot of books to read...but I think I'm getting something out of them."
    "Today I was reading part of the Tao Te Ching, part of Taoism."
    her "\"I treat those who are good with goodness,\nAnd I also treat those who are not good with goodness.\nThus goodness is attained.\""
    her "\"I am honest with those who are honest,\nAnd I am also honest with those who are dishonest.\nThus honesty is attained.\""
    her "I guess the only person whose goodness or honesty I have any control over is myself."

    $ skill_spiritual += 10
    return

label spiritual_8:
    "I read some of the Tattvartha Sutra, central to Jainism."
    "\"Rendering help to another is the function of all human beings.\""
    her "Our...function? \nThat makes us sound like robots!"
    her "Well, that's a good question - if I was a robot programmed to help other humans, what would I do differently?"

    #TODO give example?

    $ skill_spiritual += 10
    return

label spiritual_9:

    $ skill_spiritual += 10
    return

label spiritual_master:

    $ skill_spiritual += 10
    return
