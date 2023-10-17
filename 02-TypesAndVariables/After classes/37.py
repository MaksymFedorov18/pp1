personal_data= input('Please enter your full name and birthdate: ')
data_parts = personal_data.split(', ')

name_and_title = data_parts[0]

dob = data_parts[1].split()[-1]

name_parts = name_and_title.split()

title = name_parts[0]
first_name = name_parts[1]
last_name = name_parts[2]

initials = first_name[0] + last_name[0]

print(f"Description: {personal_data}")
print(f"Name: {first_name}")
print(f"Surname: {last_name}")
print(f"Initials: {initials}")
print(f"Born: {dob}")