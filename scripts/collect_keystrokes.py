import time
import psutil
import pandas as pd
from pynput import keyboard


data = []

def on_press(key):
    try:
        keystroke = key.char  # Capture character key
    except AttributeError:
        keystroke = str(key)  # Capture special keys (Shift, Ctrl, etc.)

    # Capture system usage
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    timestamp = time.time()

    # Store the data
    data.append([timestamp, keystroke, cpu_usage, memory_usage])

    # Print real-time keystroke log
    print(f"[{timestamp}] Key: {keystroke}, CPU: {cpu_usage}%, Memory: {memory_usage}%")

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass  # Stop on user interrupt

# Save collected data to CSV
df = pd.DataFrame(data, columns=["Timestamp", "Keystroke", "CPU Usage (%)", "Memory Usage (%)"])
df.to_csv("data/keystrokes_data.csv", index=False)
print("✅ Keystroke data saved to data/keystrokes_data.csv")
