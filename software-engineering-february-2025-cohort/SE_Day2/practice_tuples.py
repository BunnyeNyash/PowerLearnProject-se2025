"""
Questions:

Create a tuple called dimensions with values 100 and 200.
Print the second value.
Try changing the first value (observe the error and comment it out).
Loop through the tuple and print each value.

"""

dimensions = (100, 200)                 # 1
print(type(dimensions))

print(dimensions[1])                    # 2

# dimensions[0] = 400                   # 3
# print(dimensions)

for dimension in dimensions:            # 4
    print(dimension)
