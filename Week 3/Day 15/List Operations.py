# Project Title: List Operations

# Function to perform various operations on a list
def list_operations():
    my_list = [1, 2, 3, 4, 5]
    print(f"Original List: {my_list}")

    # Append an item to the list
    my_list.append(6)
    print(f"After appending 6: {my_list}")

    # Remove an item from the list
    my_list.remove(2)
    print(f"After removing 2: {my_list}")

    # Insert an item at a specific index
    my_list.insert(2, 10)
    print(f"After inserting 10 at index 2: {my_list}")

    # Sort the list
    my_list.sort()
    print(f"Sorted List: {my_list}")

    # Reverse the list
    my_list.reverse()
    print(f"Reversed List: {my_list}")

list_operations()
