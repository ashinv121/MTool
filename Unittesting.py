import unittest
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from MTool import ConnectionSettingsWindow, open_project, save_as_project


class TestConnectionSettings(unittest.TestCase):
    
    def setUp(self):
        self.root = tk.Tk()
        self.app = ConnectionSettingsWindow(self.root)
        
    def tearDown(self):
        self.root.destroy()
        
    def test_initial_state(self):
        # Example: Check initial state of widgets or variables
        self.assertEqual(self.app.connection_type.get(), "Serial")
        self.assertEqual(self.app.com_port.get(), "COM1")
        # Add more assertions as needed
        
    def test_validations(self):
        # Example: Test validation methods
        self.assertTrue(self.app.validate_ip_adr("192.168.1.1"))
        self.assertFalse(self.app.validate_ip_adr("invalid_ip"))
        # Add more validation tests
        
    def test_file_operations(self):
        # Example: Test file operations
        # Mock file dialog operations using unittest.mock or simulate file operations
        pass
        
    # Add more test cases for specific functionality
    
if __name__ == '__main__':
    unittest.main()

