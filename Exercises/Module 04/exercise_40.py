"""

A plumber get R$30 per worked day. Knowing this, make a program that calculate how much the plumber should receive
for the worked days minus 8% taxes.

"""

wd_value = 30.00
tax = 0.08

print('Insert the worked days')
wd = float(input())

pay_check = wd * wd_value

discount = pay_check * tax

take_home = pay_check - discount

print(f'You will receive {take_home}, {discount} was take for taxes')


