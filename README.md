# taxi_prediction_fullstack_josefin  
Fullstack ML application for predicting taxi prices.

---

# Overview

This project is a fullstack machine learning application for predicting taxi trip prices.  
It consists of:

- A FastAPI backend providing API endpoints  
- A Streamlit frontend dashboard for user interaction  
- A trained machine learning model for price prediction  

The user enters trip distance and number of passengers, and the model returns an estimated taxi price in euros (€).

---

## Dashboard Preview

![Taxi Dashboard](images/application_prediction.png)

![Taxi Dashboard](images/application_data.png)

---



## Project Structure

```text
TAXI_PREDICTION_FULLSTACK_JOSEFIN/
│
├── .venv/
├── images/
│   └── tree_structure.png
│
├── src/
│   └── taxipred/
│       ├── __init__.py
│       │
│       ├── backend/
│       │   ├── api.py
│       │   ├── data_processing.py
│       │   └── model/
│       │       └── taxi_price_prediction.joblib
│       │
│       ├── data/
│       │   ├── cleaned_data.csv
│       │   ├── frontend_data.csv
│       │   └── taxi_trip_pricing.csv
│       │
│       ├── frontend/
│       │   ├── dashboard.py
│       │   └── pages/
│       │       ├── data.py
│       │       └── health.py
│       │
│       ├── model_development/
│       │   ├── eda.ipynb
│       │   └── model_dev.ipynb
│       │
│       └── utils/
│           ├── constants.py
│           └── map_phone.jpg
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## API Endpoints

Base URL (local):

```
http://127.0.0.1:8000
```

### POST `/api/predict`

Predicts taxi trip price from input features.

Example request:

```json
{
  "Trip_Distance_km": 5.0
}
```

Example response:

```json
{
  "prediction": 18.42
}
```

---

### GET `/api/data`

Returns the dataset used in the project.  
Missing values are converted to `null`.

---

# Machine Learning Model

- Target variable: `Trip_Price`  
- Model: `RandomForestRegressor`  
- Input features used in the deployed app:  
  - `Trip_Distance_km`

The trained model is stored as a serialized file in the `model/` directory.

---

## Acknowledgements

Parts of this project were developed with assistance from ChatGPT (OpenAI) for guidance on FastAPI, Streamlit integration, and code structure.  
All implementation decisions and final code adjustments were made by the author.