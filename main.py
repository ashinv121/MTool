import tkinter as tk
from tkinter import ttk 
from modules import project_file_management, ui

class MToolApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x900")
        self.root.minsize(350, 450)
        self.root.title("M Tool")
        
        self.connection1 = None
        self.last_connection_type = "Serial"  # Default connection type
        #self.create_menu()
        self.Scada=ui.Screenlayout(root)

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # File menu
        filemenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open', command=project_file_management.open_project)
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save As", command=self.save_as_project)
        filemenu.add_command(label='Exit', command=self.root.quit)
        
        # Home menu
        home=tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Home', menu=home)
        home.add_command(label="Connect", command=self.open_conn_st_screen)

        # Connection menu
        connectionmenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Connection', menu=connectionmenu)
        connectionmenu.add_command(label="Connect", command=self.open_conn_st_screen)
        connectionmenu.add_command(label="Disconnect")

        # Help menu
        helpmenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About')

    def open_conn_st_screen(self):
        if self.connection1 is None:
            self.last_connection_type="Default"
        else:
            self.last_connection_type=self.connection1.get_connection_data()
            print(self.last_connection_type)
        self.connection1 = ui.ConnectionSettingsWindow(self.root, self.last_connection_type)
        
    def get_connection_setting(self):
        if self.connection1 is not None:
            return self.connection1.get_connection_data()
        else:
            return None
        
    def save_as_project(self):
        data = self.get_connection_setting()
        if data is not None:
            project_file_management.save_as_project(data)

        else:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MToolApp(root)
    root.mainloop()