import pandas as pd

# Load the dataset
data = pd.read_excel("dataset/flood dataset.xlsx")

# Display the first 5 rows
print("\n===== First 5 Rows =====")
print(data.head())

# Display dataset information
print("\n===== Dataset Information =====")
print(data.info())

# Display statistical summary
print("\n===== Statistical Summary =====")
print(data.describe())

# Check for missing values
print("\n===== Missing Values =====")
print(data.isnull().sum())