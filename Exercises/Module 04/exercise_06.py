"""

Read a temperature in Celsius and convert it to Fahrenheit.
Formula: F= C*(9.0/50)+32

"""

print('Please, insert the temperature in Celsius')
celsius = float(input())

fahrenheit = (celsius*(9.0/5.0)+32)
print(f'{celsius} Celsius is {fahrenheit} Fahrenheit')
