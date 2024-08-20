# Project Title: Character Frequency Counter

from collections import Counter

def char_frequency(text):
    return Counter(text)

# Example usage
input_text = "character frequency counter"
frequency = char_frequency(input_text)
print(f"Character Frequency in '{input_text}':\n{frequency}")
