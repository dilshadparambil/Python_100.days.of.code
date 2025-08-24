# NATO Alphabet Project
# You need to download all files from Intermediate/d26/my_code

import pandas

#TODO 1. Create a dictionary in this format using dictionary comprehension:
# {"A": "Alfa", "B": "Bravo"}
nato_df=pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index,row) in nato_df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_text=input("enter a word").upper()
user_list=[nato_dict[letter] for letter in user_text if letter in nato_dict]
print(user_list)
