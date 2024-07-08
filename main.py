import tkinter as tk
from modules import project_file_management, ui

def open_conn_st_screen(parent):
    ui.ConnectionSettingsWindow(parent)

def get_settings(parent):
    print(ui.ConnectionSettingsWindow(parent).get_connection_data())
    return ui.ConnectionSettingsWindow(parent).get_connection_data()
    
root = tk.Tk()
root.geometry("350x450")
root.minsize(350, 450)
root.title("M Tool")

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open', command=project_file_management.open_project)
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As", command=lambda: project_file_management.save_as_project(get_settings))
filemenu.add_command(label='Exit', command=root.quit)

# Connection menu
connectionmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Connection', menu=connectionmenu)
connectionmenu.add_command(label="Connect", command=lambda: open_conn_st_screen(root))
connectionmenu.add_command(label="Disconnect")

# Help menu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

root.mainloop()
