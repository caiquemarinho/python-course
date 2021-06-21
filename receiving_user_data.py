"""

Receiving user data

input() -> Every data received through input has the String type

"""
# Data entry
print("What is you name?")
name = input()

# Example from Python 2.x
# print("Welcome %s" % name)

# Example from Python 3.x
# print('Welcome {0}'.format(name))

# Example from Python 3.7
print(f'Welcome {name}')

print("What is your age?")
age = input()

# Processing

# Output

# Example from Python 2.x
# print("%s is %s years old" % (name, age))

# Example from Python 3.x
# print("{0} is {1} years old".format(name, age))

# Example from Python 3.7

print(f'{name} is {age} years old')

print(f'{name} was born in {2021 - int(age)}')

