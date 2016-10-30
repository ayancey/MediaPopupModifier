import win32gui
import win32con
import pywintypes
import time

volume_hwnd = 0

while True:
    try:
        win32gui.SetWindowPos(volume_hwnd, win32con.HWND_TOPMOST, 50, 60, 70, 200, 0)
    except pywintypes.error:
        volume_hwnd = win32gui.FindWindowEx(0, 0, 'NativeHWNDHost', None)
    time.sleep(0.01)
