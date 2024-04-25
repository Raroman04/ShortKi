import json
import time
import datetime
import sys
import threading
import win32gui

# Define the applications and browsers to track
APPLICATIONS = ["Word", "PowerPoint", "Excel"]
BROWSERS = ["Brave", "Chrome", "Edge", "Firefox", "Opera GX"]

class TimeEntry:
    """Represents a time entry for an application."""
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = end_time - start_time

    def serialize(self):
        """Serializes the time entry to a JSON-compatible dictionary."""
        # Format start and end times in "Month-Day-Year Hour:Minute:Second AM/PM" format
        start_time_str = self.start_time.strftime("%m-%d-%Y %I:%M:%S %p")
        end_time_str = self.end_time.strftime("%m-%d-%Y %I:%M:%S %p")

        # Calculate hours, minutes, and seconds
        total_seconds = int(self.total_time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return {
            'start_time': start_time_str,
            'end_time': end_time_str,
            'Hour': hours,
            'Minute': minutes,
            'Second': seconds
        }


class Activity:
    """Represents an activity with one or more time entries."""
    def __init__(self, name):
        self.name = name
        self.time_entries = []

    def add_time_entry(self, time_entry):
        """Adds a time entry to the activity."""
        self.time_entries.append(time_entry)

    def serialize(self):
        """Serializes the activity to a JSON-compatible dictionary."""
        return {
            'name': self.name,
            'time_entries': [entry.serialize() for entry in self.time_entries]
        }

class ActivityList:
    """Manages a list of activities."""
    def __init__(self):
        self.activities = {}

    def add_activity(self, activity):
        """Adds an activity to the list."""
        if activity.name not in self.activities:
            self.activities[activity.name] = activity

    def add_time_entry(self, app_name, time_entry):
        """Adds a time entry to the specified activity, creating the activity if necessary."""
        if app_name not in self.activities:
            self.activities[app_name] = Activity(app_name)
        self.activities[app_name].add_time_entry(time_entry)

    def serialize(self):
        """Serializes the list of activities to a JSON-compatible dictionary."""
        return [activity.serialize() for activity in self.activities.values()]

    def save_to_file(self, filename='activities.json'):
        """Saves the serialized activity list to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(self.serialize(), file, indent=4)

class AppMonitor:
    """Monitors active applications and logs activity."""
    def __init__(self):
        self.activeList = ActivityList()
        self.active_app_name = ""
        self.start_time = datetime.datetime.now()
        self.stop_event = threading.Event()

    def monitor_activity(self):
        """Monitors the active window and logs activity until the stop event is set."""
        try:
            while not self.stop_event.is_set():
                window_title = get_active_window()
                app_name = get_application_name(window_title) if window_title else None

                if app_name and app_name != self.active_app_name:
                    end_time = datetime.datetime.now()
                    if self.active_app_name:
                        time_entry = TimeEntry(self.start_time, end_time)
                        self.activeList.add_time_entry(self.active_app_name, time_entry)
                        self.activeList.save_to_file()
                    self.start_time = end_time
                    self.active_app_name = app_name

                time.sleep(1)
        finally:
            if self.active_app_name:
                end_time = datetime.datetime.now()
                time_entry = TimeEntry(self.start_time, end_time)
                self.activeList.add_time_entry(self.active_app_name, time_entry)
            self.activeList.save_to_file()

    def start(self):
        """Starts the monitoring activity in a separate thread."""
        self.monitoring_thread = threading.Thread(target=self.monitor_activity)
        self.monitoring_thread.start()

    def stop(self):
        """Stops the monitoring activity."""
        self.stop_event.set()
        self.monitoring_thread.join()

def get_active_window():
    """Retrieves the title of the active window."""
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    return None

def get_application_name(window_title):
    """Determines the name of the application from the window title."""
    for app in APPLICATIONS:
        if app in window_title:
            return f"Microsoft {app}"
    for browser in BROWSERS:
        if browser in window_title:
            return "Web Browser"
    return None

if __name__ == "__main__":
    app_monitor = AppMonitor()
    app_monitor.start()
    print("App monitoring started. Press Ctrl+C to stop.")
    try:
        # Keep the script running until a keyboard interrupt is received
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping app monitoring...")
        app_monitor.stop()
        print("App monitoring stopped.")

