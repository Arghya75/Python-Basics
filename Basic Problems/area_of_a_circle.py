# Write a Python program that calculates the area of a circle based on the radius entered by the user
import math
# creating a function to calculate the area
def calculateArea(a) :
    area = math.pi * (a**2)
    return area

# Taking the value of radius from user
r = float(input("Enter the value of the radius: "))
print(f"The required area of the given circle is {calculateArea(r)}")