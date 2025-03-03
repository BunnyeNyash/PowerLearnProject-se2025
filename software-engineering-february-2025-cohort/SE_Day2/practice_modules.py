"""
Questions:

Use the math module to calculate and print the square root of 81.
Use the random module to generate and print a random number between 1 and 10.
Use the datetime module to print today’s date.
Write your own small module (in a second file called my_module.py) that contains a function to say "Welcome to Python Practice!" and then import and call that function in practice_modules.py.

"""

import math
import random
import datetime
import my_module

num = 81
print(math.sqrt(num))                                   # 1




numbers = random.randint(1, 10)
print(numbers)                                          # 2




print(datetime.date.today())                            # 3




print(my_module.say(message="Hello Weddy!"))            # 4
