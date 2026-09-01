# Day 18 - Python Refresher
# Refreshing functions, lists, loops and conditions after a few days away.


# --------------------------------------------------
# 1. COUNT NUMBERS GREATER THAN 10
# --------------------------------------------------

# Create a list of numbers that we will pass into the function.
numbers = [5, 12, 8, 20, 3]


# This function takes a list of numbers as its parameter
# and counts how many numbers are greater than 10.
def count_large_numbers(numbers):

    # Start the counter at 0.
    # This is BEFORE the loop because we only want to set it to 0 once.
    count = 0

    # Loop through every number in the list.
    # 'number' represents one item from the list at a time.
    for number in numbers:

        # Check whether the current number is greater than 10.
        if number > 10:

            # If it is, increase the counter by 1.
            # This is the same as: count = count + 1
            count += 1

    # Return the final count AFTER every number has been checked.
    return count


# Call the function using our numbers list.
# The returned value is stored in 'result'.
result = count_large_numbers(numbers)

# Display the returned result.
print(result)  # 2


# --------------------------------------------------
# 2. ADD TOGETHER PRICES GREATER THAN £75
# --------------------------------------------------

# Create a list containing different prices.
prices = [50, 120, 30, 200, 80]


# This function takes a list of prices
# and adds together only the prices greater than £75.
def calculate_large_total(prices):

    # Start the running total at 0.
    # This is BEFORE the loop so it isn't reset every time.
    total = 0

    # Loop through each price in the list.
    for price in prices:

        # Only add the current price if it is greater than 75.
        if price > 75:

            # Add the current price onto the running total.
            # This is the same as: total = total + price
            total += price

    # Return the final total AFTER the whole list has been checked.
    return total


# Pass the prices list into the function.
# The function returns 400, which is stored in 'result'.
result = calculate_large_total(prices)

# Display the result.
print(result)  # 400


# --------------------------------------------------
# DAY 18 NOTES
# --------------------------------------------------

# A useful pattern to remember:
#
# BEFORE THE LOOP:
# Set up something that should only happen once.
#
#     count = 0
#     total = 0
#
# INSIDE THE LOOP:
# Do something for every item in the list.
#
#     for number in numbers:
#         if number > 10:
#             count += 1
#
# AFTER THE LOOP:
# Use or return the FINAL result.
#
#     return count
#
# Remember:
# count += 1      -> increases a COUNT by one
# total += price  -> adds the VALUE of price to a running total
#
# return ends the function, so if the whole list needs
# to be checked first, return should come after the loop.