# Project Title: Fibonacci Sequence Generator

# Function to generate Fibonacci sequence up to n terms
def fibonacci_sequence_generator():
    print("Fibonacci Sequence Generator")
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

    print()  # Newline at the end

fibonacci_sequence_generator()
