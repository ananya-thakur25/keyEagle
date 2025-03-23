import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import joblib
import time
import threading
import os
import pandas as pd

# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "../models/keylogger_model.pkl")

# Load trained model
model = joblib.load(model_path)

# Function to detect keylogger activity
def detect_keylogger():
    while True:
        # Get current CPU and memory usage
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Create a DataFrame for the model
        data = pd.DataFrame([[cpu_usage, memory_usage]], columns=["CPU Usage (%)", "Memory Usage (%)"])

        # Predict using the trained model
        prediction = model.predict(data)[0]

        # Set thresholds for CPU and memory usage to trigger alerts
        cpu_threshold = 70  # Adjust this threshold based on your needs
        memory_threshold = 80  # Adjust this threshold based on your needs

        # Update the status label based on detection
        if prediction == 1 or cpu_usage > cpu_threshold or memory_usage > memory_threshold:
            alert_message = f"⚠️ WARNING: Possible Keylogger Detected at {timestamp}!\nCPU Usage: {cpu_usage}%\nMemory Usage: {memory_usage}%"
            messagebox.showwarning("Keylogger Alert", alert_message)
            status_label.config(text="Status: Keylogger Detected!", foreground="#FF6B6B")
        else:
            status_label.config(text="Status: No Keylogger Detected", foreground="#4CAF50")

        # Update system metrics & progress bars
        cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        memory_label.config(text=f"Memory Usage: {memory_usage}%")
        cpu_progress["value"] = cpu_usage
        memory_progress["value"] = memory_usage

        time.sleep(2)  # Check every 2 seconds

# Function to start detection
def start_detection():
    threading.Thread(target=detect_keylogger, daemon=True).start()
    status_label.config(text="Status: Detection Started", foreground="#76C7C0")

# Main Window
root = tk.Tk()
root.title("🦅 KeyEagle")
root.geometry("900x550")
root.configure(bg="#1E1E2E")  # Dark mode background
root.resizable(False, False)

# Header Label
header = tk.Label(
    root, text="🦅 KeyEagle - Advanced Keylogger Detection",
    font=("Arial", 26, "bold"), fg="white", bg="#1E1E2E"
)
header.pack(pady=20)

# Status Label
status_label = tk.Label(root, text="Status: Not Running", font=("Arial", 15), fg="#76C7C0", bg="#1E1E2E")
status_label.pack(pady=10)

# CPU & Memory Progress Bars
metrics_frame = tk.Frame(root, bg="#1E1E2E")
metrics_frame.pack(pady=30)

cpu_label = tk.Label(metrics_frame, text="CPU Usage: 0%", font=("Arial", 15, "bold"), fg="white", bg="#1E1E2E")
cpu_label.grid(row=0, column=0, padx=20, pady=10)
cpu_progress = ttk.Progressbar(metrics_frame, orient="horizontal", length=350, mode="determinate")
cpu_progress.grid(row=0, column=1, padx=20, pady=10)

memory_label = tk.Label(metrics_frame, text="Memory Usage: 0%", font=("Arial", 15, "bold"), fg="white", bg="#1E1E2E")
memory_label.grid(row=1, column=0, padx=20, pady=10)
memory_progress = ttk.Progressbar(metrics_frame, orient="horizontal", length=350, mode="determinate")
memory_progress.grid(row=1, column=1, padx=20, pady=10)

# Play Button (No Text Inside)
play_button = tk.Button(
    root, text="▶️", font=("Arial", 40, "bold"), fg="white",
    bg="#1E1E2E", border=0, command=start_detection, cursor="hand2"
)
play_button.pack(pady=20)

# Start Detection Button
start_button = tk.Button(
    root, text="Start Detection", font=("Arial", 14, "bold"),
    bg="#4CAF50", fg="white", border=0, command=start_detection,
    cursor="hand2", padx=25, pady=10
)
start_button.pack(pady=10)

# Run Tkinter event loop
root.mainloop()
