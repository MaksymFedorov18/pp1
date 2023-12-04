import json
movie = {
    "title":"Control",
    "year": 2007,
    "actor":{"leading":"Sam Riley","supporting":"Samanta Morton"},
    "oscar":False,
    "budget": "6.4 million USD"
}

with open("favourite.json", "w") as file:
    json.dump(movie, file)