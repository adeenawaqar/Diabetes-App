import streamlit as st
import numpy as np
import pickle

st.title("Diabetes Prediction Web App ")

# Sidebar: select SVM kernel
st.sidebar.header("Choose SVM Kernel")
kernel_choice = st.sidebar.selectbox("Kernel", ("Linear", "Polynomial", "RBF"))

# Function to load corresponding model
def load_model(kernel):
    if kernel == "Linear":
        filename = "svm_linear.pkl"
    elif kernel == "Polynomial":
        filename = "svm_poly.pkl"
    else:
        filename = "svm_rbf.pkl"
    with open(filename, "rb") as file:
        model = pickle.load(file)
    return model

# User input
st.header("Enter Patient Details")
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=30)

# Predict button
if st.button("Predict"):
    model = load_model(kernel_choice)
    input_features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    
    # Prediction
    prediction = model.predict(input_features)[0]
    
    # Probability/confidence
    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(input_features)[0][prediction]
        confidence_percent = round(confidence * 100, 2)
    else:
        confidence_percent = "N/A (Model does not support probability)"
    
    # Show result
    if prediction == 1:
        st.error(f"The patient is likely to have diabetes. Confidence: {confidence_percent}")
    else:
        st.success(f"The patient is unlikely to have diabetes. Confidence: {confidence_percent}")
