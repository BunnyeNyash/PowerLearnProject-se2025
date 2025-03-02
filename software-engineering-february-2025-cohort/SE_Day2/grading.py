# Control flow example for grading student marks
# This will ask the user for input and grade the student's performance
"""
The code first prompts the user to input the student's marks.
Based on the marks, the program uses if, elif, and else to determine the student's grade:
If the marks are greater than 70, it prints "Distinction 🏆".
If the marks are between 60 and 70 (inclusive), it prints "Credit 🎖️".
If the marks are between 50 and 59 (inclusive), it prints "Pass 👍".
If the marks are less than 50, it prints "Fail ❌".
"""

# Get the marks from the students
marks = int(input("Enter your marks: "))

# Grading based on the student's marks
if marks > 70:
    print("Distinction 🏆")
elif 60 <= marks <= 70:
    print("Credit 🎖️")
elif 50 <= marks <= 59:
    print("Pass 👍")
else:
    print("Fail ❌")
  
