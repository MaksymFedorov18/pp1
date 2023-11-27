import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}", message)

# Convert temperature values to integers
temperature_values = [int(temp) for temp in temperatures]

# Calculate the average temperature
average_temperature = sum(temperature_values) / len(temperature_values)

# Print the result
print(f"The average temperature is: {average_temperature}C")
