# Day 37: Tuple Operations

def tuple_operations():
    my_tuple = (1, 2, 3, 4, 5)

    # Accessing elements in a tuple
    print("First element:", my_tuple[0])

    # Slicing a tuple
    print("Sliced tuple (2nd to 4th elements):", my_tuple[1:4])

    # Length of a tuple
    print("Length of tuple:", len(my_tuple))

    # Tuples are immutable, but you can concatenate them
    new_tuple = my_tuple + (6, 7)
    print("Concatenated tuple:", new_tuple)

if __name__ == "__main__":
    tuple_operations()
