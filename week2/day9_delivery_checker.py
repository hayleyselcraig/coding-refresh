# Create a delivery checker that uses functions to calculate delivery cost and the final order total.

# check_delivery()
# NEEDS: order_total
# RETURNS: delivery_cost

# calculate_final_total()
# NEEDS: delivery_cost, order_total
# RETURNS: final_total

# display_order()
# What information does it NEED? name, order_total, final_total
# Does it need to return anything? no

name = input("What is your name? ")
order_total = float(input("What is your order total? "))

def check_delivery(order_total):
    if order_total >= 50:
        delivery_cost = 0
    else:
        delivery_cost = 4.99
    
    return delivery_cost

delivery_cost = check_delivery(order_total)

def calculate_final_total(order_total, delivery_cost):
    final_total = order_total + delivery_cost
    return final_total

final_total = calculate_final_total(order_total, delivery_cost)

def display_order(name, order_total, final_total):
    print(f"customer name: {name}")
    print(f"Order total: {order_total}")
    print(f"Final cost with delivery: {final_total}")

display_order(name, order_total, final_total)