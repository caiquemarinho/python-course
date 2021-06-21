"""

Read a temperature in Fahrenheit and convert it to Celsius.
Formula: C= 5.0*(F-32)/9.0


"""

print('Please, insert the temperature in Fahrenheit')
fahrenheit = float(input())

celsius = 5.0*(fahrenheit-32)/9.0
print(f'{fahrenheit} Fahrenheit is {celsius} Celsius degrees')

