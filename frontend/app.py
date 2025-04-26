import streamlit as st
import requests

st.set_page_config(page_title="Diabetes Prediction App", page_icon="🧠", layout="centered")
st.title("🧠 Diabetes Prediction Interface")
st.subheader("Submit patient data to get a diabetes prediction")

# Define input fields
age = st.slider("Age", 1, 120, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", 10.0, 60.0, 30.0)
bp = st.number_input("Blood Pressure", 50, 200, 80)
s1 = st.number_input("S1: Total Cholesterol", 50, 300, 150)
s2 = st.number_input("S2: LDL", 50, 300, 100)
s3 = st.number_input("S3: HDL", 20, 150, 50)
s4 = st.number_input("S4: TCH/HDL Ratio", 0.5, 10.0, 4.5)
s5 = st.number_input("S5: log(Serum Triglycerides)", 3.0, 7.0, 5.5)
s6 = st.number_input("S6: Blood Sugar", 50, 200, 110)

# Convert sex to numerical
sex_val = 0 if sex == "Male" else 1

# Prediction button
if st.button("🔍 Predict"):
    with st.spinner("Sending data to the model..."):
        url = "https:3.145.115.164:8000/predict"
        payload = {
            "age": age,
            "sex": sex_val,
            "bmi": bmi,
            "bp": bp,
            "s1": s1,
            "s2": s2,
            "s3": s3,
            "s4": s4,
            "s5": s5,
            "s6": s6
        }

        try:
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                prediction = res.json()["prediction"]
                if prediction == 1:
                    st.success("🚨 High risk of diabetes detected.")
                else:
                    st.success("✅ Low risk of diabetes detected.")
            else:
                st.error(f"API error: {res.status_code} - {res.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")

st.caption("Made with ❤️ using Streamlit + FastAPI + ML")
