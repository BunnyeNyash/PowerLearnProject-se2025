# Weekly Coding Challenge; Data Analysis
## 📊 Python Data Analysis Challenge

🔹 **Challenge:** Perform basic data analysis on a CSV file and generate insights!

### 📌 Task Requirements:
1. **Download or create a CSV file** called `sales_data.csv` with the following columns:
      - `Date` (YYYY-MM-DD)
      - `Product`
      - `Quantity Sold`
      - `Revenue ($)`
2. **Write a Python script** to:
      - Load the CSV file using `pandas`.
      - Calculate the total revenue.
      - Find the best-selling product (based on `Quantity Sold`).
      - Identify the day with the highest sales.
      - Save the results to a new file called `sales_summary.txt`.
3. **Print the insights** in a user-friendly format.

### 🎯 Bonus Challenge:
  - Visualize sales trends using `matplotlib` or `seaborn`.

🔹 **Example CSV** (`sales_data.csv`):

| **Date**     | **Product** | **Quantity Sold** | **Revenue ($)** |
|--------------|-------------|-------------------|-----------------|
| 2025-03-01   | Laptop      | 5                 | 5000            |
| 2025-03-01   | Mouse       | 15                | 300             |
| 2025-03-02   | Laptop      | 3                 | 3000            |
| 2025-03-02   | Keyboard    | 8                 | 800             |


🔹 **Expected Output** (`sales_summary.txt`):
```
Total Revenue: $9,100  
Best-Selling Product: Mouse (15 units sold)  
Highest Sales Day: 2025-03-01
```
