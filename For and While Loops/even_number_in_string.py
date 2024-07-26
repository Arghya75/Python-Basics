# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’


# Taking user input
a = input("Enter a string: ")

# printing the string input by user
print(f"Original String: {a}")

# converting the string into a list
x = list(a)

# printing the characters which are present at an even index number
for i in x[0::2]:
    print(i)