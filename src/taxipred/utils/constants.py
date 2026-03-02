from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data"
MODEL_PATH = BASE_DIR / "backend" / "model" / "taxi_price_prediction.joblib"