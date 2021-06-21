"""

Create a program that reads 10 int numbers, ignoring the negative ones and prints the average.

"""

# sum1 = 0
# qty = 0
# avg = 0
#
# for n in range(1, 11):
#     num = int(input(f'Input ten int numbers : '))
#     if num >= 0:
#         sum1 = sum1 + num
#         qty = qty + 1
#
# avg = sum1/qty
# print(f'The average is {avg}')

# v2

sum1 = 0
qty = 0
avg = 0

while qty < 10+1:
    num = int(input(f'Input ten int numbers : '))
    if num >= 0:
        sum1 = sum1 + num
        qty = qty + 1
        print(qty)
        print(sum1-10)

avg = sum1/qty
print(f'The average is {avg}')

