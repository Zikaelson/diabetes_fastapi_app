from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os  # ✅ Import os to read environment variables

# Create the FastAPI app
app = FastAPI()

# Load your trained model
model = joblib.load("model.pkl")

# ✅ Load environment variables
API_SECRET = os.getenv("API_SECRET", "default_secret")  # fallback if not set

# Define input structure using Pydantic
class DiabetesInput(BaseModel):
    age: float
    sex: int
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the diabetes prediction API",
        "api_secret_loaded": API_SECRET  # ✅ Just showing it is loaded correctly
    }

# Prediction endpoint
@app.post("/predict")
def predict(input_data: DiabetesInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data.dict()])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Return as JSON
    return {"prediction": int(prediction)}
