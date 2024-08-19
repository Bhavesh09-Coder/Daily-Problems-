# Project Title: Dictionary Operations

# Function to perform various operations on a dictionary
def dictionary_operations():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f"Original Dictionary: {my_dict}")

    # Adding an item
    my_dict['d'] = 4
    print(f"After adding ('d': 4): {my_dict}")

    # Removing an item
    del my_dict['b']
    print(f"After removing 'b': {my_dict}")

    # Accessing a value
    print(f"Value associated with 'a': {my_dict['a']}")

    # Updating a value
    my_dict['a'] = 10
    print(f"After updating 'a' to 10: {my_dict}")

    # Get all keys and values
    print(f"Keys: {list(my_dict.keys())}")
    print(f"Values: {list(my_dict.values())}")

dictionary_operations()
