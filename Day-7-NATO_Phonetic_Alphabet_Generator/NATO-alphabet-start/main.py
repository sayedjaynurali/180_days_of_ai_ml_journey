import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:

new_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}
# print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
u_input = list(input("Enter a word: ").upper())
f_list = [new_dict[letter] for letter in u_input if letter in new_dict]
print(f_list)