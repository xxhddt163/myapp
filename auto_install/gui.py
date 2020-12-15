from os import getcwd
from os.path import join
from os import listdir
from pyautogui import click, press, locateOnScreen, hotkey
from time import sleep
import pyperclip
import cv2

"""只能用pyautogui安装的程序通用模块"""


def gui_run(app_name: str, key_index: int, confid: float or int, sleep_time: int = 5) -> bool:
    """
    :param app_name: APP名称
    :param key_index: 第几张截图为安装路径截图（截图编号从0开始）
    :param confid: 匹配图片的精度
    :param sleep_time: 匹配一轮下来找不到匹配项等待多少秒
    :return: 找到指定按钮返回True 反之返回False
    """

    path = join(getcwd(), "app_pkg", app_name + "_shot")  # png文件所在目录
    png_list = listdir(path)  # png文件列表
    index = 0
    count = 0
    for each in png_list:
        while count < 20:
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
