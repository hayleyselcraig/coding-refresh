# Day 12 - Practising lists of dictionaries, loops and filtering booking data.


# 'bookings' is a list containing multiple dictionaries.
# Each dictionary represents one photography booking.
# Each booking has the same keys: customer, shoot_type, price and paid.
bookings = [
    {
        "customer": "Lucy",
        "shoot_type": "Portrait",
        "price": 150,
        "paid": True
    },
    {
        "customer": "Emma",
        "shoot_type": "Wedding",
        "price": 500,
        "paid": False
    },
    {
        "customer": "Sophie",
        "shoot_type": "Family",
        "price": 200,
        "paid": True
    }
]


# Loop through each dictionary in the bookings list.
# 'bookings' = the whole list.
# 'item' = one individual booking dictionary at a time.
# item["paid"] accesses the value stored under the "paid" key.
# If paid is False, print the customer's name to show they have not paid.
for item in bookings:
    if item["paid"] == False:
        print(f"{item['customer']} has not paid")


# Loop through all bookings and check the shoot type.
# item["shoot_type"] gets the shoot type from the current booking.
# Only bookings where the shoot type is "Wedding" will be printed.
for item in bookings:
    if item["shoot_type"] == "Wedding":
        print(f"Wedding Booking: {item['customer']}")


# Loop through each booking and check its price.
# The > operator means "greater than".
# Only customers whose booking costs more than £180 will be printed.
for item in bookings:
    if item["price"] > 180:
        print(f"{item['customer']} - £{item['price']}")


# Loop through the bookings and check TWO conditions.
# 'and' means BOTH conditions must be True for the print statement to run.
# The customer must:
# 1. Have paid == False.
# 2. Have a booking price greater than £180.
for item in bookings:
    if item["paid"] == False and item["price"] > 180:
        print(f"{item['customer']} owes £{item['price']}")