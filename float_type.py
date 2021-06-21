"""
Float Type

Real and Decimal type

PS: Always use . not , to separate

"""

# Wrong Way

value = 1, 44

print(value)
print(type(value))

# Right Way

value = 1.44

print(value)
print(type(value))

# Also Possible to do

value1, value2 = 1, 44

print(value1)
print(type(value1))
print(value2)
print(type(value2))

# It's possible to convert a float to an integer, but it will loose precision of the number

res = int(value)
print(res)
print(type(res))


# We can also work with complex numbers

var = 5j
