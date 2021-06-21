"""

Receive two valid grades and print the average of it. A valid grade is a number between 0.0 and 10.0

"""

print('Insert the first grade')
grade1 = float(input())

print('Insert the second grade')
grade2 = float(input())

if grade1 >= 0.0:
    validation1 = True
    if grade1 <= 10.0:
        validation1 = True
    else:
        validation1 = False
else:
    validation1 = False

if grade2 >= 0.0:
    validation2 = True
    if grade2 <= 10.0:
        validation2 = True
    else:
        validation2 = False
else:
    validation2 = False

print(validation1)
print(validation2)

if validation1 and validation2:
    print(f'The average is {(grade1+grade2)/2}')
else:
    print('Invalid grade. Please input a number between 0.0 and 10.0')


