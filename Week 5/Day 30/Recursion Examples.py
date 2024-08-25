# Project Title: Recursion Examples

def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Recursive function to generate the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the recursive functions
print("Factorial of 5 is:", factorial(5))
print("Fibonacci number at position 6 is:", fibonacci(6))
