correct_pin = '0805'
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entered_pin = input("Enter the PIN code: ")

    if entered_pin == correct_pin:
        print("Access granted.")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print("Incorrect...")
            print(f"Remaining attempts: {remaining_attempts}")
        else:
            print("Sorry, your payment card has been blocked.")

