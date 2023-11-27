file = "30lines.txt"
try:
    with open("30lines.txt", 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)
        current_line = 0

        while current_line < total_lines:

            for i in range(current_line, min(current_line + 5, total_lines)):
                print(lines[i].strip())  

            input("Press Enter to continue...")
            current_line += 5

except FileNotFoundError:
    print(f"Error: File '{file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
