import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the sales data
sale_df = pd.read_csv('sale_table.csv')

# Convert sale_date to datetime
sale_df['sale_date'] = pd.to_datetime(sale_df['sale_date'])

# Prepare data for regression
daily_sales = sale_df.groupby('sale_date')['total_amount'].sum().reset_index()
daily_sales['date_ordinal'] = daily_sales['sale_date'].map(pd.Timestamp.toordinal)

X = daily_sales[['date_ordinal']]
y = daily_sales['total_amount']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting with the model
y_pred = model.predict(X_test)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Sales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.title('Linear Regression: Actual vs Predicted Sales')
plt.legend()
plt.show()
