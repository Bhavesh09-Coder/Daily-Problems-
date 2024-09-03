# Day 41: Set Comprehensions

def set_comprehensions():
    # Creating a set of squares using set comprehension
    squares_set = {x**2 for x in range(10)}
    print("Set of squares:", squares_set)

    # Filtering even numbers using set comprehension
    evens_set = {x for x in range(10) if x % 2 == 0}
    print("Set of even numbers:", evens_set)

if __name__ == "__main__":
    set_comprehensions()
