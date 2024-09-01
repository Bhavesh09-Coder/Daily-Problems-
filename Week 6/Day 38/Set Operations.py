# Day 38: Set Operations

def set_operations():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    # Union of two sets
    union_set = set_a.union(set_b)
    print("Union of set_a and set_b:", union_set)

    # Intersection of two sets
    intersection_set = set_a.intersection(set_b)
    print("Intersection of set_a and set_b:", intersection_set)

    # Difference between two sets
    difference_set = set_a.difference(set_b)
    print("Difference of set_a and set_b:", difference_set)

    # Adding elements to a set
    set_a.add(6)
    print("After adding 6 to set_a:", set_a)

if __name__ == "__main__":
    set_operations()
