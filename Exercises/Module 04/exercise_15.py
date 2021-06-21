"""

Read an angle in radians and convert it to degrees.
Formula: G = R * 180/π

"""
π = 3.14159265359


print('Input the angle in radians')
radian = float(input())

degree = float(radian*180/π)
print(f'{radian} Radiansis equal to {degree} Degrees ')
