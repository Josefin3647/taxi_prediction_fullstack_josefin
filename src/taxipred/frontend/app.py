import streamlit as st
import httpx
from pathlib import Path

URL = "http://127.0.0.1:8000/api/predict"

image_path = Path(__file__).parents[1] / "utils" / "map_phone.jpg"

st.markdown("# Taxi prediction")
st.markdown("""
            Enter the distance to your destination and the number of 
            travelers to predict the price. 
""")

st.image(image_path)

with st.form("taxi_data"):
    Trip_Distance_km = st.number_input(
        "Trip distance in km", min_value=0.1, value=1.0
    )
    Passenger_Count = st.number_input(
        "Number of passengers", min_value=1, max_value=4
    )

    submitted = st.form_submit_button("Predict the Price")

if submitted:
    payload = {
        "Trip_Distance_km": Trip_Distance_km,
        "Passenger_Count": Passenger_Count
    }

    response = httpx.post(URL, json=payload)

    if response.status_code == 200:
        prediction = response.json().get("predicted_price")
        st.markdown(f"**Predicted price:** {prediction:.2f} $")
    
    elif response.status_code == 400:
        st.warning(response.json()["detail"])
    
    else:
        st.error("Something went wrong. Please try again.")