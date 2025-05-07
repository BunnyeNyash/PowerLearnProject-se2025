import numpy as np

# create a list of numbers
numbers = [num for num in range(10, 51)]

array = np.array(numbers)
print(f"Array: {array}\n")

# find the maximum and the minimum value
print(f"The MAXIMUM number in the array is: {np.max(array)}")
print(f"The MINIMUM number in the array is: {np.min(array)}\n")

# multiply all elements by 3
multiply_by_3 = array * 3       # new array created
print(f"Array multiplied by 3: {multiply_by_3}")
