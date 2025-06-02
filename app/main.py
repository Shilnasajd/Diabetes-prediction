from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("app/model.pkl")

# Create app
app = FastAPI()

# Define input schema
class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    BMI: float
    Age: int

# API routes
@app.get("/health")
def health_check():
    return {"status": "API is running"}

@app.post("/predict")
def predict(data: PatientData):
    features = [[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.BMI,
        data.Age
    ]]
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}

@app.get("/features")
def feature_importance():
    importances = model.feature_importances_
    names = ["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]
    return dict(zip(names, importances.tolist()))
