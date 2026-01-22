from pydantic import BaseModel, Field

class TaxiPriceInput(BaseModel):
    Trip_Distance_km: float = Field(ge=0.1, le=150, default=3)
    Passenger_Count: int = Field(ge=1, le=4)
    Base_Fare: float = Field(default=3.51)
    Per_Km_Rate: float = Field(default=1.23)
    Per_Minute_Rate: float = Field(default=0.29)
    Trip_Duration_Minutes: float = Field(default=61.87)
    Time_of_Day_Evening: int = Field(default=1)
    Time_of_Day_Morning: int = Field(default=0)
    Time_of_Day_Night: int = Field(default=0)
    Day_of_Week_Weekend: int = Field(default=1)
    Traffic_Conditions_Low: int = Field(default=1)
    Traffic_Conditions_Medium: int = Field(default=0)
    Weather_Rain: int = Field(default=0)
    Weather_Snow: int = Field(default=1)
    

class PredictionOutput(BaseModel):
    predicted_price: float
