'''Practical Task 1 - Handling Strings, Lists and Dictionaries'''
# A program that reads in a string and makes each alternate character into an upper case character 
# and each other alternate character a lower case character:

def alternate_characters(sample_string):
    i = 0                                   # i is the string index
    new_sample = ""
    for i in range(len(sample_string)):     # This loop alternates characters, converting into upper and lower characters.
        if i % 2 == 0:
            new_sample += sample_string[i].upper()
        else:
            new_sample += sample_string[i].lower()
    return new_sample                       # Returns new string

# A program that reads in a string but makes each alternate word into a lower and upper case:
def alternate_words(sample_string):
    i = 0                                   # index for list
    new_list = []                           # Initialized list
    new_list = sample_string.split(' ')     # Utilizes space to create new list
    new_sentence = ""                       # Initialized string that will take the converted items from list.
    for i in range(len(new_list)):          # This loop alternates the strings in the list, converting into upper and lower case words.
        if i % 2 != 0:
            new_sentence += new_list[i].upper() + " "
        else:
            new_sentence += new_list[i].lower() + " "
    return new_sentence
        
sample_string = "Fear is the mind killer"   # Sample sentence
print(alternate_characters(sample_string))  # Calling function for Task 1 pt. 1
print(alternate_words(sample_string))       # Calling function for Task 1 pt. 2