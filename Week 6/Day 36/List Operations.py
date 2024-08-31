# Day 36: List Operations

def list_operations():
    my_list = [1, 2, 3, 4, 5]

    # Adding elements to the list
    my_list.append(6)
    print("After append:", my_list)

    # Removing elements from the list
    my_list.remove(3)
    print("After removing 3:", my_list)

    # Searching for an element
    if 4 in my_list:
        print("4 is in the list.")
    else:
        print("4 is not in the list.")

    # Slicing the list
    print("Sliced list (2nd to 4th elements):", my_list[1:4])

if __name__ == "__main__":
    list_operations()
