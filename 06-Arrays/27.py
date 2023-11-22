numbers = [12, 19, 4, 9, 10]

def star(n):
    result = ""
    for num in n:
        row = str(num * '*')
        result += f"{num}: {row}\n"
    return result

print(star(numbers))