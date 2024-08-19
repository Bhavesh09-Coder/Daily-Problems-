# Project Title: Set Operations

# Function to perform various operations on a set
def set_operations():
    my_set = {1, 2, 3, 4, 5}
    print(f"Original Set: {my_set}")

    # Adding an element
    my_set.add(6)
    print(f"After adding 6: {my_set}")

    # Removing an element
    my_set.remove(3)
    print(f"After removing 3: {my_set}")

    # Union of two sets
    new_set = {4, 5, 6, 7}
    print(f"Union of sets: {my_set | new_set}")

    # Intersection of two sets
    print(f"Intersection of sets: {my_set & new_set}")

    # Difference of two sets
    print(f"Difference of sets: {my_set - new_set}")

set_operations()
