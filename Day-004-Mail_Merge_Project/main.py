#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    sample_letter = letter_file.read()   

with open("./Input/Names/invited_names.txt", "r") as names_file:
    invited_names = names_file.readlines()

for name in invited_names:
    name = name.strip()
    new_letter = sample_letter.replace("[name]", name)
    
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as out_file:
        out_file.write(new_letter)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp