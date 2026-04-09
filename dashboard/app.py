import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("../src/model.pkl", "rb"))

st.title("Employee Attrition Prediction")

st.write("Enter employee details:")

# Inputs
age = st.slider("Age", 18, 60, 30)
monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
years_at_company = st.slider("Years at Company", 0, 40, 5)
overtime = st.selectbox("OverTime", ["Yes", "No"])

# Convert inputs
overtime = 1 if overtime == "Yes" else 0

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([[age, monthly_income, years_at_company, overtime]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Employee likely to leave ❗")
    else:
        st.success("Employee likely to stay ✅")