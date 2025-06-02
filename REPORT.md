# Diabetes Prediction Project Report

## 1. Project Objective

The goal of this project is to analyze patient health data to:
- Predict the likelihood of a patient developing diabetes.
- Identify key factors that contribute most to the risk of diabetes.

## 2. Dataset Overview

The dataset consists of patient records with the following features:
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **BMI**: Body Mass Index (weight in kg/(height in m)^2)
- **Age**: Patient age in years
- **Outcome**: Diabetes status (0 = no diabetes, 1 = diabetes)

## 3. Data Exploration & Preprocessing

- Loaded and inspected data for missing values and anomalies.
- Imputed missing numerical values using the median.
- Removed unrealistic values such as zero or negative blood pressure.
- Scaled numerical features using StandardScaler to normalize input for models.

## 4. Exploratory Data Analysis (EDA)

- Visualized feature distributions and found higher glucose and BMI values among diabetic patients.
- Observed positive correlation between glucose level and diabetes outcome.
- The dataset was imbalanced, but sufficient for model training.

## 5. Model Building & Evaluation

- Split data into training and testing sets (80% train, 20% test).
- Trained three classification models: Logistic Regression, Decision Tree, and Random Forest.
- Evaluated models using Accuracy, Precision, Recall, and F1-score.
- Random Forest yielded the best overall performance with balanced precision and recall.

## 6. Feature Importance

- Random Forest model identified **Glucose** as the most important predictor of diabetes.
- Other influential features included **BMI**, **Age**, and **Pregnancies**.
- Blood Pressure had comparatively lower influence on predictions.

## 7. API Endpoints

Developed REST API endpoints using FastAPI to:
- `/predict`: Accept patient data and return diabetes prediction.
- `/features`: Return feature importance scores from the trained model.
- `/health`: Basic API health check.

## 8. Conclusion & Future Work

- The model effectively predicts diabetes risk using routine health metrics.
- Glucose levels and BMI are key indicators for diabetes risk.
- Future improvements may include handling class imbalance with advanced techniques, tuning hyperparameters, and expanding the dataset.
- Integration with a front-end or deployment in a clinical setting could enhance practical utility.

---

*Thank you for reviewing this project!*

