# Script for the test game: defines the characters as letters which are easier to call, and uses scenes and different expressions

init python:
    renpy.music.register_channel("LoNoise","bgs")
    renpy.music.register_channel("sound2", "sfx",loop=False)


# The game starts here.

label start:

    pause 3.0

    r "Hello!!!"


