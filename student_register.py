'''Practical Task 2 - IO Operations'''
# A program that allows users to register students for an exam venue.

with open('reg_form.txt', 'w+') as file:
    try:      # Handles exception in case a number is not provided  
        num_students = int(input("How many students are going to register? "))
    except ValueError:
        print("Please provide a number")
        num_students = int(input("How many students are going to register? "))      # User input number students

    for i in range(num_students):       # Iterates through the number of students enrolled, asking for each ID
        id_student = input("Please provide ID student: ")
        file.write(str(id_student) + '\n')      #Adds the IDs to .txt file
        file.write('------------------------------\n')      # Adds dotted line after each ID