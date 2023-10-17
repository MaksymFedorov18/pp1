import random
roll= random.randint(1,6)
guess= int(input('Guess the number 1-6: '))
correct= guess == roll
print(f'Dice roll is:{roll}')
print(f'Your guess is:{correct}')