names_pl = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = names_pl[0]
for name in names_pl:
    if len(name) > len(longest_name):
        longest_name = name

print(longest_name)