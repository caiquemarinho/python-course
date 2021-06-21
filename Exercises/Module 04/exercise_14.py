"""

Read an angle in degrees and convert it to radians.
Formula: R =  G * π/180

"""
π = 3.14


print('Input the angle in degrees')
degree = float(input())

radian = float(degree*π/180)
print(f'{degree} Degrees is equal to {radian} Radians')
