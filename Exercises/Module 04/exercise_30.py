"""

Read a value in dollar currency and print it in real currency


"""
print('Input the dollar value')
dollar_value = float(input())

print('Input the dollar amount')
dollar_amount = float(input())

real_amount = float(dollar_amount*dollar_value)
print(f'{dollar_amount} dollars is equals to {real_amount} reais')


