import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("Predicción de Diabetes")

pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bloodpressure = st.number_input("Blood Pressure", min_value=0)
skinthickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
pedigree = st.number_input("Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("Predict"):

    values = [[
        pregnancies,
        glucose,
        bloodpressure,
        skinthickness,
        insulin,
        bmi,
        pedigree,
        age
    ]]

    prediction = model.predict(values)

    if prediction[0] == 1:
        st.error("Posible diabetes")
    else:
        st.success("No presenta diabetes")