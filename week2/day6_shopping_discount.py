# Function practice exercise.
# Create separate functions to calculate a shopping discount and display the result.
# Practice passing variables between functions and using return values.

name = input("What is your name? ")
shopping_total = int(input("What is your shopping total? "))
def calculate_discount(total):
    if total >= 50:
        discount_status = True
        discount = total / 10
        new_total = total - discount
    else:
        discount_status = False
        new_total = total

    return new_total, discount_status

new_total, discount_status = calculate_discount(shopping_total)


def display_result(name, shopping_total, new_total, discount_status):
    if discount_status == True:
        print(f"Hi {name}! ")
        print(f"Original total: {shopping_total} ")
        print(f"New total: {new_total} ")
    else:
        print(f"Hi {name}! ")
        print(f"Original total: {shopping_total} ")
        print("No discount applied.")

display_result(name,shopping_total, new_total, discount_status )


