from os import getcwd
from os.path import join
from os import listdir
import pyautogui
from time import sleep
import cv2

# 通过截图模拟键盘鼠标让office只安装3个主要程序
"""path: 截图文件所在路径
   png_list: 所有截图"""


def choose_menu():
    path = join(getcwd(), "app_pkg", "OFFICE2013_shot")
    png_list = listdir(path)
    count = 0
    for each in png_list:
        while count < 10:
            if pyautogui.locateOnScreen(join(path, each), confidence=0.9) is not None:
                left, top, width, height = pyautogui.locateOnScreen(join(path, each), confidence=0.9)
                x, y = left + width // 2, top + height // 2
                pyautogui.rightClick(x, y)
                pyautogui.hotkey('n')
                count = 0
                break
            else:
                sleep(2)
                count += 1
                continue
    if count < 10:
        return True
    else:
        return False
