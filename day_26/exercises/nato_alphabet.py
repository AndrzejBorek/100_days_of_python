import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
letters = {row.letter: row.code for (index, row) in
           data.iterrows()}


def word_to_nato_fonetic():
    try:
        word = input("Write your word\n")
        word_in_code = [letters[letter.upper()] for letter in word]
    except KeyError as e:
        print("You can only write characters")
        word_to_nato_fonetic()
    else:
        print(word_in_code)


word_to_nato_fonetic()
