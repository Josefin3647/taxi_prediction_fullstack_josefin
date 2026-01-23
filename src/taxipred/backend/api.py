from fastapi import FastAPI, HTTPException
from taxipred.utils.constants import DATA_PATH, REGRESSOR_PATH
from taxipred.backend.data_processing import TaxiPriceInput, PredictionOutput
import joblib
import pandas as pd
import numpy as np

df = pd.read_csv(DATA_PATH / "taxi_cleaned.csv")

app = FastAPI()

@app.get("/api/data")
async def read_data():
    return df.replace({np.nan: None}).to_dict(orient="records")

@app.post("/api/predict", response_model=PredictionOutput)
async def predict_price(payload: TaxiPriceInput):

    if payload.Trip_Distance_km > 150:
        raise HTTPException(
            status_code=400,
            detail="Please contact us for trips longer than 150 km."
        )
    
    data_to_predict = pd.DataFrame(payload.model_dump(), index=[0])
    rf = joblib.load(REGRESSOR_PATH)
    prediction = rf.predict(data_to_predict)
    return {"predicted_price": prediction[0]}
