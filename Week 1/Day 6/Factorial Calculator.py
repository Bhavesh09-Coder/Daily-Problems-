# Project Title: Factorial Calculator

# Function to calculate the factorial of a number
def factorial_calculator():
    print("Factorial Calculator")
    num = int(input("Enter a number: "))

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print(f"Factorial of {num} is {factorial}")

factorial_calculator()
