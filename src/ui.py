import tkinter as tk
from tkinter import ttk
from src.visualizations import plot_status_chart, plot_department_chart
from src.analytics import (
    patient_status_distribution,
    department_distribution,
    average_length_of_stay
)

def launch_dashboard(df):
    root = tk.Tk()
    root.title("Healthcare Analytics Dashboard")
    root.geometry("1100x650")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    tab_data = ttk.Frame(notebook)
    tab_analytics = ttk.Frame(notebook)

    notebook.add(tab_data, text="Cleaned Patient Data")
    notebook.add(tab_analytics, text="Analytics & Trends")

    # ===== DATA TABLE =====
    tree = ttk.Treeview(tab_data, columns=list(df.columns), show="headings")
    for col in df.columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=120)

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(fill="both", expand=True)

    # ===== ANALYTICS =====
    top_metrics = ttk.Label(
        tab_analytics,
        text=f"Average Length of Stay: {average_length_of_stay(df)} days",
        font=("Segoe UI", 12, "bold")
    )
    top_metrics.pack(pady=10)

    charts_frame = ttk.Frame(tab_analytics)
    charts_frame.pack(fill="both", expand=True)

    left = ttk.Frame(charts_frame)
    right = ttk.Frame(charts_frame)

    left.pack(side="left", fill="both", expand=True)
    right.pack(side="right", fill="both", expand=True)

    plot_status_chart(left, patient_status_distribution(df))
    plot_department_chart(right, department_distribution(df))

    root.mainloop()
