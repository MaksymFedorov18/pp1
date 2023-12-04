countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Ukraine", "population":4000000},
    {"name":"Germany", "population":4800000},
    {"name":"Serbia", "population":7000000},
    {"name":"Kosovo", "population":1000000},
]

print("COUNTRY\tPOPULATION")
i = 0

while i < len(countries):
    country = countries[i]
    print(f"{country['name']}\t{country['population']}")
    i += 1