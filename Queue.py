class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def delete(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the front element
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

# Create a queue
queue = Queue()

# Insert elements into the queue
queue.insert(5)
queue.insert(10)
queue.insert(15)

# Delete elements from the queue
print("Deleted element:", queue.delete())
print("Deleted element:", queue.delete())

# Check if the queue is empty
print("Is the queue empty?", queue.is_empty())
