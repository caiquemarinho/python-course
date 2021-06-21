"""

Variable Scope


            Scope
|-----------------------------|

1 - Global Variables:
    - They are recognized in the in whole application.

2 - Local Variables:
    - They are recognized only in the block or file were the declaration happened.

To declare a variable in Python we do:

variable_name = variable_value

Python is a language with with dynamic type, that means that in the act of
declare a variable you do not specify it's type.

"""

number = 42
print(number)
print(type(number))

number = 'Geek'
print(number)
print(type(number))

# print(invalid)

number = 42
# new = 0 Declaring the variable outside of the block makes it a global variable.

if number > 10:
    new = number + 10  # The declaration of the variable happens in the block, making it a local variable.
    print(new)

print(new)
