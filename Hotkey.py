import sys
import subprocess
import keyboard
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class HotkeyThread(QThread):
    def __init__(self, hotkey=None, action=None):
        super().__init__()
        
        self.winword_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
        self.powerpoint_path = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
        self.excel_path = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
        self.browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    def run(self):
        keyboard.add_hotkey("ctrl+alt+w", self.open_word)
        keyboard.add_hotkey("ctrl+alt+p", self.open_powerpoint)
        keyboard.add_hotkey("ctrl+alt+e", self.open_excel)
        keyboard.add_hotkey("ctrl+alt+b", self.open_browser)
        keyboard.wait("esc")

    def open_word(self):
        try:
            subprocess.Popen(self.winword_path)
        except Exception as e:
            print(f"Failed to open Microsoft Word: {e}")

    def open_powerpoint(self):
        try:
            subprocess.Popen(self.powerpoint_path)
        except Exception as e:
            print(f"Failed to open Microsoft PowerPoint: {e}")

    def open_excel(self):
        try:
            subprocess.Popen(self.excel_path)
        except Exception as e:
            print(f"Failed to open Microsoft Excel: {e}")

    def open_browser(self):
        try:
            subprocess.Popen(self.browser_path)
        except Exception as e:
            print(f"Failed to open the browser: {e}")
