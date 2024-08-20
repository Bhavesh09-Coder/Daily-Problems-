# Project Title: JSON File Operations

import json

def write_to_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_from_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Example usage
filename = "sample.json"
data = {"Name": "Alice", "Age": 25, "City": "Wonderland"}
write_to_json(filename, data)

# Reading the content back
file_content = read_from_json(filename)
print(f"Content of '{filename}':\n{file_content}")
