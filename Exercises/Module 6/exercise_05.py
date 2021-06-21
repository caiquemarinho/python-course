"""

Write a code that will SUM 10 different values

"""

sum1 = 0
i = 1

# while i < 10+1:
#     num = int(input('Input the number to sum: '))
#     sum1 = sum1 + num
#     i = i + 1
# print(sum1)


for i in range(1, 11):
    num = int(input('Input the number to sum: '))
    sum1 = sum1 + num
print(sum1)
