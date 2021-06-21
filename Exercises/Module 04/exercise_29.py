"""

Read four grades, make the arithmetic mean and print it.

"""

print('Insert the first value')
grade1 = float(input())

print('Insert the second value')
grade2 = float(input())

print('Insert the third value')
grade3 = float(input())

print('Insert the fourth value')
grade4 = float(input())

am = float((grade1 + grade2 + grade3 + grade4)/4)
print(f'The arithmetic mean is {am}')
