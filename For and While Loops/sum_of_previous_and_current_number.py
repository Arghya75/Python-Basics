# Write a Python program that prints the sum of the current number and the previous number from a list of integers. For the first element, consider the previous number as 0
# Example
# For the list [1, 2, 3, 4, 5], the output should be:
#     Current Number: 1, Previous Number: 0, Sum: 1
#     Current Number: 2, Previous Number: 1, Sum: 3
#     Current Number: 3, Previous Number: 2, Sum: 5
#     Current Number: 4, Previous Number: 3, Sum: 7
#     Current Number: 5, Previous Number: 4, Sum: 9


print("Printing current and previous number sum in a range(10)")

# Initializing the previous Number
previousNumber = 0

# Starting loop for iteration
for i in range(10):

# calculating the sum and storing it into a variable
    current_sum = previousNumber + i
    print(f"Current Number: {i}, previous number: {previousNumber}, Sum: {current_sum}")

# after printing the required output the number stored in the previousNumber variable will be updated as i
    previousNumber = i