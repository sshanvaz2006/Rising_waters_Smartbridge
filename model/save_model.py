import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_excel("dataset/flood dataset.xlsx")

X = data.drop("flood", axis=1)
y = data["flood"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "model/flood_prediction_model.pkl")

# Save the scaler
joblib.dump(scaler, "model/scaler.pkl")

print("Model Saved Successfully!")