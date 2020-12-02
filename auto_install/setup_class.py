from pywinauto import Application
import time


class Program:
    def __init__(self, program_path, program_name, program_type, main_window):
        """实例化应用对象，实例化主窗口文件"""
        if program_name == "OFFICE2013" or program_name == "CAD2007":
            self.app = Application(backend=program_type).start(program_path + "\\" + program_name + "\\" + "setup")
        else:
            self.app = Application(backend=program_type).start(program_path + "\\" + program_name + "\\" + program_name)
        self.program_name = program_name
        self.main_window = main_window
        self.program_type = program_type
        while True:
            if self.app.window(title=main_window).wait("ready", timeout=300):
                self.main = self.app[main_window]
                break

    def check_window(self, obj_name, obj_class=""):
        """检测目标对象是否就绪"""
        if obj_class != "":
            if self.program_type == "win32":  # win32类型的程序检测
                if self.main.window(title_re=obj_name, class_name=obj_class).wait("ready", timeout=300):
                    self.main = self.app[self.main_window].child_window(title=obj_name, class_name=obj_class)
            elif self.program_type == "uia":  # uia类型
                if self.main.window(title_re=obj_name, control_type=obj_class).wait("ready", timeout=300):
                    self.main = self.app[self.main_window].child_window(title=obj_name, control_type=obj_class)
        elif obj_class == "":
            if self.main[obj_name].wait("ready", timeout=300):
                self.main = self.app[self.main_window][obj_name]

    def button_click(self):
        """按下指定按钮"""
        self.main.click_input()
        self.main = self.app[self.main_window]

    def main_edit(self):
        """编辑edit总执行程序"""
        if self.program_type == "win32":
            self.__edit_text_win32()
        elif self.program_type == "uia":
            self.__edit_text_uia()

    def __edit_text_win32(self):
        """编辑edit win32类程序"""
        path = r"D:\Program Files"
        self.main.set_text(path + "\\" + self.program_name)
        self.main = self.app[self.main_window]

    def __edit_text_uia(self):
        path = r"D:\Program Files"
        self.main.click_input()
        time.sleep(1)
        self.main.type_keys("^a")  # ctrl + a
        time.sleep(.5)
        self.main.type_keys(path + "\\" + self.program_name)
        self.main = self.app[self.main_window]
