# Project Title: Word Counter

def count_words(text):
    words = text.split()
    return len(words)

# Example usage
input_text = "This is a simple word counting program."
word_count = count_words(input_text)
print(f"Input Text: {input_text}")
print(f"Word Count: {word_count}")
