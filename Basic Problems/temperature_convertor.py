# Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

# Defining a function for the above problem
def convertTemp (a) :
    result = ((9*a)+160)/5
    return result

# Taking celsius temperature as input from the user
celsiusTemp = float(input("Enter the temperature in celsius: "))

# Calling the Function to convert the temperature
convert = convertTemp(celsiusTemp)

# Printing the converted temperature
print(f"The {celsiusTemp} degree celsius is equal to {convert} degree fahrenheit")