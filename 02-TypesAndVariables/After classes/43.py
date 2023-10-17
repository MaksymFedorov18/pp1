name = input("Enter your name: ")
numerical_representations = []
for char in name:
    numerical_representation = ord(char)
    numerical_representations.append(numerical_representation)

print("Numerical representations of characters in your name:")
for i in range(len(name)):
    print(f"{name[i]}: {numerical_representations[i]}")