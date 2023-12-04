import json
name= input("Enter your name: ")
surname= input("Enter your surname: ")
age= int(input("Enter your age: "))
is_student= bool(input("Are you a student?(0 for No or 1 for Yes): "))
height= int(input("Enter your height(in cm): "))
weight= int(input("Enter your weight(in kg): "))

student = {
    "name": name,
    "surname": surname,
    "age": age,
    "is_student": is_student,
    "height": height,
    "weight": weight
}

with open("student.json", "w") as file:
    json.dump(student,file)