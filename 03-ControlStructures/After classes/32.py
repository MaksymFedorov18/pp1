question_1 = input('Are you interested in computer science? (Y/N): ').upper()
question_2 = input('Do you like playing computer games? (Y/N): ').upper()
question_3 = input('Do you have an Instagram account? (Y/N): ').upper()

if question_1 == "Y":
    question_1 = True
else:
    question_1 = False

if question_2 == "Y":
    question_2 = True
else:
    question_2 = False

if question_3 == "Y":
    question_3 = True
else:
    question_3 = False

print(f'Interested in computer science:', "Yes" if question_1 else "No")
print(f'Playing computer games:', "Yes" if question_2 else "No")
print(f'Has an Instagram account:', "Yes" if question_3 else "No")
