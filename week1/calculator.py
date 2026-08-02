## This calculator program will welcome the user, ask for their name, ask for two numbers, ask what operation they want then display the answer.

def welcome():
    print("Welcome to the calculator program!")
welcome()
name = input("What is your name? ")
first_num = (int(input("What is your first number? ")))
second_num = (int(input("What is your second number? ")))
operation = input("What operation would you like to use? + - * / ")

if operation == "+":
    result = first_num + second_num
elif operation == "-":
    result = first_num - second_num
elif operation == "*":
    result = first_num * second_num
elif operation == "/":
    result = first_num / second_num
else:
    print("Error, invalid input. Please try again.")
print(f"Thanks {name} for using the calculator program!")
print(f"{first_num} {operation} {second_num} = {result}")


