"""

Loop While

while boolean expression
    execute the loop

The while block will be executed until the boolean expression becomes true.


"""

num = 1

# First Example (You need to be careful with a stop criteria, otherwise a infinite loop will be created.

while num < 10+1:
    print(num)
    num = num + 1\


# Second Example

answer = ''

while answer != 'Yes':
    answer = input('Are you done, Jessica? ')
