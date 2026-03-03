from pydantic import BaseModel, Field

class TaxiPriceInput(BaseModel):
    Trip_Distance_km: float = Field(gt=0, le=10000, default=3)
    Per_Km_Rate: float = Field(default=1.23)
    Trip_Duration_Minutes: float = Field(default=61.87)
    Per_Minute_Rate: float = Field(default=0.29)
    
class PredictionOutput(BaseModel):
    predicted_price: float
