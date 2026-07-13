from fastapi import APIRouter, HTTPException
import pandas as pd

from app.schemas import CustomerData
from app.model_loader import model

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }


@router.post("/predict")
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