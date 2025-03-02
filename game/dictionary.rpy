default dictionary_entries = {
    "steampunk": "A genre of science fiction that has a historical setting and typically features steam-powered machinery.",
    "alchemy": "The medieval forerunner of chemistry, focused on the transmutation of matter.",
    # Add other dictionary words here
}


#notify when a new word is learned
init python:
    def notify_new_word(word):
        if word not in persistent.seen_words:
            persistent.seen_words.add(word)
            renpy.notify(f"New word added to dictionary: {word}")


init python:
    def highlight_word(word):
        if word not in persistent.seen_words:
            persistent.seen_words.add(word)
            return "[color=#FFD700]" + word + "[/color]"  # Highlight word in gold
        else:
            return word  # Normal display if already seen
