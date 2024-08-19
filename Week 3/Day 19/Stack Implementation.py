# Project Title: Stack Implementation

# Class to represent a stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from stack")
            return item
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage of the Stack class
def stack_example():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Top of stack: {stack.peek()}")
    stack.pop()
    print(f"Stack size: {stack.size()}")

stack_example()
