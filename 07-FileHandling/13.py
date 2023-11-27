films = ["A Nightmare on Elm Street", "A Bronx Tale", "Anaconda", "Amistad", "Awakenings"]
counter = 0
file = open("movies.txt" , "w")
for element in films:
    counter+=1
    file.write(f"{counter}. {element}\n")
file.close()
