import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.dropna()
    df.columns = [col.lower().strip() for col in df.columns]
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_path = BASE_DIR / "data" / "sample.csv"
    output_path = BASE_DIR / "data" / "cleaned_sample.csv"

    clean_data(input_path, output_path)