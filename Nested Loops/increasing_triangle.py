# Print the following pattern:
#                 *
#                 * *
#                 * * *
#                 * * * *
#                 * * * * *


# counting the row number of the pattern and inserting it in a variable
n = 5

# fist loop which stands for the rows
for i in range(n):
# Second loop which stands for the coloumn
    for j in range(i+1):
        print("*", end=" ")
    print()