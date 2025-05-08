import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests


# Create a NumPy array of numbers from 1 to 10 and calculate the mean.
array = np.array(range(1, 11))
mean = np.mean(array)
print(f"Mean: {mean}")



# Load a small dataset into a pandas DataFrame and display summary statistics.
data = {
    "Name": ["Alice", "Bobby", "Mark", "Bunnye", "John", "Pinto"],
    "English": [90, 80, 95, 90, 98, 85],
    "Mathematics": [85, 90, 94, 90, 90, 90],
    "Geography": [80, 80, 75, 90, 100, 85]
}

df = pd.DataFrame(data)
print(f"\nSUMMARY STATISTICS:\n {df.describe()}")



# Fetch data from a public API using requests and print a key piece of information.
url = "https://dog.ceo/api/breeds/image/random"


response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    data = response.json()
    print(f"Image URL: {data['message']}")
else:
    print("Failed to retrieve the Image URL")



# Plot a simple line graph using matplotlib (e.g., a list of numbers).
x = [num for num in range(5, 20)]
y = [num ** 2 for num in range(5, 20)]

plt.plot(x, y)
plt.title("A List of Numbers")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()
