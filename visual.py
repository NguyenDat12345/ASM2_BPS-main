import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
customer_df = pd.read_csv('customer_table.csv')
market_trend_df = pd.read_csv('market_trend_table.csv')
product_detail_df = pd.read_csv('product_detail_table.csv')
product_group_df = pd.read_csv('product_group_table.csv')
sale_df = pd.read_csv('sale_table.csv')
website_access_df = pd.read_csv('Website_Access_Category_table.csv')

# Print column names to diagnose the issue
print("Website Access DataFrame columns:", website_access_df.columns)

# 1. Line Chart: Sales trend over time

# Convert sale_date column to datetime
sale_df['sale_date'] = pd.to_datetime(sale_df['sale_date'])

# Calculate total sales amount per day
daily_sales = sale_df.groupby('sale_date')['total_amount'].sum()

# Plot the Line Chart
plt.figure(figsize=(10, 6))
daily_sales.plot(kind='line', color='blue')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Pie Chart: Website access distribution by category

# Identify the correct column name
if 'access_category' in website_access_df.columns:
    access_counts = website_access_df['access_category'].value_counts()
else:
    # If the column name is different, adjust here
    print("Available columns:", website_access_df.columns)
    access_counts = website_access_df[website_access_df.columns[0]].value_counts()

# Plot the Pie Chart
plt.figure(figsize=(8, 8))
access_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightblue', 'lightgreen'])
plt.title('Website Access Distribution by Category')
plt.ylabel('')  # Hide the y-label
plt.tight_layout()
plt.show()

# 3. Donut Chart: Distribution of product categories

# Count total products by category
product_category_counts = product_detail_df['product_category'].value_counts()

# Plot the Donut Chart
plt.figure(figsize=(8, 8))
plt.pie(product_category_counts, labels=product_category_counts.index, autopct='%1.1f%%', colors=['gold', 'lightblue', 'lightgreen'])
# Create a white circle at the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, color='white', fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Product Distribution by Category')
plt.ylabel('')  # Hide the y-label
plt.tight_layout()
plt.show()
