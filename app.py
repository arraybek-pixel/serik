import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("diabetes_model.pkl","rb"))

st.title("Diabetes Risk Prediction")

st.subheader("Patient Health Information")

preg = st.number_input("Pregnancies (Number of pregnancies)",0,20)
glucose = st.number_input("Glucose Level",0,200)
bp = st.number_input("Blood Pressure",0,150)
skin = st.number_input("Skin Thickness",0,100)
insulin = st.number_input("Insulin Level",0,900)
bmi = st.number_input("BMI (Body Mass Index)",0.0,60.0)
dpf = st.number_input("Diabetes Pedigree Function (Genetic risk)",0.0,3.0)
age = st.number_input("Age",1,120)

if st.button("Predict Diabetes Risk"):

    data = np.array([[preg,glucose,bp,skin,insulin,bmi,dpf,age]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")
