import pandas as pd

# Load collected data
df = pd.read_csv("data/keystrokes_data.csv")

# Simple logic to label suspicious behavior
df["Label"] = 0  # Default: Normal activity
df.loc[df["CPU Usage (%)"] > 40, "Label"] = 1  # High CPU usage → Potential keylogger

# Save labeled dataset
df.to_csv("data/labeled_keystrokes_data.csv", index=False)
print("✅ Labeled dataset saved to data/labeled_keystrokes_data.csv")
