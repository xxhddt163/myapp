from pywinauto import Application
from pyautogui import locateOnScreen, click, tripleClick, hotkey
from time import sleep
from os import getcwd, listdir
from os.path import join
from pyperclip import copy, paste


def new_window_ready_title(title):
    """通过title名判断新的窗口是否连接成功"""
    while True:
        try:
            application = Application().connect(title_re=title)
            if application.top_window().wait("ready", timeout=20):
                return application
            else:
                sleep(3)
                continue
        except:
            continue


def crack_cad():
    cad = Application().start(r'D:\Program Files\Autodesk\AutoCAD 2014\acad.exe')
    cad.top_window().wait('ready', timeout=20)  # 打开CAD程序并检查是否就绪
    sleep(2)
    temp = new_window_ready_title('Autodesk 许可')
    temp.top_window().wait('ready', timeout=20)  # 检查许可程序是否就绪
    png_file = listdir(join(getcwd(), 'app_pkg', 'CAD2014_shot', 'step1'))

    for each in png_file:  # 点击许可协议到激活界面
        x, y = object_coord(join(getcwd(), 'app_pkg', 'CAD2014_shot', 'step1', each), x_add=0)
        if x and y:
            click(x, y)

    x, y = object_coord(join(getcwd(), 'app_pkg', 'CAD2014_shot', 'step2', '0.png'))  # 检测并复制申请号
    if x and y:
        tripleClick(x, y)
        hotkey('ctrl', 'c')
        key_soft = Application().start(join(getcwd(), 'app_pkg', 'CAD2014', 'crack', 'xf-adsk64'))
        key_soft.top_window().wait('ready', timeout=20)  # 打开CAD注册机并检测是否就绪
        key_soft.top_window()['Request :Edit'].set_text(paste())  # 将申请号粘贴进注册机
        sleep(2)
        key_soft.top_window()['CButton'].click_input()  # 按下注册机Patch按钮
        sleep(2)
        key_soft.top_window()['确定Button'].click_input()  # 按下注册机Patch按钮之后弹出的小窗口
        sleep(2)
        for temp in range(1):
            key_soft.top_window()['GButton'].click_input()  # 按下2次注册机Generate按钮
        dict_temp = key_soft.top_window()._ctrl_identifiers()
        for each in dict_temp.keys():  # 通过按钮便签值获取激活码
            if 'Activation :Edit' in dict_temp[each]:
                temp = str(each)
                key = temp.split("'")[1]
                copy(key)
                sleep(2)
        key_soft.top_window()['QQButton'].click_input()  # 按下注册机Quit按钮
        x, y = object_coord(join(getcwd(), 'app_pkg', 'CAD2014_shot', 'step2', '1.png'), x_add=0)  # 按下我具有激活码按钮
        if x and y:
            click(x, y)
            hotkey('ctrl', 'v')  # 粘贴激活码
            sleep(1)
            x, y = object_coord(join(getcwd(), 'app_pkg', 'CAD2014_shot', 'step2', '2.png'), x_add=0)  # 按下下一步按钮
            if x and y:
                click(x, y)
                x, y = object_coord(join(getcwd(), 'app_pkg', 'CAD2014_shot', 'step2', '3.png'),
                                    x_add=0)  # 按下完成按钮
                if x and y:
                    click(x, y)


def object_coord(png_path, x_add=200):
    """根据路径解析出路径内所有按钮png文件，并按下按钮"""
    count = 0
    while count < 10:
        if locateOnScreen(png_path) is not None:
            left, top, width, height = locateOnScreen(png_path)
            x, y = left + width // 2 + x_add, top + height // 2
            return x, y
        else:
            sleep(1)
            count += 1
    if count < 10:
        return True
    else:
        return False


if __name__ == '__main__':
    crack_cad()
