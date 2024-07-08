# Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.


# Creating a Function for the problem
def typeChecker(a) :
    if a>0 :
        return "The number you've entered is Positive"
    elif a == 0:
        return "The number you've entered is Zero"
    else :
        return "The number you've entered is Negative"

# Taking User Input
m = int(input("Enter the number to be checked: "))
print(typeChecker(m))

