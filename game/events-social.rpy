# Afternoon Events
# Social

# Intro Event and the default
label social_0:
    "I went to town and helped out at the library."
    $ skill_social += 10

    return

label social_1:

    $ skill_social += 10
    return

label social_2:
    $ skill_social += 10

    return

label social_3:
    "One of the things I missed most about Earth was having my own shower and bath. While we washed up well enough with water from the well, we still enjoyed going to the community bath once a week or so to really get clean."
    her "I really need a bath."
    him "Really? You smell great to me."
    her "Ick, you need a bath, too! Let's go tonight."
    # TODO: finish this
    him ""
    $ skill_social += 10
    return

label social_4:

    $ skill_social += 10
    return

label social_5:

    $ skill_social += 10
    return

label social_6:

    $ skill_social += 10
    return

label social_7:

    $ skill_social += 10
    return

label social_8:

    $ skill_social += 10
    return

label social_9:

    $ skill_social += 10
    return

label social_master:

    $ skill_social += 10
    return
