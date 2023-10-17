height= float(input('Enter your height in cm: '))
weight= float(input('Enter your weight in kg: '))
height_m= height / 100
BMI= weight / (height_m ** 2)
correct_weight= 18.5 <= BMI <= 24.9
print(f'Your BMI index:{BMI}')
print(f'Correct weight:{correct_weight}')