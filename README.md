# Diabetes Prediction with REST API

## Overview
Predict diabetes using a patient dataset and expose predictions via FastAPI endpoints.

## Dataset
Generated synthetic dataset with columns:
- Pregnancies
- Glucose
- Blood Pressure
- BMI
- Age
- Outcome

## Steps
1. Data exploration & cleaning
2. Model training & evaluation
3. REST API creation

## Endpoints

- `swagger` - http://127.0.0.1:8000/docs

- `/health` - API health check
- `/predict` - POST patient data and get prediction
- `/features` - Get feature importance from model

## How to Run
```bash
python generate_dataset.py
uvicorn app.main:app --reload
