import matplotlib.pyplot as plt

# Create a bar chart showing 5 different countries and their population.
country = ["China", "United States", "Russia", "Kenya", "Netherlands"]
population = [1416100000, 347276000, 143997000, 57532500, 18346800]

plt.bar(country, population, color="green")
plt.title("Total population by country (2025)")
plt.xlabel("Country")
plt.ylabel("Total Population")
plt.show()



# Create a pie chart showing how a student spends 24 hours of their day.
activities = ["sleeping", "eating", "reading", "gaming", "exercising", "school"]
hours = [8, 2, 6, 2, 1, 5]

plt.pie(hours, labels=activities, autopct="%1.1f%%", startangle=90)
plt.title("How a Student Spends their 24 hrs")
plt.axis('equal')
plt.show()



# Make a line chart that shows temperature changes during the day (morning, noon, evening, night).
period = ["morning", "noon", "evening", "night"]
temperature = [20, 30, 26, 22]

plt.plot(period, temperature)
plt.title("Temperature Changes Through the Day")
plt.xlabel("period")
plt.ylabel("Temperature in degrees")
plt.show()
