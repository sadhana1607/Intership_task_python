import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import joblib

# 1️⃣ Load Dataset
df = pd.read_csv("housing.csv")   # Make sure your file name is housing.csv
print("Dataset Loaded Successfully.\n")

# 2️⃣ Basic Preview
print("First 5 Rows:\n", df.head(), "\n")
print("Dataset Info:\n")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum(), "\n")

# 3️⃣ Handle Missing Values
df = df.fillna(df.mean(numeric_only=True))

# 4️⃣ Feature & Target Selection
# Update these columns according to your dataset
X = df.drop("price", axis=1)
y = df["price"]

# 5️⃣ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6️⃣ Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 7️⃣ Predictions
y_pred = model.predict(X_test)

# 8️⃣ Evaluate Model
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Model R² Score: {r2}")
print(f"Mean Squared Error: {mse}")

# 9️⃣ Save Model
joblib.dump(model, "house_price_model.pkl")
print("\nModel saved as: house_price_model.pkl")

# 🔟 Prediction Example
example_input = X_test.iloc[0].tolist()
example_prediction = model.predict([example_input])

print("\nExample Input:", example_input)
print("Predicted Price:", example_prediction[0])

print("\n✔ Task 2 Completed Successfully.")