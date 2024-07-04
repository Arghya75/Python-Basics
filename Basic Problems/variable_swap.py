#  Write a Python program to swap the values of two variables without using a temporary variable.

# Taking two input from user as variable
a = input("Enter the first element of variable a: ")
b = input("Enter the second element of variable b: ")
# Printing the original Variables
print(f"The original variable's are a = {a} and b = {b}")
# Swapping the variables
a, b = b, a
# Printing the swapped values
print(f"The swaped variable's are a = {a} and b = {b}")