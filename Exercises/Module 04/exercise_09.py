"""

Read a temperature in Celsius and convert is to Kelvins.
Formula: K = C + 273.15

"""

print('Input the temperature in Celsius')
celsius = float(input())

kelvins = float(celsius + 273.15)
print(f'{celsius} Celsius is {kelvins} Kelvins')
