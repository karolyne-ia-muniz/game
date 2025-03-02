define ly = Character("Lydia")
define pov = Character("[povname]")
define ma = Character("Marcellus")
define no = Character("Norval")
define an = Character("Andrew")
define se = Character("Selina")
define a = Character("Alicia")
define b = Character("Benedict")

define persistent.seen_words = set()

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


    


# The game starts here.

label start:
    $ povname = renpy.input("What is your name?" , length = 30)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Lydia"
    pov "My name is [povname]."
    jump chapter1

    return
