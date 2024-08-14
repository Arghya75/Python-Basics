# The commission on a shop employee's total sales is as follows :
# 1. If Sales <= Tk. 50 then there is no commission
# 2. If Tk. 50 < Sales <= Tk. 500 then commission = 10% of sales
# 3. If Sales > Tk. 500 then commission = Tk 50 + 8% of Sales above Tk. 500
# Write a program segment which reads on the total sales of the employee and calculates his commission.

def sales(a) :
    commission = 0
    if (a <= 50) :
        commission = 0
    elif(50 < a <= 500):
        commission = a * 0.1
    else:
        commission = 50 + 8*(a - 500)
    return commission

n = float(input("Enter your sales: TK. "))
print(f"You have recieved Tk. {sales(n)} as your commission")