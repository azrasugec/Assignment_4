def bubble_sort(data):
    # Python list için
    if isinstance(data, list):
        n = len(data)
        for i in range(n):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    # Linked list için
    elif hasattr(data, 'head'):  # LinkedList gibi davranıyorsa
        end = None
        while end != data.head:
            current = data.head
            while current.next != end:
                next_node = current.next
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                current = current.next
            end = current
        return data

