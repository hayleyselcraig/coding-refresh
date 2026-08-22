# Day 15 - Functions Refresher
# Revising functions, parameters, arguments, return values,
# conditions, dictionaries and loops.


# --------------------------------------------------
# 1. SIMPLE FUNCTION WITH ONE PARAMETER
# --------------------------------------------------

# 'name' is a parameter.
# A parameter acts as a placeholder for information that
# will be given to the function when it is called.
def greet_user(name):
    print(f"Hello {name}")


# "Hayley" is the argument being passed into the function.
# Inside the function, name will contain "Hayley".
greet_user("Hayley")


# --------------------------------------------------
# 2. FUNCTION WITH TWO PARAMETERS
# --------------------------------------------------

# A function can receive more than one piece of information.
# Here, name and age are both parameters.
def greet_user_with_age(name, age):
    print(f"Hello {name}, you are {age} years old.")


# Arguments are matched to parameters by position:
# name = "Hayley"
# age = 26
greet_user_with_age("Hayley", 26)


# --------------------------------------------------
# 3. USING RETURN
# --------------------------------------------------

# 'return' sends a value back to wherever the function was called.
# This is different from print(), which only displays something.
def add_numbers(num1, num2):
    return num1 + num2


# The function returns 17.
# That returned value is then stored inside 'total'.
total = add_numbers(10, 7)

# Print the value that was returned and stored.
print(total)


# --------------------------------------------------
# 4. CALCULATING AND RETURNING A VALUE
# --------------------------------------------------

def calculate_price(price, quantity):

    # Multiply the two values and store the answer.
    final_price = price * quantity

    # Send the calculated value back out of the function.
    return final_price


# 10 and 3 are passed into the function.
# The returned value (30) is stored in total.
total = calculate_price(10, 3)
print(total)


# --------------------------------------------------
# 5. DISCOUNT FUNCTION
# --------------------------------------------------

# This function takes a price and discount,
# calculates the new amount and returns it.
def calculate_discount(price, discount):

    final_amount = price - discount

    return final_amount


# 100 - 20 = 80
# The returned value is stored in final_price.
final_price = calculate_discount(100, 20)
print(final_price)


# --------------------------------------------------
# 6. FUNCTION WITH IF / ELSE
# --------------------------------------------------

# This function checks a condition before deciding
# which value should be returned.
def check_booking_price(price):

    # > means greater than.
    # £300 itself would NOT count as expensive.
    if price > 300:
        return "Expensive booking"

    # If the condition above is False, run this instead.
    else:
        return "Standard booking"


result = check_booking_price(500)
print(result)


# --------------------------------------------------
# 7. FUNCTION WITH TWO CONDITIONS
# --------------------------------------------------

# This function checks both the price and payment status.
def check_booking(price, paid):

    # 'and' means BOTH conditions must be True.
    #
    # Condition 1: price must be greater than 300
    # Condition 2: paid must be False
    if price > 300 and paid == False:
        return "Payment needed"

    # If either condition is False, return "Booking okay".
    else:
        return "Booking okay"


result = check_booking(500, False)
print(result)


# --------------------------------------------------
# 8. PASSING A DICTIONARY INTO A FUNCTION
# --------------------------------------------------

# 'bookings' is a LIST.
# Each item inside the list is a DICTIONARY representing one booking.
bookings = [
    {"customer": "Emma", "price": 500, "paid": False},
    {"customer": "Lucy", "price": 150, "paid": True},
    {"customer": "Sophie", "price": 350, "paid": False}
]


# This function receives ONE booking dictionary at a time.
#
# bookings = the whole list
# booking  = one dictionary from the list
def check_payment(booking):

    # Access the value stored under the "paid" key
    # in the current booking dictionary.
    if booking["paid"] == False:

        # Access the customer and price values from
        # the same dictionary and place them into an f-string.
        return f'{booking["customer"]} needs to pay £{booking["price"]}'

    else:
        return f'{booking["customer"]} has paid'


# Loop through the whole bookings list.
# 'booking' represents ONE dictionary at a time.
for booking in bookings:

    # Pass the current dictionary into check_payment().
    #
    # The function RETURNS a message.
    # print() then displays that returned message.
    print(check_payment(booking))