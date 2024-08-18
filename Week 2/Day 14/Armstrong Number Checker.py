# Project Title: Armstrong Number Checker

# Function to check if a number is an Armstrong number
def armstrong_number_checker():
    print("Armstrong Number Checker")
    num = int(input("Enter a number: "))
    digits = len(str(num))
    sum_of_powers = sum(int(digit) ** digits for digit in str(num))

    if num == sum_of_powers:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

armstrong_number_checker()
