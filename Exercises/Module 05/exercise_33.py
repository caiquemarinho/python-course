"""

Receive a product and change it's price according to the table.

0 - 50$ -> 5%
50 - 100 -> 10%
100 + ->15%

"""
print('Insert the product price')
product = float(input())

# Finding out the new price of the product.
if product < 50:
    new_price = product+(product*0.05)
elif (product >= 50) and (product <= 100):
    new_price = product+(product*0.10)
else:
    new_price = product+(product*0.15)
print(new_price)


# Message to the user.
if new_price <= 80:
    print(f'Cheap! The new price is {new_price}')
elif (new_price > 80) and (new_price <= 120):
    print(f'Decent price! The new price is {new_price}')
elif (new_price > 120) and (new_price <= 200):
    print(f'Expensive! The new price is {new_price}')
elif new_price > 200:
    print(f'Very Expensive! The new price is {new_price}')

