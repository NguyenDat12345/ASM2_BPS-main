import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np

# Step 1: Load the sales data and prepare it
sale_df = pd.read_csv('sale_table.csv')

# Convert sale_date to datetime
sale_df['sale_date'] = pd.to_datetime(sale_df['sale_date'])

# Aggregate sales by date
daily_sales = sale_df.groupby('sale_date')['total_amount'].sum().reset_index()

# Step 2: Apply Linear Regression
# Prepare the data for Linear Regression
daily_sales['date_ordinal'] = daily_sales['sale_date'].map(pd.Timestamp.toordinal)
X = daily_sales[['date_ordinal']]
y = daily_sales['total_amount']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict using the test set
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Sales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.title('Actual vs Predicted Sales')
plt.legend()
plt.show()

# Step 3: Predict Future Sales
# Predict future sales (e.g., next 30 days)
future_dates = pd.date_range(daily_sales['sale_date'].max(), periods=30, freq='D')
future_dates_ordinal = future_dates.map(pd.Timestamp.toordinal).values.reshape(-1, 1)

# Predict future sales
future_sales_pred = model.predict(future_dates_ordinal)

# Plot future sales predictions
plt.figure(figsize=(10, 6))
plt.plot(future_dates, future_sales_pred, color='green', linewidth=2, label='Predicted Future Sales')
plt.xlabel('Date')
plt.ylabel('Predicted Sales Amount')
plt.title('Predicted Future Sales for Next 30 Days')
plt.legend()
plt.show()
