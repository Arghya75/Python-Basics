# Write a Python program using a for loop to print the multiplication table of a given number N.

num = int(input("Enter the Number: "))

print(f"Multiplication Table for {num}")
for i in range (1, 11) :
    r = num * i
    print(f"{num} x {i} = {r}")