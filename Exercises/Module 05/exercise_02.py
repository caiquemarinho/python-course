"""

Read a number. If the number is positive calculate de square root of the number, if it's not throw an error message

"""
import math

print('Insert the number')
num1 = int(input())

if num1 > 0:
    print(f'The square root of {num1} is {math.sqrt(num1)}')
elif num1 == 0:
    print('Zero has no square root')
else:
    print('Error! Negative numbers do note have square root')

