# app.py
import streamlit as st
import numpy as np
from sklearn.svm import SVC

st.title("Diabetes Prediction Web App")
st.write("Enter patient details below to predict the likelihood of diabetes:")

# User Input
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=30)

# Prepare features for prediction
input_features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])

# Dummy SVM Model (for testing without pickle)
# Note: This is a fake model, just for Streamlit app to run
model = SVC(probability=True)
# Fit dummy model on random data
X_dummy = np.random.rand(10, 8)
y_dummy = np.random.randint(0, 2, 10)
model.fit(X_dummy, y_dummy)

# Prediction Button
if st.button("Predict"):
    prediction = model.predict(input_features)
    prediction_prob = model.predict_proba(input_features)  # Optional probability

    if prediction[0] == 1:
        st.error("The patient is likely to have diabetes.")
    else:
        st.success("The patient is unlikely to have diabetes.")




