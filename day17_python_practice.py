# Day 17 - Python Problem Solving
# Practising functions, loops, conditions, lists and return values.


# --------------------------------------------------
# 1. CALCULATE TOTAL OF EXPENSIVE PRICES
# --------------------------------------------------

prices = [120, 250, 80, 300, 150]


# This function takes a list of prices as its parameter.
# It adds together only the prices greater than £150.
def calculate_expensive_total(prices):

    # Start the running total at 0.
    total = 0

    # Loop through each price in the list.
    # 'price' represents one number from the list at a time.
    for price in prices:

        # Only add the price if it is greater than 150.
        if price > 150:
            total += price

    # Return the final total AFTER every price has been checked.
    return total


result = calculate_expensive_total(prices)
print(result)  # 550


# --------------------------------------------------
# 2. CALCULATE THE AVERAGE SCORE
# --------------------------------------------------

scores = [70, 80, 90, 60, 100]


# This function calculates the average of all scores in the list.
def calculate_average(scores):

    # Start the running total at 0.
    total = 0

    # Add every score to the total.
    for score in scores:
        total += score

    # len(scores) tells us how many items are in the list.
    # We calculate the average AFTER the loop has finished
    # because we need the final total first.
    average = total / len(scores)

    return average


result = calculate_average(scores)
print(result)  # 80.0


# --------------------------------------------------
# 3. FIND THE HIGHEST SCORE
# --------------------------------------------------

# This function finds the largest number in the scores list.
def find_highest_score(scores):

    # Start by assuming the first score is the highest.
    # scores[0] means the first item in the list.
    highest = scores[0]

    # Check every score in the list.
    for score in scores:

        # If the current score is greater than the highest
        # score found so far, update 'highest'.
        if score > highest:
            highest = score

    # Return the highest score after checking the whole list.
    return highest


result = find_highest_score(scores)
print(result)  # 100


# --------------------------------------------------
# 4. FIND THE LOWEST SCORE
# --------------------------------------------------

# This uses the same idea as finding the highest score,
# but this time we look for a smaller number.
def find_lowest_score(scores):

    # Start by assuming the first score is the lowest.
    lowest = scores[0]

    # Check every score in the list.
    for score in scores:

        # If the current score is lower than the lowest
        # score found so far, update 'lowest'.
        if score < lowest:
            lowest = score

    return lowest


result = find_lowest_score(scores)
print(result)  # 60


# --------------------------------------------------
# 5. FIND THE RANGE OF THE SCORES
# --------------------------------------------------

# The range is the difference between the
# highest and lowest values.
def find_range(scores):

    # Start both values using the first item in the list.
    lowest = scores[0]
    highest = scores[0]

    # We can find both the lowest and highest
    # using the SAME loop.
    for score in scores:

        # Check if we have found a new lowest score.
        if score < lowest:
            lowest = score

        # Check if we have found a new highest score.
        if score > highest:
            highest = score

    # This happens AFTER the loop because we need to know
    # the final highest and lowest values first.
    score_range = highest - lowest

    return score_range


result = find_range(scores)
print(result)  # 40

# --------------------------------------------------
# DAY 17 NOTES
# --------------------------------------------------

# A common pattern when working with lists inside functions:
#
# 1. Create a starting value
#       total = 0
#       highest = scores[0]
#       lowest = scores[0]
#
# 2. Loop through the list
#       for score in scores:
#
# 3. Check or update something inside the loop
#       total += score
#
#       if score > highest:
#           highest = score
#
# 4. Do calculations that need the FINAL values
#    after the loop has finished.
#
# 5. Return the final result.
#
# IMPORTANT:
# return ends the function.
# If we need the loop to check every item,
# don't return too early inside the loop.