# File: affection.rpy

'init python:
    # You could even make a helper function
    def adjust_affection(char, amount):
        if char == "andrew":
            global affection_andrew
            affection_andrew += amount
        elif char == "marcellus":
            global affection_marcellus
            affection_marcellus += amount
        elif char == "norval":
            global affection_norval
            affection_norval += amount
            '

default affection_andrew = 0
default affection_marcellus = 0
default affection_norval = 0