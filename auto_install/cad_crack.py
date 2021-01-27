import auto_install
from time import sleep
from pywinauto import Application
import gui
from pyautogui import locateOnScreen, tripleClick, hotkey, doubleClick, click
from os.path import join
from os import getcwd
import pyperclip
import cv2


def crack_cad():
    """破解CAD2014"""
    auto_install.desk_top()
    sleep(.5)
    cad = Application().start(r'D:\Program Files\Autodesk\AutoCAD 2014\acad.exe')  # 打开CAD程序
    path = join(getcwd(), "app_pkg", "CAD2014_shot")
    result = gui.gui_run(app_name='CAD2014', key_index=8, confid=9)  # 点击至激活界面
    if result:
        x, y = find_coord(path.join("5.png"), x_add=200)  # 复制申请号
        tripleClick(x, y)
        sleep(1)
        hotkey('ctrl', 'c')

        key_gen = Application().start(join(getcwd(), "app_pkg", "CAD2014", "crack", "key.exe"))  # 打开注册机
        sleep(3)
        key_gen.top_window()['Edit'].set_text(pyperclip.paste())  # 将申请号粘贴进注册机
        sleep(.5)
        key_gen.top_window()['CButton'].click_input()  # 按下注册机Patch
        sleep(2)
        key_gen.top_window()['Button'].click_input()  # 按下弹窗的确定
        sleep(1)
        key_gen.top_window()['GButton'].click_input()  # 按下Generate
        sleep(1)
        key_gen.top_window()['GButton'].click_input()

        x, y = find_coord(path.join("6.png"), x_add=200)
        doubleClick(x, y)
        sleep(1)
        hotkey('ctrl', 'c')  # 复制激活码
        key_gen.top_window()['QQButton'].click_input()  # 退出注册机
        x, y = find_coord(path.join("7.png"))
        click(x, y)
        sleep(1)
        x, y = find_coord(path.join("8.png"))
        click(x, y)
        sleep(1)
        pyperclip.paste()
        x, y = find_coord(path.join("9.png"))
        click(x, y)
        x, y = find_coord(path.join("10.png"))
        click(x, y)


def find_coord(png_path, x_add=0):
    for time in range(20):
        if locateOnScreen(png_path, confidence=9) is not None:
            left, top, width, height = locateOnScreen(png_path, confidence=9)
            x, y = left + width // 2 + x_add, top + height // 2
            return x, y
        else:
            continue
