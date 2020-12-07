from os import getcwd
from os.path import join
from os import listdir
from pyautogui import click, press, locateOnScreen, hotkey
from time import sleep
import pyperclip

"""只能用pyautogui安装的程序通用模块"""


def gui_run(app_name, key_index, confid):
    """app_name: 程序名称
       key_value: 编辑栏，非按钮"""

    path = join(getcwd(), "app_pkg", app_name + "_shot")  # png文件所在目录
    png_list = listdir(path)  # png文件列表
    count = 0
    for each in png_list:
        while True:
            if locateOnScreen(join(path, each), confidence=confid) is not None:
                left, top, width, height = locateOnScreen(join(path, each), confidence=confid)
                x, y = left + width // 2, top + height // 2
                if count == key_index:
                    click(x, y)
                    press('home')
                    press('delete')
                    press('left')
                    pyperclip.copy('d')
                    hotkey('ctrl', 'v')
                else:
                    click(x, y)
                break
            else:
                sleep(5)
                continue
        count += 1
