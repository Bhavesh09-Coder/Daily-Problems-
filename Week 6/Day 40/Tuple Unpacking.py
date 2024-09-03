# Day 40: Tuple Unpacking

def tuple_unpacking():
    # Unpacking a tuple into variables
    my_tuple = (1, 2, 3)
    a, b, c = my_tuple
    print("Unpacked values:", a, b, c)

    # Using tuple unpacking in a function
    def return_tuple():
        return (4, 5, 6)

    x, y, z = return_tuple()
    print("Values from function:", x, y, z)

if __name__ == "__main__":
    tuple_unpacking()
