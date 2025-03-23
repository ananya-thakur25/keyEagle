import pandas as pd
import matplotlib.pyplot as plt
import os

# Correct the path
csv_path = os.path.join(os.path.dirname(os.path.dirname(_file_)), "data/labeled_keystrokes_data.csv")

# Load dataset
df = pd.read_csv(csv_path)

# Plot CPU usage
plt.figure(figsize=(10, 5))
plt.plot(df["CPU Usage (%)"], label="CPU Usage (%)", color="blue")
plt.xlabel("Keystroke Index")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Over Time")
plt.legend()
plt.show()
