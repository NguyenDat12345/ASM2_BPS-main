import pandas as pd

# Read the CSV files
website_access_df = pd.read_csv('Website_Access_Category_table.csv')
sale_df = pd.read_csv('sale_table.csv')
product_group_df = pd.read_csv('product_group_table.csv')
product_detail_df = pd.read_csv('product_detail_table.csv')
market_trend_df = pd.read_csv('market_trend_table.csv')
customer_df = pd.read_csv('customer_table.csv')

# Print column names to verify
print("Sale DataFrame columns:", sale_df.columns)
print("Market Trend DataFrame columns:", market_trend_df.columns)

# Check and handle missing data
website_access_df.dropna(inplace=True)

# Calculate the mean only for numeric columns in sale_df
numeric_columns = sale_df.select_dtypes(include='number').columns
sale_df[numeric_columns] = sale_df[numeric_columns].fillna(sale_df[numeric_columns].mean())

product_group_df.dropna(inplace=True)
product_detail_df.dropna(inplace=True)

# Check if 'trend_date' column exists before processing (renaming 'trend_date' to 'date' for clarity)
if 'trend_date' in market_trend_df.columns:
    market_trend_df['trend_date'] = pd.to_datetime(market_trend_df['trend_date'], errors='coerce')
    market_trend_df.dropna(subset=['trend_date'], inplace=True)
else:
    print("Column 'trend_date' not found in market_trend_df")

customer_df.dropna(inplace=True)

# Check if 'total_amount' column exists in sale_df and process it
if 'total_amount' in sale_df.columns:
    sale_df = sale_df[sale_df['total_amount'] > 0]
else:
    print("Column 'total_amount' not found in sale_df")

# Save the cleaned data
website_access_df.to_csv('cleaned_website_access.csv', index=False)
sale_df.to_csv('cleaned_sale.csv', index=False)
product_group_df.to_csv('cleaned_product_group.csv', index=False)
product_detail_df.to_csv('cleaned_product_detail.csv', index=False)
if 'trend_date' in market_trend_df.columns:
    market_trend_df.to_csv('cleaned_market_trend.csv', index=False)
customer_df.to_csv('cleaned_customer.csv', index=False)

print("Data cleaning and preprocessing completed successfully.")
