for number in range(1, 31):
    output = ""

    if number % 3 == 0:
        output += "THREE"

    if number % 5 == 0:
        output += "FIVE"

    if number % 3 == 0 and number % 5 == 0:
        output = "BINGO"

    if not output:
        output = number

    print(output, end=" ")



