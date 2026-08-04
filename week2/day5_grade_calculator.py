## Create a Student Grade Calculator program which will ask the user for their name and three test scores. It will then calculate the average and return the average.

name = input("What is your name? ")
score1 = int(input("What is your first test score? "))
score2 = int(input("What is your second test score? "))
score3 = int(input("What is your third test score? "))

def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average

def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"
    
average = calculate_average(score1, score2, score3)
grade = get_grade(average)

print(f"Well done {name}!")
print(f"Average: {average}")
print(f"Grade: {grade}")