# Mail Merge 
# You need to download the Input and Output directories from Intermediate/d24/my_code

with open("./Input/Names/invited_names.txt") as name_file:
    name_list=name_file.readlines()

with open ("./Input/Letters/starting_letter.txt") as letter_file:
    contents=letter_file.read()
    for name in name_list:
        fixed_name=name.strip()
        fixed_contents=contents.replace("[name]",fixed_name)
        print(fixed_contents)
        with open(f"./Output/ReadyToSend/letter_for_{fixed_name}","w") as output_file:
            output_file.write(fixed_contents)
