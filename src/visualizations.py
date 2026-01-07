import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use("seaborn-v0_8-whitegrid")

STATUS_COLORS = {
    "recovered": "#2ecc71",
    "admitted": "#f1c40f",
    "critical": "#e74c3c",
    "unknown": "#95a5a6"
}

def plot_status_chart(parent, data):
    fig, ax = plt.subplots(figsize=(6,4))
    colors = [STATUS_COLORS.get(k, "#3498db") for k in data.index]

    ax.bar(data.index, data.values, color=colors)
    ax.set_title("Patient Status Distribution")
    ax.set_ylabel("Number of Patients")

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def plot_department_chart(parent, data):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.barh(data.index, data.values, color="#3498db")
    ax.set_title("Department Load")

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
