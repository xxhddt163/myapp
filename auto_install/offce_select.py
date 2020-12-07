from os import getcwd
from os.path import join
from os import listdir
import pyautogui
from time import sleep

# 通过截图模拟键盘鼠标让office只安装3个主要程序
"""path: 截图文件所在路径
   png_list: 所有截图"""


def choose_menu():
    path = join(getcwd(), "app_pkg", "office_shot")
    png_list = listdir(path)
    for each in png_list:
        while True:
            if pyautogui.locateOnScreen(join(path, each), confidence=0.7) is not None:
                left, top, width, height = pyautogui.locateOnScreen(join(path, each), confidence=0.9)
                x, y = left + width // 2, top + height // 2
                pyautogui.rightClick(x, y)
                pyautogui.hotkey('n')
                break
            else:
                sleep(1)
                continue