
from Calculator import Calculator

print("Welcome to Calculator")
num1 = input("Enter First Number : ")
num2 = input("Enter Second Number : ")

calculate = Calculator(num1, num2)

while True:
    # Get user input
    action = input(
        "Enter operation (+, -, *, /) or 'quit' to exit: ").lower()

    match action:
        case "+":
            print("Sum  is ", calculate.add())
        case "-":
            print("Substract  is ", calculate.subtract())
        case "*":
            print("Multiply  is ", calculate.multiply())
        case "/":
            print("Divide  is ", calculate.divide())
        case "quit":
            print("Exiting calculator. Goodbye!")
            break
        case _:
            print(
                "Invalid operation. Please enter a valid operation (add, subtract, multiply, divide) or 'quit'.")
            continue
