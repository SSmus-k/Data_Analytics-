def patient_status_distribution(df):
    return df["status"].value_counts()

def department_distribution(df):
    return df["department"].value_counts()

def critical_patients(df):
    return df[df["status"] == "critical"]

def average_length_of_stay(df):
    return round(df["length_of_stay"].mean(), 2)
