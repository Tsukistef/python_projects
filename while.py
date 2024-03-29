'''Iteration - Task 1'''
# Create a file called while.py.
# Write a program that continually asks the user to enter a number.
# When the user enters “-1”, the program should stop requesting the user to enter a number,
# The program must then calculate the average of the numbers entered, excluding the -1.
# Make use of the while loop repetition structure to implement the program.

sum = 0
counter = 0
i = 0
num_different = False
# while loop 
while num_different == False:       
    i = int(input("Enter a number: "))
    if i == -1:
        num_different = True
        break
    sum += i
    counter += 1
average = sum / counter
print("Average is: "+ str(average))
