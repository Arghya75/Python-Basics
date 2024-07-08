# Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

def checkType (a) :
    result = type(a).__name__
    return result


#Example Usages
var1 = 42
var2 = 43.5
var3 = "I am Arghya Chakraborty"
var4 = [1,22,3,4,5,6]
var5 = (1,2,3,4,5,6)

# Printing The types
print(f"The data type of {var1} is {checkType(var1)}")
print(f"The data type of {var2} is {checkType(var2)}")
print(f"The data type of {var3} is {checkType(var3)}")
print(f"The data type of {var4} is {checkType(var4)}")
print(f"The data type of {var5} is {checkType(var5)}")