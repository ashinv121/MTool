import tkinter as tk
from tkinter import ttk, messagebox
import re
from modules import project_file_management

class ConnectionSettingsWindow:

    def __init__(self, parent, connection_type_string):
        self.parent = parent
        self.conn_screen = tk.Toplevel()
        self.conn_screen.title("Connection Setting")
        self.conn_screen.resizable(False, False)
        self.connection_type_string=connection_type_string

        default={
                    "Connection type": "Serial",
                    "COM port": "Com6",
                    "Baud rate": "9600 baud",
                    "Parity option": "None Parity",
                    "Stop bit option": "1 Stop Bit",
                    "Mode RTU": 1,
                    "Mode ASCII": 0,
                    "Ip address": "192.168.3.250",  
                    "Port": 502,
                    "connection timeout":100,
                    "Response timeout": 100,
                    "Delay between polls": 100
                    }


        if self.connection_type_string == "Default":
                self.connection_type_string = default
        elif self.connection_type_string["Connection type"] == "Serial":
            self.connection_type_string.update({
                "Ip address": "192.168.3.250",  
                "Port": 502,
                "connection timeout":100,
                })
        elif self.connection_type_string["Connection type"] == "Modbus TCP":
             self.connection_type_string.update({
                 "COM port": "Com6",
                    "Baud rate": "9600 baud",
                    "Parity option": "None Parity",
                    "Stop bit option": "1 Stop Bit",
                    "Mode RTU": 1,
                    "Mode ASCII": 0,
             })

        elif self.connection_type_string["Connection type"] == "Modbus UDP":
            self.connection_type_string.update({
                 "COM port": "Com6",
                    "Baud rate": "9600 baud",
                    "Parity option": "None Parity",
                    "Stop bit option": "1 Stop Bit",
                    "Mode RTU": 1,
                    "Mode ASCII": 0,
                    "connection timeout":100,
             })


        # Center the connection settings screen
        self.parent.update_idletasks()
        x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - (308 // 2)
        y = self.parent.winfo_y() + (self.parent.winfo_height() // 2) - (335 // 2)
        self.conn_screen.geometry(f"+{x}+{y}")
    
        # Style configuration
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 10))
        style.configure('TLabel', font=('Helvetica', 10))
        style.configure('TCombobox', font=('Helvetica', 10))
        
        # Connection type frame
        self.frame1 = ttk.Frame(self.conn_screen, borderwidth=2, relief="groove", padding="2 2 2 2")
        self.frame1.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.frame1, text="Connection Type:").grid(row=0, column=0, columnspan=2, padx=2, pady=2)
        
        self.connection_type = tk.StringVar(value=self.connection_type_string["Connection type"])
        values = ["Serial", "Modbus TCP", "Modbus UDP"]
        self.connection_type_combobox = ttk.Combobox(self.frame1, values=values, state='readonly', textvariable=self.connection_type)
        self.connection_type_combobox.grid(row=1, column=0, columnspan=2, padx=2, pady=2)
        self.connection_type_combobox.bind('<<ComboboxSelected>>', self.update_settings_state)
        
        # Button frame
        self.frame2 = ttk.Frame(self.conn_screen, borderwidth=2, relief="groove")
        self.frame2.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.rowconfigure(0, weight=1)
        ttk.Button(self.frame2, text="OK", width=15, command=self.on_ok).grid(row=0, column=0, padx=5, pady=2, sticky="nsew")
        ttk.Button(self.frame2, text="CANCEL", width=15, command=self.conn_screen.destroy).grid(row=1, column=0, padx=5, pady=2, sticky="nsew")
        
        # Serial settings frame
        self.frame3 = ttk.Frame(self.conn_screen, borderwidth=2, relief="groove", padding="2 2 2 2")
        self.frame3.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.frame3, text="Serial Setting:", justify="left").grid(row=0, column=0, columnspan=2, padx=2, pady=2)
        
        com_ports = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]
        self.com_port = tk.StringVar(value=self.connection_type_string["COM port"])
        self.com_port_combobox = ttk.Combobox(self.frame3, values=com_ports, state='readonly', textvariable=self.com_port, width=20)
        self.com_port_combobox.grid(row=1, column=0, columnspan=2, padx=2, pady=2)
        
        baud_rates = ["2400 baud", "4800 baud", "9600 baud", "19200 baud", "38400 baud", "57600 baud", "115200 baud"]
        self.baud_rate = tk.StringVar(value=self.connection_type_string["Baud rate"])
        self.baud_rate_combobox = ttk.Combobox(self.frame3, values=baud_rates, state='readonly', textvariable=self.baud_rate, width=20)
        self.baud_rate_combobox.grid(row=2, column=0, columnspan=1, padx=2, pady=2)
        
        parity_options = ["None parity", "Even parity", "Odd parity"]
        self.parity_option = tk.StringVar(value=self.connection_type_string["Parity option"])
        self.parity_option_combobox = ttk.Combobox(self.frame3, values=parity_options, state='readonly', textvariable=self.parity_option, width=20)
        self.parity_option_combobox.grid(row=3, column=0, columnspan=1, padx=2, pady=2)
        
        stopbit_options = ["1 Stop Bit", "2 Stop Bit"]
        self.stopbit_option = tk.StringVar(value=self.connection_type_string["Stop bit option"])
        self.stopbit_option_combobox = ttk.Combobox(self.frame3, values=stopbit_options, state='readonly', textvariable=self.stopbit_option, width=20)
        self.stopbit_option_combobox.grid(row=4, column=0, columnspan=1, padx=2, pady=2)
        
        # Mode settings frame
        self.frame4 = ttk.Frame(self.conn_screen, borderwidth=2, relief="groove", padding="2 2 2 2")
        self.frame4.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")
        
        self.frame4_1 = ttk.Frame(self.frame4, borderwidth=2, relief="groove")
        self.frame4_1.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.frame4_1, text="Mode").grid(row=0, column=0, rowspan=2, padx=2, pady=2)
        
        self.mode_rtu = tk.IntVar(value=self.connection_type_string.get("Mode RTU",0))
        self.mode_ascii = tk.IntVar(value=self.connection_type_string.get("Mode ASCII",0))
        self.mode_rtu_chk_btn = ttk.Checkbutton(self.frame4_1, text="RTU", variable=self.mode_rtu)
        self.mode_rtu_chk_btn.grid(row=0, column=1, padx=2, pady=2, sticky="w")
        self.mode_ascii_chk_btn = ttk.Checkbutton(self.frame4_1, text="ASCII", variable=self.mode_ascii)
        self.mode_ascii_chk_btn.grid(row=1, column=1, padx=2, pady=2, sticky="w")
        
        self.frame4_2 = ttk.Frame(self.frame4, borderwidth=2, relief="groove")
        self.frame4_2.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.frame4_2, text="Response Timeout").grid(row=0, column=0, columnspan=2, padx=2, pady=2)
        self.response_timeout = tk.IntVar(value=self.connection_type_string["Response timeout"])
        self.response_timeout_entry=ttk.Entry(self.frame4_2, textvariable=self.response_timeout, width=10)
        self.response_timeout_entry.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.frame4_2, text="[ms]").grid(row=1, column=1, padx=2, pady=2)
        
        self.frame4_3 = ttk.Frame(self.frame4, borderwidth=2, relief="groove")
        self.frame4_3.grid(row=2, column=0, padx=2, pady=2, sticky="nsew")
        ttk.Label(self.frame4_3, text="Delay Between Polls").grid(row=0, column=0, columnspan=2, padx=2, pady=2)
        self.delay_between_polls = tk.IntVar(value=self.connection_type_string["Delay between polls"])
        self.poll_number_entry=ttk.Entry(self.frame4_3, textvariable=self.delay_between_polls, width=10)
        self.poll_number_entry.grid(row=1, column=0, padx=2, pady=2,sticky="nsew")
        ttk.Label(self.frame4_3, text="[ms]").grid(row=1, column=1, padx=2, pady=2)
        
        # Modbus TCP/UDP settings frame
        self.frame5 = ttk.Frame(self.conn_screen, borderwidth=2, relief="groove", padding="2 2 2 2")
        self.frame5.grid(row=2, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")
        
        ttk.Label(self.frame5, text="Modbus TCP/UDP Setting").grid(row=0, column=0, columnspan=3, padx=2, pady=2)
        
        ttk.Label(self.frame5, text="IP Address").grid(row=1, column=0, padx=2, pady=2)
        self.ip_address = tk.StringVar(value=self.connection_type_string["Ip address"])
        self.ip_address_entry=ttk.Entry(self.frame5, textvariable=self.ip_address, width=20)
        self.ip_address_entry.grid(row=2, column=0, padx=2, pady=2)
        
        ttk.Label(self.frame5, text="Port").grid(row=1, column=1, padx=2, pady=2)
        self.port = tk.IntVar(value=self.connection_type_string["Port"])
        self.port_entry=ttk.Entry(self.frame5, textvariable=self.port, width=10)
        self.port_entry.grid(row=2, column=1, padx=2, pady=2)
        
        ttk.Label(self.frame5, text="Con Timeout").grid(row=1, column=2, padx=2, pady=2)
        self.con_timeout = tk.IntVar(value=self.connection_type_string["connection timeout"])
        self.con_timeout_entry=ttk.Entry(self.frame5, textvariable=self.con_timeout, width=10)
        self.con_timeout_entry.grid(row=2, column=2, padx=2, pady=2)
        self.update_settings_state()

        #Enter and ESC button for Connection screen.
        self.conn_screen.bind("<Return>", lambda event: self.on_ok())
        self.conn_screen.bind("<Escape>", lambda event: self.conn_screen.destroy())

        self.conn_screen.grab_set()

        
    
    def update_settings_state(self, event=None):
        connection_type = self.connection_type.get()
        
        # Serial settings state
        serial_state = 'normal' if connection_type == "Serial" else 'disabled'
        self.com_port_combobox.config(state=serial_state)
        self.baud_rate_combobox.config(state=serial_state)
        self.parity_option_combobox.config(state=serial_state)
        self.stopbit_option_combobox.config(state=serial_state)
        self.mode_rtu_chk_btn.config(state=serial_state)
        self.mode_ascii_chk_btn.config(state=serial_state)

        # Modbus TCP/UDP settings state
        modbus_tcp_state = 'normal' if connection_type == "Modbus TCP" else 'disabled'
        modbus_udp_state = 'normal' if connection_type == "Modbus UDP" else 'disabled'
        self.ip_address_entry.config(state='normal' if connection_type in ["Modbus TCP", "Modbus UDP"] else 'disabled')
        self.port_entry.config(state='normal' if connection_type in ["Modbus TCP", "Modbus UDP"] else 'disabled')
        self.con_timeout_entry.config(state=modbus_tcp_state)
    
    def validate_ip_adr(self, ip):
        pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$")
        return pattern.match(ip)

    def validate_port_number(self, port_str):
        try:
            port = int(port_str)
            if not (1 <= port <= 65535):
                return False, "Port number must be between 1 and 65535."
            return True, ""
        except ValueError:
            return False, "Please enter a valid integer for the port number."

    def validate_response_timeout_setting(self, timeout_ms):
        try:
            timeout_ms = int(timeout_ms)
            if not (50 <= timeout_ms <= 10000):
                return False, "Response timeout must be between 50 and 10000."
            return True, ""
        except ValueError:
            return False, "Please enter a valid integer for the Response timeout."

    def validate_poll_setting(self, time_ms):
        try:
            time_ms = int(time_ms)
            if not (0 <= time_ms <= 10000):
                return False, "Poll time must be between 100 and 10000."
            return True, ""
        except ValueError:
            return False, "Please enter a valid integer for the Poll time."

    def validate_connection_timeout_setting(self, timeout_ms):
        try:
            timeout_ms = int(timeout_ms)
            if not (50 <= timeout_ms <= 10000):
                return False, "Connection timeout must be between 50 and 10000."
            return True, ""
        except ValueError:
            return False, "Please enter a valid integer for the Connection timeout."

    def on_ok(self):

        connection_type = self.connection_type.get()
        valid, error_message = self.validate_response_timeout_setting(self.response_timeout_entry.get())
        if not valid:
            tk.messagebox.showerror("Invalid Response Timeout", error_message)
            return
            
        valid, error_message = self.validate_poll_setting(self.poll_number_entry.get())
        if not valid:
                tk.messagebox.showerror("Invalid Poll Setting", error_message)
                return              
        # Implement the logic to handle the OK button click event
        if connection_type == "Serial":
            
            self.connection_data={"Connection type":"Serial",
            "COM port": self.com_port.get(),
            "Baud rate": self.baud_rate.get(),
            "Parity option": self.parity_option.get(),
            "Stop bit option": self.stopbit_option.get(),
            "Mode RTU":self.mode_rtu.get(),
            "Mode ASCII":self.mode_ascii.get(),
            "Response timeout": self.response_timeout.get(),
            "Delay between polls": self.delay_between_polls.get()
            }
            
        elif connection_type in ["Modbus TCP", "Modbus UDP"]:
            if not self.validate_ip_adr(self.ip_address_entry.get()):
                tk.messagebox.showerror("Invalid IP", "Please enter a valid IP address.")
                return
            valid, error_message = self.validate_port_number(self.port_entry.get())
            if not valid:
                tk.messagebox.showerror("Invalid Port Number", error_message)
                return
            self.connection_data={
                    "Connection type":"Modbus UDP",
                    "Ip address" :self.ip_address_entry.get(),
                    "Port":self.port_entry.get(),
                    "Response timeout": self.response_timeout.get(),
                    "Delay between polls": self.delay_between_polls.get()
                    }
            if  connection_type == "Modbus TCP":
                valid, error_message = self.validate_connection_timeout_setting(self.con_timeout_entry.get())
                if not valid:
                    tk.messagebox.showerror("Invalid Poll Setting", error_message)
                    return
                self.connection_data["Connection type"]="Modbus TCP"
                self.connection_data["connection timeout"]=self.con_timeout_entry.get()
          
        self.conn_screen.destroy()

    def get_connection_data(self):
        return self.connection_data
