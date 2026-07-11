import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_NAME = os.getenv("MODEL_NAME")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
    AWS_REGION = os.getenv("AWS_DEFAULT_REGION")