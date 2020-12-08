from os import getcwd
from os.path import join
from os import listdir
from pyautogui import click, press, locateOnScreen, hotkey
from time import sleep
import pyperclip
import cv2

"""只能用pyautogui安装的程序通用模块"""


def gui_run(app_name, key_index, confid, sleep_time=5):
    """app_name: 程序名称
       key_value: 编辑栏，非按钮"""

    path = join(getcwd(), "app_pkg", app_name + "_shot")  # png文件所在目录
    png_list = listdir(path)  # png文件列表
    index = 0
    count = 0
    for each in png_list:
        while count < 10:
            if locateOnScreen(join(path, each), confidence=confid) is not None:
                left, top, width, height = locateOnScreen(join(path, each), confidence=confid)
                x, y = left + width // 2, top + height // 2
                if key_index == index:
                    click(x, y)
                    press('home')
                    press('delete')
                    press('left')
                    pyperclip.copy('d')
                    hotkey('ctrl', 'v')
                    count = 0
                else:
                    click(x, y)
                    count = 0
                break
            else:
                sleep(sleep_time)
                count += 1
                continue
        index += 1
    if count < 10:
        return True
    else:
        return False
