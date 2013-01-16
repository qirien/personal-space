# Event content for all the events that can happen in the evening,
# where we relax together

# Relationship Focus Events
# TODO; Have them talk about missing (or not) families on Earth.
# TODO: Have them tour the farm and talk about progress/problems
# TODO: Sunset on the new planet


label relax_together_0:
    "We watched a movie together. It was pretty good, but the ending was terrible."
    him "See, what they needed was to have the girlfriend show back up at the end--"
    her "--leading a horde of zombie warriors! Oh, that would have been so much better!"
    him "And what about the pterodactyl? They didn't do anything with that."
    her "I know, I kept thinking someone was going to ride it."
    him "I thought it was going to turn out to be a cyborg pterodactyl."
    her "That would have been awesome!"
    "Sometimes talking about the movie is more fun than the actual movie itself..."
    $relaxed += 5
    $loved += 5
    return

label relax_together_1:
    "One of the things I missed most about Earth was having my own shower and bath. While we washed up well enough with water from the well, we still enjoyed going to the community bath once a week or so to really get clean."
    her "I really need a bath."
    him "Really? You smell great to me."
    her "Ick, you need a bath, too! Let's go tonight."
    him "Sure, after dinner and...dessert."
    her "You made dessert?! What kind?"
    him "I was thinking we'd make some dessert...together."
    her "Ohhh, {b}that{/b} kind of dessert. The kind we don't need to use sugar rations for..."
    him "Yes...though we could have dessert first, you know. Sometimes it's fun to break the rules."
    menu:
        "\"Dessert\" first?"
        "Dinner first.":
            her "How about dinner first? You can think of it as an appetizer..."
            him "Hmmm, you're very appetizing."
            "We played footsie under the table while we ate and gave each other suggestive looks. Dinner didn't last very long..."
            $ loved += 5
            $ made_love += 1
        "Dessert first.":
            her "Life is short; eat dessert first!"
            "And what a dessert it was..."
            $ loved += 5
            $ made_love += 1
        "No dessert tonight.":
            her "I think I'd rather skip dessert tonight..."
            him "Oh...okay. Sure, let's just eat dinner."
            $ loved -= 2
    "Afterwards, we packed up our towels and toiletries and headed down to the bathhouse."
    "We built a fire to heat up one of the tubs of water, and took turns washing off and then soaking in the small tub."
    "It felt so good to soak and relax together."
    $ relaxed += 5
    return

label relax_together_2:
    return

label relax_together_3:
    return

label relax_together_4:
    return

label relax_together_5:
    return

label relax_together_6:
    return

label relax_together_7:
    return

label relax_together_8:
    return

label relax_together_9:
    return

label relax_together_10:
    return

label relax_together_11:
    return

label relax_together_12:
    return

label relax_together_13:
    return

label relax_together_14:
    return

label relax_together_15:
    return

label relax_together_16:
    return

label relax_together_17:
    return

label relax_together_18:
    return

label relax_together_19:
    return

label relax_together_20:
    return

label relax_together_21:
    return

label relax_together_22:
    return

label relax_together_23:
    return
