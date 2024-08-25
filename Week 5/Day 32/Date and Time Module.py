# Project Title: Date and Time Module

import datetime

# Get the current date and time
now = datetime.datetime.now()

# Display current date and time
print("Current date and time:", now)

# Format the date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)
