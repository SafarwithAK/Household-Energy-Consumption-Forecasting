import streamlit as st
import pandas as pd
import pickle


with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Household Energy Consumption Forecasting")
st.write("Enter household details to predict electricity consumption (kWh).")


Household_size = st.number_input("Household Size", min_value=1, max_value=20, value=1)
Avg_temp = st.number_input("Average Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
Has_AC = st.selectbox("Has AC?", ["Yes", "No"])
Peak_usage = st.number_input("Peak Hours Usage (kWh)", min_value=0.0, max_value=100.0, value=1.0)

if st.button("Predict kWh Consumption"):
    Has_AC_numeric = 1 if Has_AC == "Yes" else 0

    input_data = pd.DataFrame([[Household_size, Avg_temp, Has_AC_numeric, Peak_usage]],
                              columns=["Household_Size", "Avg_Temperature_C", "Has_AC", "Peak_Hours_Usage_kWh"])

    prediction = model.predict(input_data)[0]
    st.success(f" Estimated Consumption: {prediction:.2f} kWh")