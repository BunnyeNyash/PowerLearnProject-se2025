my_list = []                                        # Create an empty list called my_list.

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# print(my_list)

my_list.insert(1, 15)                               # Insert the value 15 at the second position in the list
# print(my_list)

my_list.extend([50, 60, 70])                        # Extend my_list with another list: [50, 60, 70]
# print(my_list)

del my_list[-1]                                     # Remove the last element from my_list
# print(my_list)

my_list.sort()                                      # Sort my_list in ascending order
# print(my_list)

# Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(f"index of 30: {index_of_30}")
