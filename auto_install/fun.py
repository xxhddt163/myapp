from pywinauto import Application
import time
from os import path


class Program:
    def __init__(self, program_path, program_name, program_type):
        self.app = Application(backend=program_type).start(program_path + "\\" + program_name)


p = Program(r"C:\Users\admin\Desktop\soft", "QQ", "win32")
pass
pass
