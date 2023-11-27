with open("30lines.txt", "r") as file:
    file_content = file.readlines()

with open("copy.txt", "w") as file_copy:
    file_copy.write(file_content)