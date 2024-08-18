# Project Title: Leap Year Checker

# Function to check if a year is a leap year
def leap_year_checker():
    print("Leap Year Checker")
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

leap_year_checker()
