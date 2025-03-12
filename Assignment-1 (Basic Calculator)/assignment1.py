number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
operator = input("Enter the operator: ")

if operator == "+":
    print("The result is: ", int(number1) + int(number2))
elif operator == "-":
    print("The result is: ", int(number1) - int(number2))
elif operator == "*":
    print("The result is: ", int(number1) * int(number2))
elif operator == "/":
    print("The result is: ", int(number1) / int(number2))
else:
    print("Invalid operator")