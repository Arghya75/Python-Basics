# Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.

def nSum (n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

N = int(input("Enter the number up to which you want to calculate the sum of natural numbers: "))
print(nSum(N))