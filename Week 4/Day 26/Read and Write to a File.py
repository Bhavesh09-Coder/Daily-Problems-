# Project Title: Read and Write to a File

def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Example usage
filename = "sample.txt"
text_to_write = "This is an example of writing to a file."
write_to_file(filename, text_to_write)

# Reading the content back
file_content = read_from_file(filename)
print(f"Content of '{filename}':\n{file_content}")
