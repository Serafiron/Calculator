import math

#it now has functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Don't divide by zero!")
        return 0
    else:
        return a / b
    
def adventure():
    print("Welcome to The Math Adventure!")
    print("In this adventure, you will be asked questions, and you will answer them in numbers.")
    print("Occasionally, you will also be asked to do arithmetic operations.")
    print("The Adventure is still a work in progress!")
    print("In the waiting, why not check out the creator's Modern Poetry?")
    
while True:
    print("\nSelect operation: ")
    print("q. Quit")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Start a Math Adventure")

    choice = input("Enter choice: ")
    
    if choice == 'q':
        break
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)
        print("The result is: ", result)

    elif choice == "2":
        result = subtract(num1, num2)
        print("The result is: ", result)

    elif choice == "3":
        result = multiply(num1, num2)
        print("The result is: ", result)

    elif choice == "4":
        result = divide(num1, num2)
        print("The result is: ", result)

    elif choice == "5":
        print("Welcome to the start of Math Adventure!")
        print("In this text-based adventure, you will receive tasks and progress towards the ending using your skills with them.")
        adventure()

    else:
        print("Invalid input!")