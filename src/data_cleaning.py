import pandas as pd

def clean_patient_data(df):
    df = df.copy()

    df.columns = df.columns.str.lower().str.strip()

    df.drop_duplicates(inplace=True)

    text_cols = ["gender", "department", "diagnosis", "status"]
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip().str.lower()

    df["department"].replace({
        "orthopaedics": "orthopedics",
        "neurology ": "neurology",
        "nan": "unknown"
    }, inplace=True)

    df["gender"].replace({"nan": "unknown"}, inplace=True)

    df["admission_date"] = pd.to_datetime(df["admission_date"], errors="coerce")
    df["discharge_date"] = pd.to_datetime(df["discharge_date"], errors="coerce")

    df["length_of_stay"] = (
        df["discharge_date"] - df["admission_date"]
    ).dt.days

    df["status"].fillna("unknown", inplace=True)

    return df
