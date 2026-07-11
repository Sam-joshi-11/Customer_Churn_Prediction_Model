from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
)

MODEL_PATH = "artifacts/customer_churn_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

class CustomerData(BaseModel):
    CreditScore: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float

    Geography_Germany: int
    Geography_Spain: int

    Gender_Male: int

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }

@app.post("/predict")
def predict(data: CustomerData):
    try:

        input_df = pd.DataFrame([data.model_dump()])

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        return {
            "prediction": int(prediction),
            "churn_probability": round(float(probability), 4)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
