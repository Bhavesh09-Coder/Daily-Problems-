# Project Title: Tuple Operations

# Function to perform various operations on a tuple
def tuple_operations():
    my_tuple = (1, 2, 3, 4, 5)
    print(f"Original Tuple: {my_tuple}")

    # Accessing an element by index
    print(f"Element at index 2: {my_tuple[2]}")

    # Slicing a tuple
    print(f"Slice from index 1 to 3: {my_tuple[1:4]}")

    # Concatenating tuples
    new_tuple = my_tuple + (6, 7)
    print(f"Concatenated Tuple: {new_tuple}")

    # Tuple length
    print(f"Length of the tuple: {len(my_tuple)}")

    # Check if an element exists in a tuple
    print(f"Is 3 in the tuple? {'Yes' if 3 in my_tuple else 'No'}")

tuple_operations()
