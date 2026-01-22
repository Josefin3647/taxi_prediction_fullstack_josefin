from pathlib import Path

DATA_PATH = Path(__file__).parents[1] / "data"

MODEL_PATH = Path(__file__).parents[1] / "model_development"
REGRESSOR_PATH = MODEL_PATH / "taxi_price_prediction.joblib"