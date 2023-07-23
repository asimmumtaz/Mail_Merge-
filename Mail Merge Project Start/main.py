import glob

PLACE_HOLDER = "[name]"
name_txt = "./Input/Names/invited_names.txt"
letter_txt = "./Input/Letters/starting_letter.txt"
letter_withName = "./Output/ReadyToSend/example.txt"

asim = input("Please enter something: ")

with open(name_txt, "r") as name_file:
    names = name_file.readlines()

with open(letter_txt,"r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACE_HOLDER,stripped_name)
       
        with open(f"./Output/ReadyToSend/{stripped_name}.txt","w") as final_letter:
            final_letter.write(new_letter)
print(asim)
asim = input("Please enter something: ")

# # print(glob.glob("./Output/*/*.txt"))

# textfile = []

# # for file in glob.glob("./Output/*/*.txt"):
# #     textfile.append(file)

# # print(textfile)

# import os

# textfile = os.listdir("./Output/ReadyToSend/")
# print(textfile)

# for ar in textfile:
#     with open(ar, "r") as file:
#         print(file.read())