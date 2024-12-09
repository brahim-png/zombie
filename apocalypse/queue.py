# queue.py

class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, item):
        """Add an item to the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the first item from the queue."""
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)
