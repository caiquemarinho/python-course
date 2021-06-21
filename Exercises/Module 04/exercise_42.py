"""

Receive and calculate the salary of an employee, knowing that this employee have a 5% bonus on his base salary and also
gets a 7% discount on his base salary

"""

tax = 0.07
bonus = 0.05


print('Insert your base salary')
base_salary = float(input())

discount = base_salary - tax

salary = (base_salary - (base_salary*tax)) + base_salary*bonus

print(f'Your pay check is {salary}')