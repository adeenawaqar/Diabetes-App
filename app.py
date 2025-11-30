import streamlit as st
import numpy as np

st.title("Diabetes Prediction Web App")

# User input
pregnancies = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose", 0, 200, 120)
age = st.number_input("Age", 0, 120, 30)

# Prepare input
input_features = np.array([pregnancies, glucose, age])

# Predict button
if st.button("Predict"):
    # Dummy logic: glucose > 140 ya age > 50 → diabetes
    if glucose > 140 or age > 50:
        st.error("The patient is likely to have diabetes.")
    else:
        st.success("The patient is unlikely to have diabetes.")
