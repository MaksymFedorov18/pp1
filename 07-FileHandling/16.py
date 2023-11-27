file_name = input("Enter file name: ")
try:
    file = open(f"{file_name}", "r")
    file_content = file.readlines()
    lines_number = len(file_content)
    file.close()
    print("Number of lines:", lines_number)

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
