import pyautogui
import time
import pygetwindow as gw
import psutil
import win32gui
import win32process
import ctypes

pyautogui.FAILSAFE = False

IsWindowVisible = ctypes.windll.user32.IsWindowVisible
GWL_STYLE = -16
WS_VISIBLE = 0x10000000

# check if window belongs to main app
def is_main_window(hwnd):
    if not win32gui.IsWindowVisible(hwnd) or not win32gui.IsWindowEnabled(hwnd):
        return False
    parent = win32gui.GetParent(hwnd)
    if parent != 0:
        return False  # Exclude child windows
    style = win32gui.GetWindowLong(hwnd, GWL_STYLE)
    return (style & WS_VISIBLE) == WS_VISIBLE

# gets parent pid
def get_parent_pid(process_name):
    for proc in psutil.process_iter(['name', 'ppid']):
        if proc.info['name'] == process_name:
            parent = psutil.Process(proc.info['ppid'])
            return parent.pid
    return None

#gets all window handlse for process id
def get_window_handles_by_pid(pid):
    def callback(hwnd, hwnds):
        _, process_pid = win32process.GetWindowThreadProcessId(hwnd)
        if process_pid == pid:
            hwnds.append(hwnd)
        return True

    handles = []
    win32gui.EnumWindows(callback, handles)
    return handles

# gets main window handle for pid
def get_main_window_handle(pid):
    handles = get_window_handles_by_pid(pid)
    for hwnd in handles:
        if is_main_window(hwnd):
            return hwnd
    return None


if __name__ == "__main__":
    subprocess_name = "LeagueClientUxRender.exe" 
    parent_pid = get_parent_pid(subprocess_name)

    if parent_pid:
        hwnd = get_main_window_handle(parent_pid)
        if hwnd:
            title = win32gui.GetWindowText(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            width = rect[2] - rect[0]
            height = rect[3] - rect[1]

            # proportinal offset based on widow size
            x_offset = 1280 / 2560
            y_offset = 1100 / 1440

            target_x = rect[0] + int(width * x_offset)
            target_y = rect[1] + int(height * y_offset)
            print(target_x,target_y)
        else:
            print(f"Main window not found for parent PID: {parent_pid}")
    else:
        print(f"Parent process not found for {subprocess_name}")

    # bring to front if in bg
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.1)

    pyautogui.moveTo(target_x, target_y, duration=0)
    time.sleep(0.1)

    pyautogui.click()
