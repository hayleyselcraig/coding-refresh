# Profile Builder
# Day 2 of my Coding Refresh
# Practising variables, user input, f-strings and if statements.

## Ask the user for their Name, Age, Favourite colour, Favourite animal and Dream job. Store them in variables.
name = input("Welcome! What is your name? ").title()
age = input("What age are you? ")
fav_colour = input("What is your favourite colour? ")
fav_animal = input("What is your favourite animal? ")
dream_job = input("Lastly, What is your dream job? ")

print("----------------------------")
print("USER PROFILE")
print("Welcome to your personalised profile.")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favourite Colour: {fav_colour}")
print(f"Favourite Animal: {fav_animal}")
print(f"Dream Job: {dream_job}")

coding_preference = input("Do you enjoy coding? Yes or No ").title()
if coding_preference == "Yes":
    print(f"Thats brilliant! {name} Keep practicing and you will make a great {dream_job}!")
elif coding_preference == "No":
    print(f"Thats okay {name}, confidence comes with practice!")
else:
    print("Invalid input, can you answer with Yes or No.")