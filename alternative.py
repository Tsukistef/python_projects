'''Practical Task 1 - Handling Strings, Lists and Dictionaries'''
# A program that reads in a string and makes each alternate character into an upper case character 
# and each other alternate character a lower case character:

def alternate_characters(sample_string):
    i = 0
    new_sample = ""
    for i in range(len(sample_string)):
        if i % 2 == 0:
            new_sample += sample_string[i].upper()
        else:
            new_sample += sample_string[i].lower()
    return new_sample

# A program that reads in a string but makes each alternate word into a lower and upper case:

def alternate_words(sample_string):
    i = 0
    new_list = []
    new_list = sample_string.split(' ')
    new_sentence = ""
    for i in range(len(new_list)):
        if i % 2 != 0:
            new_sentence += new_list[i].upper() + " "
        else:
            new_sentence += new_list[i].lower() + " "
    return new_sentence
        
sample_string = "Fear is the mind killer"
print(alternate_characters(sample_string))
print(alternate_words(sample_string))