'''Practical Task 2 - Recursion'''
# Create a function that takes a list of integers as argument
def largest_number_recursive(list_int):
    # Base case: if the list has only one element, return that element
    if len(list_int) == 1:
        return list_int[0]
        # Recursive case - compares the first element with the largest number in the rest of the list
    return max(list_int[0], largest_number_recursive(list_int[1:]))

# Example for test
print(largest_number_recursive([7, 12, 8, 10, 4]))
