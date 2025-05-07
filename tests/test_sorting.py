import unittest

from sorting_algorithms import *



class TestSorting(unittest.TestCase):

    # Original test cases

    l1 = [9,8,7,6,5,4,3,2,1]

    linked_list1 = convert_to_linked_list(l1)



    # Test cases with negative values

    l2 = [-3, 5, -7, 2, -1, 0, 4]

    linked_list2 = convert_to_linked_list(l2)



    # Single item test cases

    l3 = [42]

    linked_list3 = convert_to_linked_list(l3)



    def test_bubble_sort_list(self):

        self.assertEqual(bubble_sort(self.l1), [1,2,3,4,5,6,7,8,9])

        self.assertEqual(bubble_sort(self.l2), [-7,-3,-1,0,2,4,5])

        self.assertEqual(bubble_sort(self.l3), [42])



    def test_bubble_sort_linked_list(self):

        self.assertEqual(list(bubble_sort(self.linked_list1)), [1,2,3,4,5,6,7,8,9])

        self.assertEqual(list(bubble_sort(self.linked_list2)), [-7,-3,-1,0,2,4,5])

        self.assertEqual(list(bubble_sort(self.linked_list3)), [42])



if __name__ == "__main__":

    unittest.main()



