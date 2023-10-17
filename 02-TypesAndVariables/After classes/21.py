height = float(input('Enter your height in cm: '))
inches = height / 2.54
feet = inches // 12
remain = inches % 12
print(f'I am {height}cm tall, i.e. {int(feet)} feet and {int(remain)} inches')