import pandas as pd
import tkinter as tk

from src.data_cleaning import clean_data
from src.analytics import patient_status_counts, department_load
from src.visualizations import plot_status_distribution, plot_department_load
from src.ui import DashboardUI

df = pd.read_csv("data/raw/patient_data.csv")
df = clean_data(df)

status_counts = patient_status_counts(df)
dept_counts = department_load(df)

fig1 = plot_status_distribution(status_counts)
fig2 = plot_department_load(dept_counts)

root = tk.Tk()
DashboardUI(root, [fig1, fig2])
root.mainloop()
