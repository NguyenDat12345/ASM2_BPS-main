import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the sales data
sale_df = pd.read_csv('sale_table.csv')

# Convert sale_date to datetime
sale_df['sale_date'] = pd.to_datetime(sale_df['sale_date'])

# Aggregate sales by date
daily_sales = sale_df.groupby('sale_date')['total_amount'].sum().reset_index()

# Prepare data for regression
daily_sales['date_ordinal'] = daily_sales['sale_date'].map(pd.Timestamp.toordinal)
X = daily_sales[['date_ordinal']]
y = daily_sales['total_amount']

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict future sales (next 30 days)
future_dates = pd.date_range(daily_sales['sale_date'].max(), periods=30, freq='D')
future_dates_ordinal = future_dates.map(pd.Timestamp.toordinal).values.reshape(-1, 1)
future_sales_pred = model.predict(future_dates_ordinal)

# Plotting the Line Chart
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['sale_date'], daily_sales['total_amount'], color='blue', label='Historical Sales')
plt.plot(future_dates, future_sales_pred, color='green', linestyle='--', label='Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.title('Machine Learning: Historical and Predicted Sales Line Chart')
plt.legend()
plt.show()
