basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# Create a new dictionary 'person' containing data from both dictionaries
person = basic_data.copy()
person.update(advanced_data)

# Display the contents of the 'person' dictionary
print("Contents of the 'person' dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
