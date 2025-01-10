#function
def add (num1, num2):
    result = num1 + num2
    print("The result is: " + str(result))
def subtract (num1, num2):
    result = num1 - num2
    print("The result is: " + str(result))
def multiplication (num1, num2):
    result = num1 * num2
    print("The result is: " + str(result))
def division (num1, num2):
    result = num1 / num2
    print("The result is: " + str(result))


def simplecalc():

    print("Welcome Preschoolers to Simple Calcualator")
    while True:
        print("Please choose an operation: ")
        print("""
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division
        5.Quit""")
        operation = int(input("(1-5) :"))
        if operation == 1:
            add1 = int(input("Enter the first number you would like to add: "))
            add2 = int(input("Enter the second number you would like to add: "))
            add(add1,add2)
        if operation == 2:
            subtract1 = int(input("Enter the first number you would like to add: "))
            subtract2 = int(input("Enter the second number you would like to add: "))
            subtract(subtract1,subtract2)
        if operation == 3:
            multiplication1 = int(input("Enter the first number you would like to add: "))
            multiplication2 = int(input("Enter the second number you would like to add: "))
            multiplication(multiplication1,multiplication2)
        if operation == 4:
            division1 = int(input("Enter the first number you would like to add: "))
            division2 = int(input("Enter the second number you would like to add: "))
            division(division1,division2)
        if operation == 5:
            print("Thank you for using the simple calculator!")
            break
#main
simplecalc()
