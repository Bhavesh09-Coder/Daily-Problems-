# File reading and writing
def read_file(file_name):
    """Reads the content of a file."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_file(file_name, content):
    """Writes content to a file."""
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content written to {file_name}")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")

# Usage example
write_file('example.txt', 'Hello, this is a sample file content.')
read_file('example.txt')
