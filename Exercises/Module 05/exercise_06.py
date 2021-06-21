"""

Receive two real numbers, show the higher one and print the difference between those numbers.

"""

print('Insert the first number')
num1 = int(input())

print('Insert the second number')
num2 = int(input())

if num1 > num2:
    print('The first number is the higher one')
    print(f'The difference is {num1-num2}')
else:
    print('The second number is the higher one')
    print(f'The difference is {num2 -num1}')


