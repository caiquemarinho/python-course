"""

Receive ten values and print the average of it.

"""

sum1 = 0
qty = 0
avg = 0

for n in range(1, 11):
    num = int(input(f'Input ten int numbers : '))
    if num >= 0:
        sum1 = sum1 + num
        qty = qty + 1

avg = sum1/qty
print(f'The average is {avg}')


# som = 0
# avg = 0
# qty = 0
#
# print('Type 10 int numbers')
# for number in range(1,11):
#     num = int(input())
#     if num >= 0
#         som =  som + 1
#         qty =  qty + 1
# avg = som / qty
