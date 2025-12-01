default character_entries = {
    "selina": {
        "name": "Selina Sterling",
        # "image": "images/marcellus.png",
        "details": [
            "My mom. She died a while ago.",
            "."
        ]
    },

        "marcellus": {
        "name": "Marcellus Amos Harriden",
        # "image": "images/marcellus.png",
        "details": [
            "Army Captain. Currently is locaded in Pratterbarrow along side Tenent Novall",
            "."
        ]
    },
        "norval":{
        "name": "Norval Lucius Bennett",
        #"image" 
        "details":[
            "First Lieutenant, Marcellus second in command. "
        ]
    
    },
        "andrew":{
            "name": "Andrew Alexander Buckle" ,
            # image: "images/andrew.png",
            "details": [
                "One of my oldest friends, alongside Alicia, his sister.",

            ]
    },
        "alicia":{
            "name": "Alicia Alexander Buckle",
            #image,
            "details": [
                "She was my best childhood friend, but with time we grew more distant."
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
