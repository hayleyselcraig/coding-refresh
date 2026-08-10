# Day 11 Challenge - Create a photography booking manager using dictionaries, user input and conditionals.
booking = {
    "customer": "Lucy",
    "shoot_type": "Portrait",
    "price": 120,
    "paid": False
}

print(booking["customer"])

booking["price"] = 150

booking["location"] = "Edinburgh"

payment_status = input("Has the customer paid yet? ")
if payment_status == "yes":
    booking["paid"] = True
else:
    booking["paid"] = False

for key in booking:
    print(f"{key}: {(booking[key])}")