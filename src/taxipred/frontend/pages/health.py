import streamlit as st
import httpx

API_URL = "http://127.0.0.1:8000"

try:
    response = httpx.get(f"{API_URL}/health", timeout=5)

    if response.status_code == 200:
        st.metric("API Status", "Online", "Healthy")
    else:
        st.metric("API Status", "Error", delta_color="inverse")

except Exception:
    st.metric("API Status", "Offline", delta_color="inverse")