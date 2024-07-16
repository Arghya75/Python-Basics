# Make a python program using the concepts of recursion which will print the factorial of any given number taken from user.
# Example of Factorial :
# 6! = 6*5*4*3*2*1
# 5! = 5*4*3*2*1

# Defining a function to calculate the factorial
def factorialCal(n) :
    if (n==0 or n==1):
        return 1
    else:
        return n * factorialCal(n-1)

# Taking User Input for which the factorial is to be calculated
a = int(input("Enter a number: "))

# Printing the result of factorial 
print(f"{a}! = {factorialCal(a)}")