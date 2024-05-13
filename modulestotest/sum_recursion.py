'''Practical Task 1 - Recursion'''
# Create a function that takes a list of integers and a single integer as arguments.
# single integer 'i' represent the index point.
def adding_up_to(list_num, i):
    # Conditional statements for base case
    if i <= 0:
        # if list reached index 0 or no item in the list
        return list_num[0] if list_num else 0
    if i > len(list_num):
        # If i is greater than the list length
        return "index bigger than list"
    # Recursive case
    return list_num[i] + adding_up_to(list_num, i - 1)

# Examples Test
print(adding_up_to([2, 2, 4, 5], 9))
print(adding_up_to([4, 2, 5, 6, 7, 3], 5))
print(adding_up_to([1, 5, 8, 3], 0))