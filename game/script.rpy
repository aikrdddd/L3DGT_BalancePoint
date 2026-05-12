# Script for the test game: defines the characters as letters which are easier to call, and uses scenes and different expressions

init python:
    renpy.music.register_channel("LoNoise","bgs")
    renpy.music.register_channel("sound2", "sfx",loop=False)


# The game starts here.

label start:

    pause 2.0

    scene home_bedroom with dissolve 

    pause 0.5

    show Penny happy:
        zoom 0.5 xalign 0.33 yalign 1.0
    show Blake happy:
        zoom 0.5 yalign 1.0 xalign 0.66
    with pixellate

    pause 0.5
    p"I created a new Ren'Py game."
    b "I learnt how to use pause and transitions"

    show Penny:
        easein 3.0 xalign 0.66

    show Blake:
        easeout 3.0 xalign 0.33

    pause 0.5
    play LoNoise bgm_whimsy

    p "I learnt how to use {b}images and dialogue!{/b}"

    b "Not like it was all that difficult to learn, {i}you don't have much to {size=50}brag{/size} about...{/i}"

    show Penny sad

    pause 1.0

    show Penny angry:
        easein 0.3 xalign 0.5
    pause 0.2
    play sound sfx_punch

    pause 0.1
    play sound2 sfx_shock
    show Blake sad:
        easein 0.05 xalign 0.73

    p "What would you know?! Your hands never leave your pockets!"

    pause 1
    show Blake angry
    stop music

    pause 0.5
    play sound2 sfx_shock
    b "DID YOU JUST SMACK ME ON THE HEAD?!"
    call pondering
    pause 1.0
    jump k_choice

label violence:
    pause 1.0
    show Blake angry with dissolve
    b "You should've seen this coming!"
    play sound2 sfx_punch 
    pause 0.2
    scene black
    pause 1.0


    # ends the game
    
    jump ending

label knowledge:
    pause 1.0
    show Blake sad
    b"Okay, maybe I dont know enough about this kinda thing. Teach me?"
    pause 1.0
    show Penny happy with dissolve
    p"You know that was all I wanted to hear."
    pause 1.0
    scene black with dissolve
    pause 1.0

    jump ending

menu k_choice:

    "You realise this means war.":
        jump violence

    "Maybe I was too hasty.":
        jump knowledge

label ending:
    
    e "To be continued..."
    return
