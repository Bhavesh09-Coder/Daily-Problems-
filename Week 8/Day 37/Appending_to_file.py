# Appending content to a file
def append_to_file(file_name, content):
    """Appends content to an existing file."""
    try:
        with open(file_name, 'a') as file:
            file.write(content)
            print(f"Content appended to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
append_to_file('example.txt', '\nAppending some more text.')
read_file('example.txt')
