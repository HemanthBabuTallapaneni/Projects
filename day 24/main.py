PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()
with open("./Input/Letters/starting_letter.txt") as letter:
    letters = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letters.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
