import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a folder for charts
if not os.path.exists("output_charts"):
    os.makedirs("output_charts")

# Load CSV file
df = pd.read_csv("data.csv")  # Make sure your file name is data.csv
print("CSV Loaded Successfully!\n")

# Show first 5 rows
print("First 5 Rows:")
print(df.head(), "\n")

# Dataset info
print("Dataset Info:")
print(df.info(), "\n")

# Statistical summary
print("Statistical Summary:")
print(df.describe(), "\n")

# Missing values check
print("Missing Values:")
print(df.isnull().sum(), "\n")

# Get numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Bar chart (only if numeric columns exist)
if len(numeric_cols) > 0:
    plt.figure(figsize=(10,4))
    df[numeric_cols[0]].plot(kind='bar')
    plt.title(f"Bar Chart of {numeric_cols[0]}")
    plt.xlabel("Index")
    plt.ylabel(numeric_cols[0])
    plt.savefig("output_charts/bar_chart.png")
    plt.close()

# Scatter plot (if at least 2 numeric columns)
if len(numeric_cols) >= 2:
    plt.figure(figsize=(6,4))
    plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
    plt.title("Scatter Plot")
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.savefig("output_charts/scatter_plot.png")
    plt.close()

# Correlation heatmap
if len(numeric_cols) >= 2:
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("output_charts/heatmap.png")
    plt.close()

print("\n✔ Analysis Completed Successfully!")
print("✔ Charts saved in 'output_charts' folder.")