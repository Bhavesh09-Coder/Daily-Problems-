# Day 42: List, Tuple, and Set Methods

def list_tuple_set_methods():
    # List methods
    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)
    my_list.pop(0)
    print("Modified list:", my_list)

    # Tuple methods (limited due to immutability)
    my_tuple = (1, 2, 3, 4, 5)
    print("Count of 3 in tuple:", my_tuple.count(3))

    # Set methods
    my_set = {1, 2, 3, 4, 5}
    my_set.add(6)
    my_set.remove(1)
    print("Modified set:", my_set)

if __name__ == "__main__":
    list_tuple_set_methods()
