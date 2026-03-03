import streamlit as st
import httpx
from pathlib import Path
from taxipred.utils.constants import BASE_DIR

URL = "http://127.0.0.1:8000/api/predict"

image_path = BASE_DIR / "utils" / "map_phone.jpg"

st.markdown("# Taxi Price prediction")
st.markdown("""
            Enter the trip distance below and get a price prediction. 
""")

st.image(image_path)

st.divider()

with st.form("taxi_data"):
    Trip_Distance_km = st.number_input(
        "Enter the trip distance in km", min_value=0.1, value=1.0, max_value=10000.0, step=0.1
    )

    submitted = st.form_submit_button("Predict the Price")

if submitted:
    payload = {
        "Trip_Distance_km": Trip_Distance_km
    }
 
    response = httpx.post(URL, json=payload)

    if response.status_code == 200:
        prediction = response.json().get("predicted_price")
        st.metric("Predicted Price (€)", round(prediction, 2))
    
    elif response.status_code == 400:
        st.warning(response.json()["detail"])
    
    else:
        st.error("Something went wrong. Please try again.")