import pandas as pd
from pathlib import Path

# ABSOLUTE BASE DIRECTORY OF THIS FILE
BASE_DIR = Path(__file__).resolve().parent

print("SCRIPT FILE:", Path(__file__).resolve())
print("BASE_DIR:", BASE_DIR)

def clean_data(input_file, output_file):
    print("READING:", input_file)
    print("EXISTS:", input_file.exists())

    df = pd.read_csv(input_file)
    df = df.dropna()
    df.columns = [col.lower().strip() for col in df.columns]
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_path = BASE_DIR / "data" / "sample.csv"
    output_path = BASE_DIR / "data" / "cleaned_sample.csv"

    clean_data(input_path, output_path)
