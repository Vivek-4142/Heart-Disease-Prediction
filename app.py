import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------------
# Safe Model & Scaler Loading
# -----------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "models", "heart_model.pkl")
scaler_path = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(page_title="Heart Disease Predictor", layout="wide")

st.title("🫀 Heart Disease Risk Prediction")
st.markdown("Enter patient clinical parameters to predict heart disease risk.")

# -----------------------------------
# Sidebar Inputs
# -----------------------------------
st.sidebar.header("Patient Information")

age = st.sidebar.slider("Age", 20, 100, 50)
sex = st.sidebar.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.sidebar.selectbox("Chest pain type", [0, 1, 2, 3])
bp = st.sidebar.number_input("BP", 80, 200, 120)
chol = st.sidebar.number_input("Cholesterol", 100, 600, 200)
fbs = st.sidebar.selectbox("FBS over 120 (0 = No, 1 = Yes)", [0, 1])
ekg = st.sidebar.selectbox("EKG results", [0, 1, 2])
max_hr = st.sidebar.number_input("Max HR", 60, 220, 150)
exang = st.sidebar.selectbox("Exercise angina (0 = No, 1 = Yes)", [0, 1])
oldpeak = st.sidebar.number_input("ST depression", 0.0, 6.0, 1.0, step=0.1)
slope = st.sidebar.selectbox("Slope of ST", [0, 1, 2])
ca = st.sidebar.selectbox("Number of vessels fluro", [0, 1, 2, 3])
thal = st.sidebar.selectbox("Thallium", [0, 1, 2, 3])

# -----------------------------------
# Prediction Button
# -----------------------------------
if st.button("Predict Risk"):

    # Create DataFrame with EXACT training column names
    input_data = pd.DataFrame([[
        age,
        sex,
        cp,
        bp,
        chol,
        fbs,
        ekg,
        max_hr,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]], columns=[
        "Age",
        "Sex",
        "Chest pain type",
        "BP",
        "Cholesterol",
        "FBS over 120",
        "EKG results",
        "Max HR",
        "Exercise angina",
        "ST depression",
        "Slope of ST",
        "Number of vessels fluro",
        "Thallium"
    ])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    st.info(f"Probability Score: {probability:.2f}")