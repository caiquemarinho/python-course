"""

Breaks

Leaving loops with brakes

Works the same way on C or Java

Brake forces to leave the loop in a programed way.


"""

# First Example

for number in range(1,11):
    if number == 6:
        break
    else:
        print(number)
print('Exiting the loop')

# Second Example

while True:
    command = input('Type leave to exit ')
    if command == 'leave':
        break
