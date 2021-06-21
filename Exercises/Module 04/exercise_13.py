"""

Read a distance in kilometers and convert it to miles
Formula: M = K/1.61

"""

print('Insert the distance in kilometers')
kilometers = float(input())

miles = float(kilometers/1.60934)
print(f'{kilometers} kilometers is equals to {miles} miles')
