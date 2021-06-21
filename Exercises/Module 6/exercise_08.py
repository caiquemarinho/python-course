"""

Make a program that reads 10 values and prints the lower and the higher value on it.

"""

higher = 0
lower = 0

for n in range(1, 11):
    num = int(input(f'Input a number: '))
    if n == 1:
        higher = num
        lower = num
    if num > higher:
        higher = num
    if num < lower:
        lower = num


print(f'The higher number is is {higher} and the lower number is {lower}')