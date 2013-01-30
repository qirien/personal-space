# Afternoon Events
# Social

# Intro Event and the default
label social_0:
    "I met up with my friend Sara and we talked together. She is a great listener and understands me so well."
    $ skill_social += 10

    return

label social_1:
    "One day I was at the Peron's house. Natalia had found some fruits while hiking that the scientists deemed edible. She had picked so many; her table was covered with them."
    her "These look really good!"
    "Natalia" "Here, try one."
    her "Thanks...Oh!"
    "They tasted sweet and juicy, but they were full of hard, bitter seeds."
    "Natalia" "I'm going to cut them in half, and then scrape out the seeds and dry them. Want to help? You can take some home with you."
    her "Sure!"
    "We cut and scraped and talked together all afternoon."
    $ skill_social += 10
    $ community_level += 2
    return

# Convert shuttle into community center
# TODO: should this be a monthly event? It would be kind of silly if you did this in month 21 or something...
label social_2:
    her "Excuse me, Mayor Grayson?"
    boss "Yes, [her_name]?"
    her "What are we going to do with the shuttle? I know people are recycling a lot of the electronics and the fuel tanks already, but it seems like a waste to have such a nice space just stripped for parts."
    boss "What did you have in mind?"
    her "We could use it for a community center. We need a place where a large number of people can gather, whether it's for community meetings, celebrations, or emergencies."
    boss "That's a great idea! In fact, if I remember correctly, there were some instructions about converting the shuttle into a building. I just hadn't got around to it yet. I'll put the construction group on that as soon as possible."
    "Once the construction group figured out how to convert the shuttle, the mayor asked everyone who could to come help work on the new community center."
    
    $ skill_social += 10
    $ community_level += 2
    return

# Invite family over for dinner
label social_3:
    "Even though we had all lived together for months, there were some people in the community we didn't know very well."
    scene bg farm_interior with fade
    her "I invited the Blairs over for dinner tomorrow night."
    him "Are they the ones that have, like, ten kids?"
    her "Yes..."
    him "Okay, that will be interesting...where are we all going to sit?"
    her "I thought we'd just sit outside. I guess I should make some food that kids like, too."
    him "Maybe some fruit?"
    her "Yeah, I'll figure it out, don't worry."
    "I worked hard on the food, and spread out some blankets to sit on, even though it meant I'd have more laundry to do to get all the dust out."
    scene bg farm_exterior with fade
    "Mrs. Blair" "Thanks so much for having us over for dinner. That doesn't happen very often, you know, since we have such a large family."
    her "Well, hopefully I made enough food! Let's eat!"
    if (skill_domestic >= 10):
        "I served make-your-own-wraps, where you could put in beans or cheese or vegetables or whatever you wanted. I had some salsa or salad dressing that people could put on, too. They were delicious, and the kids liked them too."
    else:
        "I just put out a bunch of beans, rice, fruit, and vegetables, and let people choose what they wanted. It tasted a little bland, but the kids seemed to like it."
    "Then the kids all played hide-and-seek around the farm while we talked with the Blairs."
    if (profession == "teacher"):
        her "The kids are doing great in school."
        "Mrs. Blair" "I'm glad to hear that! They look forward to it; they say you are a wonderful teacher."
        her "That's nice to hear. Joanna is about ready to graduate, I think. She knows way more than I do about geology and physics already."
        "Mrs. Blair" "Yes, it's too bad there's no university here, but I think she will do fine studying with the scientists here."
    if (is_pregnant):
        "Mrs. Blair" "I hear you are expecting a baby, congratulations!"
        her "Thank you! So many new things keep happening; sometimes it's a little overwhelming."
        "Mrs. Blair" "Yes, that's true. But mostly babies just need love. Everything else you can figure out as you go."
        her "But...what if I don't love the baby right away?"
        "Mrs. Blair" "You want to love the baby, don't you?"
        her "Yes, of course!"
        "Mrs. Blair" "Well, that's enough love to start with. Do you have someone to deliver the baby yet?"
        her "I guess I assumed someone at the clinic would do it?"
        "Mrs. Blair" "Let me help you, too. Call me on the radio when it's time, and I'll meet you at the clinic or wherever you are."
        her "Really? That would be great; you seem to be an expert on having kids, but I'm not sure if anyone at the clinic knows much about babies."
        "Mrs. Blair" "I'd be happy to help."
    elif (want_kids):
        her "So...Mrs. Blair, you seem like an expert on kids."
        "Mrs. Blair" "You could say that. Besides my own ten, I've been at twenty deliveries or so, helping the mother through labor."
        her "Really? We want to have kids, sometime..."
        "Mrs. Blair" "Well, I hope you'll let me help you. There's a lot that the doctors don't know about babies and new mothers."
        if (profession == "doctor"):
            her "Yes, I know about all the medical conditions and treatments, but not very much about the actual babies themselves."
        else:
            her "That's probably true..."
    else:
        "[his_name] and I talked to the Blairs about our farms and crops, and what things seemed to help the crops grow better, and what the kids were doing."

    "We talked and talked, until finally, it got dark. One of the moons was shining brightly; the other was dark."
    "Mrs. Blair" "Thanks so much for having us over, [her_name]. I'm glad we got to know you a little better."
    her "Thanks for coming, we enjoyed your company."
    "[his_name] and I watched them start walking for home."
    him "I wonder what our family will look like in a few years?"
    if (want_kids or is_pregnant):
        her "It will be different, won't it?"
    elif (loved >= 0):
        her "As long as you and me are in it, it will be just fine."
    else:
        her "Who knows?"

    scene black with fade
    
    $ skill_social += 10
    $ community_level += 2
    return

#organize lunch group
label social_4:
"Sara and I met for lunch every week to chat and take a break."
Sara "How are your neighbors doing?"
her "We ate with the Blairs a while back and they were healthy! We're all starting to live off the land; it's kind of exciting."
Sara "I know! Hopefully we won't starve or anything. But along with eating, we should be sure to keep ourselves socially healthy too."
menu:
    "I should get out more.":
        her "Yeah, we should see if we can get a lunch group going! Lots of people are on break now; let's ask around."
        "We found a few other people who seemed interested in gathering at the community center for lunch every Friday."
    "I'm not worried.":
        her "I feel pretty socially healthy now. I see you, my boss, and my husband pretty regularly."
        Sara "But we're going to be here the rest of our lives! Shouldn't we get to know everyone?"
        menu:
            "I don't want to meet everyone.":
                her "Sometimes I feel like it's easier to like people when I don't know them."
                Sara "True. And if everyone knew each other we'd be more likely to gossip and get all drama-y."
                her "Maybe I could stand to meet a few new people though."
                Sara "Look, there's someone else on her lunch break, let's introduce ourselves."
                if $met_Lily = False: "We met Lily, one of the workers in the science lab. She invited us to come visit her to learn more about alien botany."
                if $met_Lily = True: "I had already met Lily, but I introduced her to Sara and we had an enjoyable lunch together."
            "I guess.":
                her "Well, if I'm going to meet them all eventually I might as well get to know them sooner rather than later."
                Sara "Exactly. Look, some other people are taking their breaks now too, let's ask them if they want to have lunch with us."
                "We interrupted a few conversations, but luckily everyone was in a good mood and seemed happy to meet us. We decided to meet every Friday for lunch in the community center."
            
    $ skill_social += 10
    $ community_level += 2
    return

# Organize community movie night!
# Watch a neighbor's kids; think about having own kids
label social_5:

    $ skill_social += 10
    $ community_level += 2
    return

# What to do about some gossip? If true, action should be taken, but if not, person could be damaged
label social_6:

    $ skill_social += 10
    return

# Community Shindig
label social_7:
    scene bg path with fade
    play music "music/Prelude22.ogg" fadeout 3.0

    "One day Sara and I took a walk together."
    sara "I think this town needs something special."
    her "Like what? Indoor plumbing?"
    sara "No, silly, I mean a special event! Like a festival, a party, a shindig! Something to cheer everyone up, give them hope."
    her "Yeah, I know what you mean. We've all been working pretty hard..."
    sara "So let's plan one!"
    her "If we got Mayor Grayson in on it, he might have some special food or something we could use."
    sara "Good idea."
    "We asked him about it, and he thought it sounded great."
    boss "It's about time we had a celebration of some kind. Earth Day is in two weeks - we could have it then. But I don't know who to ask to plan it - everyone is so busy..."
    sara "Just leave it to us. We'll have a party ready in two weeks!"
    
    $ party_music = ""
    $ party_entertainment = ""
    $ party_decorations = ""

    "We decided to make it a potluck, so everyone could share the different foods they had grown. We also obtained some goodies from the dwindling rations in the storehouse."
    sara "Look! Potato chips! And fruit punch mix!"
    her "Wow, I haven't had those in...a long time."
    sara "OK, I think we have the food down. What else should we have?"
    menu party_menu:
        "What does the party still need?"
        "Music" if (party_music == ""):
            her "We need some music."
            sara "Yeah...should we use recorded music, or see if we can get someone to play live?"
            menu:
                "What kind of music?"
                "Recorded music":
                    her "Recorded music is fine; then we we have more control over it, and it's better for dancing."
                    sara "Let's get a good playlist setup of lots of different kinds of dance music."
                    her "Good point; everyone here probably likes different things, so I will send out an e-mail asking everyone to send me their favorite dance song."
                    $ party_music = "recorded"
                "Live music":
                    her "Live music is better because it's people you actually know playing the music."
                    if (skill_creative >= 50):
                        her "I can play, you know."
                        sara "Of course! Can you get a group together to play some songs?"
                    else:
                        sara "Yes! That would be so cool. Can you be in charge of that?"
                    her "Sure, I'll send out an e-mail. Maybe some people will want to play or sing solos, too."
                    $ party_music = "live"
                    
            sara "OK, we've got the music!"
            jump party_menu
                                    
        "Entertainment" if (party_entertainment == ""):
            her "We should have some kind of entertainment."
            sara "Yeah, something everyone would like..."
            menu:
                "How about:"                
                "Party games":
                    her "Maybe some party games? Like musical chairs or something? Is that dumb?"
                    sara "Not if we play it right..."
                    her "There are also a lot of people. We might need to split them up into small groups."
                    sara "I have some ideas; leave it to me!"
                    $ party_entertainment = "games"
                "Talent show":
                    her "How about a talent show? I'm sure lots of people have things they can do, even if it's just jokes or a skit or something."
                    sara "Sure! We'll just organize the performances and be the announcers."
                    $ party_entertainment = "talent show"
                "Contest":
                    her "Maybe some kind of contest?"
                    sara "Okay, this is totally redneck, but what about a wood chopping contest?"
                    her "Ha ha, that actually could be fun. We'd need some other contests, too, though..."
                    sara "Leave it to me! I'll have a bunch of fun contests."
                    $ party_entertainment = "contests"
            jump party_menu

        "Decorations" if (party_decorations == ""):
            her "Some kind of decorations would be fun..."
            sara "Yeah, it's not like we can just go to the party store and get some balloons or something, though."
            her "How about wildflowers?"
            sara "Oh, yeah, we could just have a vase of wildflowers on each table."
            her "I'll see if I can get some old jars or bottles to use as vases."
            if (skill_creative >= 20):
                her "Maybe we could glue old papers or scraps of cloth on them to make them look nice? I'll figure something out."
                sara "Sounds good! We don't need a lot of decorations; just enough to show that it's a party. I'll see if I can make the lights in the new community room change color."
            $ party_decorations = "flowers"
            jump party_menu

        "Nothing else":
            her "I think that's enough."
            jump done_party_menu

label done_party_menu:
    "Sara and I worked hard for two weeks getting everything ready. Finally, the night of the party came..."
    scene black with fade
    "As people started to arrive, they seemed to brighten when they saw the community center ready for a party."
    if (party_decorations == "flowers"):
        "The flowers we picked looked nice. Even though they were nothing like Earth flowers, they had their own beauty. And Sara had programmed some of the lights to glow softly blue and green, like an ocean."

    if (party_music == "recorded"):
        "We played some great dance music, and some people really got into dancing! It was really interesting to hear the variety of songs everyone sent us. There was pop music, ballads, slow love songs, techno, rap... Even though some of it was in languages we didn't all know, it was still good for dancing."
    elif (party_music == "live"):
        if (skill_creative >= 50):
            "I was a little nervous about playing music for everyone, but as soon as I started playing I lost myself in the songs."

        "It turned out we had a lot of musicians in our little community. Some of them played together - we had some great Irish dancing music with a fiddle and flute - but there were a lot of solos, too."

    "Everyone brought some food from their farm to share. There were lots of different soups and salads, some strange fruits that Natalia found while hiking, some local game meat, some hearty rolls, and an egg casserole."
    if (have_goat == True):
        "We brought some cheese we had made from our goat's milk, along with a few vegetables."
    else:
        "We brought some fresh vegetables and some salsa."

    if (party_entertainment == "games"):
        "After we ate, Sara broke us up into small groups for games."
        "The first one was 'Two Truths and a Lie' where we each had to tell three things about ourselves, and the group would try to guess which one wasn't true."
        her "Hi, I'm [her_name]. I met my husband [his_name] only six months before coming to Talam, I helped organize this party, and I used to-"
        menu:
            "Used to what? (I need to tell a plausible lie...)"
            "Eat bacon ice cream":
                her "-eat bacon ice cream."
            "Work as a roller-skating carhop":
                her "-work as a roller-skating carhop."
            "Hate looking at the stars":
                her "-hate looking at the stars."
        "Everyone guessed my lie right away, but that's okay. I was more interested in hearing what everyone else had to say."
        him "Hi, my name's [his_name]. I like to write poetry, I won a sheep-riding rodeo when I was five years old, and in high school I was known as The Candid Bandit."
        "(Well, I know he likes to write poetry...but I have no idea which of the other things is true!"
        him "No one has a guess which one of those is a lie?"
        menu:
            "What should I guess?"
            "The sheep-riding is a lie.":
                her "I'll guess the sheep-riding."
                him "Nope!"
            "The Candid Bandit nickname is a lie.":
                her "Nobody called you 'The Candid Bandit'."
                him "You're right. But maybe they should..."
            "I'm not going to guess.":
                "I had no clue."
        him "I really did win a sheep-riding rodeo when I was five. Just held on forever. I wouldn't let go even when they told me it was over. Nobody has called me 'The Candid Bandit' yet, but you can if you want to."
        her "(I'm not going to call him that!)"
                 
        "We also played a game called 'Mafia' where we had to guess who in our group was secretly a bad guy, and also a game called 'Unfortunately' where each person told one sentence of a story, starting with the words 'Fortunately' or 'Unfortunately'."
        "It was fun to get to know our neighbors better and relax for a bit."

    elif (party_entertainment == "talent show"):
        "We had a few entries in the talent show, but not a lot. The Mayor got up and told jokes, some of which were even funny. Some of the Blair children sang a silly song about a goat, and Thuc Nguyen juggled knives. We had no idea he could do that!"
        "But I was even more surprised when [his_name] took the stage. I whispered to Sara,"
        her "You didn't tell me he had an act!"
        sara "I thought you'd like being surprised!  Shhh, watch."
        him "I just have a poem for you all, and then I'll leave you alone."
        "I was apprehensive. His previous 'poems' were not that impressive."
        him "Here on this lonely planet\nFar from that of our birth,"
        him "We're trying to make our own\nNew planet, just like Earth."
        him "The skies aren't really blue here,\nA red sun flares above,"
        him "But we've got what's most important:\nFriends, family, and love."
        him "So though we often struggle\nIn our small community,"
        him "We'd better work and get along,\nOr we'll be extrasolar history."

        menu:
            "That was..."
            "Touching":
                "...actually sort of touching. It wouldn't win any poetry contests, but I think it described how we all felt. Everyone applauded, including myself."
            "Funny":
                "...kind of funny. 'Extrasolar history', hee hee. Everyone seemed to agree with me; they laughed and applauded."
            "Embarrassing":
                "...embarrassing. Poetry should be a private thing, shouldn't it? But the other people seemed to like it, and they applauded politely."
                $ loved -= 5
        "We all felt closer together after enjoying the performances together."

    elif (party_entertainment == "contests"):
        "Next came the contests. Sara was in charge of those."
        sara "All right, listen up! We've got four contests tonight, and I need participants to make these a success! So I hope you will all consider taking part in a contest, even if it's just for fun! The contests are: Wood Chopping, Space Ship Construction, Colony Trivia, and Adamantium Chef."
        menu:
            "Which contest should I enter?"
            "Wood Chopping":
                "I decided to enter the wood chopping contest."
                sara "Line up, everyone! Now, the goal is to see who can chop the most wood in one minute! Ready, set...GO!"
                "I raised the axe and let it fall to split the wood, barely taking time to aim. I was concentrating so hard, I didn't even notice what anyone else was doing."
                him "Go, [her_name]!"
                sara "Time's up!"
                if (skill_physical >= 70):
                    "They counted the wood in each person's pile, and I managed to chop more wood than anyone else! I guess all the exercise I'd been doing really paid off."
                else:
                    "They counted the wood in each person's pile, but I hadn't really chopped very much. My arms were sore and I was sweating all over, but it was still fun."
            "Space Ship Construction":
                "I decided to enter the Space Ship Construction contest."
                sara "This is a game for teams of two, so find a partner!"
                him "Let's do it."
                her "Yeah, you and me, right now."
                sara "I have a box of materials for each team. Your goal is to build the sturdiest and coolest-looking cardboard spaceship you can in five minutes! Then we will launch them from the roof and see whose has the best landing."
                sara "Ready, set...GO!"
                "[his_name] and I rummaged through the box. Sara had gathered trash from everyone and cleaned it off so we could use it on our creation."
                him "Let's make the box the body of the spaceship."
                her "OK, we'll also need some wings..."
                if (loved <= 0):
                    him "Why are you putting that tin foil there?"
                    her "It's reflective, like a solar panel."
                    him "Solar panels aren't reflective."
                    her "We don't have a lot of time! I'm just doing the best I can!"
                else:
                    "We worked together fluidly, like dancers, attaching a piece here and wrapping a piece there, not needing to talk much."
                "We finished just as the time was up."
                if (loved > 0):
                    if (skill_creative >= 70):
                        "Ours didn't have the best landing, but it looked so artistic and sleek that they gave it the best score anyway. We won the contest!"
                    elif (skill_technical >= 70)):
                        "Ours didn't look the best, but it actually kind flew off the roof and glided for a bit before landing gracefully on the ground. We won the contest!"
                else:
                    "Ours was kind of a disaster. We felt relieved when the contest was over."
            "Colony Trivia":
                "I decided to enter the triva contest. They had questions about the shuttle, the colony, and the people on the colony."
                if (skill_knowledge >= 70):
                    "Because of all my research, I was able to answer a lot of the questions about the shuttle and the colony."
                elif (skill_spiritual >= 70):
                    "Because of my connections in the community, I was able to answer a lot of the questions about the people in the colony."
                sara "And for the last question, which will determine the winner of the trivia contest:"
                sara "What is Mayor Grayson's favorite song?"
                menu:
                    "The mayor's favorite song?"
                    "\"Walkin' on the Sun\"":
                        her "\"Walkin' on the Sun\" is his favorite song."
                        sara "Sorry, that's not it."
                        "I didn't win, but I had fun anyway."
                    "\"It Came Out of the Sky\"":
                        her "\"It Came Out of the Sky\" is his favorite song."
                        sara "Sorry, that's not it."
                        "I didn't win, but I had fun anyway."
                    "\"Jupiter\", from 'The Planets'":
                        her "\"Jupiter\", from 'The Planets' is his favorite song."
                        sara "Sorry, that's not it."
                        "I didn't win, but I had fun anyway."
                    "\"It's the End of the World\"":
                        her "\"It's the End of the World\" is his favorite song."
                        sara "That's right! [her_name], you are the winner!"
                        "It was fun win, and also to learn more about everyone."
            "Adamantium Chef":
                "I decided to enter the Adamantium Chef contest."
                $ party_meat = False
                $ party_gravy = False
                $ party_strawberries = False
                $ party_potato_chips = False
                $ party_onions = False
                $ party_cheese = False
                sara "All right, listen up contestants! You have five minutes to make the tastiest concoction you can out of the leftover food on the tables! Ready, set...GO!"
                "We all scanned through the leftovers. We each had a bowl for mixing, and a dish for serving."
                menu party_chef:
                    "I scooped up some:"
                    "Meat" if (not party_meat):
                        "meat. I looked around for the next ingredient."
                        $ party_meat = True
                        jump party_chef
                    "Gravy" if (not party_gravy):
                        "gravy. I looked around for the next ingredient."
                        $ party_gravy = True
                        jump party_chef
                    "Strawberries" if (not party_strawberries):
                        "strawberries. I looked around for the next ingredient."
                        $ party_strawberries = True
                        jump party_chef
                    "Potato Chips" if (not party_potato_chips):
                        "potato chips. I looked around for the next ingredient."
                        $ party_potato_chips = True
                        jump party_chef
                    "Onions" if (not party_onions):
                        "onions. I looked around for the next ingredient."
                        $ party_onions = True
                        jump party_chef
                    "Cheese" if (not party_cheese):
                        "cheese. I looked around for the next ingredient."
                        $ party_cheese = True
                        jump party_chef
                    "Nothing else":
                        "...and I mixed them all together as best as I could."
                if (skill_domestic >= 70):
                    "Despite the strange ingredients, I melded them together into a mouthwatering concoction. The judges picked mine to be the winner!"
                elif (skill_domestic >= 30):
                    "Despite the strange ingredients, I managed to make something that didn't taste terrible, but it certainly wasn't the best."
                else:
                    "I tasted my concotion, and it was pretty terrible. Still, it was fun to play the game."

    sara "Well, the party's almost over, guess it's time to clean up."
    her "Yeah, is that going to be just you and me?"
    boss "Thank you, Sara and [her_name], for organizing such a wonderful celebration for us. I know you've put a lot of work into it. But, folks, I see quite a mess here in our community hall. I don't think it's fair that these two ladies should have to do all the work, so I'd like to ask one person from each family to stay and help clean up."
    "I was relieved to hear that, and even more relieved to see that a lot of people stayed to help clean up. Not just one person from each family, either - entire families got to work clearing plates, putting away chairs, mopping up spills, and doing dishes."
    her "Thanks, Mayor Grayson."
    boss "Thank you! I think the party was a success."

    $ skill_social += 10
    $ community_level += 5
    return

# Teach 'enrichment' class on [profession]
label social_8:

    $ skill_social += 10
    return

label social_9:

    $ skill_social += 10
    return

# Fill vacancy on Community Council
label social_master:

    $ skill_social += 10
    $ community_level += 10
    return
