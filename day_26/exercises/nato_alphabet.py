import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

letters = {row.letter: row.code for (index,row) in
           data.iterrows()}

name = input("Write your name\n")
name_in_code = [letters[letter.upper()] for letter in name]
print(name_in_code)
