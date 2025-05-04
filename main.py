from sorting_algorithms import *
from ds import *

# Test verisi
test_seq = [9, 8, 7, 6, 5, 4, 3, 2, 1]
test_seq_ll = convert_to_linked_list(test_seq)

# PART I – Sorting with Python list
sorted_pl = bubble_sort(test_seq)
print("\nSorted - Python Lists:", sorted_pl)

# PART II – Sorting with Linked list
print("Input type: ", type(test_seq_ll))
print("Linked List having the following data: ", list(test_seq_ll))
print("Sorted - Input: Linked List:")
sorted_ll = bubble_sort(test_seq_ll)
sorted_ll.print_all_nodes()

