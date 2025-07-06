import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

try:
    # Load the dataset
    data = pd.read_csv('house_prices.csv')
except FileNotFoundError:
    print("Error: 'house_prices.csv' not found. Please ensure the file is in the same directory as this script.")
    exit(1)

# Basic data exploration
print("Dataset Info:")
print(data.info())
print("\nFirst few rows of the dataset:")
print(data.head())

# Handle missing values (if any)
data = data.dropna()

# Define features (X) and target (y)
X = data[['square_feet', 'bedrooms', 'bathrooms']]
y = data['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nModel Performance:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Print model coefficients for JavaScript
print("\nModel Coefficients for JavaScript:")
print(f"coef_square_feet = {model.coef_[0]:.2f}")
print(f"coef_bedrooms = {model.coef_[1]:.2f}")
print(f"coef_bathrooms = {model.coef_[2]:.2f}")
print(f"intercept = {model.intercept_:.2f}")

# Plot actual vs predicted prices
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Prices')
plt.savefig('price_prediction_plot.png')
plt.show()