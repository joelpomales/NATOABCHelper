#!/bin/bash

# Created yesterday!

nato_alphabet=("A" "Alpha" "B" "Bravo" "C" "Charlie" "D" "Delta" "E" "Echo" "F" "Foxtrot" "G" "Golf" "H" "Hotel" "I" "India" "J" "Juliet" "K" "Kilo" "L" "Lima" "M" "Mike" "N" "November" "O" "Oscar" "P" "Papa" "Q" "Quebec" "R" "Romeo" "S" "Sierra" "T" "Tango" "U" "Uniform" "V" "Victor" "W" "Whiskey" "X" "Xray" "Y" "Yankee" "Z" "Zulu")

nato_pronunciation() {
    local word=$1
    local pronunciations=()

    for ((i=0; i<${#word}; i++)); do
        letter=${word:i:1}
        letter=${letter^^}

        found=false
        for ((j=0; j<${#nato_alphabet[@]}; j+=2)); do
            if [[ ${nato_alphabet[j]} == "$letter" ]]; then
                pronunciations+=("[${nato_alphabet[j+1]}]")
                found=true
                break
            fi
        done

        if [[ $found == false ]]; then
            pronunciations+=("$letter")
        fi
    done

    echo "${pronunciations[*]}"
}

if [ $# -gt 0 ]; then
    # If there are arguments, join them into a single string and translate to NATO phonetic alphabet
    letters="$*"
    nato_pronunciation "$letters"
else
    # If there are no arguments, prompt the user to enter a word or phrase and translate it to NATO phonetic alphabet
    read -p "Enter a word or phrase to translate to NATO phonetic alphabet: " word
    nato_pronunciation "$word"
fi

