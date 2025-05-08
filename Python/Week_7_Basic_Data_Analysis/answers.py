import pandas as pd
import matplotlib.pyplot as plt

# Load csv file
data = pd.read_csv("sales_data.csv")

# create a DataFrame
df = pd.DataFrame(data)
print(df)

# Calculate total revenue
total_revenue = df["Revenue ($)"].sum()


# Best-selling product
best_selling_product = df.groupby("Product")["Quantity Sold"].sum().idxmax()
best_selling_value = df.groupby("Product")["Quantity Sold"].sum().max()




# Day with highest sales
highest_sales_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()

# results in a new file
with open("sales_summary.txt", "w") as file:
    file.write(f"Total Revenue: {total_revenue}\n")
    file.write(f"Best-Selling Product: {best_selling_product} ({best_selling_value} units sold)\n")
    file.write(f"Highest Sales Day: {highest_sales_day}")


# insights
print(f"\nTotal Revenue: {total_revenue}\n")
print(f"Best-Selling Product: {best_selling_product} ({best_selling_value} units sold)\n")
print(f"Highest Sales Day: {highest_sales_day}")



# Visualization using matplotlib

# total revenue over time
revenue_by_date = df.groupby("Date")["Revenue ($)"].sum()
revenue_by_date.plot(kind="line", marker="o", color="green")
plt.title("Total Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=70)
plt.show()


# quantity sold per product
quantity_by_product = df.groupby("Product")["Quantity Sold"].sum()
quantity_by_product.plot(kind="bar", color="green")
plt.title("Quantity Sold per Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=70)
plt.show()
