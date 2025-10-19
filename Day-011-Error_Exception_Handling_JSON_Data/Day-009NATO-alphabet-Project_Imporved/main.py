import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:

new_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}
# print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    u_input = list(input("Enter a word: ").upper())
    try:
        f_list = [new_dict[letter] for letter in u_input]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(f_list)

generate_phonetic()

# while True:
#     try:
#         u_input = list(input("Enter a word: ").upper())
#         f_list = [new_dict[letter] for letter in u_input]
#     except KeyError:
#         print("Sorry only letters in the alphabet please.")
#     else:
#         print(f_list)
#         break