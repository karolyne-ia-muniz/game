default character_entries = {
    "selina": {
        "name": "Selina Sterling",
        # "image": "images/marcellus.png",
        "details": [
            "My mom. She died a while ago.",
            "."
        ],
        "unlocked_details": 0
    },

        "marcellus": {
        "name": "Marcellus Amos Harriden",
        # "image": "images/marcellus.png",
        "details": [
            "Army Captain. Currently is locaded in Pratterbarrow along side Tenent Novall",
            "."
        ],
        "unlocked_details": 0
    },
        "norval":{
        "name": "Norval Lucius Bennett",
        #"image" 
        "details":[
            "First Lieutenant, Marcellus second in command. "
        ],
        "unlocked_details": 0
    
    },
        "andrew":{
            "name": "Andrew Alexander Buckle" ,
            # image: "images/andrew.png",
            "details": [
                "One of my oldest friends, alongside Alicia, his sister.",

            ],
            "unlocked_details": 0
    },
        "alicia":{
            "name": "Alicia Alexander Buckle",
            #image,
            "details": [
                "She was my best childhood friend, but with time we grew more distant."
            ],
            "unlocked_details": 0
        }
    
}

screen character_codex():
    tag menu
    use navigation(_("Characters"))

    frame:
        xfill True
        vbox:
            spacing 10
            for char_id, data in character_entries.items():
                if data["unlocked_details"] > 0:
                    frame:
                        xfill True
                        padding (10, 10)
                        vbox:
                            text data["name"] size 24 bold True
                            for i in range(data["unlocked_details"]):
                                text "• [data['details'][i]]"
                            # Optional: show "More info available" if not fully unlocked
                            if data["unlocked_details"] < len(data["details"]):
                                text "(More details to discover...)" italic True color "#aaa"

'''init python:
    def unlock_character_info(character, new_info_count):
        # Increase the amount of information unlocked for the character
        character_entries[character]["unlocked_details"] = min(
            new_info_count, len(character_entries[character]["details"])
        )
'''
init python:
    def notify_new_info(character):
        renpy.notify(f"New information unlocked for {character}!")

init python:
    def unlock_next_character_detail(char_id):
        current = character_entries[char_id]["unlocked_details"]
        total = len(character_entries[char_id]["details"])
        if current < total:
            character_entries[char_id]["unlocked_details"] += 1
            notify_new_info(character_entries[char_id]["name"])