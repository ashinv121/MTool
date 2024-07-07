from tkinter import filedialog
import json

def save_project():
    pass

def save_as_project():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=(("Json Files", "*.json"), ("All Files", "*.*")),
        title="Save File"
    )
    if file_path:
        data = {"Name": "Mtool",
                "Version":1.0
                }
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print("File saved successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        print("Save operation cancelled.")

def open_project():
    try:
        file_path = filedialog.askopenfilename(
            filetypes=(("Json Files", "*.json"), ("All Files", "*.*")),
            title="Open File"
        )
        if file_path:
            with open(file_path, 'r') as file:
                data = json.load(file)
            print("File opened successfully.")
            return data
        else:
            print("Open operation cancelled.")
            return None
    except Exception as e:
        print(f"Error opening file: {e}")
        return None
