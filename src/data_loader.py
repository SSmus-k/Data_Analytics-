import pandas as pd

RAW_PATH = "data/raw/patient_data.csv"
CLEAN_PATH = "data/processed/patient_data_cleaned.csv"

def load_raw_data():
    return pd.read_csv(RAW_PATH)

def save_clean_data(df):
    df.to_csv(CLEAN_PATH, index=False)

def load_clean_data():
    return pd.read_csv(CLEAN_PATH)
