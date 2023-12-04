winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}
sum = 0
for value in winter_semester.values():
    sum += int(value)

print("The total number of hours in the winter semester is",sum)