# Day 16 - Python Problem Solving
# Practising functions, conditions, lists, dictionaries and loops.

## EXERCISE 1
# Write a function called check_age that:
# takes age as a parameter
# returns "Adult" if the age is 18 or over
# otherwise returns "Under 18"
# call it with 26
# store what it returns in result
# print result

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Under 18"
    
result = check_age(26)
print(result)

## EXERCISE 2
# Create a function called:
# check_temperature
# It takes one parameter:
# temperature
# It should return:
# "Hot" if the temperature is 25 or higher
# "Warm" if the temperature is 15 or higher
# "Cold" otherwise

def check_temperature(temp):
    if temp >= 25:
        return "Hot"
    elif temp >= 15:
        return "Warm"
    else:
        return "Cold"
    
result = check_temperature(18)
print(result)

## EXERCISE 3
# Create a function called:
# count_passes
# It should:
# take scores as a parameter
# go through every score in the list
# count how many scores are 50 or higher
# return the final count

scores = [45, 72, 88, 31, 65, 90]
def count_passes(scores):
    count = 0
    for number in scores:
        if number >= 50:
            count += 1
    return count
    
result = count_passes(scores)
print(result)

## EXERCISE 4
# Write a function
# calculate_total
# It should:
# take prices as a parameter
# start a variable called total at 0
# loop through every price
# add each price to total
# after the loop has finished, return total
# call the function and print the result

prices = [120, 250, 80, 300, 150]

def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

result = calculate_total(prices)
print(result)


