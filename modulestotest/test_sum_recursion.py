import unittest
from sum_recursion import adding_up_to

class TestAddingUpTo(unittest.TestCase):
    def test_single_element_list(self):
        # Test adding_up_to function with a single element list
        result = adding_up_to([5], 0)
        self.assertEqual(result, 5)  # Assert that the result is equal to the single element in the list

    def test_empty_list(self):
        # Test adding_up_to function with an empty list
        result = adding_up_to([], 5)
        self.assertEqual(result, "index bigger than list")  # Assert that the result is an error message when the list is empty

    def test_index_bigger_than_list(self):
        # Test adding_up_to function with an index larger than the list size
        result = adding_up_to([1, 2, 3], 5)
        self.assertEqual(result, "index bigger than list")  # Assert that the result indicates an error message

    def test_sum_up_to_index(self):
        # Test adding_up_to function with a list summing up to a certain index
        result = adding_up_to([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, 1 + 2 + 3)  # Assert that the result is the sum of elements up to the specified index

if __name__ == '__main__':
    unittest.main()
