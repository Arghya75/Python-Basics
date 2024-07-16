# Create a python program to calculate the average of best two CT numbers of students from the three CT numbers


# Defining a Funciton for returning average
def bestTwo (a, b, c):
    '''This function takes three parameters as arguments and make a list using the arguments. Then it sort the numbers in descending order. Then return the average of best two CT numbers.'''
    ctNumbers = [a, b, c]
    ctNumbers.sort(reverse=True) # Sorting the numbers in descending order
    sum = ctNumbers[0] + ctNumbers[1] # Adding the best two numbers
    avg = sum / 2 # Calculating the average of best two
    return avg

# Taking user input of the CT numbers.
m = int(input("Enter your first CT numbers: "))
n = int(input("Enter your second CT numbers: "))
o = int(input("Enter your third CT numbers: "))

# Printing the average of best two CT numbers.
print(f"The average of best two CT numbers are {bestTwo(m, n, o)}")