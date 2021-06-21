"""

 Cathetus and the hypotenuse

"""
import math


print('Insert the first value')
a = float(input())

print('Insert the second value')
b = float(input())

hypotenuse = float(a**2+b**2)//2
print(f'The hypotenuse is: {hypotenuse}')

hypotenuse2 = float(a**2+b**2)

# print(math.sqrt(hypotenuse2))
print(f'The hypotenuse is: {math.sqrt(hypotenuse2)}')