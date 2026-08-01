def calculator(a, b, operation = str(input())):
    if operation == "+":
        print(f"Addition = {a+b}")
    elif operation == "-":
        print(f"subtraction = {a-b}")
    elif operation == "*":
        print(f"Multiplication = {a*b}")
    elif operation == "/":
        print(f"Division = {a/b}")
    else:
        print(f"Provided argument does not meet calculator's requirement")

calculator(10, 5)