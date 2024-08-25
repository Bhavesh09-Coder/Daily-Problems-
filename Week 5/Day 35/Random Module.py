# Project Title: Random Module

import random

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)

# Generate a random floating-point number between 0 and 1
random_float = random.random()

# Choose a random item from a list
items = ['apple', 'banana', 'cherry']
random_choice = random.choice(items)

# Display results
print("Random integer between 1 and 10:", random_int)
print("Random floating-point number between 0 and 1:", random_float)
print("Random choice from list:", random_choice)
