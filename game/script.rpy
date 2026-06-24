# Script for the test game: defines the characters as letters which are easier to call, and uses scenes and different expressions

init python:
    renpy.music.register_channel("LoNoise","bgs")
    renpy.music.register_channel("sound2", "sfx",loop=False)

# default show_message = True

# screen new_main_menu():

#     grid 2 2:
#         align (0.5,0.5)

#         textbutton "Start" action Start()
#         textbutton "Load" action ShowMenu("load")
#         textbutton "Settings" action ShowMenu("preferences")
#         textbutton "Quit" action Quit()

# first scene
label start:
    
    # call screen new_main_menu

    $ product = 0
    $ stress = 0
    
    scene bedroom with dissolve
    pause 0.5

    show Rocco:
        zoom 0.16 xalign 0.3 yalign 0.1
    with pixellate
    pause 0.5

    show Rocco speak
    r "!!!! "
    
Go with friends for the whole afternoon
If player chooses "Go with friends for the whole afternoon"

Narration  
Avoiding tasks 

-1 Productivity
+1 Stress


Should Rocco go 
out or stay in?
Decline and only focus on work
If player chooses "Decline and focus only on work"

Narration
Overworking!

+1 Productivity
+1 Stress


Join friends briefly, then leave 
early to go do work




If player chooses "Join friends briefly, then leave to focus on tasks”

Narration:
Making room for both responsibilities and social activities can help maintain motivation and well being

+1 Productivity
-1 Stress

    menu:

        "Start homework immediately":
            '+ productivity + stress'
            $ product += 1
            $ stress += 1

        "Check your phone":
            '+ stress'
            $ product -= 1
            $ stress += 1

        "Make a quick day plan":
            '+ productivity'
            $ product += -1


    if product > 2:
        # call custom_screens
        # return
        n "You were quite productive today"
        return

    else:
        n "You weren't very productive.."
        return

    n "Game over!"
    n "Thanks for playing"
    




