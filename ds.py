class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_all_nodes(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

def convert_to_linked_list(input_list):
    ll = LinkedList()
    for item in input_list:
        ll.append(item)
    return ll

