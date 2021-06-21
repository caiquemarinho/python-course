"""
Lists

Lists in Python work like vectors (arrays) ins another languages, with the difference
of being dynamic and also receiving any type of data.


Language C/Java Arrays
    - Have a fixed data type;
    If you create an array int type, this arrays will always have
    the int type and will have max 5 values.


Python
    - It's Dynamic does not have a fixed type.
    You can create a list and add as many elements/types as you want
    binding only to the amount of resource available in the computer.

    Lists in Python []

"""

list1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

list2 = ['C', 'a', 'i', 'q', 'u', 'e']

list3 = []

list4 = list(range(11))

list5 = list('Caique')

# We can easy check if a value is present in a list.

num = 15
if num in list4:
    print(f'{num} Found')
else:
    print(f'{num} Not Found')


# We can easily order a list

list1.sort()
print(list1)

list5.sort()
print(list5)

# We can easily count the number of values in a list.
print(list1.count(1))
print(list5.count('e'))

print("test")

