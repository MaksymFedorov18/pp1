facebook = int(input("Do you have a Facebook account? (1 for yes, 0 for no): "))
twitter = int(input("Do you have a Twitter account? (1 for yes, 0 for no): "))
instagram = int(input("Do you have an Instagram account? (1 for yes, 0 for no): "))

can_be_influencer = (facebook + twitter + instagram) >= 2

if can_be_influencer:
    print("This person can be a good influencer.")
else:
    print("This person may not be a good influencer.")
