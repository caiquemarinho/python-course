"""

Receive the height and the gender of the user then print their ideal weight

"""

print('Input your height')
height = float(input())

print('Input your gender')
gender = input()

if gender == 'male':
    print(f'Your ideal weight is {(72.7*height)-58}')
elif gender == 'female':
    print(f'Your ideal weight is {(62.1 * height) - 44.7}')
else:
    print('Invalid parameter')
