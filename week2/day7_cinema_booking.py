# 🏪 Day 7 Challenge – Cinema Ticket Booking
# ⏱️ 30–40 minutes
# Your program should:
# Welcome the user.
# Ask for:
# their name
# their age
# how many tickets they want
# Then work out the ticket price using these rules:
# Under 12 → £5 per ticket
# 12–64 → £10 per ticket
# 65+ → £7 per ticket
# Finally display something like:

# Function 1:
# Purpose: get ticket price
# Parameters: total
# Returns: total

# Function 2:
# Purpose: display booked tickets
# Parameters: name, ticket_quantity, ticket_price, total
# Returns: total

name = input("What is your name? ")
age = int(input("What is your age? "))
ticket_quantity = int(input("How many tickets do you wnat to book? "))

def get_ticket_price(age):
    if age <= 12:
        ticket_price = 5
    elif age <= 64:
        ticket_price = 10
    else:
        ticket_price = 7

    return ticket_price
ticket_price = get_ticket_price(age)

def calculate_ticket_price(ticket_price, ticket_quantity):
     total = ticket_price * ticket_quantity
     return total

total = calculate_ticket_price(ticket_price, ticket_quantity)

def display_ticket(name, ticket_quantity, ticket_price, total):
     print(f"Hi {name}!")
     print(f"Tickets: {ticket_quantity}")
     print(f"Price per ticket: {ticket_price}")
     print(f"Total: {total}")

display_ticket(name, ticket_quantity, ticket_price, total)