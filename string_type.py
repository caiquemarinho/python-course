"""
String Type

In Python a data is a string type when:

Is between simple quotation marks -> 'A string', '234', 'a', 'True' '42.3'
Is between quotation marks -> "A string", "234", "a", "True" "42.3"
Is between triple simple quotation marks -> '''A string''', '''234''', '''a''', '''True''' '''42.3'''
"""
# Is between triple quotation marks -> """A string""", """234""", """a""", """True""" """42.3"""
""""
name = 'Joe'
print(name)
print(type(name))

name = "Joe's Bar"
print(name)
print(type(name))

name = 'Joe \nDive'
print(name)
print(type(name))

name =  " ""Joe
Dive"" "
print(name)
print(type(name))
"""

name = 'Geek University'

print(name.upper())
print(name.lower())

print(name.split())  # Turns the string in to a list of strings

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

print(name[0:4])  # Method called string slice.
print(name[5:15])  # Method called string slice.

# [   0,       1      ]
# ['Geek' 'University']
print(name.split()[0])

print(name.split()[1])

print(name[::-1])  # [::-1] -> It goes from the first element until the last one and inverts it

print(name.replace('e', 'i'))



