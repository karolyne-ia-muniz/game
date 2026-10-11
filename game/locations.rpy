# game/locations.rpy
default location_entries = {
    "pratterbarrow": {
        "name": "Pratterbarrow",
        "image": "images/pratterbarrow.png",
        "description": "A small city located in the border of Qedrurg and Soltara, Praterbarrow represents a what's missing in the big city life, calmness and tranquility. The residents, acostumed with the almost frozen in time city, don't seem to realize the extesion of ongoing war. ",
        "unlocked": False
    }
}

init python:
    def unlock_location(loc_id):
        if not location_entries[loc_id]["unlocked"]:
            location_entries[loc_id]["unlocked"] = True
            renpy.notify(f"New location discovered: {location_entries[loc_id]['name']}!")