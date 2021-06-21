"""

Read a temperature in Kelvins and convert is to Celsius.
Formula: C = K - 273.15

"""

print('Input the temperature in Kelvins')
kelvins = float(input())

celsius = float(kelvins - 273.15)
print(f'{kelvins} Kelvins is {celsius} Celsius degrees')
