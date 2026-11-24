# Q42. Perform calculator operations using match case (Python 3.10+).
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
match operator:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")
