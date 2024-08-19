# Project Title: Linked List Implementation

# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Appended {data} to linked list")

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Prepended {data} to linked list")

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            print(f"Deleted {data} from linked list")
        else:
            current = self.head
            previous = None
            while current and current.data != data:
                previous = current
                current = current.next
            if current:
                previous.next = current.next
                print(f"Deleted {data} from linked list")
            else:
                print(f"{data} not found in linked list")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage of the LinkedList class
def linked_list_example():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.display()
    linked_list.prepend(5)
    linked_list.display()
    linked_list.delete(20)
    linked_list.display()

linked_list_example()
