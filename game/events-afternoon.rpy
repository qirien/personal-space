# Event content for all the events that can happen in the afternoon,
# where we work on a hobby

# Basic Afternoon Events
label act_domestic:
    "I cleaned the house and got dinner ready."
    $ skill_domestic += 10

    return

label act_creative:
    "I worked on a quilt for our bedroom."
    $ skill_creative += 10

    return

label act_technical:
    "I tuned up some of the farm equipment."
    $ skill_technical += 10

    return

label act_spiritual:
    "I took a walk and spent some time just thinking."
    $ skill_spiritual += 10

    return

label act_social:
    "I went to town and helped out at the library."
    $ skill_social += 10

    return

label act_knowledge:
    "I read up on the latest science research."
    $ skill_knowledge += 10

    return

label act_physical:
    "I went for a run and lifted some weights."
    $ skill_physical += 10

    return


# DOMESTIC EVENTS

label domestic_1:
    "I planted an herb garden under our front window. When the plants are a little bigger, they will make the food rations taste much better."
    $ skill_domestic += 10
    return

label domestic_2:
    her "I've got to do something about these windows. They are too bright when the sun is low. But it's not as if I can just buy some cloth..."
    if (skill_social >= 10):
        her "I'll ask around for everyone's scraps of cloth, and sew them together to make some curtains"
    else:
        her "I could probably sew these old dishtowels together to make some curtains..."
    her "There! That's better."
    $ skill_domestic += 10
    return

