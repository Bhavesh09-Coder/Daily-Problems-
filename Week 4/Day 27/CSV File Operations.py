# Project Title: CSV File Operations

import csv

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def read_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Example usage
filename = "sample.csv"
data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
write_to_csv(filename, data)

# Reading the content back
print(f"Content of '{filename}':")
read_from_csv(filename)
