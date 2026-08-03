## Create a function called calculate_average(), takes three numbers as parameters, returns the average, calls the function three different times with different numbers and then prints each result.

# The function is responsible for everything:
# - asking the user for input
# - calculating the average
# - returning the result
def calculate_average():
    first_num = int(input("First number: "))
    second_num = int(input("Second number: "))
    third_num = int(input("Third number: "))

    average = (first_num + second_num + third_num) / 3

    return average


average = calculate_average()
print(average)

# The function only performs the calculation.
# The user input happens outside the function and is passed in as arguments.
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average


first_num = int(input("First number: "))
second_num = int(input("Second number: "))
third_num = int(input("Third number: "))

average = calculate_average(first_num, second_num, third_num)

print(average)

# This is useful for testing.
# Instead of asking the user, we pass fixed values directly into the function.
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average


average = calculate_average(5, 3, 6)

print(average)