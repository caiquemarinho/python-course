""""
While R =! 0

"""
r = 1

while r != 0:
    print(f'Insert R1')
    r1 = int(input())
    print(f'Insert R2')
    r2 = int(input())

    r = r1*r2/(r1+r2)
