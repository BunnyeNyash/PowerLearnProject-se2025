"""
Questions:

Write a function greet_user that takes a name and prints "Hello, [name]!"
Write a function calculate_area that takes length and width and returns the area.
Write a function is_even that takes a number and returns True if it’s even, False if not.
Call each function at least once with sample inputs.

"""

def greet_user(name):                               # 1
    print(f"Hello, {name}!")

greet_user("Weddy")





def calculate_area(width, height):                  # 2
    area = width * height
    return area

print(calculate_area(20, 100))




num = int(input("Enter a number: "))                # 3

def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    
print(is_even(num))
