import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("diabetes_model.pkl","rb"))

st.title("Diabetes Risk Prediction")

preg = st.number_input("Pregnancies",0,20)
glucose = st.number_input("Glucose",0,200)
bp = st.number_input("Blood Pressure",0,150)
skin = st.number_input("Skin Thickness",0,100)
insulin = st.number_input("Insulin",0,900)
bmi = st.number_input("BMI",0.0,60.0)
dpf = st.number_input("Diabetes Pedigree Function",0.0,3.0)
age = st.number_input("Age",1,120)

if st.button("Predict"):

    data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")
