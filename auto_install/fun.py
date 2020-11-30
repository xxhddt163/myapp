from pywinauto import Application
import time
import os


class Program:
    def __init__(self, program_path, program_name, program_type, main_window):
        """实例化应用对象，实例化主窗口文件"""
        self.app = Application(backend=program_type).start(program_path + "\\" + program_name)
        self.program_name = program_name
        while True:
            if self.app.window(title=main_window).wait("ready", timeout=300):
                self.main_window = self.app[main_window]
            time.sleep(1)

    def check_window(self, obj_name):
        """检测目标对象是否就绪"""
        if self.main_window.window(title_re=obj_name).wait("ready", timeout=300):
            self.main_window = self.main_window.child_window(title=obj_name)

    def button_click(self):
        """按下指定按钮"""
        self.main_window.click_input()

    def edit_text_win32(self):
        """编辑edit win32类程序"""
        path = r"D:\Program Files"
        self.main_window.set_text(path + "\\" + self.program_name)

    def edit_text_uia(self):
        path = r"D:\Program Files"
        self.main_window.click()
        time.sleep(.5)
        self.main_window.type_keys("%a")
        time.sleep(.5)
        self.main_window.type_keys(path + "\\" + self.program_name)


p = Program(os.getcwd(), "Wechat", "uia", "微信安装向导")
p.check_window()
