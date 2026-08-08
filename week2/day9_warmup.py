# Warm-up: Create a function that converts minutes into seconds.

minutes = int(input("How many minutes would you like to convert? "))

def convert_to_seconds(minutes):
    seconds = minutes * 60
    return seconds

seconds = convert_to_seconds(minutes)

print(f"Minutes: {minutes}")
print(f"Secconds: {seconds}")