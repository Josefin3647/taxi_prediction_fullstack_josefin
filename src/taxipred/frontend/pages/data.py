import streamlit as st
import httpx
import pandas as pd

st.title("Taxi Dataset")

DATA_URL = "http://127.0.0.1:8000/api/data"

response = httpx.get(DATA_URL)

if response.status_code == 200:
    df = pd.DataFrame(response.json())
    st.dataframe(df.head(200))
else:
    st.error("Could not fetch data from API")