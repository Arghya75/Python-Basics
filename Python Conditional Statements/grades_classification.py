# Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria:
#     – 90% or above: A+
#     – 80-89%: A
#     – 70-79%: B
#     – 60-69%: C
#     – Below 60%: Fail

def gradeClass (a) :
    if a >= 90 :
        return "You obtained A+"
    elif a>= 80:
        return "You obtained A"
    elif a>= 70:
        return "You obtained B"
    elif a>= 60:
        return "You obtained C"
    else:
        return "Sorry, You are failed."

obtainedNum = int(input("Enter your percentage: "))
print(gradeClass(obtainedNum))
