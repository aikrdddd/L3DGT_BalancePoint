# Script for the test game: defines the characters as letters which are easier to call, and uses scenes and different expressions

init python:
    renpy.music.register_channel("LoNoise","bgs")

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
    

    $ product = 0
    $ stress = 0
    
    scene bedroom with dissolve
    pause 0.1

    show Rocco:
        zoom 0.16 xalign 0.3 yalign 0.1
    with fade

    n "It's Monday Morning"

    show Rocco speak
    r "!!!! "
    r "I've gotta go to school today. Seems like I still have some time."

    show Rocco
    pause 0.1

    n "What should Rocco do?"
    menu:

        "Start homework immediately":
            n 'Remember to have some time for yourself in the mornings!'
            $ product += 1
            $ stress += 1

        "Check your phone":
            show Rocco cry
            n 'Putting things off and staring at a screen for your first moments of the day can put your mood down'
            show Rocco
            $ product -= 1
            $ stress += 1

        "Make a quick day plan":
            show Rocco smile
            n 'Creating a simple plan can reduce stress and make large tasks feel more manageable.'
            show Rocco
            $ product += 1

    scene bg town with dissolve
    pause 0.1

    show Rocco:
        zoom 0.16 xalign 0.3 yalign 0.1

    n "It's Monday Lunch"
    f "C'mon dude, you should let loose and hang with us!"
    n"Should Rocco go out or stay in?"

    menu:

        "Go with friends for the whole afternoon":
            show Rocco cry
            n 'Dont avoid your work..'
            show Rocco
            $ product -= 1
            $ stress += 1

        "Decline and focus only on work":
            show Rocco cry
            n 'Youre overworking yourself!'
            show Rocco
            $ product += 1
            $ stress += 1

        "Join friends briefly, then leave early to go do work":
            show Rocco smile
            n 'Making room for both responsibilities and social activities can help maintain motivation and well being'
            show Rocco
            $ product += 1
            $ stress -+ 1
    
    if product > 1:
        show Rocco smile
        n "You were quite productive today"
        show Rocco
        return

    else:
        show Rocco cry
        n "You weren't very productive.."
        show Rocco
        return

        
    n "Game over!"
    n "Thanks for playing"

    




