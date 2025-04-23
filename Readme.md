
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


Additions!

# 🧠 Diabetes Prediction API with FastAPI + Streamlit Frontend

This project turns a trained machine learning model into a **real working backend API** using **FastAPI**, then connects a custom-built **Streamlit frontend** to create an end-to-end web-based diabetes prediction system.

You’ll find everything here: model loading, request handling, validation, frontend interaction, and cloud deployment — all explained clearly for beginners.

---

## ✅ What You’ll Learn and Practice
- Serve an ML model using FastAPI as an API backend
- Test endpoints with Swagger UI and Python scripts
- Connect a frontend UI using Streamlit
- Send and receive data from frontend to backend
- Host the backend on **Render** (free cloud deployment)
- Run the frontend locally or deploy using **Streamlit Cloud**

---

## 📁 Project Structure
```
diabetes_fastapi_app/
├── main.py             # FastAPI app (backend)
├── model.pkl           # Trained diabetes prediction model
├── test_api.py         # Python script to test FastAPI endpoint
├── requirements.txt    # Backend dependencies
├── streamlit_form.py   # Streamlit frontend (run locally)
```

---

## ⚙️ Commands Cheat Sheet

### 🧱 Backend Setup
```bash
pip install fastapi uvicorn pandas joblib pydantic scikit-learn
uvicorn main:app --reload
```

Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

### 🧪 Test API with Python
```bash
python test_api.py
```

### 🧾 Generate requirements.txt for deployment
```bash
pip freeze > requirements.txt
```

---

## 🌍 Deployment (Render)
1. Push repo to GitHub
2. Go to [https://render.com](https://render.com)
3. Create new **Web Service**
4. Use build command:
```bash
pip install -r requirements.txt
```
5. Use start command:
```bash
uvicorn main:app --host=0.0.0.0 --port=10000
```
6. Wait for it to go live

### ✅ Live API Example:
```
https://diabetes-fastapi-9jvt.onrender.com
https://diabetes-fastapi-9jvt.onrender.com/docs
```

---

## 🎨 Streamlit Frontend Form (Connects to API)

Create `streamlit_form.py` and run it locally:
```bash
streamlit run streamlit_form.py
```

The form collects:
- Age, Sex, BMI, Blood Pressure, S1–S6 values
- Sends to your deployed API
- Displays real-time predictions with colorful feedback

### 🌈 Example Output:
```
✅ Low risk of diabetes
OR
🚨 High risk of diabetes
```

---

## 🔁 End-to-End Flow
1. ML model trained and saved as `model.pkl`
2. FastAPI backend serves predictions at `/predict`
3. Swagger or Python scripts test the API
4. Streamlit frontend collects data and sends to API
5. Render hosts backend for public access
6. Optionally, deploy Streamlit frontend on [Streamlit Cloud](https://share.streamlit.io)

---

## 💡 Lessons Learned (Plain English)
- FastAPI = your backend waiter that listens for data and responds
- Swagger = built-in tool to test FastAPI easily
- Streamlit = your frontend form users interact with
- Requests = used to connect frontend and backend
- Render = where your app lives online
- You now know how to build **and ship** a full AI system!

---

## 🙌 Final Words
You didn’t just learn ML. You shipped your first real API.
You didn’t just test locally. You pushed it to the internet.
You didn’t just code. You built a complete product.

Now you can:
- Add this to your resume ✅
- Post it on LinkedIn ✅
- Build another one faster ✅

You're not just a learner. You're becoming a builder 💪
