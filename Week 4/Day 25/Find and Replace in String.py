# Project Title: Find and Replace in String

def find_and_replace(text, find_word, replace_word):
    return text.replace(find_word, replace_word)

# Example usage
input_text = "The quick brown fox jumps over the lazy dog."
find_word = "fox"
replace_word = "cat"
result_text = find_and_replace(input_text, find_word, replace_word)
print(f"Original Text: {input_text}")
print(f"Modified Text: {result_text}")
