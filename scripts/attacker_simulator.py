import time
import psutil
import random
import string
from pynput import keyboard

# Function to simulate high CPU and memory usage
def simulate_high_usage():
    print("🚨 Simulating high CPU and memory usage...")
    try:
        while True:
            # Allocate more memory (1 GB)
            _ = [bytearray(1024 * 1024 * 1024) for _ in range(10)]  # Allocate 1 GB
            # Simulate CPU usage (more intensive)
            for _ in range(10**8):  # Increase the loop iterations
                pass
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopped high CPU and memory usage simulation.")

# Function to simulate rapid keystroke logging
def simulate_keystroke_logging():
    print("⌨️ Simulating rapid keystroke logging...")
    def on_press(key):
        try:
            print(f"Key pressed: {key.char}")
        except AttributeError:
            print(f"Special key pressed: {key}")

    # Start listening to keystrokes
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n🛑 Stopped keystroke logging simulation.")

# Run the attacker simulation
if __name__ == "__main__":
    print("🔥 Starting attacker simulation...")
    try:
        simulate_high_usage()
        simulate_keystroke_logging()
    except KeyboardInterrupt:
        print("\n🛑 Attacker simulation stopped.")
