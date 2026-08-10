# Day 11 - Dictionary Booking Challenge
# Practising creating and working with a Python dictionary.


# Create a dictionary to store photography booking information.
booking = {
    "customer" : "Emma",
    "shoot_type" : "Family",
    "price" : 180,
    "location" : "Edinburgh"
}

# Update the price value in the dictionary.
booking["price"] = 200

# Add a new key called "paid" with a Boolean value.
booking["paid"] = False



# Loop through the dictionary keys and print each key with its value.
for key in booking:
    print(f"{key}: {(booking[key])}")