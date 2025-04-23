
# 🧠 Diabetes Prediction API with FastAPI

This project turns a trained machine learning model into a **real working backend API** using **FastAPI**. It predicts whether a person is likely to have diabetes based on health features such as age, BMI, blood pressure, glucose, and more.

You’ll find everything here: model loading, request handling, validation, and testing — all explained clearly for beginners.

---

## ✅ What You’ll Learn and Practice
- How to serve an ML model using FastAPI
- How to create API endpoints (GET and POST)
- How to validate inputs using `pydantic`
- How to test your API using Python code
- The difference between frontend (like Streamlit) and backend (like FastAPI)
- How to run and use a backend in real life

---

## 📁 Project Structure
```
diabetes_fastapi_app/
├── main.py             # The FastAPI app and routes
├── model.pkl           # Your trained ML model
├── test_api.py         # Python script to test your API
```

---

## ⚙️ Commands You Used (Cheat Sheet)

### 🔹 Create Project Folder
```bash
mkdir diabetes_fastapi_app
cd diabetes_fastapi_app
code .
```

### 🔹 Install FastAPI and Dependencies
```bash
pip install fastapi uvicorn pydantic pandas joblib
```

### 🔹 Add your trained model file
Copy `model.pkl` from your Streamlit project into this folder:
```text
📁 diabetes_fastapi_app/
    └── model.pkl ✅
```

### 🔹 Run the FastAPI Server
```bash
uvicorn main:app --reload
```
Then open your browser:
```http
http://127.0.0.1:8000        # Base URL
http://127.0.0.1:8000/docs   # Swagger testing interface
```

### 🔹 Test the API from Python
Create `test_api.py`:
```python
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "age": 50,
    "sex": 1,
    "bmi": 30.0,
    "bp": 80,
    "s1": 150,
    "s2": 100,
    "s3": 50,
    "s4": 4.5,
    "s5": 5.5,
    "s6": 110
}

response = requests.post(url, json=data)
print("Response:", response.json())
```
Run with:
```bash
python test_api.py
```

✅ Output:
```json
{"prediction": 1}
```

---

## 🔌 main.py – Full FastAPI Code Example
```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model.pkl")

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

@app.get("/")
def read_root():
    return {"message": "Welcome to the diabetes prediction API"}

@app.post("/predict")
def predict(input_data: DiabetesInput):
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)[0]
    return {"prediction": int(prediction)}
```

---

## 🧠 What This Backend Does
- Loads a trained model (`model.pkl`)
- Accepts data through POST requests at `/predict`
- Validates the input format using Pydantic
- Runs the prediction using logistic regression
- Returns a JSON response

---

## 🧠 Key Concepts You’ve Learned
| Concept | What It Means |
|--------|----------------|
| Backend | The part of your system that runs in the background and handles logic and predictions |
| API | An endpoint that listens for requests and responds with results |
| FastAPI | A Python tool for building backend APIs easily |
| Swagger UI | A live interface to test your API visually |
| JSON | The format your data is sent and returned in |
| `uvicorn` | The tool that runs your FastAPI server |
| Pydantic | Validates and parses incoming data |
| `requests.post()` | How you send data from Python to your API |

---

## 🚨 Reminders
- You must keep your FastAPI server running to test it.
- If it’s not running, `test_api.py` will fail with connection errors.
- You can open a second terminal tab to run Python tests while the server stays running in the first tab.

---

## 🔄 What’s Next?
- Push this project to GitHub
- Deploy the API to the web (Render or Railway)
- Connect this backend to a frontend app (Streamlit, React, HTML form)
- Add logs, authentication, and advanced error handling

---

## 🙌 Final Words
This project helped you cross the line from running models locally to **serving ML predictions as a real backend** — that’s a HUGE step in becoming a production-ready data scientist or machine learning engineer.

You’re not just building projects anymore — you’re building systems 💥
