"""

Make a program that will read the work hours in a month and generate the salary of an employee with a 10% bonus.

"""

bonus = 1.10

print('Insert the amount of worked hours')
wh = float(input())

print('Insert the value value of your hours')
hv = float(input())

salary = (hv * wh)*bonus
print(f'Your salary is {salary}')
