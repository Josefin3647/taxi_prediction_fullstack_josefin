from fastapi import FastAPI
from taxipred.utils.constants import DATA_PATH, REGRESSOR_PATH
from taxipred.backend.data_processing import TaxiPrice
import pandas as pd
import numpy as np

df = pd.read_csv(DATA_PATH / "taxi_cleaned.csv")

app = FastAPI()

@app.get("/api/data")
async def read_data():
    return df.replace({np.nan: None}).to_dict(orient="records")

@app.post("/api/predict")
async def predict_price(payload: TaxiPrice):
    return TaxiPrice
