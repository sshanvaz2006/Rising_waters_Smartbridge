# Rising Waters SmartBridge

# System Architecture

## Overview

The Rising Waters SmartBridge project is a Machine Learning based flood prediction web application developed using Flask. The system predicts flood risk based on environmental parameters entered by the user.

The architecture consists of two phases:

- Model Training Phase
- Prediction Phase

---

## Architecture Components

### 1. Flood Dataset

The historical flood dataset is stored in Excel format (`flood_dataset.xlsx`). This dataset is used to train the Machine Learning model.

### 2. Data Preprocessing

Before training, the dataset is cleaned and preprocessed using Pandas and NumPy. Missing values are handled and the data is prepared for model training.

### 3. Model Training

The Machine Learning model is trained using Scikit-learn. Once training is complete, the trained model is saved as:

- flood_prediction_model.pkl

### 4. Flask Web Application

The Flask application provides the graphical user interface for users to interact with the prediction system.

### 5. Input Form

Users enter flood-related environmental parameters through the web interface.

### 6. Prediction Engine

The Flask application loads the saved Machine Learning model and generates predictions based on user inputs.

### 7. Result Display

The predicted flood risk is displayed back to the user through the web application.

---

# Architecture Diagram

*(Insert architecture_diagram.png here when creating the final report.)*

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- JavaScript
- Pickle