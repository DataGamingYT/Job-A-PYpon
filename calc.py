operation = 0

print("Please select one of the following operations to use.")
print("-----------------------------------------------------")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")

operation = input("Choose a, b, c, or d : ")
operationLower = operation.lower()

if operationLower == "a" or operationLower == "b" or operationLower == "c" or operationLower == "d":
    num1 = int(input("Please input a number to use : "))
    num2 = int(input("Please input another number to use : "))

    if operation == "a":
        print(num1 + num2)
    elif operation == "b":
        print(num1 - num2)
    elif operation == "c":
        print(num1 * num2)
    elif operation == "d":
        print(num1 / num2)
else:
    print("Not a valid input. Try again.")
