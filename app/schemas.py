from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    CreditScore: int = Field(
        ...,
        ge=300,
        le=900,
        description="Customer credit score"
    )

    Age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Customer age"
    )

    Tenure: int = Field(
        ...,
        ge=0,
        le=10,
        description="Years with the bank"
    )

    Balance: float = Field(
        ...,
        ge=0,
        description="Account balance"
    )

    NumOfProducts: int = Field(
        ...,
        ge=1,
        le=4,
        description="Number of bank products"
    )

    HasCrCard: int = Field(
        ...,
        ge=0,
        le=1,
        description="0 = No, 1 = Yes"
    )

    IsActiveMember: int = Field(
        ...,
        ge=0,
        le=1,
        description="0 = No, 1 = Yes"
    )

    EstimatedSalary: float = Field(
        ...,
        ge=0,
        description="Estimated annual salary"
    )

    Geography_Germany: int = Field(..., ge=0, le=1)
    Geography_Spain: int = Field(..., ge=0, le=1)

    Gender_Male: int = Field(..., ge=0, le=1)