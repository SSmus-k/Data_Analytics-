from src.data_loader import load_raw_data, save_clean_data
from src.data_cleaning import clean_patient_data
from src.ui import launch_dashboard

df_raw = load_raw_data()
df_clean = clean_patient_data(df_raw)

save_clean_data(df_clean)

launch_dashboard(df_clean)
