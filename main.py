import sys
import os
import logging
# import src_images
# import sqlite3
import hashlib
import json
# import datetime
from pynput import mouse
# from dateutil import parser
import time
# import win32gui
import psutil
# import win32com.client
import subprocess
import ctypes
import threading
from collections import defaultdict
import keyboard
import uiautomation as auto
from winotify import Notification, audio
from database import create_database, insert_user, fetch_user_from_database
from PySide6.QtCore import QThread, Signal, Qt, QTimer, QMetaObject, Slot, QObject, QEvent, QTime
from PySide6.QtGui import QColor, QGuiApplication
from PySide6.QtWidgets import QMainWindow, QWidget, QDialog, QApplication, QLabel, QProgressBar, QPushButton, QLineEdit, QMessageBox, QFileDialog, QGraphicsEffect, QGraphicsDropShadowEffect
from LoginPage_UI import Ui_Login
from CreateAccPage_UI import Ui_CreateAcc
from MainWindow import Ui_MainHomePage
from SplashScreenPage_UI import Ui_SplashScreen
from FeedBackPage_UI import Ui_Feedback
from Hotkey import HotkeyThread
# from AppMonitoring import AppMonitor
from overlayWord import Ui_WordOverlay
from overlayPowerPoint import Ui_PowerPointOverlay
from overlayExcel import Ui_ExcelOverlay
from overlayBrowser import Ui_Browser
from config import APP_SETTINGS
from utils import get_window_text

counter = 0

# Set up logging configuration
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='w')


class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.widget.setGraphicsEffect(self.shadow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(35)

        self.show()
    
    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)
        counter += 3

        if counter > 100:
            self.timer.stop()
            self.close()
            self.login_window = LoginWindow()
            self.login_window.show()


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)

        self.ui.LoginButton.clicked.connect(self.open_home_page)
        self.ui.CreateButton.clicked.connect(self.open_create_account)

    def open_create_account(self):
        self.create_account_window = CreateAccountWindow()
        self.create_account_window.show()
        self.hide()

    def open_home_page(self):
        try:
            username = self.ui.Enter_Username.text()
            password = self.ui.Enter_Password.text()

            if not username or not password:
                QMessageBox.warning(self, "Missing Input", "Please input your username and password.")
                return

            user_data = fetch_user_from_database(username)

            if not user_data:
                QMessageBox.warning(self, "Incorrect Credentials", "Incorrect username or password.")
                return

            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

            if hashed_password != user_data[2]:
                QMessageBox.warning(self, "Incorrect Credentials", "Incorrect username or password.")
                return

            self.home_page_window = HomeWindow(username)
            self.home_page_window.show()
            self.hide()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            logging.error(f"An error occurred: {str(e)}")

    def closeEvent(self, event):
        QApplication.instance().exit(0)


class CreateAccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateAcc()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)

        self.ui.Goback_button.clicked.connect(self.go_back_to_login)
        self.ui.registerbutton.clicked.connect(self.register_user)

    def register_user(self):
        username = self.ui.enter_username.text()
        password = self.ui.enter_password.text()
        confirm_password = self.ui.enter_confirmpass.text()

        if not username or not password:
            QMessageBox.warning(self, "Missing Input", "Please enter a username and password.")
            return

        if len(password) < 8:
            QMessageBox.warning(self, "Password Too Short", "Password must be at least 8 characters long.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Incorrect Password", "Passwords do not match.")
            return

        existing_user = fetch_user_from_database(username)
        if existing_user:
            QMessageBox.warning(self, "Username Already Exists", "The username already exists. Please choose a different username.")
            return

        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        insert_user(username, hashed_password)

        QMessageBox.information(self, "Registration Successful", "User registered successfully!")

    def go_back_to_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def closeEvent(self, event):
        QApplication.instance().exit(0)


class AppDetectionThread(QThread):
    app_detected = Signal(str)

    def __init__(self, parent=None):
        super(AppDetectionThread, self).__init__(parent)
        self.active = True
        self.displayed_apps = set()
        self.known_apps = APP_SETTINGS['known_apps']

    def run(self):
        while self.active:
            current_apps = set()
            for proc in psutil.process_iter(attrs=['pid', 'name']):
                try:
                    process_name = proc.info['name']
                    current_apps.add(process_name)
                    if process_name in self.known_apps and process_name not in self.displayed_apps:
                        self.app_detected.emit(self.known_apps[process_name])
                        self.displayed_apps.add(process_name)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            self.displayed_apps = self.displayed_apps.intersection(current_apps)
            time.sleep(1)

    def stop(self):
        self.active = False

class WindowMonitorThread(QThread):
    window_updated = Signal(str)

    def __init__(self):
        super().__init__()
        self.active_windows = defaultdict(int)
        self.known_apps = {
            "Word": "WINWORD.EXE",
            "PowerPoint": "POWERPNT.EXE",  # Update with the correct executable name
            "Excel": "EXCEL.EXE",  # Update with the correct executable name
            "Google Chrome": "CHROME.EXE",  # Update with the correct executable name
            "Microsoft Edge": "MSEDGE.EXE"  # Update with the correct executable name
        }
        self.current_window = None

    def run(self):
        while True:
            active_window = self.get_active_window()
            if active_window != self.current_window:
                self.update_window_duration(self.current_window)
                self.current_window = active_window
                self.window_updated.emit(self.get_most_used_window())
            time.sleep(1)  # Adjust the sleep duration as needed

    def get_active_window(self):
        active_window_name = ""
        for proc in psutil.process_iter(['name', 'exe']):
            try:
                process_name = proc.info['name']
                process_exe = proc.info['exe']
                if process_exe and any(exe in process_exe for exe in self.known_apps.values()):
                    active_window_name = process_name
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return active_window_name

    def update_window_duration(self, window_name):
        if window_name:
            self.active_windows[window_name] += 1

    def get_most_used_window(self):
        if self.active_windows:
            most_used_window = max(self.active_windows, key=self.active_windows.get)
            for app_name, exe_name in self.known_apps.items():
                if exe_name in most_used_window:
                    return app_name
        return "No active window"

class HomeWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.ui = Ui_MainHomePage()
        self.ui.setupUi(self)

        self.username = username
        self.ui.UsernameInput.setText(self.username)
        self.switch_windows_count = 0
        self.copy_paste_count = 0
        self.last_click_time = 0
        self.click_delay = 0.1  # Adjust the delay as needed (in seconds)

        self.window_monitor_thread = WindowMonitorThread()
        self.window_monitor_thread.window_updated.connect(self.update_most_used_software)
        self.window_monitor_thread.start()

        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

        self.ui.KeyCapButton.setChecked(False)

        self.hotkey_thread = HotkeyThread()
        self.hotkey_thread.start()

        self.hotkey_active = False
        self.hotkey_sequence = []
        self.executable_path = ""
        self.settings_file = APP_SETTINGS['settings_file']
        self.load_settings()

        self.ui.BindHotkey_Button.clicked.connect(self.ask_for_keys)
        self.ui.Add_ExeorFile_Button.clicked.connect(self.select_executable)

        self.app_detection_thread = AppDetectionThread()
        self.app_detection_thread.app_detected.connect(self.showOverlay)
        self.app_detection_thread.start()

        self.init_shortcut_monitoring()

        self.shortcut_counts = defaultdict(int)
        self.ui.Min5Button.clicked.connect(lambda: self.set_timer(5))
        self.ui.Min10Button.clicked.connect(lambda: self.set_timer(10))
        self.ui.Min30Button.clicked.connect(lambda: self.set_timer(30))
        self.ui.Min60Button.clicked.connect(lambda: self.set_timer(60))
        self.ui.StartButton.clicked.connect(self.start_timer)
        self.ui.StopButton.clicked.connect(self.stop_timer)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.remaining_time = QTime(0, 0, 0)
        self.is_timer_mode = False
        self.is_running = False

        self.ui.NotificationCheckBox.clicked.connect(self.update_notification_state)
        self.ui.DisableSoftwareOverlayCheckBox.clicked.connect(self.update_overlay_state)

    def update_most_used_software(self, window_name):
        self.ui.MostUsedSoftwareInput.setText(window_name)

    def init_shortcut_monitoring(self):
        self.monitoring_thread = threading.Thread(target=self.monitor_shortcuts)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()
        
    def set_timer(self, minutes):
        self.remaining_time = QTime(0, minutes, 0)
        self.ui.Starttimer00.setText(self.remaining_time.toString("hh:mm:ss"))
        self.is_timer_mode = True

    def start_timer(self):
        if not self.is_running:
            self.timer.start(1000 if self.is_timer_mode else 10)
            self.is_running = True

    def stop_timer(self):
        if self.is_running:
            self.timer.stop()
            self.show_notification()
            self.is_running = False
        else:
            self.reset_timer()

    def reset_timer(self):
        self.remaining_time = QTime(0, 0, 0)
        if self.is_timer_mode:
            self.ui.Starttimer00.setText(self.remaining_time.toString("hh:mm:ss"))
        else:
            self.ui.label_10.setText(self.remaining_time.toString("hh:mm:ss.zzz"))

    def update_time(self):
        if self.is_timer_mode:
            self.remaining_time = self.remaining_time.addSecs(-1)
            if self.remaining_time <= QTime(0, 0, 0):
                self.timer.stop()
                self.show_notification()
                self.is_running = False
            self.ui.Starttimer00.setText(self.remaining_time.toString("hh:mm:ss"))
        else:
            self.remaining_time = self.remaining_time.addMSecs(10)
            self.ui.label_10.setText(self.remaining_time.toString("hh:mm:ss.zzz"))

    def show_notification(self):
        if not self.ui.NotificationCheckBox.isChecked():
            notif = Notification(app_id="ShortKi",
                                 title="Timer / StopWatch finished!",
                                 msg="Let's see your results!",
                                 duration="long")
            notif.set_audio(audio.Default, loop=False)
            notif.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition().toPoint() - self.oldPos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()

    def monitor_shortcuts(self):
        shortcuts = APP_SETTINGS['shortcuts']

        for shortcut in shortcuts:
            keyboard.add_hotkey(shortcut, lambda sc=shortcut: self.on_shortcut(sc))

        keyboard.wait()

    def on_shortcut(self, shortcut):
        self.shortcut_counts[shortcut] += 1
        self.update_shortcut_usage_display()
    
    def update_shortcut_usage_display(self):
        QMetaObject.invokeMethod(self, "update_labels", Qt.QueuedConnection)

    @Slot()
    def update_labels(self):
        self.ui.numOfKeyboardShortcutInput.setText(str(len(self.shortcut_counts)))

        if self.shortcut_counts:
            most_used = max(self.shortcut_counts, key=self.shortcut_counts.get)
            self.ui.MostUsedKeyboardShortcutInput.setText(f"{most_used} used {self.shortcut_counts[most_used]} times")

    def ask_for_keys(self):
        QMessageBox.information(self, "Bind Hotkey", "After closing this message, press three keys to bind as a hotkey.")
        QTimer.singleShot(500, self.capture_hotkey)

    def capture_hotkey(self):
        self.hotkey_sequence = []
        logging.info("Please press three keys for the hotkey binding...")

        for i in range(3):
            event = keyboard.read_event()
            self.hotkey_sequence.append(event.name)

        hotkey_str = '+'.join(self.hotkey_sequence)
        logging.info(f"Hotkey set to: {hotkey_str}")
        keyboard.add_hotkey(hotkey_str, self.launch_exe)
        self.save_settings()

    def select_executable(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)")
        if file_path:
            self.executable_path = file_path
            self.save_settings()

            QMessageBox.information(self, "File Selected", f"Selected file: {file_path}")

    def save_settings(self):
        settings = {
            "hotkey": '+'.join(self.hotkey_sequence),
            "executable_path": self.executable_path
        }
        with open(self.settings_file, "w") as file:
            json.dump(settings, file)

    def load_settings(self):
        self.update_settings()

    def update_settings(self):
        try:
            with open(APP_SETTINGS['settings_file'], 'r') as file:
                settings = json.load(file)
                hotkey = settings.get('hotkey', 'Bind Keys')
        except Exception as e:
            logging.error(f"Error loading settings: {e}")

    def set_hotkey(self, hotkey):
        if self.hotkey_active:
            keyboard.unhook_all_hotkeys()
        self.hotkey = hotkey
        keyboard.add_hotkey(self.hotkey, self.launch_exe)
        self.hotkey_active = True

    def launch_exe(self):
        if self.executable_path:
            try:
                subprocess.Popen(self.executable_path, shell=True)
            except OSError as e:
                if e.winerror == 740:
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, self.executable_path, None, 1)
                else:
                    raise
        else:
            QMessageBox.warning(self, "Executable Not Found", "Please select an executable file to launch.")

    def launch_file(self):
        if self.executable_path:
            try:
                os.startfile(self.executable_path)
            except OSError as e:
                QMessageBox.critical(self, "Error", f"Could not open the file: {e}")

    def showOverlay(self, app_name):
        if not self.ui.NotificationCheckBox.isChecked() and not self.ui.DisableSoftwareOverlayCheckBox.isChecked():
            overlay_classes = {
                "Word": WordOverlayWindow,
                "PowerPoint": PowerPointOverlayWindow,
                "Excel": ExcelOverlayWindow,
                "Browser": BrowserOverlayWindow
            }
            if app_name in overlay_classes:
                self.overlay = overlay_classes[app_name]()
                self.overlay.show()

    def center_on_screen(self, window):
        screen = QGuiApplication.primaryScreen().geometry()
        window.move((screen.width() - window.frameSize().width()) / 2,
                    (screen.height() - window.frameSize().height()) / 2)

    def update_notification_state(self):
        if self.ui.NotificationCheckBox.isChecked():
            if hasattr(self, 'notification_thread') and self.notification_thread.is_alive():
                self.notification_thread.stop()
                self.notification_thread.join()
        else:
            if not hasattr(self, 'notification_thread') or not self.notification_thread.is_alive():
                self.notification_thread = NotificationThread()
                self.notification_thread.start()

    def update_overlay_state(self):
        if self.ui.DisableSoftwareOverlayCheckBox.isChecked():
            if hasattr(self, 'overlay') and self.overlay is not None:
                self.overlay.close()
                self.overlay = None

    def on_click(self, x, y, button, pressed):
        if pressed:
            current_time = time.time()
            if current_time - self.last_click_time >= self.click_delay:
                self.last_click_time = current_time

                try:
                    # Initialize COM for the current thread
                    initializer = auto.UIAutomationInitializerInThread()
                    element = auto.ControlFromPoint(x, y)
                    if element:
                        print(f"Clicked on element: {element.Name}, Control Type: {element.ControlType}")
                        if element.Name and element.Name.lower() in ["copy", "paste", "paste ctrl+v", "copy ctrl+c"]:
                            print(f"Clicked on {element.Name}")
                            self.copy_paste_count += 1
                            if self.copy_paste_count == 6:
                                self.send_notification()
                                self.copy_paste_count = 0  # Reset the count after sending the notification

                        application_names = ["google chrome", "word", "powerpoint", "excel"]
                        if element.Name and isinstance(element.Name, str):
                            for app_name in application_names:
                                if app_name in element.Name.lower():
                                    self.switch_windows_count += 1  # Use the instance attribute
                                    if self.switch_windows_count == 6:
                                        self.switch_window_notif()
                                        self.switch_windows_count = 0  # Reset the count after sending the notification
                                    break

                except Exception as e:
                    print(f"Error occurred: {str(e)}")
                finally:
                    # Uninitialize COM for the current thread
                    initializer.Uninitialize()

    def send_notification(self):
        # Create a notification with a title and a message
        notif = Notification(app_id="ShortKi", title="Use these shortcuts to make your life easy!", icon=r"C:\Users\PRSR\Documents\ShortKi Capstone march 26\src\images\keycap.jpg", duration="long")
        
        # Set an audio alert for the notification (optional)
        notif.set_audio(audio.Default, loop=False)
        
        # Add an action button (optional)
        notif.add_actions(label="Ctrl+C and Ctrl+V", launch="")
        
        # Show the notification
        notif.show()

    def switch_window_notif(self):
        # Create a notification with a title and a message
        notif = Notification(app_id="ShortKi", title="Use these shortcuts to make your life easy!",
                            icon=r"C:\\Users\\PRSR\\Documents\\ShortKi Capstone march 26\\src\\images\\keycap.jpg",
                            duration="long")
        # Set an audio alert for the notification (optional)
        notif.set_audio(audio.Default, loop=False)
        # Add an action button (optional)
        notif.add_actions(label="Alt+Tab", launch="")
        # Show the notification
        notif.show()

    def closeEvent(self, event):
        feedback_window = FeedbackWindow(self.username)
        result = feedback_window.exec()
        keyboard.unhook_all_hotkeys()
        self.hotkey_thread.terminate()

        self.app_detection_thread.stop()
        self.app_detection_thread.wait()

        self.listener.stop()

        if self.hotkey_active:
            keyboard.unhook_all_hotkeys()
            self.hotkey_active = False
        super().closeEvent(event)
        event.accept()


class WordOverlayWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WordOverlay()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.show()


class PowerPointOverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PowerPointOverlay()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.show()


class BrowserOverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Browser()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.show()


class ExcelOverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ExcelOverlay()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.show()


class FeedbackWindow(QDialog):
    def __init__(self, username, parent=None):
        super().__init__(parent)
        self.ui = Ui_Feedback()
        self.ui.setupUi(self)
        self.setFixedSize(710,350)
        self.ui.submit_button.clicked.connect(self.submit_feedback)
        self.username = username

    def submit_feedback(self):
        feedback = self.ui.response_bar.text()
        if feedback:
            with open(APP_SETTINGS['feedback_file'], "a") as file:
                file.write(f"Username: {self.username}\n")
                file.write(f"Feedback: {feedback}\n")
                file.write("\n")
            self.ui.response_bar.clear()
            QMessageBox.information(self, "Feedback Submitted", "Thank you for your feedback!")
            self.close()
        else:
            QMessageBox.warning(self, "Empty Feedback", "Please enter your feedback before submitting.")

    def reject(self):
        super().reject()


if __name__ == "__main__":
    app = QApplication([])
    create_database()
    splash_screen = SplashScreen()
    splash_screen.show()
    app.exec()