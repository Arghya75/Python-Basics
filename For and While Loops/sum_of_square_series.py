# Write a program that reads a number N and print the sum of the series:
# 1^(2)+2^(2)+3^(2)+.............+N^(2)

def summation(N):
    sum = 0
    for i in range(1, N+1):
        sum = sum + i*i
    return sum

a = int(input("Enter your number: "))
print(summation(a))