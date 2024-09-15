# Queue implementation using collections.deque in Python

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(list(self.queue))

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.display()
