# Project Title: Queue Implementation

# Class to represent a queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to queue")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued {item} from queue")
            return item
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage of the Queue class
def queue_example():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Front of queue: {queue.front()}")
    queue.dequeue()
    print(f"Queue size: {queue.size()}")

queue_example()
