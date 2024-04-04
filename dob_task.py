'''Practical Task 1 - IO Operations'''
# Write a program that reads the data from the text file provided (DOB.txt) and print out a section of names and one of DOBs.


with open("DOB.txt", 'r') as file:
    lines = file.readlines()

names_list = []
dob_list = []

for line in lines:      #Iterates through the lines and select first 2 words for names, the ones after 2: for dob.
    words = line.split()
    names = ' '.join(words[:2])  # Select the first two words
    names_list.append(names)
    dobs = ' '.join(words[2:])  # Selects everything after the second index
    dob_list.append(dobs)
 
#Printing lists of names and dobs 
print("\nName\n") 
for name in names_list:
    print(name)
print("\nBirthdate\n")
for dob in dob_list:
    print(dob)

