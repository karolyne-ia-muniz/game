default character_entries = {
    "marcellus": {
        "name": "Marcellus Amos Harriden",
        # "image": "images/marcellus.png",
        "details": [
            "Army Captain. Currently is locaded in Pratterbarrow along side Tenent Novall",
            "."
        ]
    },
        "norvall":{
        "name": "Norval Lucius Bennett",
        #"image" 
        "details":[
            "First Lieutenant, Marcellus second in command. "
        ]
    },
        "selina": {
        "name": "Selina Alexander Bucke",
        # "image": "images/marcellus.png",
        "details": [
            "My mom, that has passed away a while ago.",
            "."
        ]
    }
}


init python:
    def unlock_character_info(character, new_info_count):
        # Increase the amount of information unlocked for the character
        character_entries[character]["unlocked_details"] = min(
            new_info_count, len(character_entries[character]["details"])
        )

init python:
    def notify_new_info(character):
        renpy.notify(f"New information unlocked for {character}!")
