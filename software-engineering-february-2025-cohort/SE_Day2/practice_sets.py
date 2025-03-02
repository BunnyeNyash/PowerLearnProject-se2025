"""
Questions:

Create a set called fruits with these items: "apple", "banana", "cherry", "apple".
Print the set (observe duplicates are removed).
Add "orange" to the set.
Remove "banana" from the set.
Check if "cherry" is in the set and print a message if it is.

"""

fruits = {"apple", "banana", "cherry", "apple"}                 # 1
print(type(fruits))

print(fruits)                                                   # 2

fruits.add("orange")                                            # 3
print(fruits)

fruits.remove("banana")                                         # 4
print(fruits)

if "cherry" in fruits:                                          # 5
    print("cherry in fruits")
  
