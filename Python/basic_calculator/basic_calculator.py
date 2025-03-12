# basic calculator program to do basic arithmetic calculations

# rules
print("""
    You will be required to input two numbers
      number 1
      number 2

    You will then have to input the mathematical operation you want done to your two numbers
      * represents Multiplicaation
      - represents subtraction
      + represents addition
      / represents division

    click "ENTER" after each input
""")

# ask user for input
    # 2 numbers
    # mathematical operation

while True:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    mathematical_operation = input("Enter your mathematical operation. (+, -, *, or /) :  ")

    if mathematical_operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result} ")
        break
    elif mathematical_operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result} ")
        break
    elif mathematical_operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result} ")
        break
    elif mathematical_operation == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {result} ")
        break
    else:
        print("Only *, +, -, and / operators are allowed. Please try again\n")
        
