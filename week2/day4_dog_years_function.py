## This function will take 2 arguments name and age. It will calculate the dog years by multiplying age by 7. It will then print to the user the dogs name and age in dog years.

def calculate_dog_years(name, age):
    dog_years = age * 7
    return f"{name}'s age in dog years is {dog_years}"
print(calculate_dog_years("Ellie", 5))
print(calculate_dog_years("Belle", 4))
print(calculate_dog_years("Tiana", 2))