from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Load model and scaler
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load("app/model.pkl")
scaler = joblib.load("app/scaler.pkl")

app = FastAPI()

class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    BMI: float
    Age: int

@app.get("/health")
def health_check():
    return {"status": "API is running"}

@app.post("/predict")
def predict(data: PatientData):
    # 1) Build a 2D list from the incoming JSON
    features = [[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.BMI,
        data.Age
    ]]
    # 2) Scale exactly the same way you did at training-time
    features_scaled = scaler.transform(features)

    # 3) Predict on scaled features
    prediction = model.predict(features_scaled)
    return {"prediction": int(prediction[0])}

@app.get("/features")
def feature_importance():
    importances = model.feature_importances_
    names = ["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]
    return dict(zip(names, importances.tolist()))
