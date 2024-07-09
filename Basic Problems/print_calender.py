# Write a Python program that prints the calender for a given month and year

# Importing Calender Module
import calendar

# Taking user input of the month and year
x = int(input("Input the month: "))
y = int(input("Input the year: "))

# Printing the calender
print(f"The required calender for the month {calendar.month_name[x]}, {y} is: ")
print(f"{calendar.month(y,x)}")
