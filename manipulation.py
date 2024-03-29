'''Data Types and Conditional Statements - Task'''
# Ask user to enter a sentence.
user_sentence = input("Enter a sentence: ")

# save user response in variable str_manip.
str_manip = user_sentence

# Using the string value, write code to:
# 1. Calculate and display string length of str_manip;
print(len(str_manip))

# 2. Find the last letter of str_manip;
last_letter = str_manip[-1]

# 3. Replace every occurrence of this letter in str_manip with "@";
str_manip = str_manip.replace(str_manip[-1], "@")
print(str_manip)

# 4. Print the last three characters in str_manip backwards;
print(str_manip[-1:-4:-1])

# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip.
print(str_manip[0:3] + str_manip[-2:])



