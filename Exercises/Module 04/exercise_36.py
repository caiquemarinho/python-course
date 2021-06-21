"""

Read the ray and height of a cylinder and print it's volume.
Formula: V =  π * ray² * height

"""

π = 3.14159265359

print('Insert the ray of the cylinder')
r = float(input())

print('Insert the height of the cylinder')
h = float(input())

v = π * r**2 * h
print(f'The volume of the cylinder is: {v}')

v2 = π * (r**2 * h)
print(f'The volume of the cylinder is: {v2}')
