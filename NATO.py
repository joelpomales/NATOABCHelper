# First attempt at the script
# Created by ChatGPT with my guidance. 2023-03-26

# Define a dictionary that maps each letter to its corresponding pronunciation
nato_alphabet = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu"
}

# Define a function that takes a string as input and returns the corresponding NATO phonetic alphabet
def nato_spelling(word):
    spelling = []
    for letter in word.upper():
        if letter in nato_alphabet:
            spelling.append(nato_alphabet[letter])
        else:
            spelling.append(letter)
    return spelling

# Test the function
word = input("Enter a word: ")
print(nato_spelling(word))