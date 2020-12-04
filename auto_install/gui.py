import os
import pyautogui
import time

"""只能用pyautogui安装的程序通用模块"""


def gui_run(app_name, key_index):
    """app_name: 程序名称
       key_value: 编辑栏，非按钮"""

    path = os.getcwd() + "\\" + app_name + "_shot" + "\\"  # png文件所在目录
    png_list = os.listdir(path)  # png文件列表
    count = 0
    for each in png_list:
        while True:
            if pyautogui.locateCenterOnScreen(path + each) is not None:
                x, y = pyautogui.locateCenterOnScreen(path + each)  # 获取按钮所在坐标中心位置
                if count == key_index:
                    pyautogui.tripleClick(x, y)
                    time.sleep(0.5)
                    pyautogui.typewrite("D:\Program Files" + "\\" + app_name)
                else:
                    pyautogui.click(x, y)
                break
            else:
                continue
        count += 1
