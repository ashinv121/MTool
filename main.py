import tkinter as tk
from modules import project_file_management, ui
connection1=None

def open_conn_st_screen(parent):
   global connection1
   connection1 = ui.ConnectionSettingsWindow(parent)
   
def getconnection_setting():
   global connection1
   if connection1 is not None:
      return connection1.get_connection_data()
   else:
      return None
   
def save_as_project():
   data=getconnection_setting()
   print(data)
   if data is not None:
      project_file_management.save_as_project(data)
   else:
      pass

      
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
filemenu.add_command(label="Save As", command=lambda: save_as_project())
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
