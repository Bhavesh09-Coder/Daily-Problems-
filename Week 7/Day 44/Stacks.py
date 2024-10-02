# Stack implementation using list in Python

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

# Example usage
s = Stack()
s.push(5)
s.push(10)
print(s.peek())
s.pop()
s.display()