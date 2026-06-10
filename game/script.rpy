# Script for the test game: defines the characters as letters which are easier to call, and uses scenes and different expressions

init python:
    renpy.music.register_channel("LoNoise","bgs")
    renpy.music.register_channel("sound2", "sfx",loop=False)

default show_message = True

screen new_main_menu():

    grid 2 2:
        if show_message:
            text "Welcome back!" align (0.5,0.3)
        align (0.5,0.5)

        textbutton "Start" action Start()
        textbutton "Load" action ShowMenu("load")
        textbutton "Settings" action ShowMenu("preferences")
        textbutton "Quit" action Quit()

label start:
    
    call screen new_main_menu

    return
    # $ product = 0
    # $ stress = 0
    
    # scene bedroom with dissolve
    # pause 0.5

    # show Rocco:
    #     zoom 0.5 xalign 0.23 yalign 1.0
    # with pixellate
    # pause 0.5

    # show Rocco speak
    # r "!!!! "

    # menu:

    #     "Choice 1":
    #         '+ productivity'
    #         $ product += 3

    #     "Choice 2":
    #         '+stress'
    #         $ stress += 1

    #     "Choice 3":
    #         'good'
    #         $ product += -1

    # if product > 2:
    #     call custom_screens
    #     return

    # n "Game over!"
    # n "Thanks for playing"
    




