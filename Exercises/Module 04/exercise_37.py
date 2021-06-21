"""

Read a value and print it applying a 12% discount to it.

"""

print('Please, insert the value')
value = float(input())

new_value = value - (value * 0.12)

value_discounted = value * 0.12

print(f'The new value is {new_value} and the amount discounted was {value_discounted}')



