# Project Title: Grade Calculator

# Function to calculate grade based on marks
def grade_calculator():
    print("Grade Calculator")
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Grade: {grade}")

grade_calculator()
