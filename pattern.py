'''Iteration - Task 2'''
# Create a Python file called pattern.py
# Write a code to output pattern in assignment with an if-else statement, in combination with a single for loop.

star = "******"
index = 0
for i in range(0, 9):       # This for-loop iterates through the number of rows
    if i < 5:               # This will make sure that the sequence adds 1 to the index and one '*' to each row, until 5 '*' are printed.
        index += 1
        print(star[0:index])
    else:                       # When i = 4, the index starts decreasing by 1, therefore subtracting '*' from star string.
        index -= 1
        print(star[0:index])
        