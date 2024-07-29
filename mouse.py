import pyautogui
import time as time_module

def get_mouse_position():
    """Prints the current position of the mouse cursor. Use this to find coordinates."""
    print("Move the mouse to the desired position and press Ctrl-C to get the coordinates.")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"X: {x}, Y: {y}")
            time_module.sleep(1)
    except KeyboardInterrupt:
        print("Coordinate capture stopped.")

get_mouse_position()
