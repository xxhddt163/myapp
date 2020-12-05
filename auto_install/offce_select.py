from os import getcwd
from os.path import join
from os import listdir
import pyautogui

# 通过截图模拟键盘鼠标让office只安装3个主要程序
"""path: 截图文件所在路径
   png_list: 所有截图"""


def choose_menu():
    path = join(getcwd(), "app_pkg", "office_shot")
    png_list = listdir(path)
    for each in png_list:
        while True:
            if pyautogui.locateCenterOnScreen(join(path, each)) is not None:
                x, y = pyautogui.locateCenterOnScreen(join(path, each))  # 获取按钮所在坐标中心位置
                pyautogui.rightClick(x, y)
                pyautogui.hotkey('alt', 'n')
                break
            else:
                continue
