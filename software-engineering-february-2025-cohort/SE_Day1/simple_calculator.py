# A Fun Calculator where we add, subtract, multiply, and divide two numbers

# Ask user for the numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Basic mathematical calculations
sum_result = num1 + num2                        # addition
difference_result = num1 - num2                 # subtraction
product_result = num1 * num2                    # multiplication
division_result = num1 / num2                   # division

# Printing out results to the user
print(f"Results of your two numbers:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Multiplication: {product_result}")
print(f"Division: {division_result}")
