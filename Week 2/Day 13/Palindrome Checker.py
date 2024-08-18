# Project Title: Palindrome Checker

# Function to check if a string is a palindrome
def palindrome_checker():
    print("Palindrome Checker")
    text = input("Enter a string: ")

    if text == text[::-1]:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")

palindrome_checker()
