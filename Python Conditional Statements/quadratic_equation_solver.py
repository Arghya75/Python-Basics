# Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.

import math
# Creating a function for the problem
def eqSolver(x, y, z):
    d = (y**2) - (4*x*z) # Calculates the Discriminant
    # Checking are the roots real or complex?
    if d>= 0 :
        print("Roots are real")
        # As the roots are real so calculating the roots
        firstResult = (-y + math.sqrt(d))/(2*x)
        secondResult = (-y - math.sqrt(d))/(2*x)
        return firstResult, secondResult
    else:
        return "Roots are complex"

a = float(input("Enter the co-efficient of x-square :"))
b = float(input("Enter the co-efficient of x :"))
c = float(input("Enter the value of the constant:"))
result = (eqSolver(a, b, c))

# Checking the result and printing it as readable format
if isinstance(result, tuple) :
    print(f"The results are {result[0]} and {result[1]}")
else :
    print(result)