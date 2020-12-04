import os
import pyautogui

# 通过截图模拟键盘鼠标让office只安装3个主要程序
"""path: 截图文件所在路径
   png_list: 所有截图"""


def choose_menu():
    path = os.getcwd() + "\\" + "office_shot" + "\\"
    png_list = os.listdir(path)
    for each in png_list:
        while True:
            if pyautogui.locateCenterOnScreen(path + each, confidence=0.9) is not None:
                x, y = pyautogui.locateCenterOnScreen(path + each, confidence=0.9)  # 获取按钮所在坐标中心位置
                pyautogui.rightClick(x, y)
                pyautogui.hotkey('alt', 'n')
                break
            else:
                continue
