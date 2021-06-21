"""

Receive two numbers and print which one is higher

"""

print('Insert the first number')
num1 = int(input())

print('Insert the second number')
num2 = int(input())


if num1 > num2:
    print(f'{num1} is higher than {num2}')
elif num1 == num2:
    print('The numbers are equal')
else:
    print(f'{num2} is higher than {num1}')
