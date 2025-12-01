define ly = Character("Lydia")
define pov = Character("[povname]")
define ma = Character("Marcellus")
define no = Character("Norval")
define an = Character("Andrew")
define se = Character("Selina")
define a = Character("Alicia")
define b = Character("Benedict")
define air = Character("Pilot")

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
    image PoseMyteste = "images/PoseMyteste.png"
    image teste1 = "images/teste1.png"
    image living = "images/living.jpg"
    jump chapter1

    return

#"# Debug screen: Affection Tracker
#label debug_affection:
#   scene bg black
#  show screen debug_affection_screen
#    pause  # Wait for click or keypress
#    hide screen debug_affection_screen
#    return

# In script.rpy — only while testing!
#init python:
#    config.keymap['debug_affection'] = ['d']  # Press D to open debug''

#label after_load:
#    if config.developer:
#        $ renpy.call_in_new_context(debug_affection_hotkey)

#label debug_affection_hotkey:
#    python:
#        ui.keymap(debug_affection=["d"])
#        ui.interact(suppress_overlay=True, suppress_underlay=True)
#    return"