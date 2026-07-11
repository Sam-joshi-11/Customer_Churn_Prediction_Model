import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
import mlflow
import mlflow.xgboost
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from pydantic import BaseModel,Field
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,ConfusionMatrixDisplay,roc_auc_score,roc_curve


file = r'data/Churn_Modelling.csv'
if not os.path.exists(file):
    print(f"Error {file} is not found")
    exit()

df = pd.read_csv(file)
print("First 5 rows are :\n",df.head())
print("Last 5 rows are :\n",df.tail())
print("Description of the Dataset :\n",df.describe())
print("Information of Dataset")
df.info()
print("Nulll values Count",df.isnull().sum())

df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)

X = df.drop("Exited",axis=1)
Y = df['Exited']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

corr = df.select_dtypes(include=np.number).corr()
plt.figure(figsize=(8,7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues")
plt.title("Correlation of the Features")
plt.show()

mlflow.set_experiment("Customer_Churn_Prediction")

params = {
    "random_state": 42,
    "n_estimators": 100,
    "learning_rate": 0.1,
    "max_depth": 6,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "eval_metric": "logloss"
}

with mlflow.start_run():

    # Create Model
    model = XGBClassifier(**params)

    # Train Model
    model.fit(X_train, Y_train)

    # Predictions
    Y_pred = model.predict(X_test)
    Y_prob = model.predict_proba(X_test)[:, 1]

    # Metrics
    accuracy = accuracy_score(Y_test, Y_pred)
    roc_auc = roc_auc_score(Y_test, Y_prob)

    # Log Parameters
    mlflow.log_params(params)

    # Log Metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("roc_auc", roc_auc)

    # Log Model
    model_info = mlflow.xgboost.log_model(
    xgb_model=model,
    name="customer_churn_model",
    registered_model_name="CustomerChurnModel"
)
    print(f"Model URI: {model_info.model_uri}")

print("Accuracy:", accuracy_score(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))
print("ROC-AUC:", roc_auc_score(Y_test, Y_prob))


cm = confusion_matrix(Y_test, Y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

fpr, tpr, thresholds = roc_curve(Y_test, Y_prob)

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f"AUC = {roc_auc_score(Y_test, Y_prob):.3f}")
plt.plot([0,1],[0,1],'k--')

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()


os.makedirs("artifacts", exist_ok=True)
joblib.dump(model, "artifacts/customer_churn_model.pkl")