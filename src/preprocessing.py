import pandas as pd

# Load dataset
data = pd.read_excel("dataset/flood dataset.xlsx")

print("===== First 5 Rows =====")
print(data.head())

print("\nDataset Shape:", data.shape)
# Separate Features and Target

X = data.drop("flood", axis=1)

y = data["flood"]

print("\nFeatures (X)")
print(X.head())

print("\nTarget (y)")
print(y.head())

from sklearn.model_selection import train_test_split

# Split dataset into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

from sklearn.preprocessing import StandardScaler

# Create scaler
scaler = StandardScaler()

# Fit and transform training data
X_train = scaler.fit_transform(X_train)

# Transform testing data
X_test = scaler.transform(X_test)

print("\nFeature Scaling Completed Successfully!")