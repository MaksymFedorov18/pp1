def hotel_list(hotels):
    return ", ".join([hotel["name"] for hotel in hotels])

def avg_price(hotels):
    if not hotels:
        return 0
    total_price = sum(hotel["price"] for hotel in hotels)
    return round(total_price / len(hotels))


Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

print("Hotels in Krakow:", hotel_list(Hotels_in_Krakow))
print("Average hotel price in Krakow:", avg_price(Hotels_in_Krakow))


print("\nHotels in Sopot:", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot:", avg_price(hotels_in_Sopot))


krakow_avg = avg_price(Hotels_in_Krakow)
sopot_avg = avg_price(hotels_in_Sopot)

if krakow_avg < sopot_avg:
    print("\nCheaper hotels in: Krakow")
elif krakow_avg > sopot_avg:
    print("\nCheaper hotels in: Sopot")
else:
    print("\nHotel prices are the same in Krakow and Sopot")