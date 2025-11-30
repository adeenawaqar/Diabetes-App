import streamlit as st
import pickle
import numpy as np

st.title("Diabetes Prediction Web App ")
st.write("""
Welcome! This app predicts the likelihood of diabetes based on patient details.
Select an SVM kernel and enter patient data to get predictions.
""")

st.sidebar.header("Select SVM Kernel")
kernel_choice = st.sidebar.selectbox("Choose Kernel", ("Linear", "Polynomial", "RBF"))

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

st.header("Enter Patient Details")
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level (IU/mL)", min_value=0, max_value=900, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
age = st.number_input("Age", min_value=0, max_value=120, value=30)

if st.button("Predict Diabetes"):
    model = load_model(kernel_choice)
    
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    
    prediction = model.predict(input_data)[0]
    
    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(input_data)[0][prediction]
        confidence_percent = round(confidence * 100, 2)
    else:
        confidence_percent = "N/A (Model does not support probability)"
    
    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f" The patient is likely to have diabetes. Confidence: {confidence_percent}")
    else:
        st.success(f" The patient is unlikely to have diabetes. Confidence: {confidence_percent}")




