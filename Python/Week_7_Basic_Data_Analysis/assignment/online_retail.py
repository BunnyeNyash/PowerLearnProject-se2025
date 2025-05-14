# Analyzing Data with Pandas and Visualizing Results with Matplotlib
# Dataset: Online Retail from UCI ML Repo
# Source: https://archive.ics.uci.edu/dataset/352/online+retail
# Note: Original Excel file converted to CSV
# Objective
# To load and analyze the Online Retail dataset using pandas and create four visualizations (line chart, bar chart, histogram, scatter plot) in a single window using matplotlib to gain insights into sales patterns.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta

# Set seaborn theme for better plot aesthetics
sns.set_theme(style="whitegrid", font_scale=1.1)

# Load and Explore the Dataset
# Loading the Data
try:
    # Load the CSV file
    df = pd.read_csv('Online_Retail.csv', encoding='latin1')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Online_Retail.csv not found. Please ensure the file is in the working directory.")
    raise
except Exception as e:
    print(f"Error loading file: {e}")
    raise

# Display first few rows with relevant columns
print("\nFirst 5 rows of the dataset (selected columns):")
print(df[['InvoiceNo', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'Country']].head().to_string(index=False))

# Check data types and missing values
print("\nDataset Info:")
print(df.dtypes.to_string())
print("\nMissing Values:")
print(df.isnull().sum().to_string())

# Data Cleaning
# Convert InvoiceDate to datetime (format: MM/DD/YYYY H:MM, e.g., '12/1/2010 8:26')
try:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')
    print("Converted string InvoiceDate to datetime (format: MM/DD/YYYY H:MM).")
except Exception as e:
    print(f"Error converting InvoiceDate: {e}")
    raise

# Remove rows with negative Quantity (cancellations) to focus on sales
df = df[df['Quantity'] > 0]

# Handle missing CustomerID by dropping rows (not critical for this analysis)
df = df.dropna(subset=['CustomerID'])

# Create TotalPrice column for revenue analysis
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Verify cleaning
print(f"\nAfter cleaning, dataset shape: {df.shape}")
print("\nMissing Values after cleaning:")
print(df.isnull().sum().to_string())

# Basic Data Analysis
# Summary statistics for numerical columns
print("\nSummary Statistics for Numerical Columns:")
stats = df[['Quantity', 'UnitPrice', 'TotalPrice']].describe().round(2)
print(stats.to_string())

# Group by Country and compute total TotalPrice
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)
print("\nTotal Sales by Country (Top 5, in £):")
print(country_sales.head().round(2).to_string())

# Group by Description to find top products by total sales
product_sales = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False)
print("\nTop 5 Products by Total Sales (in £):")
print(product_sales.head().round(2).to_string())

# Data Visualization
# Create a single figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(17, 30))
fig.suptitle('Online Retail Data Analysis Visualizations', fontsize=16, fontweight='bold', y=0.98)

# 1. Line Chart: Total Sales Over Time (Monthly)
monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['TotalPrice'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
axes[0, 0].plot(monthly_sales.index, monthly_sales.values, marker='o', color='blue', linewidth=2)
axes[0, 0].set_title('Total Sales Over Time (Monthly)', fontsize=12, pad=8)
axes[0, 0].set_xlabel('Date', fontsize=10)
axes[0, 0].set_ylabel('Total Sales (£)', fontsize=10)
axes[0, 0].tick_params(axis='x', rotation=45, labelsize=9)
axes[0, 0].tick_params(axis='y', labelsize=9)
axes[0, 0].grid(True, linestyle='--', alpha=0.7)
axes[0, 0].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# 2. Bar Chart: Total Sales by Top 5 Countries
top_countries = country_sales.head(5)
sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index, ax=axes[0, 1], palette='Blues_r', legend=False)
axes[0, 1].set_title('Total Sales by Top 5 Countries', fontsize=12, pad=8)
axes[0, 1].set_xlabel('Total Sales (£)', fontsize=10)
axes[0, 1].set_ylabel('Country', fontsize=10)
axes[0, 1].tick_params(axis='x', labelsize=9, rotation=60)
axes[0, 1].tick_params(axis='y', labelsize=9)
axes[0, 1].get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# 3. Histogram: Distribution of TotalPrice
axes[1, 0].hist(df['TotalPrice'], bins=50, range=(0, df['TotalPrice'].quantile(0.99)), color='skyblue', edgecolor='black')
axes[1, 0].set_title('Distribution of Total Price per Transaction', fontsize=12, pad=8)
axes[1, 0].set_xlabel('Total Price (£)', fontsize=10)
axes[1, 0].set_ylabel('Frequency', fontsize=10)
axes[1, 0].tick_params(axis='x', labelsize=9)
axes[1, 0].tick_params(axis='y', labelsize=9)
axes[1, 0].get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# 4. Scatter Plot: Quantity vs. UnitPrice
sns.scatterplot(x='UnitPrice', y='Quantity', hue='Country', size='TotalPrice', data=df, alpha=0.5, ax=axes[1, 1])
axes[1, 1].set_title('Quantity vs. Unit Price by Country', fontsize=12, pad=8)
axes[1, 1].set_xlabel('Unit Price (£)', fontsize=10)
axes[1, 1].set_ylabel('Quantity', fontsize=10)
axes[1, 1].tick_params(axis='x', labelsize=9)
axes[1, 1].tick_params(axis='y', labelsize=9)
axes[1, 1].legend(bbox_to_anchor=(1.05, 1.1), loc='upper left', fontsize=8, title_fontsize=9, frameon=True, borderpad=0.5)

# Adjusting layout to prevent overlap
plt.tight_layout(rect=[0.02, 0, 0.95, 0.95], h_pad=6.0, w_pad=2.0)
plt.subplots_adjust(hspace=0.6)
plt.show()



# Findings and Insights
# I analyzed the Online Retail dataset (541,909 rows) to uncover sales trends. After cleaning, dropping 135,080 rows missing `CustomerID`, 1,454 with no `Description` and removing cancellations, I focused on actual sales. The `InvoiceDate` format (`12/1/2010 8:26`) was tricky, but I fixed it with `%m/%d/%Y %H:%M`. I created `TotalPrice` (`Quantity` × `UnitPrice`) to track revenue.

# Most orders are small (median `TotalPrice`: £11.80, `Quantity`: 6), but some hit £168,469.60. The UK dominates with £7,308,391.55, far ahead of the Netherlands (£285,446.34). Top products are “PAPER CRAFT , LITTLE BIRDIE” (£168,469.60), “REGENCY CAKESTAND 3 TIER” (£142,592.95), and “WHITE HANGING HEART T-LIGHT HOLDER” (£100,448.15). I was surprised a paper craft led.

# My 2x2 plots showed:
# - **Line chart**: Sales peak in November/December, the holiday season.
# - **Bar chart**: UK’s sales exceeds others, showing its core market.
# - **Histogram**: Most transactions are under £50, with a few big ones.
# - **Scatter plot**: Higher `UnitPrice` means lower `Quantity`, especially in the UK—likely decor items.

# Conclusion
# The UK drives sales (£7.3M), with “PAPER CRAFT , LITTLE BIRDIE” topping at £168,469.60. Holiday peaks suggest marketing focus then. Most orders are small, but big spenders exist. Plots highlighted patterns like the UK’s dominance.

print("\nAnalysis complete.")
