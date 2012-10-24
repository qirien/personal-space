# Afternoon Events
# Domestic

# Intro Event and the default
label domestic_0:
    "I cleaned the house and got dinner ready."
    $ skill_domestic += 10

    return

label domestic_1:
    "I planted an herb garden under our front window. When the plants are a little bigger, they will make the food rations taste much better."
    $ skill_domestic += 10
    return

label domestic_2:
    show her normal
    her "I've got to do something about these windows. They are too bright when the sun is low. But it's not as if I can just buy some cloth..."
    if (skill_social >= 10):
        her "I'll ask around for everyone's scraps of cloth, and sew them together to make some curtains"
    else:
        her "I could probably sew these old dishtowels together to make some curtains..."
    her "There! That's better."
    $ skill_domestic += 10
    return

label domestic_3:
    #show her worried at center
    her "Something's been nibbling at my herbs..."
    "I peeked out the window every time I passed, trying to see what it was. Finally, I saw a strange small animal that looked kind of like a cross between a frog and a rabbit. I chased it away, but what about next time?"
    her "I know!  I'll make a fence!"
    "I gathered some sticks from some of the local plants, and tied them together with vines. When I tried to pound in the corners, the sticks broke in the hard dirt."
    #show her angry at center
    "I took a break for a snack and thought about it. I decided to try wetting the dirt first.  Then I was able to pound in the corners and finish my fence."
    #show her happy
    her "Whew! It's done!"
    $ skill_domestic += 10

    return

label domestic_4:

    return

label domestic_5:

    return

label domestic_6:

    return

label domestic_7:

    return

label domestic_8:
    return

label domestic_9:
    return

label domestic_master:
    return
