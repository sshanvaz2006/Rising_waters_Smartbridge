import os
import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
MODEL_PATH = os.path.join(BASE_DIR, "model", "flood_prediction_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")

print("BASE_DIR =", BASE_DIR)
print("MODEL_PATH =", MODEL_PATH)
print("SCALER_PATH =", SCALER_PATH)

print("Model exists:", os.path.exists(MODEL_PATH))
print("Scaler exists:", os.path.exists(SCALER_PATH))

# Load model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    temp = float(request.form["Temp"])
    humidity = float(request.form["Humidity"])
    cloud = float(request.form["Cloud Cover"])
    annual = float(request.form["ANNUAL"])
    janfeb = float(request.form["Jan-Feb"])
    marmay = float(request.form["Mar-May"])
    junsep = float(request.form["Jun-Sep"])
    octdec = float(request.form["Oct-Dec"])
    avgjune = float(request.form["avgjune"])
    sub = float(request.form["sub"])

    features = pd.DataFrame(
        [[
            temp,
            humidity,
            cloud,
            annual,
            janfeb,
            marmay,
            junsep,
            octdec,
            avgjune,
            sub
        ]],
        columns=[
            "Temp",
            "Humidity",
            "Cloud Cover",
            "ANNUAL",
            "Jan-Feb",
            "Mar-May",
            "Jun-Sep",
            "Oct-Dec",
            "avgjune",
            "sub"
        ]
    )

    # Scale features
    features = scaler.transform(features)

    # Predict
    prediction = model.predict(features)[0]

    # Display message
    if prediction == 1:
        result = "⚠️ Flood Likely - Take Necessary Precautions"
    else:
        result = "✅ No Flood Risk Detected"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)