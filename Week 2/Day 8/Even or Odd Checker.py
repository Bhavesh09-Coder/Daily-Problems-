# Project Title: Even or Odd Checker

# Function to check if a number is even or odd
def even_or_odd_checker():
    print("Even or Odd Checker")
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

even_or_odd_checker()
