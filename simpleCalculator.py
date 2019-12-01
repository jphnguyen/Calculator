def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Zero division error. Please enter a valid number.")
        return 0


print("Please select what function to use.")
print("(1) Addition")
print("(2) Subtraction")
print("(3) Multiplication")
print("(4) Division")


def calculate():

    while True:
        option = input("please enter your option here: ")
        num1 = input("Enter first number here: ")
        num2 = input("Enter second number here: ")

        if option == "1":
            print(addition(float(num1), float(num2)))
        elif option == "2":
            print(subtraction(float(num1), float(num2)))
        elif option == "3":
            print(multiplication(float(num1), float(num2)))
        elif option == "4":
            print(division(float(num1), float(num2)))
        else:
            print("Input error")

calculate()
