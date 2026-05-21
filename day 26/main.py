#============= DAY 26 ================#
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

phonetic_dict = {row.letter: row.code for (index,  row) in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

#============ DAY 30 =================#
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

phonetic_dict = {row.letter: row.code for (index,  row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters allowed.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
