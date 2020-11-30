from pywinauto import Application
import time
import os


class Program:
    def __init__(self, program_path, program_name, program_type, main_window):
        """实例化应用对象，实例化主窗口文件"""
        self.app = Application(backend=program_type).start(program_path + "\\" + program_name)
        while True:
            if self.app.window(title=main_window).wait("ready", timeout=300):
                self.main_window = self.app[main_window]
            time.sleep(1)

    def check_window(self, obj_name):
        """检测目标对象是否就绪"""
        if self.main_window.window(title_re=obj_name).wait("ready", timeout=300):
            self.main_window = self.main_window.child_window(title=obj_name)


p = Program(os.getcwd(), "Wechat", "uia", "微信安装向导")
pass
pass
