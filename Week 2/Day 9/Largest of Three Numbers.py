# Project Title: Largest of Three Numbers

# Function to find the largest of three numbers
def largest_of_three_numbers():
    print("Largest of Three Numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    largest = max(num1, num2, num3)
    print(f"The largest number is {largest}")

largest_of_three_numbers()
