# Day 14 - Python refresher after a short break
# Revising lists, loops, conditions, counting and dictionaries.


# --------------------------------------------------
# COUNTING ITEMS IN A LIST
# --------------------------------------------------

# Create a list containing different booking prices.
prices = [120, 250, 80, 300, 150]

# Create a count variable and start it at 0.
# This will keep track of how many prices are greater than £150.
count = 0

# Loop through the prices list.
# 'number' represents ONE price from the list at a time.
for number in prices:

    # Check whether the current number is greater than 150.
    if number > 150:

        # If the condition is True, increase count by 1.
        # += 1 is the same as writing: count = count + 1
        count += 1

# Print the FINAL count after the whole list has been checked.
# This is outside the for loop so it only prints once.
print(count)


# --------------------------------------------------
# DICTIONARY REFRESHER
# --------------------------------------------------

# Create a dictionary containing information about one booking.
# A dictionary stores information as key:value pairs.
booking = {
    "customer": "Emma",
    "shoot_type": "Wedding",
    "price": 500,
    "paid": False
}

# Access the value stored under the "customer" key.
# Dictionary values are accessed using:
# dictionary_name["key"]
#
# Here:
# booking = the whole dictionary
# "customer" = the key we want to access
# "Emma" = the value stored under that key
print(booking["customer"])

# Challenge - Photography Booking List
## Using that one list of dictionaries, write code that does these things:
# Print every customer's name.
# Print only the customers who have not paid.
# Print only the Wedding bookings.
# Print the customer's name and price if their booking costs more than £200.
# Harder: Print the customer's name only if their booking costs more than £200 AND they haven't paid.

bookings = [
    {
        "customer": "Emma",
        "shoot_type": "Wedding",
        "price": 550,
        "paid": False
    },
    {
        "customer": "Lucy",
        "shoot_type": "Portrait",
        "price": 150,
        "paid": True
    },
    {
        "customer": "Sophie",
        "shoot_type": "Family",
        "price": 250,
        "paid": False
    },
    {
        "customer": "Ryan",
        "shoot_type": "Wedding",
        "price": 600,
        "paid": True
    }
]

# Print every customer's name.
for booking in bookings:
    print(booking["customer"])

# Print only the customers who have not paid.
for booking in bookings:
    if booking["paid"] == False:
        print(f'{booking["customer"]} has not paid.')

# Print only the Wedding bookings.
for booking in bookings:
    if booking["shoot_type"] == "Wedding":
        print(f'{booking["customer"]} has booked shoot type: {booking["shoot_type"]}')

# Print the customer's name and price if their booking costs more than £200.
for booking in bookings:
    if booking["price"] > 200:
        print(f'{booking["customer"]} booking costs £{booking["price"]}')

# Harder: Print the customer's name only if their booking costs more than £200 AND they haven't paid.
for booking in bookings:
    if booking["price"] > 200 and booking["paid"] == False:
        print(f'{booking["customer"]} booking costs £{booking["price"]} and they have not yet paid.')