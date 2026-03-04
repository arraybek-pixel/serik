import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("diabetes_model.pkl","rb"))

st.title("Diabetes Risk Prediction")

# модель қанша feature күтетінін автоматты анықтау
n_features = model.n_features_in_

inputs = []

for i in range(n_features):
    value = st.number_input(f"Feature {i+1}", value=0.0)
    inputs.append(value)

if st.button("Predict"):

    data = np.array([inputs])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")
