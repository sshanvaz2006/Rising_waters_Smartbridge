import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Machine Learning Models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Accuracy
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_excel("dataset/flood dataset.xlsx")

# Features
X = data.drop("flood", axis=1)

# Target
y = data["flood"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("========== Decision Tree ==========")

dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)

dt_prediction = dt.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_prediction)

print("Decision Tree Accuracy:", dt_accuracy * 100)


print("\n========== Random Forest ==========")

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_prediction = rf.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_prediction)

print("Random Forest Accuracy:", rf_accuracy * 100)

print("\n========== KNN ==========")

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

knn_prediction = knn.predict(X_test)

knn_accuracy = accuracy_score(y_test, knn_prediction)

print("KNN Accuracy:", knn_accuracy * 100)

print("\n========== XGBoost ==========")

xgb = XGBClassifier(
    random_state=42,
    eval_metric="logloss"
)

xgb.fit(X_train, y_train)

xgb_prediction = xgb.predict(X_test)

xgb_accuracy = accuracy_score(y_test, xgb_prediction)

print("XGBoost Accuracy:", xgb_accuracy * 100)


print("\n========== Model Comparison ==========")

print(f"Decision Tree : {dt_accuracy*100:.2f}%")
print(f"Random Forest : {rf_accuracy*100:.2f}%")
print(f"KNN           : {knn_accuracy*100:.2f}%")
print(f"XGBoost       : {xgb_accuracy*100:.2f}%")