import pandas as pd
import joblib
import psutil
import time

# Load trained model
model = joblib.load("models/keylogger_model.pkl")

# Function to detect keylogger activity
def detect_keylogger():
    while True:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        timestamp = time.time()

        # Create a DataFrame for the model
        data = pd.DataFrame([[cpu_usage, memory_usage]], columns=["CPU Usage (%)", "Memory Usage (%)"])

        # Predict
        prediction = model.predict(data)[0]

        # Set a threshold for CPU usage to trigger alerts
        cpu_threshold = 70  # Adjust this threshold based on your needs

        if prediction == 1 or cpu_usage > cpu_threshold:
            print(f"⚠️ WARNING: Possible Keylogger Detected at {timestamp}!")

        time.sleep(2)  # Check every 2 seconds

# Run detection
detect_keylogger()
