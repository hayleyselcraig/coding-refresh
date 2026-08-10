# Practising Python dictionaries using photography booking information.

## Creating a dictionary withs KEYS:VALUES.
booking = {
    "customer": "Sarah",
    "shoot_type": "Wedding",
    "price": 250
}

## Printing the dictionary using f strings.
print("Booking Details")
print(f"Customer: {booking["customer"]}")
print(f"Shoot Type: {booking["shoot_type"]}")
print(f"Price: £{booking["price"]}")

## Updating a value ("portrait" will replace "wedding") (300 will replace 250)
booking["shoot_type"] = "Portrait"
booking["price"] = 300

## Adding a new key and value to the dictionary.
booking["date"] = "15th August"

## Accessing a dictionary- will print as this: {'customer': 'Sarah', 'shoot_type': 'Portrait', 'price': 250}
print(booking)

## Deleting a key from the dictionary.
del booking["price"]

print(booking)

for key in booking:
    print(f"{key}: {(booking[key])}")