"""

Read the salary of the employee amd and the loan monthly pay. If the pay is higher than 20% of the employee's
salary print that the loan is being denied.

"""

print('Input your salary')
salary = float(input())

print('Input the monthly pay')
pay = float(input())

threshold = salary*0.20
print(threshold)

if pay <= threshold:
    print('Loan accepted')
else:
    print('Loan denied')
