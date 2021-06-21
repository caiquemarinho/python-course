"""

Ranges

 - We need to know loops to use the range.
 - We need to understand range to better work with for loops.

Ranges are used to generate numeric sequences, not in a random way, but in a specific way.

range(stop_value)

PS: The stop value is not included, default starting at 0, and incrementing 1.

"""

# First Example

for num in range(11):
    print(num)

# Second Example

for num in range(1, 11):
    print(num)

# Third Example

for num in range(1, 11, 2):
    print(num)

# Fourth Example

for num in range(10, 0, -1):
    print(num)
