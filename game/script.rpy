# Script for the test game: defines the characters as letters which are easier to call, and uses scenes and different expressions

init python:
    renpy.music.register_channel("LoNoise","bgs")
    renpy.music.register_channel("sound2", "sfx",loop=False)



# The game starts here.

label start:

    $ product = 0
    $ stress = 0
    $ = 0
    
    scene bedroom with dissolve
    pause 0.5

    show Rocco:
        zoom 0.5 xalign 0.23 yalign 1.0
    with pixellate
    pause 0.5

    show Rocco speak
    r "!!!! "

    menu:

        "Choice 1":
            '+ productivity'
            $ product += 1

        "Choice 2":
            '+stress'
            $ stress += 1

        "Choice 3":
            'good'
            $ product += -1

    if product > 2:
        call endingtest
        return

    n "Game over!"
    n "Thanks for playing"
    




