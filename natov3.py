# This one's similar from the other one.

import sys

nato_alphabet = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "Xray", "Y": "Yankee",
    "Z": "Zulu"
}

def nato_pronunciation(word):
    """
    Takes a string as input and returns the NATO phonetic pronunciation of each letter
    """
    pronunciations = []
    for letter in word.upper():
        if letter in nato_alphabet:
            pronunciations.append(f"[{nato_alphabet[letter]}]")
        else:
            pronunciations.append(letter)
    return " ".join(pronunciations)

# Check if the script was called with command line arguments
if len(sys.argv) > 1:
    # If there are arguments, join them into a single string and translate to NATO phonetic alphabet
    letters = " ".join(sys.argv[1:])
    print(nato_pronunciation(letters))
else:
    # If there are no arguments, prompt the user to enter a word or phrase and translate it to NATO phonetic alphabet
    word = input("Enter a word or phrase to translate to NATO phonetic alphabet: ")
    print(nato_pronunciation(word))