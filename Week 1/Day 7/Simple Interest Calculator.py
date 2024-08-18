# Project Title: Simple Interest Calculator

# Function to calculate simple interest
def simple_interest_calculator():
    print("Simple Interest Calculator")
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (in %): "))
    time = float(input("Enter time (in years): "))

    interest = (principal * rate * time) / 100
    print(f"Simple Interest: {interest}")

simple_interest_calculator()
