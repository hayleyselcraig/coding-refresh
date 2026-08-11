# Day 12 Warm-up - Practising accessing and updating dictionary values.

booking = {
    "customer": "Sophie",
    "shoot_type": "Family",
    "price": 175,
    "paid": False
}

# Print only the customer's name.
print(booking["customer"])

# Print only the shoot type.
print(booking["shoot_type"])

# Change the price to 200.
booking["price"] = 200

# Change paid to True.
booking["paid"] = True

# Add a new key called location with the value "Edinburgh".
booking["location"] = "Edinburgh"

# Print the whole dictionary.
print(booking)

# Create a new dictionary containing two lists.
booking = [
    {
    "customer": "Sophie",
    "shoot_type": "Family",
    "price": 175,
    "paid": False
    },
    {
    "customer": "Emma",
    "shoot_type": "Portrait",
    "price": 150,
    "paid": True
    }
    ]

# Print the customer name from the first booking.
print(booking[0]["customer"])

# Print the shoot type from the second booking.
print(booking[1]["shoot_type"])

# Loop through a list of dictionaries.
# 'booking' is the whole list containing all of the booking dictionaries.
# 'item' represents one individual booking dictionary at a time as the loop runs.
# item["customer"] accesses the customer value from the current dictionary.

for item in booking:
    print(item["customer"])

# Loop through each booking and access the shoot_type value
# from the current booking dictionary.

for item in booking:
    print(item["shoot_type"])

# Loop through each dictionary in the booking list.
# 'item' represents one booking dictionary at a time.
# Check the value stored under the "paid" key for the current booking.
# If the value is False, print the customer's name to show they have not paid.
for item in booking:
    if item["paid"] == False:
        print(f"{item['customer']} has not paid yet.")
    else:
        print(f"{item['customer']} has paid.")