import string

def alphabet_position(letter):
    alpha = string.ascii_lowercase
    return alpha.index(letter.lower())

def rotate_character(char, rot):
    alpha = string.ascii_lowercase
    if not char.isalpha():
        return char
    else:
        result = (alpha[(alphabet_position(char.lower())+rot) % 26])
    if char.isupper():
        return result.upper()
    else:
        return result

def encrypt(text, key):
    newtext = ""
    for char in text:
        newtext += rotate_character(char, key)
    return newtext
