from pywinauto import Application
import time
import os

"""
QQ:
1："腾讯QQ安装向导" win32
2：title="自定义选项", class_name="Button"
3: title="添加到快速启动栏", class_name="Button"
4：title="开机自动启动", class_name="Button"
5：title="C:\Program Files (x86)\Tencent\QQ", class_name="Edit"
6: title="立即安装", class_name="Button"

微信：
1："微信安装向导" uia
2：title="安装微信"
3: title = "开始使用"
"""


class Setup:
    """自动安装软件"""

    def __init__(self):
        self.step = {"QQ": ["自定义选项",
                            "添加到快速启动栏",
                            "开机自动启动",
                            "C:\Program Files (x86)\Tencent\QQ",
                            "立即安装",
                            "完成安装"],
                     "微信": ["安装微信",
                            "开始使用"]}
        self.app = Application(backend='win32').start(r"C:\Users\admin\Desktop\soft\QQ.exe")
        self.main_window = ''
        self.main()

    def check_window(self, volume1):
        """检测窗口是否已经加载"""
        while True:
            if self.main_window.window(title=volume1).wait('ready', timeout=300):  # 等待指定按钮出现
                return self.main_window.child_window(title=volume1)
            time.sleep(1)

    def main(self):
        if self.app.window(title="腾讯QQ安装向导").wait('ready', timeout=300):  # 等待界面出现才执行
            self.main_window = self.app["腾讯QQ安装向导"]
            self.run()

    def run(self):
        """执行命令安装程序"""
        for each in self.step['QQ']:
            if ":" not in each:
                cache = self.check_window(each)
                cache.click_input()
            elif ":" in each:
                cache = self.check_window(each)
                cache.set_text(each.replace('C', 'D'))


if __name__ == '__main__':
    s = Setup()
