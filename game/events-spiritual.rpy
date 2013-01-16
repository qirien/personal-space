# Afternoon Events
# Spiritual

# Intro Event and the default
label spiritual_0:
    scene bg path
    "I took a walk and spent some time just thinking."
    $ skill_spiritual += 10

    return

label spiritual_1:
    scene bg path
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
    her "What do {b}I{/b} believe?"

    menu:
        "What do {b}I{/b} believe?"
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
    her "I don't really {b}hate{/b} anyone, but I think the same thing could be said for disagreements, or times when I feel mad. You don't stop arguing by arguing; you stop arguing with love and seeing the other person's point of view."
    her "Now can I actually {b}do{/b} that?"

    $ skill_spiritual += 10

    return

label spiritual_3:
    scene bg talam
    "I watched the sun set while flying creatures gathered in the sky."
    $ skill_spiritual += 10
    return


label spiritual_4:
    "Another book Naomi loaned me was the Hindu Upanishads."
    her "\"That one, who is able to visualize the presence of Atma (the Soul) in all other moving things and even creatures and is able to visualize the presence of all such things within the Atma, never gets angry and he never hates anything in life.\""
    her "So...I should try to visualize the souls of all the living things?"
    her "Ugh, even those nasty bugs that sneak in the cracks of our house to drink out of our wash basin?!"
    her "I guess even they have a soul of sorts...they are just thirsty, aren't they? They're not {b}trying{/b} to scare the crap out of me in the morning. Poor things..."
    her "...and I guess I should try to visualize the souls of other people, too."
    #TODO give example?
    
    $ skill_spiritual += 10
    return

label spiritual_5:
    scene bg path
    "I decided to take a break from reading for a while...I wanted to experience some of the things I read about for myself."
    menu:
        "I decided to:"
        "Meditate":
            "I found a quiet place and sat down, emptying my thoughts. I tried to be like the ocean, letting thoughts drift away like bits of kelp. Without my thoughts, what was I?"
            "Without any distractions, without any worldly cares, I could just...{b}be{/b}. The boundary between myself and other living things seemed smaller, somehow, and I floated in a sea of stars and souls."
        "Pray":
            "I prayed to God to help me find the truth I had been looking for. I prayed that our little colony would make it. I prayed that [his_name] and I would make it. I prayed for forgiveness and comfort and peace and something to fill the emptiness that I felt sometimes even when I was happy."
            "And...I felt something. It was like the feeling you get when you know someone far away is thinking about you, or the feeling you get when someone looks in your eyes and sees your soul, or the feeling of belonging and being loved and knowing everything will be okay."
            "It wasn't lightning or thunder; I didn't faint or scream or shout; but it was {b}something{/b}, and it was something that I wanted to draw closer to."
        "Ponder":
            "As I walked I pondered. I thought about the stars; how many trillions of stars were there, and how small our one little planet was. I marvelled at how many living things there were, just on our own little farm, not to mention in the universe."
            "I was just one of those little lives. Could I make a difference? What was the point of my life, unless I made things better for at least some other little lives near mine?"

    $ relaxed += 5
    $ skill_spiritual += 10
    return

label spiritual_6:
    "In the Koran I read:"
    "\"You will not attain piety until you expend of what you love; and whatever thing you expend, God knows of it.\""
    her "What is piety, anyway? Maybe I'll ask Sister Naomi..."
    scene bg path
    naomi "What is piety? Come with me, and I will show you."
    "I followed her across town, and she still kept walking. I started to feel impatient."
    her "Where are we going?"
    naomi "We are needed."
    scene bg talam
    "We walked past one farm, and then another. We had been walking for almost an hour. Finally, we reached the farthest farm from town. It belonged to the Engels - they were newlyweds like [his_name] and me. They were the farthest farm for a reason; they seemed to like to be by themselves."
    if (profession == "doctor"):
        "I had seen her at the clinic; she was expecting a baby, but due to some complications she had to be on bed rest most of the time."
    elif (skill_social >= 30):
        "I heard she was expecting a baby but had to stay in bed for some reason."
    "When we got there, Sister Naomi knocked on the door and called out,"
    naomi "Helen, it's Naomi. May I come in?"
    "Helen" "Of course, Naomi."
    "We entered their small cabin, not that much different from our own. Helen was in bed doing some knitting."
    her "What are you making?"
    "Helen" "It's supposed to be a baby hat, but it isn't turning out very well. I don't think any baby's head is shaped like this!"
    "She held up her misshapen knitting and laughed, but I could tell something was really bothering her. Naomi didn't say anything, though - she just held Helen's hand and looked at me. What was I supposed to say?"
    menu:
        "What should I say?"
        "I think the hat looks fine.":
            her "I think the hat looks fine. It's not like the baby's going to care if it's a little crooked; he'll just be happy to have a mom who loves him enough to make him a hat at all."
            "She laughed"
            "Helen" "You have a point there. Hopefully it will at least stay on."
        "The problem is with this row of stitches here." if skill_creative >= 60 :
            her "The problem is with this row of stitches here. See?"
            "Helen" "Oh, you're right! I'll have to redo these last six rows..."
            her "The rest of it looks great; do you like knitting?"
        "It must be hard to stay in bed all day.":
            her "It must be hard to stay in bed all day."
            "Helen" "It's not that hard; all I have to do is sit here. Like a hen sitting on her eggs, keeping this baby alive is about all I'm good for these days."
        "I'm expecting, too" if is_pregnant:
            her "I'm expecting, too."
            "Helen" "Oh? Congratulations."
            her "Thanks...It's a weird feeling, isn't it?"
            "Helen" "What is?"
            her "Knowing that someone else, a little stranger, is depending on you so much."
            "Helen" "That's true..."
        "I wish I was expecting, too" if want_kids & (is_pregnant == False):
            her "I wish I was expecting, too."
            "Helen" "Oh...sorry."
            her "Yeah, we really want to have kids, but who knows how long it might take?"
            "Helen" "We weren't really anticipating becoming parents so soon..."
            her "Well, I think you will do great. It's cool that you're making something for the baby."

    "We sat in silence for a few minutes. I didn't know what to say. I hoped Naomi would say something wise and comforting, but she didn't."
    "Helen" "The truth is, I hate knitting."
    her "You do?"
    "Helen" "Yes! But the one thing I hate more than knitting is feeling useless! I wish I could be helping Jan with the garden, or working at the school, or {b}something{/b} other than sitting around for three more months!"
    "Helen" "At least this way I'm accomplishing something, even if it's just embarassing myself."
    her "Helen, it's not how much we get done that counts."
    "Helen" "What does count, then?"
    menu:
        her "It's.."
        "Relationships":
            her "It's the relationships you are building with other people, like your husband and your new baby."
            "Helen" "I don't feel like I'm building relationships. I feel like I'm wasting my time."
        "Love":
            her "It's the love you nurture in your heart and the hearts of others."
            "Helen" "I don't think I'm doing that. I'm just sitting here."
        "Good Deeds":
            her "It's the things you do for others that matter most."
            "Helen" "I can't do anything! I just sit here, all day!"
        "Fun":
            her "Having fun! That's the most important thing! So if you're not having fun knitting, do something else! It's not worth being sad over."
            "Helen" "What else can I do?! I just have to sit here."
    her "Well, why are you just sitting here?"
    "Helen" "I guess that's what's best for the baby right now."
    her "Well, you wouldn't be doing that if you didn't love your baby already. I know it's a sacrifice, but it's worth it. You have a choice, and you are choosing what's best for your baby. You're a great mom already."
    
    "We talked some more about other things, and Naomi left a book that she had brought, and then it was time for us to go. It was getting late, and it would take me a while to walk all the way home from Helen's house, but I felt that it was worth it."
    her "But...what did any of that have to do with piety?"
    naomi "You read \"You will not attain piety until you expend of what you love\"."
    her "Well...Helen gave up a lot of what she loves - freedom, feeling useful, getting things done."
    naomi "You gave up something today, too."
    her "I did?"
    naomi "You gave of your time and of yourself. Thank you, [her_name]."
    
    $ skill_spiritual += 10
    return

label spiritual_7:
    "Naomi sure sent me a lot of books to read...but I think I'm getting something out of them."
    "Today I was reading part of the Tao Te Ching."
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
    scene bg wedding
    "Sometimes I went to the worship services that Sister Naomi led."
    naomi "...and all are alike unto God. He invites all to come unto him and partake of his goodness. Do you think it matters what planet we are on?  Of course it doesn't. We all have the same access to divine inspiration and guidance, no matter where we are."
    naomi "Now let us pray."
    "I thought she was going to pray for us, but instead we had a few minutes of silence where everyone could pray on their own."
    menu:
        "I..."
        "Didn't know what to say.":
            "I didn't know what to say, so I just kind of sat there. I guess it was peaceful."
        "Poured out my heart to God.":
            "I poured out my heart to God. I told Him everything that was bothering me, everything that made me happy, and asked for His help. Praying about all that helped me feel at peace."
        "Prayed for peace and understanding.":
            "I wished for an increase in love, peace, and understanding in the  people of Talam -- and Earth. I also prayed for peace in my own heart, and began to feel it even as the services ended."

    "Every week she had different things to say, but she always ended with about ten minutes of just quiet, where people could pray or meditate or just think. I didn't always make time for quiet moments in my everyday life, so I enjoyed this bit of peace."
    $ skill_spiritual += 10
    $ relaxed += 5

    return

label spiritual_master:

    $ skill_spiritual += 10
    return