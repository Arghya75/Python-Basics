# Write a Python program that takes an integer as input and prints whether it is even or odd.

# Creating a function about even or odd
def isEven (a):
# Applying condition to check whether the value is even or odd
    if a % 2 == 0 :
        return f"{a} is even"
    else:
        return f"{a} is odd"

# Taking a number as user input which will be checked
num = int(input("Enter the number to be checked: "))
# Printing the given number is even or odd
print(isEven(num))