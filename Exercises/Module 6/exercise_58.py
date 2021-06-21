"""

Make a program that SUM the amount of cousin primes in a range


"""
list_cousin = []
sum1 = 0

print('Please input a number: ')
n = int(input())

print('Please input a number: ')
n2 = int(input())

for x in range(n, n2 + 1):
    cont = 0
    for y in range(1, x + 1):
        if x % y == 0:
            cont += 1
    if cont <= 2:
        list_cousin.append(x)
        sum1 = sum1 + cont

print(list_cousin)
print(f'There are {len(list_cousin)} cousin numbers between {n} and {n2}.')
