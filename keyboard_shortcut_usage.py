import keyboard
from collections import defaultdict
import json

# Dictionary to hold the count of each shortcut
shortcut_counts = defaultdict(int)

# Define the shortcuts you want to monitor
shortcuts = {
    "ctrl+c": "Copy",
    "ctrl+v": "Paste",
    "ctrl+x": "Cut",
    "alt+tab": "Switch windows",
    "win+x": "Quick Link Menu",
    "ctrl+y": "Redo",
    "ctrl+z": "Undo",
    "ctrl+shift+n": "Create New Folder / Incognito",
    "ctrl+shift+esc": "Task Manager",
    "shift+win+s": "Screen Shot",
    "ctrl+i": "Apply Italic",
    "ctrl+u": "Apply Underline",
    "ctrl+b": "Apply Bold",
    "ctrl+e": "Center Text",
    "ctrl+n": "Create new document / presentation / window",
    "ctrl+s": "Save",
    "ctrl+]": "Increase font size",
    "ctrl+[": "Decrease font size",
    "ctrl+j": "Justify text",
    "ctrl+f1": "Toggle Ribbon",
    "ctrl+m": "Add a new slide in PPT",
    "f5": "Start presentation in PPT",
    "ctrl+d": "Duplicate object in PPT / Bookmark current page",
    "ctrl+g": "Group object in PPT",
    "ctrl+t": "Open new tab",
    "ctrl+w": "Close current tab",
    "ctrl+tab": "Switch to the next tab",
    "ctrl+shift+tab": "Switch to the previous tab",
    "ctrl+shift+t": "Reopen the last closed tab",
    "ctrl+l": "Focus the address bar",
    "ctrl+h": "Open history",
    "ctrl+a": "Select all",

    # Add more shortcuts here
}

# Callback function to increment the count and save to a file
def on_shortcut(shortcut):
    global shortcut_counts
    shortcut_counts[shortcut] += 1
    print(f"{shortcuts[shortcut]} used {shortcut_counts[shortcut]} times")
    save_to_json()

# Function to save the counts to a JSON file
def save_to_json():
    with open('shortcut_usage.json', 'w') as json_file:
        json.dump(shortcut_counts, json_file, indent=4)

# Hook to the keyboard events
for shortcut in shortcuts:
    keyboard.add_hotkey(shortcut, on_shortcut, args=[shortcut])

# Start an infinite loop to keep the script running
print("Monitoring keyboard shortcuts. Press ESC to stop.")
keyboard.wait('esc')

# Cleanup
keyboard.unhook_all_hotkeys()
print("Keyboard monitoring stopped. Shortcut counts have been saved to 'shortcut_usage.json'.")
