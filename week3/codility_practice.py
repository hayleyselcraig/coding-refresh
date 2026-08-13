# Codility Practice 1 - Find the next number divisible by 5.
#
# Challenge:
# Write a function that takes a positive integer N.
# Starting AFTER N, find the first number that is divisible by 5.
# Return that number.
#
# Examples:
# N = 7  -> return 10
# N = 14 -> return 15
# N = 20 -> return 25


def solution(N):

    # Start at N + 1 because the question asks for a number
    # GREATER THAN N, so we don't want to check N itself.
    current_number = N + 1

    # Keep looping while current_number is NOT divisible by 5.
    #
    # % gives us the remainder after division.
    # A number divisible by 5 will have a remainder of 0.
    #
    # Example:
    # 10 % 5 = 0
    # 11 % 5 = 1
    while current_number % 5 != 0:

        # If the current number is not divisible by 5,
        # increase it by 1 and check again.
        current_number += 1

    # When the while loop stops, current_number must now
    # be divisible by 5, so return it as the answer.
    return current_number


# Test the function with different values.
print(solution(7))   # Expected: 10
print(solution(14))  # Expected: 15
print(solution(20))  # Expected: 25


# Codility Practice 2 - Count Positive Numbers
#
# Challenge:
# Write a function that takes a list of integers called A.
# Count how many numbers in the list are greater than 0.
# Return the final count.
#
# Example:
# A = [-3, 5, 0, 8, -2, 4]
# Answer = 3


def solution(A):

    # Start the count at 0 because we haven't
    # found any positive numbers yet.
    count = 0

    # Loop through every number in the list A.
    # 'number' represents one number from the list at a time.
    for number in A:

        # Check whether the current number is greater than 0.
        if number > 0:

            # If it is positive, add 1 to the count.
            count += 1

    # After ALL numbers have been checked,
    # return the final number of positive values.
    return count


# Test the function.
print(solution([-3, 5, 0, 8, -2, 4]))  # Expected: 3

# Test a list containing no positive numbers.
print(solution([-5, -2, -1]))  # Expected: 0


# PROBLEM-SOLVING PLAN:
#
# 1. What am I GIVEN?
#    -> A list of numbers called A.
#
# 2. What am I trying to FIND?
#    -> How many numbers are positive.
#
# 3. What do I need to CHECK?
#    -> Each number in A to see if it is greater than 0.
#
# 4. What needs to CHANGE?
#    -> Add 1 to count whenever a positive number is found.
#
# 5. What do I RETURN?
#    -> count

# Codility Practice 3 - Find the Largest Number
#
# Challenge:
# Write a function that takes a list of integers called A.
# Find the largest number in the list and return it.
#
# Example:
# A = [4, 12, 7, 3, 18, 6]
# Answer = 18


def solution(A):

    # Start by assuming the first number in the list
    # is the largest number.
    #
    # We use A[0] rather than 0 because the list
    # could contain only negative numbers.
    largest_number = A[0]

    # Loop through every number in the list A.
    # 'number' represents one number from the list at a time.
    for number in A:

        # Check if the current number is greater than
        # the largest number we have found so far.
        if number > largest_number:

            # If it is larger, update largest_number
            # so it now stores the current number.
            largest_number = number

    # Once every number has been checked,
    # return the largest number found.
    return largest_number


# Test with positive numbers.
print(solution([4, 12, 7, 3, 18, 6]))  # Expected: 18

# Test with negative numbers.
print(solution([-8, -2, -15, -4]))  # Expected: -2



# 1. What am I GIVEN? a list of numbers 
# 2. What am I trying to FIND? all the even numbers in the list
# 3. What will I need to go through/check? what numnbers can be divided by 2 and have a remainder of 0 
# 4. What needs to CHANGE as the program runs? even_numbers 
# 5. What should I RETURN? total
# There's one extra thing to think about this time: how could you tell Python whether a number is even?
# Have a go at all of that yourself, even if you're unsure about the even-number check. 👀


def solution(A):
    total = 0
    for number in A:
        if number % 2 == 0:
            total += number
    return total


# 1. What am I GIVEN?
# 2. What am I trying to FIND?
# 3. What will I need to go through/check?
# 4. What might need to CHANGE as the program runs?
# This one is trickier, so a guess is completely fine.
# 5. What should I RETURN?
# Then one extra question:
# 6. Looking at [1, 2, 3, 5, 6], how could you tell that 4 is missing?
# Write out your thinking first rather than code. 👀

# Codility Practice 5 - Find the Missing Number
#
# Challenge:
# A is a list of numbers that should count upwards from 1,
# but one number is missing.
# Find and return the missing number.
#
# Example:
# A = [1, 2, 3, 5, 6]
# Answer = 4


# PROBLEM-SOLVING PLAN:
#
# 1. What am I GIVEN?
#    -> A list of numbers called A.
#
# 2. What am I trying to FIND?
#    -> The missing number.
#
# 3. What do I need to CHECK?
#    -> Whether the current number exists in A.
#
# 4. What needs to CHANGE?
#    -> current_number increases by 1 each time
#       while the number exists in the list.
#
# 5. What should I RETURN?
#    -> current_number once a number is not found in A.


def solution(A):

    # Start at 1 because the number sequence should begin at 1.
    current_number = 1

    # Keep looping while current_number exists in the list.
    #
    # For example:
    # 1 in A -> True, so continue
    # 2 in A -> True, so continue
    # 3 in A -> True, so continue
    # 4 in A -> False, so stop the loop
    while current_number in A:

        # If the number exists, increase current_number by 1
        # and check the next number.
        current_number += 1

    # When the loop stops, current_number is the first number
    # that was not found in the list.
    # Therefore, it is our missing number.
    return current_number


# TESTS

print(solution([1, 2, 3, 5, 6]))  # Expected: 4

print(solution([1, 2, 4, 5]))     # Expected: 3

print(solution([2, 3, 4, 5]))     # Expected: 1

    
    