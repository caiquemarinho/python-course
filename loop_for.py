"""

Loop for

Loop -> Is a programming structure that repeats a sequence of instructions
For -> Is one of those structures

Examples:
    C or Java

    for (int i =0; i < limit(Eg. 10); i++) {
        //loop execution
    }

    Python

    for item in limit:
    //loop execution

Loops are used to iterate upon iterable values:

Examples:

    String -
     name = 'Geek University'

    List -
    list = [1, 3, 5, 7, 9]

    Range -
    numbers =  range(1,10)

"""
# Var

name = 'Geek University'
my_list = [1, 3, 5, 7, 9]
numbers = range(1,10)

# For Example 1 - String

for letter in name:
    print(letter)

# For example 2 - List

for number in my_list:
    print(number)

# For example 3 - Range

for number in range(1,10):
    print(number)

for _, letter in enumerate(name):
    print(letter)
    print(_)


for value in enumerate(name):
    print(value)

print('Input the quantity you want to print')
qty = int(input())
sum1 = 0

for n in range(1, qty+1):
    num = int(input(f'Input the number you want to sum: '))
    sum1 = sum1 + num
print(f'The sum is {sum1}')

