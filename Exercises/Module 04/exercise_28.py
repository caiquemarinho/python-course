"""

Read three values and present the sum of the squares of the given numbers.

"""

print('Insert the first value')
num1 = int(input())

print('Insert the second value')
num2 = int(input())

print('Insert the third value')
num3 = int(input())

total = int(num1**2 + num2**2 + num3**2)
print(f'The sum of the squares of the given numbers is: {total}')
