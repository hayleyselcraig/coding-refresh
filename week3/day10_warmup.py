## Create a function that converts kilometres into miles.
## 1 kilometre = 0.621371 miles

kilometres = float(input("How many kilometres do you want to convert? "))

def convert_to_miles(kilometres):
    miles = kilometres * 0.621371
    return miles

miles = convert_to_miles(kilometres)

print(f"Kilometres: {kilometres}")
print(f"Miles: {miles}")