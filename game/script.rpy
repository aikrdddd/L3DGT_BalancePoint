# Script for the test game: defines the characters as letters which are easier to call, and uses scenes and different expressions

init python:
    renpy.music.register_channel("LoNoise","bgs")
    renpy.music.register_channel("sound2", "sfx",loop=False)


# The game starts here.

label start:

    pause 3.0

    scene home_bedroom with dissolve 

    play LoNoise bgm_whimsy

   
    show Penny sad

    pause 1.0

   
    call pondering
    pause 1.0
    jump k_choice

label violence:
    
    # ends the game
    
    jump ending

label knowledge:
    

    jump ending

menu k_choice:

    "You realise this means war.":
        jump violence

    "Maybe I was too hasty.":
        jump knowledge

label ending:
    
    e "To be continued..."
    return
