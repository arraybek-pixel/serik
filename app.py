import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("diabetes_model.pkl","rb"))

st.title("Diabetes Risk Prediction")

# модель күтіп тұрған feature саны
n = model.n_features_in_

values = []

for i in range(n):
    v = st.number_input(f"Risk Factor {i+1}", value=0.0)
    values.append(v)

if st.button("Predict Diabetes Risk"):

    data = np.array([values])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low Risk of Diabetes")
