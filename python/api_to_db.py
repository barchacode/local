import pandas as pd
import requests
from pathlib import Path
def run_pipeline():
 base_dir = Path(__file__).resolve().parent.parent
 url="https://api.open-meteo.com/v1/forecast?latitude=33.6844&longitude=73.0479&hourly=temperature_2m"
 response = requests.get(url)
 data = response.json()

 df = df = pd.DataFrame(data["hourly"])

 raw_path = base_dir / "data" / "weather_raw.csv"
 df.to_csv(raw_path, index=False)

 print(type(df["time"].iloc[0]))
 print(df.head())
 df["time"] = pd.to_datetime(df["time"])
 df["date"] = df["time"].dt.date
 df["hour"] = df["time"].dt.hour

 df = df[["time", "date", "hour", "temperature_2m"]]
 df = df.rename(columns={"temperature_2m": "temperature"})

 clean_path = base_dir / "data" / "weather_cleaned.csv"
 df.to_csv(clean_path, index=False)
if __name__ == "__main__":
    run_pipeline()
 