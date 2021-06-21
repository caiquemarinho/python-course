"""

Take a number and print the first N even numbers.

"""

print('Please input a number of odd numbers you want:')
n = int(input())

for even in range(0, n*2, 2):
    print(even)

