# first ending

label endingtest:

    # screen text_verticalgrid:
    #     hbox:
    #         xalign 0.5
    #         yalign 0.5
    #         spacing 20
    #         frame:
    #             xpadding 40
    #             ypadding 20
    #             xalign 0.5
    #             yalign 0.5
    #             text "This text is on top"
    #         frame:
    #             xpadding 40
    #             ypadding 20
    #             xalign 0.5
    #             yalign 0.5
    #             text "This text is on the bottom"

    screen jump_question:
        frame:
            xpadding 50
            ypadding 30
            xalign 0.9
            yalign 0.1
            textbutton "The Question" action [ToggleScreen("jump_to_the_question"), Jump("the_question")]

    pause 1.0