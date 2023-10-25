washing_times = {
    "jacket": 40,
    "underwear": 70,
    "shoes": 20
}

washing_product = input("Enter the washing product (jacket, underwear, or shoes): ").lower()
rinse = input("Include an additional rinse? (True or False): ").lower() == "true"
spin = input("Include an additional spin? (True or False): ").lower() == "true"

if washing_product in washing_times:
    total_washing_time = washing_times[washing_product]
    if rinse:
        total_washing_time += 15
    if spin:
        total_washing_time += 9
    print(f"Total washing time: {total_washing_time} minutes")
else:
    print("Invalid washing product. Please choose 'jacket,' 'underwear,' or 'shoes.'")