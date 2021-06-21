"""

Read a real number. If it is positive print it's square root, if it's not print the square of it.

"""
import math

print('Insert a number')
num1 = float(input())

if num1 > 0:
    print(f'The square root of {num1} is {math.sqrt(num1)}')
else:
    print(f'The square of {num1} is {num1**2}')



