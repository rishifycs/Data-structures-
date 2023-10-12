class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current and current.next:
                if current.next.data == data:
                    current.next = current.next.next
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Example usage:
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)

sll.display()  # Output: 1 -> 2 -> 3 -> None

sll.prepend(0)
sll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

sll.delete(2)
sll.display()  # Output: 0 -> 1 -> 3 -> None
