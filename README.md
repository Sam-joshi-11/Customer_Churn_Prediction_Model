# Customer Churn Prediction API

A production-ready Machine Learning API for predicting customer churn using **XGBoost**, **FastAPI**, **Docker**, and **MLflow**. The application is containerized with Docker and deployed on **Render**, providing a scalable REST API for real-time predictions.

---

## Project Overview

Customer churn prediction helps businesses identify customers who are likely to leave. This project trains an XGBoost classification model and exposes it through a RESTful FastAPI service.

The project follows a modular architecture with separate components for model loading, request validation, API routing, and training.

---

## Features

-  Customer Churn Prediction using XGBoost
-  FastAPI REST API
-  Modular Project Structure
-  MLflow Experiment Tracking
-  Docker Containerization
-  Render Cloud Deployment
-  Input Validation using Pydantic
-  Interactive Swagger Documentation
-  Production-ready Project Structure

---

# Project Structure

```text
Customer_Churn_Prediction_Model
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── model_loader.py
│   └── __init__.py
│
├── artifacts/
│   └── customer_churn_model.pkl
│
├── config/
│   └── config.py
│
├── data/
│   └── Churn_Modelling.csv
│
├── train.py
├── Dockerfile
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore
```

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| ML Model | XGBoost |
| API | FastAPI |
| Experiment Tracking | MLflow |
| Validation | Pydantic |
| Data Processing | Pandas |
| Containerization | Docker |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Sam-joshi-11/Customer_Churn_Prediction_Model.git

cd Customer_Churn_Prediction_Model
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the API

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Run with Docker

Build

```bash
docker build -t customer-churn-api .
```

Run

```bash
docker run -p 8000:8000 customer-churn-api
```

---

# Live Deployment

**Render URL**

```
https://customer-churn-prediction-model-9em9.onrender.com
```

Swagger Docs

```
https://customer-churn-prediction-model-9em9.onrender.com/docs
```

---

# API Endpoint

## POST `/predict`

### Sample Request

```json
{
  "CreditScore": 300,
  "Age": 18,
  "Tenure": 10,
  "Balance": 0,
  "NumOfProducts": 1,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 0,
  "Geography_Germany": 1,
  "Geography_Spain": 1,
  "Gender_Male": 1
}
```

---

### Sample Response

```json
{
  "prediction": 0,
  "churn_probability": 0.0682
}
```


# Future Improvements

- Health Check Endpoint
- API Versioning
- Structured Logging
- MLflow Model Registry Integration
- AWS S3 Model Storage
- Authentication (JWT/API Key)
- Monitoring & Metrics
- Frontend Dashboard (React/Streamlit)

---

# Author

**Samarth Joshi**

- GitHub: https://github.com/Sam-joshi-11
- LinkedIn: https://www.linkedin.com/in/samarthjoshi2410 
---

# Support

If you found this project useful, consider giving it a ⭐ on GitHub.
