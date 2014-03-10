# Afternoon Events
# Spiritual

# the default
label spiritual_def:
    scene bg path with fade
    "I took a walk and spent some time just thinking."
    $ skill_spiritual += 5

    return

# Intro Event
label spiritual_0:
    "I went to the colony's spiritual leader, just to talk. I'd been thinking a lot about what makes us human, and what there may be that we cannot see."
    scene bg church with fade
    show naomi at midright with dissolve
    show her serious at midleft with moveinleft
    "Naomi Grayson" "Welcome, [her_name]. How can I help you?"
    her surprised "Hi...uh, What should I call you, anyway? Pastor? Reverend?"
    naomi "Why don't you call me \"Sister Naomi\"? While I'm not a nun of any religion, I like to emphasize that we are all like children when it comes to matters of the spirit."
    her normal "OK, Sister Naomi...what exactly do you do here?"
    naomi "When people have questions about what they should do, or what to believe, sometimes it is helpful for them to have a guide. Since there are people of many different faiths here on Talam, I try and guide them in a way that is helpful for their religious background."
    her serious "But what do you believe?"
    naomi "Is that really the question you should be asking?"
    her surprised "Huh?"
    naomi "What do {b}you{/b} believe?"

    menu:
        "What do {b}I{/b} believe?"
        "I don't know.":
            her concerned "I don't really know what I believe. My parents didn't talk about spiritual things much."
        "I have strong beliefs.":
            her normal "I've thought a lot about religion and spirituality, and I have my own reasons for my beliefs, but I still want to learn from others and their experiences."
        "I don't think it matters.":
            her annoyed "What does it matter what I believe? I'm only interested in what's true."

    naomi "It is good to want to learn. May I suggest learning about several of the main religions people believe in here on Talam, and let your experiences there guide you further?"
    her normal "I would like to learn more, yes."
    naomi "I have several books you can borrow, if you would like. But as you study, listen with your heart as well as your mind. Read as if the writer is speaking to you, about your own life, and perhaps you will find some truth that you need."
    $ skill_spiritual += 10
    return

# Reading a little each day
label spiritual_1:
    scene bg farm_interior with fade
    show her serious at center with dissolve
    "I downloaded some of the books Naomi sent me and took a look at them."
    "There were books from all over the world, from all different religions."
    "This was going to be a lot of reading."
    "Maybe I'd start on that next time..."
    "I mean, I should probably decide if it was even worth studying."
    "I thought about different religious texts and how and why they were written. A lot of them had been copied by hand over hundreds or thousands of years... clearly, the people writing them had thought they were incredibly important."
    "Even though each writer was partly a product of his or her own culture, they also each felt like they had something new to add, something so important that people passed it on for generations..."
    her surprised "If this is what humanity's ancestors have thought were the most important things to know about being a human, shouldn't I at least take a look?"
    show her normal
    "I decided to read a little bit each day."
    $ skill_spiritual += 10
    return

# Reading the Dhammapada
label spiritual_2:
    scene bg farm_interior with fade
    show her serious at center with dissolve
    "One of the books Naomi loaned me was the Dhammapada, a collection of sayings of the Buddha. There were a lot of good teachings, but I was struck by one part in particular..."
    her serious "\"For hatred does not cease by hatred at any time: hatred ceases by love, this is an eternal rule.\""
    her concerned "..."
    her serious "I don't really {b}hate{/b} anyone, but I think the same thing could be said for disagreements, or times when I feel mad. You don't stop arguing by arguing; you stop arguing with love and seeing the other person's point of view."
    her surprised "Now can I actually {b}do{/b} that?"

    $ skill_spiritual += 10

    return

# Peace in nature
# TODO: Change to Naomi's sermon from events-evening-
label spiritual_3:
    scene bg talam with fade
    "I watched the sun set while flying creatures gathered in the sky."
    show her serious at center with dissolve
    her concerned "They seem so free and at peace... Animals never worry about what someone's saying behind their backs, or try to get other animals in trouble, or worry about their childhoods... I could probably learn a lot from them."
    show her serious
    "I felt peaceful, while at the same time motivated to be better."
    $ skill_spiritual += 10
    return

# Reading the Upanishads
label spiritual_4:
    scene bg farm_interior with fade
    show her normal at center

    "Another book Naomi loaned me was the Hindu Upanishads."
    her serious "\"That one, who is able to visualize the presence of Atma (the Soul) in all other moving things and even creatures and is able to visualize the presence of all such things within the Atma, never gets angry and he never hates anything in life.\""
    her surprised "So...I should try to visualize the souls of all the living things?"
    her annoyed "Ugh, even those nasty bugs that sneak in the cracks of our house to drink out of our wash basin?! I can try..."
    "I thought about it for a few minutes."
    her surprised "I guess even they have a soul of sorts...they are just thirsty, aren't they? They're not {b}trying{/b} to scare the crap out of me in the morning. Poor things..."
    her concerned "...and I guess I should try to visualize the souls of other people, too."
    menu:
        "Whom should I think about?"
        "[his_name]":
            her serious "[his_name]'s soul... Sometimes he acts kind of rude, but I think that is usually when he is worried about something. He probably feels like the whole farm is his responsibility, and if anything goes wrong he has to fix it on his own."
            her normal "So instead of getting mad at him for being rude, maybe I could try and see what he's worried about."
        "My boss":
            her annoyed "I hate it when Mayor Grayson tells me how to do my job... but how does he see the situation?"
            her concerned "..."
            her sad "I guess he probably is worried about the colony, and wants to make sure everything goes well so that we can all survive together."
            her serious "What a huge responsibility that would be! And he actually does a good job, most of the time.  He could use my support, not my annoyance."
        "Sara":
            her annoyed "Sara comes to me about every little problem...sometimes it gets kind of annoying."
            her serious "But I know she doesn't really have any other friends, and her husband isn't much of a talker, either."
            her normal "She always seems to feel better after we talk...maybe if I can keep in mind how important it is to her I can be a better listener and friend to her."

    "Thinking about another person's perspective did help me to understand them better, so maybe I wouldn't get mad at them as easily in the future."
    
    $ skill_spiritual += 10
    return

# Pondering, praying, meditating
label spiritual_5:
    scene bg path with fade
    "I decided to take a break from reading for a while...I wanted to experience some of the things I read about for myself."
    menu:
        "I decided to:"
        "Meditate":
            "I found a quiet place and sat down, emptying my thoughts. I tried to be like the ocean, letting thoughts drift away like bits of kelp. Without my thoughts, what was I?"
            "Without any distractions, without any worldly cares, I could just...{b}be{/b}. The boundary between myself and other living things seemed smaller, somehow, and I floated in a sea of stars and souls."
            "The physical world I could see was such a small portion of the universe..."
        "Pray":
            "I prayed to God to help me find the truth I had been looking for. I prayed that our little colony would make it. I prayed that [his_name] and I would make it. I prayed for forgiveness and comfort and peace and something to fill the emptiness that I felt sometimes even when I was happy."
            "And...I felt something. It was like the feeling you get when you know someone far away is thinking about you, or the feeling you get when someone looks in your eyes and sees your soul, or the feeling of belonging and being loved and knowing everything will be okay."
            "It wasn't lightning or thunder; I didn't faint or scream or shout; but it was {b}something{/b}, and it was something that I wanted to draw closer to."
        "Ponder":
            "As I walked I pondered. I thought about the stars; how many trillions of stars were there, and how small our one little planet was. I marvelled at how many living things there were, just on our own little farm, not to mention in the universe."
            "I was just one of those little lives. Could I make a difference? What was the point of my life, unless I made things better for at least some other little lives near mine?"
            "I felt inspired to do better, and be better."
  
    $ relaxed += 5
    $ skill_spiritual += 10
    return

# Reading the Koran; helping Helen Engel
label spiritual_6:
    scene bg farm_interior with fade
    show her normal at center
    "In the Koran I read:"
    her serious "\"You will not attain piety until you expend of what you love; and whatever thing you expend, God knows of it.\""
    her surprised "What is piety, anyway? Maybe I'll ask Sister Naomi..."
    scene bg church with fade
    show naomi at midright with dissolve
    show her serious at midleft with moveinleft
    naomi "What is piety? Come with me, and I will show you."
    "I followed her across town, and she still kept walking. I started to feel impatient."
    her annoyed "Where are we going?"
    naomi "We are needed."
    scene bg talam with fade
    "We walked past one farm, and then another. We had been walking for almost an hour. Finally, we reached the farthest farm from town. It belonged to the Engels - Helen and Sven were newlyweds like [his_name] and me. They were the farthest farm for a reason; they seemed to like to be by themselves."
    if (profession == "doctor"):
        "I had seen her at the clinic; she was expecting a baby, but due to some complications she had to be on bed rest most of the time."
    elif (skill_social >= 30):
        "I heard she was expecting a baby but had to stay in bed for some reason."
    "When we got there, Sister Naomi knocked on the door and called out,"
    naomi "Helen, it's Naomi. May I come in?"
    helen "Of course, Sister Naomi."
    scene bg farm_interior flip
    show helen at quarterright with dissolve
    show naomi at center
    show her normal at midleft
    with  moveinleft
    "We entered their small cabin, not that much different from our own. Helen was in bed doing some knitting."
    her surprised "What are you making?"
    helen "It's supposed to be a baby hat, but it isn't turning out very well. I don't think any baby's head is shaped like this!"
    "She held up her misshapen knitting and laughed, but I could tell something was really bothering her. Naomi didn't say anything, though - she just held Helen's hand and looked at me. What was I supposed to say?"
    menu:
        "What should I say?"
        "I think the hat looks fine.":
            her normal "I think the hat looks fine. It's not like the baby's going to care if it's a little crooked; he'll just be happy to have a mom who loves him enough to make him a hat at all."
            "She laughed."
            helen "You have a point there. Hopefully it will at least stay on."
        "{i}The problem is with this row of stitches here.{/i}" if (skill_creative >= 60) :
            her serious "The problem is with this row of stitches here. See?"
            helen "Oh, you're right! I'll have to redo these last six rows..."
            her normal "The rest of it looks great; do you like knitting?"
        "It must be hard to stay in bed all day.":
            her concerned "It must be hard to stay in bed all day."
            helen "It's not that hard; all I have to do is sit here. Like a hen sitting on her eggs, keeping this baby alive is about all I'm good for these days."
        "{i}I'm expecting, too{/i}" if is_pregnant:
            her normal "I'm expecting, too."
            helen "Oh? Congratulations."
            her serious "Thanks...It's a weird feeling, isn't it?"
            helen "What is?"
            her concerned "Knowing that someone else, a little stranger, is depending on you so much."
            helen "That's true..."
        "{i}I wish I was expecting, too{/i}" if want_kids and (not is_pregnant):
            her concerned "I wish I was expecting, too."
            helen "Oh...sorry."
            her serious "Yeah, we really want to have kids, but who knows how long it might take?"
            helen "We weren't really anticipating becoming parents so soon..."
            her normal "Well, I think you will do great. It's cool that you're making something for the baby."

    "We sat in silence for a few minutes. I didn't know what to say. I hoped Naomi would say something wise and comforting, but she didn't."
    helen "The truth is, I hate knitting."
    her surprised "You do?"
    helen "Yes! But the one thing I hate more than knitting is feeling useless! I wish I could be helping Ilian with the garden, or working at the library, or {b}something{/b} other than sitting around for three more months!"
    helen "At least this way I'm accomplishing something, even if it's just embarassing myself."
    her serious "Helen, it's not how much we get done that counts."
    helen "What does count, then?"
    menu:
        her "It's.."
        "Relationships":
            her normal "It's the relationships you are building with other people, like your husband and your new baby."
            helen "I don't feel like I'm building relationships. I feel like I'm wasting my time."
        "Love":
            her normal "It's the love you nurture in your heart and the hearts of others."
            helen "I don't think I'm doing that. I'm just sitting here."
        "Good Deeds":
            her normal "It's the things you do for others that matter most."
            helen "I can't do anything! I just sit here, all day!"
        "Fun":
            her happy "Having fun! That's the most important thing! So if you're not having fun knitting, do something else! It's not worth being sad over."
            helen "What else can I do?! I just have to sit here."
    her surprised "Well, why are you just sitting here?"
    helen "I guess that's what's best for the baby right now."
    her normal "Well, you wouldn't be doing that if you didn't love your baby already. I know it's a sacrifice, but it's worth it. You have a choice, and you are choosing what's best for your baby. You're a great mom already."
    
    "We talked some more about other things, and Naomi left a book that she had brought, and then it was time for us to go. It was getting late, and it would take me a while to walk all the way home from Helen's house, but I felt that it was worth it."
    scene bg path with fade
    show naomi at midleft
    show her normal at midright
    with moveinleft
    show overlay night
    her surprised "But...what did any of that have to do with piety?"
    naomi "You read \"You will not attain piety until you expend of what you love\"."
    her serious "Well...Helen gave up a lot of what she loves - freedom, feeling useful, getting things done."
    naomi "You gave up something today, too."
    her surprised "I did?"
    naomi "You gave of your time, and of yourself. Thank you, [her_name]."
    show her normal
    
    $ skill_spiritual += 10
    $ community_level += 2
    return

# Reading the Tao Te Ching
label spiritual_7:
    scene bg farm_interior with fade
    show her normal at center with dissolve
    "Naomi sure sent me a lot of books to read...but I think I'm getting something out of them."
    "Today I was reading part of the Tao Te Ching."
    her serious "\"I treat those who are good with goodness,\nAnd I also treat those who are not good with goodness.\nThus goodness is attained.\""
    her "\"I am honest with those who are honest,\nAnd I am also honest with those who are dishonest.\nThus honesty is attained.\""
    her surprised "I guess the only person whose goodness or honesty I have any control over is myself. If people were only nice when other people were nice, soon no one would feel like they had to be nice."
    her serious "I guess that's kind of like turning the other cheek, isn't it?"
    "There were a lot of teachings that seemed to be in common across different religions, even if their theology and cultures were widely different."
    her concerned "Some of these scriptures are so old... people sacrificed a lot to make sure they were passed down to future generations... What wisdom will I pass on to future generations?"
    "I thought about that for a long time."

    $ skill_spiritual += 10
    return

# Reading the Tattvartha Sutra
label spiritual_8:
    scene bg farm_interior with fade
    show her normal at center with dissolve

    "I read some of the Tattvartha Sutra, central to Jainism."
    her serious "\"Rendering help to another is the function of all human beings.\""
    her surprised "Our...function? \nThat makes us sound like robots!"
    her normal "Well, that's a good question - if I was a robot programmed to help other humans, what would I do differently?"

    her concerned "Maybe I would think about other people more?"
    her happy "What if I had sensors that could detect when people needed my help? That would sure be handy."
    her serious "I suppose that getting in the habit of thinking about other people would help with that."
    her concerned "I do that sometimes, but how can I remember to think about others more? Just wanting to isn't going to make it happen..."
    her serious "I suppose that's why mindfulness and prayer are such an important part of most religions. Without daily reminders, we forget about the little changes we want to make."

    "I decided to set aside a time each day to think about how I can help all the people in my life. I would even add items to my schedule or to-do list on my computer pad if there were specific things I wanted to do that day."
    "At first it felt a little awkward - slightly as if I was programming a robot."
    "But I was able to think about others more and help them in specific ways."
    her serious "Sara is often lonely; I should invite her to lunch this week.  Hmmm, Ms. Peron was mentioning that she loves potatoes, and I don't think they are growing any on their farm - I could give them some of ours."
    her concerned "[his_name] has been really stressed out lately - he'd probably like it if I spent some time with him."
    her normal "It's been really nice of Sister Naomi to lend me these books and take the time to talk to me so much lately - I should tell her thank you for that."
    
    "They were just little things, but I could tell they meant a lot to the people I helped."

    $ community_level +=3
    $ skill_spiritual += 10
    return

# attending church and praying
label spiritual_9:
    scene bg church with fade
    show naomi at center with dissolve
    "Sometimes I went to the worship services that Sister Naomi led."
    naomi "...we are all invited to come and partake of goodness and peace. Do you think it matters what planet we are on?  Of course it doesn't. We all have the same access to divine inspiration and guidance, no matter where we are."
    naomi "Now let us pray."
    "I thought she was going to pray for us, but instead we had a few minutes of silence where everyone could pray on their own."
    menu:
        "I..."
        "Didn't know what to say.":
            "I didn't know what to say, so I just kind of sat there. I guess it was peaceful."
        "Poured out my heart to God.":
            "I poured out my heart to God. I talked about everything that was bothering me, everything that made me happy, and asked for help. Praying about all that helped me feel at peace."
        "Prayed for peace and understanding.":
            "I wished for an increase in love, peace, and understanding in the  people of Talam -- and Earth. I also prayed for peace in my own heart, and began to feel it even as the services ended."

    "Every week she had different things to say, but she always ended with about ten minutes of just quiet, where people could pray or meditate or just think. I didn't always make time for quiet moments in my everyday life, so I enjoyed this bit of peace."
    $ skill_spiritual += 10
    $ relaxed += 5
    $ community_level += 2

    return

# Reading the Bible
label spiritual_master:
    scene bg farm_interior with fade
    show her normal at center

    "I had read so many religious texts from all over the world, but last I started reading the Bible."
    "I was touched by how many people Jesus helped, and his continual teaching that people stop seeing people who were different as \"others\" but instead treat them as neighbors."
    "A lot of the stories were familiar, but there were some things I had never read before."
    "I read in 1 Thessalonians, \"In every thing give thanks,\" and it made me stop and think."
    her surprised "Can I really give thanks for {b}everything{/b}?"
    "There were a lot of things I was definitely not grateful for - pests, bad weather, sickness, arguments..."
    her concerned "I can't give thanks for those things."
    "But then I read it again."
    her normal "It doesn't say to give thanks {b}for{/b} everything, but {b}in{/b} every thing... so I should give thanks no matter what situation I'm in?"
    her happy "I guess there is always something to be grateful for, even when things are going wrong."
    "I thought about when the bugs had destroyed most of our corn."
    her serious "Even though we lost a lot of our corn, we did learn more about the planet. And our other crops haven't had many pest problems... the weather is nice, and we still have plenty of food to eat."
    her normal "I like my job; I've been doing a lot of good there. And I'll always have [his_name]..."
    her happy "I do have a lot to be thankful for..."
    "I felt my attitude changing even as I recognized how many good things I had in my life."

    scene bg church with fade
    show naomi at midright
    show her normal at midleft
    with dissolve
    # TODO: I was thinking about having Sister Naomi have a stroke, and [her_name] agrees to care for her sometimes to give Pavel a break, and also takes over for her?  Maybe too much... maybe Naomi talks about her own spiritual experiences?
    "Later, I was talking to Sister Naomi, and she mentioned that she was a little sick and hoped she would be feeling better before it was time to deliver her sermon."
    her surprised "You don't have anyone who can fill in for you?"
    naomi "No, I'm the only one who works here at the chapel."
    her concerned "That's no good. You should be able to have a break once in a while."
    naomi "Hmmm, I wonder who could do that..."
    her normal "Why don't you let me handle things this week? Even if you're feeling better, you should take a week off."
    naomi "Yes, I think it would be good for everyone to hear from someone new, anyway. Thank you, [her_name]."

    scene black with fade
    "I was a little nervous about speaking about such important things in front of half the colony. I knew they all had different beliefs, too - I didn't want to offend anyone."
    "But I prayed for help, and decided to prepare a sermon on gratitude, using some stories and verses from all the scriptures I had read."
    
    scene bg church with fade
    show her serious at center
    "The congregation was a little surprised to see me up at the stand instead of Sister Naomi, but we sang and prayed together like normal, and then I delivered my sermon."
    "It wasn't too bad, but it was way too short! I was supposed to talk for another fifteen minutes!"
    "I started to panic, but then a wave of calm swept it away. I had an idea."
    her normal "Let's not wait until later to be grateful. Let's give thanks right now. If you would like, please take turns sharing with us one thing you are grateful for."
    "I sat down. Would anyone volunteer?"
    hide her
    "The silence continued. A few people shuffled in their seats."
    show ilian at center with dissolve
    ilian "I'm thankful for my wife, Sara. She never complains, and is always smiling cheerfully."
    hide ilian
    show lily at center with dissolve
    lily "I'm thankful for electricity."
    hide lily 
    show thuc at center with dissolve
    thuc "I'm grateful to Mayor Grayson. He's fair and cares about everyone."
    hide thuc
    show julia at center with dissolve
    julia "I'm thankful for the doctor's quick care, so Van didn't choke to death."
    hide julia
    "Even some of the kids chimed in."
    "Raul Peron" "No school today!"
    "Miranda Nguyen" "We haven't been eaten by wolfslugs!"
    "Van Nguyen" "Mommy and daddy."
    
    "They were all simple things, but thinking about them made us all feel so blessed and full of hope."
    scene bg church with fade
    show naomi at midright with dissolve
    show her normal at midleft with moveinleft
    naomi "So, how did it go?"
    her happy "It went well! I think it helped that everyone got to give their ideas at the end."
    naomi "That's true; that probably helped make it real for them."
    her normal "I love helping people feel positive and hopeful."
    naomi "We certainly need that here, don't we?"
    her happy "Yes. I'd be happy to help you anytime, Sister Naomi."
    naomi "Thank you. I'm grateful to have you helping me, [her_name]."

    $ skill_spiritual += 10
    $ community_level += 10
    return
