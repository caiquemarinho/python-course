"""

To help a salesman you are developing a software that will receive a value and generates the:

Total amount with 10% discount.
A finance pay if split in 3x
The salesman cut in case if it's paid in cash (5% of the sales value after the discount)
The salesman cut if it's financed (5% of the full value)

"""

cash_discount = 0.10
cut = 0.05

print('Insert the value of the product')
product = float(input())

cash = product - (product * cash_discount)

finance = product / 3

sm_cut_cash = cash * cut

sm_cut_finance = finance * cut

print(f'Cash value is {cash}')

print(f'Finance value os {finance}')

print(f'Salesman cut paying in cash is {sm_cut_cash}')

print(f'Salesman cut paying financed is {sm_cut_finance}')
