import threading
import time
from pynput.keyboard import Key, Controller
import keyboard

# Initialize the keyboard controller
keyboard_controller = Controller()

# Auto-clicker state
auto_clicker_running = False

def auto_clicker():
    global auto_clicker_running
    while True:
        if auto_clicker_running:
            # Press and release the Enter key
            keyboard_controller.press(Key.enter)
            keyboard_controller.release(Key.enter)
            time.sleep(0.01)  # Adjust for speed (lower for faster)
        else:
            time.sleep(0.1)

def toggle_auto_clicker():
    global auto_clicker_running
    auto_clicker_running = not auto_clicker_running
    print("Auto-clicker running:", auto_clicker_running)

# Start the auto-clicker in a separate thread
thread = threading.Thread(target=auto_clicker, daemon=True)
thread.start()

# Register the hotkey (Alt+G) to toggle the auto-clicker
keyboard.add_hotkey('alt+g', toggle_auto_clicker)

print("Auto-clicker started. Press Alt+G to toggle it on/off.")
print("Press Ctrl+C to exit.")

# Keep the script running
keyboard.wait()
