"""

Calculate the sum of the first 50 even numbers.

"""
qty = 0
list0 = []
list1 = []

print('Please input a number of even numbers you want:')
n = int(input())
nl0 = int(n * 2 + 1)
print(nl0)

# while qty == 0:
#     list0 = list(range(1, 101))
#     list1 = sum(list0[1:50])
#     qty += 1
# print(list1)

list0 = list(range(1, nl0))
list1 = sum(list0[1:n])
print(list1)
