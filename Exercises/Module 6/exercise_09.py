"""

Take a number and print the first N odd numbers.

"""

print('Please input a number of odd numbers you want:')
n = int(input())

for odd in range(1, n*2, 2):
    print(odd)
