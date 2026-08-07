
name = input("What is your name? ")
height = int(input("What is your height in cm? "))

def check_height(height):
    if height >= 140:
        ride_status = "Full Access."
    elif height >= 120 and height <= 139:
        ride_status = "Adult Required."
    else:
        ride_status = "Too short."
    return ride_status

ride_status = check_height(height)

def display_result(name, height, ride_status):
    print(f"Hi {name}!")
    print(f"Your height: {height}")
    print(f"Ride Status: {ride_status}")

display_result(name, height, ride_status)