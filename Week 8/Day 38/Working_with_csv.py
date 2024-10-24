import csv

# Reading from a CSV file
def read_csv(file_name):
    """Reads content from a CSV file and prints it."""
    try:
        with open(file_name, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                print(row)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Writing to a CSV file
def write_csv(file_name, data):
    """Writes a list of rows to a CSV file."""
    try:
        with open(file_name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)
            print(f"Data written to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example data and usage
data = [['Name', 'Age', 'Country'], ['Alice', '24', 'USA'], ['Bob', '30', 'UK'], ['Charlie', '29', 'Canada']]
write_csv('people.csv', data)
read_csv('people.csv')
