import unittest
from sorting_algorithms import *
from ds import *

class TestSorting(unittest.TestCase):
    l1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    linked_list1 = convert_to_linked_list(l1)

    l2 = [-5, -1, -7, -3]
    linked_list2 = convert_to_linked_list(l2)

    def test_bubble_sort_list(self):
        self.assertEqual(bubble_sort(self.l1), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bubble_sort_linked_list(self):
        self.assertEqual(list(bubble_sort(self.linked_list1)), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bubble_sort_list_negative(self):
        self.assertEqual(bubble_sort(self.l2), sorted(self.l2))

    def test_bubble_sort_linked_list_negative(self):
        self.assertEqual(list(bubble_sort(self.linked_list2)), sorted(self.l2))

if __name__ == "__main__":
    unittest.main()

