"""
Questions:

Create a dictionary called student with these key-value pairs: name = "Alex", age = 20, grade = "B".
Print the student's name.
Update the grade to "A".
Add a new key-value pair for course = "Computer Science".
Loop through the dictionary, printing both keys and values.

"""

student = {
    "name" : "Alex",
    "age" : 20,
    "grade" : "B"
    }
print(type(student))                                    # 1

print(student["name"])                                  # 2

student["grade"] = "A"                                  # 3
print(student)

student.update({"course" : "Computer Science"})         # 4
print(student)

for key, value in student.items():                      # 5
    print(f"{key} : {value}")

