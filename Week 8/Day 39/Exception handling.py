# Exception handling basics
def divide(a, b):
    """Performs division and handles any exceptions."""
    try:
        result = a / b
        print(f"Result of {a} / {b} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
divide(10, 2)
divide(10, 0)
