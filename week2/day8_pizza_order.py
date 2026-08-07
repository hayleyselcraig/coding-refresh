
# Ask the customer these questions: What is your name? and How many pizzas would you like?
# each pizza costs £12

# Function 1 — calculate_total()
# Its job is to calculate the total price of the order.
# It should return the total.

# Function 2 — check_discount()
# This function receives the total from the first part.
# If the total price is:
# £50 or more → 10% discount
# Under £50   → no discount
# It should return the final price after any discount.

# Function 3 — display_order()

# calculate_total()
# What information does it NEED? pizza_quantity and pizza_price
# What does it RETURN? total
# check_discount()
# What information does it NEED? total
# What does it RETURN? final_total
# display_order()
# What information does it NEED? name, pizza_quantity, total, final total
# Does it actually need to return anything?

name = input("What is your name? ")
pizza_quantity = int(input("How many pizza's would you like to order? "))
pizza_price = 12

def calculate_total(pizza_quantity, pizza_price):
    total = pizza_quantity * pizza_price
    return total

total = calculate_total(pizza_quantity, pizza_price)

def check_discount(total):
    if total >= 50:
        discount = total / 10
        final_total = total - discount
    else:
        final_total = total
    
    return final_total

final_total = check_discount(total)

def display_order(name, pizza_quantity, total, final_total):
    print(f"Customer: {name}")
    print(f"Number of pizza's: {pizza_quantity}")
    print(f"Original total: {total}")
    print(f"Final total: {final_total}")

display_order(name, pizza_quantity, total, final_total)