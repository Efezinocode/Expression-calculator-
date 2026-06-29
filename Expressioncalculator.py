print("Enter calculation (example: 10 + 3 or 10+3)")

while True:

    expression = input("Enter calculation: ")

    expression = expression.replace(" ", "")

    operator = None

    for op in ["+", "-", "*", "/"]:
        if op in expression:
            operator = op
            break

    if operator is None:
        print("Invalid operator")
        continue

    parts = expression.split(operator)

    if len(parts) != 2:
        print("Invalid format")
        continue

    try:
        num1 = int(parts[0])
        num2 = int(parts[1])

    except:
        print("Invalid numbers")
        continue

    if operator == "+":
        print("Answer:", num1 + num2)

    elif operator == "-":
        print("Answer:", num1 - num2)

    elif operator == "*":
        print("Answer:", num1 * num2)

    elif operator == "/":

        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Answer:", num1 / num2)