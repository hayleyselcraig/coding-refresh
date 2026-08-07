# Warm-up: Create a function that calculates a person's age in 5 years.

name = input("What is your name? ")
age = int(input("What is your age? "))

def age_in_five_years(age):
    new_age = age + 5
    return new_age

new_age = age_in_five_years(age)
print(f"Hi {name}!, your current age is {age}.")
print(f"Your age in five years will be {new_age}.")