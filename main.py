import pyautogui
import time

pyautogui.FAILSAFE = False

target_x = 1250
target_y = 1000

if __name__ == "__main__":
    # Move the mouse to the target position
    pyautogui.moveTo(target_x, target_y, duration=0)
    time.sleep(0.1)
    # # Perform a click
    pyautogui.click()
