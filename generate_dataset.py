import pandas as pd
import numpy as np

# Generate random data
np.random.seed(42)
data = {
    "Pregnancies": np.random.randint(0, 10, 100),
    "Glucose": np.random.randint(70, 200, 100),
    "BloodPressure": np.random.randint(50, 122, 100),
    "BMI": np.round(np.random.uniform(18.0, 45.0, 100), 1),
    "Age": np.random.randint(21, 70, 100),
    "Outcome": np.random.randint(0, 2, 100)
}

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("data/sample_diabetes_data.csv", index=False)
print("Sample dataset saved to 'data/sample_diabetes_data.csv'")
