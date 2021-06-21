"""

Calculate the BMI of the user.

"""

print('Input your height')
height = float(input())

print('Input your weight')
weight = float(input())

bmi = weight / height**2

print(bmi)

# if BMI < 18.5:
#     print('Bellow weight')
# elif BMI >= 18.5

if bmi < 18.5:
    print('Under ideal weight')
elif (bmi >= 18.5) and (bmi < 25.0):
    print("Ideal weight")
elif (bmi >= 25.0) and (bmi < 30.0):
    print('Above ideal weight')
elif (bmi >= 30.0) and (bmi < 35.0):
    print('Obesity 1')
elif (bmi >= 35.0) and (bmi <= 40):
    print('Obesity 2')
else:
    print('Obesity 3')

