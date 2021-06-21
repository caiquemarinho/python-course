"""

Receiving the step height and the height that the user wants to reach calculate
how many stair steps the user will go over to achieve a certain height

"""

print('Insert the stair step height')
stair_height = float(input())

print('Insert the height you want to achieve')
height = float(input())

total_steps = height/stair_height
print(total_steps)
