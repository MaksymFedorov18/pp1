ean_13 = input("Enter the EAN-13 number: ")
if ean_13.isdigit() and len(ean_13) == 13:
    if ean_13[:3] == "590":
        print('Article number is correct')
        print('Article manufactured in Poland')
    else:
        print('Article number is correct')
        print("Article wasn't manufactured in Poland")
else:
    print('Article number is not correct')