"""

Read a number. If the number is positive calculate de square root of the number and it's square, if it's not throw an error message

"""
import math

print('Insert the number')
num1 = int(input())

if num1 > 0:
    print(f'The square root of {num1} is {math.sqrt(num1)} and the square is {num1**2}')
elif num1 == 0:
    print('Zero has no square root')
else:
    print('Error! Negative numbers do note have square root')
