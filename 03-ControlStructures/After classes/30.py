time_24_hour = input("Enter time (24-hour format, hh:mm): ")
hours, minutes = map(int, time_24_hour.split(':'))

if hours < 12:
    period = "am"
    if hours == 0:
        hours = 12
else:
    period = "pm"
    if hours > 12:
        hours -= 12

time_12_hour = f"{hours}:{minutes:02d}{period}"
print(f"Time in 12-hour format: {time_12_hour}")