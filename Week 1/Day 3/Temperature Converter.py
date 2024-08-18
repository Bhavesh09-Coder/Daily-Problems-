# Project Title: Temperature Converter

# Function to convert temperature between Celsius and Fahrenheit
def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))
    scale = input("Convert to (C/F): ").upper()

    if scale == 'C':
        result = (temp - 32) * 5.0/9.0
        print(f"{temp} Fahrenheit is {result} Celsius")
    elif scale == 'F':
        result = (temp * 9.0/5.0) + 32
        print(f"{temp} Celsius is {result} Fahrenheit")
    else:
        print("Invalid scale")

temperature_converter()
