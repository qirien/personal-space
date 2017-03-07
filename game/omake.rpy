#TODO: Add omake about baby?

label omake:
    scene black with fade
    "In Japan, \"omake\" are extra or deleted scenes for a show or game."
    "So here is an omake from {i}Our Personal Space{/i}."
    call brennan_omake from _call_brennan_omake
    return
    
label brennan_omake:
    scene bg path with fade
    show brennan normal with dissolve
    
    brennan "Nothing like a nice bath after a hard day's work... Hopefully no one's using it."
    
    scene bg bathhouse with fade
    $ is_nude = True
    show her serious at midright, squatting
    show him nude serious at midleft, squatting
    show bathhouse_overlay
    with dissolve
    
    her normal "So then he says, \"I'd never forget a pretty face like yours.\""
    him nude surprised "Seriously!?  What a cheeseball!"
    her annoyed "I know! Like I'm supposed to feel flattered because some random guy likes my physical appearance."
    him nude happy "And you've already got me, so what more could you want in a man?"
    her flirt "I don't know, maybe more flattering cheesy lines?"
    him nude serious "Ohhh, [her_nickname], you're so sexy, you make my heart race faster than a space shuttle."
    her serious "You're so sexy, you're illegal to bring on space shuttles."
    him nude happy "Ha ha ha!"
    her laughing "Ha ha ha ha ha!"
    
    brennan "..."
    
    scene bg path with fade
    $ is_nude = False
    show brennan normal with dissolve
    brennan mad "There go my plans for a bath."
    brennan normal "Maybe I'll see if Pete's busy..."
    
    scene bg library with fade
    show pete at midleft
    show helen at midright
    show baby boy at midrightbaby
    with dissolve
    pete happy "You're the Milky Way in my night sky, baby."
    helen "Is that a nursing joke?"
    pete normal "Nah, I was just tryin' to be romantic."
    helen "Sorry, it's hard for me to think about anything else while I'm feeding the baby. Can we be romantic when I'm done?"
    pete "No time like the present. How 'bout I rub your feet until you're done?"
    show pete at squatting with move
    helen happy "Ohhh. Mmmmm. Oh, Pete, that feels sooo good."
    
    brennan "..."
    
    scene bg path with fade
    show brennan with dissolve
    brennan mad "Sounds like he's busy."
    brennan normal "Maybe I'll just head home."
    
    scene bg farm_interior flip with fade
    show pavel at midleft    
    show naomi sad at midright
    with dissolve
    
    pavel "{i}Priya{/i}, have you seen my computer around here?"
    naomi "Yes, it's right here, but I wanted to speak with you first."
    pavel "What is it?"
    naomi "That was very kind of you, what you did for Miranda today."
    pavel "What? I just asked her to see if she would mind babysitting for our new parents once in a while."
    naomi normal "But it helped her feel like you trusted her, as an adult member of the community. That is just what she needed."
    pavel "Well, good. I'm just trying to help everyone..."
    naomi "I know you are, beloved. That's one of the things I adore about you."
    pavel "I couldn't do it without you, {i}priya{/i}."
    show pavel at center with move
    
    brennan "..."
    
    scene bg sunset with fade
    show brennan at midleft with dissolve
    brennan mad "I don't want to interrupt... they don't have that many romantic moments."
    brennan happy "At least there's a beautiful sunset."
    
    brennan happy "..."
    show lily at midright with moveinright
    show brennan normal
    lily "Brennan?"
    brennan happy "Dr. Lily! It's so pleasant to see someone who--"
    lily upset "Someone who what?"
    brennan normal "Someone who is not snogging."
    lily normal "Oh. No, I have not been doing that."
    brennan "What brings you this way?"
    lily upset "It is the anniversary of Winston's death. I found some flowers, and thought I might place them on his grave."
    brennan "Winston was your husband, right?"
    lily normal "Yes."
    brennan normal "...I see. Well, don't let me stop you."
    lily "I won't."
    hide lily with moveoutleft
    brennan normal "...Bye."
    brennan mad "Even Dr. Lily has someone..."
    brennan normal "..."
    play bg_sfx "sfx/clipclop.mp3"
    brennan mad "Who's there?!"
    
    show lettie at right with moveinright
    brennan normal "Lettie?"
    play bg_sfx "sfx/whinny.mp3"
    brennan happy "Did I ever tell you what a good-looking horse you are?"
    play bg_sfx "sfx/horse-snort.mp3"
    brennan normal "I haven't? Well, just look at those long, straight legs! And that wavy mane! And, if I may be so bold, a marvelous tail."
    play bg_sfx "sfx/whinny.mp3"
    brennan "At least {b}you{/b} understand."
    
    scene black with fade
    
    "End .:."
    return