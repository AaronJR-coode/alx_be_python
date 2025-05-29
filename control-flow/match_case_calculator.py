num1 = int(input("Enter The First number: "))
num2 = int(input("Enter The Second number: "))
operation = input("Choose the operation (+, -, *, /): ")


match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        result = num1/num2
    case _:
            print("Invalid operation! Please choose from +, -, *, /")


print(f"The result is: {result}")
