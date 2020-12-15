from datetime import datetime
from setup_class import Program
import os
from time import localtime, strftime, sleep
from pywinauto import Application
from easygui import textbox
import offce_select
from pyautogui import press, size, rightClick
import gui
from comtypes.gen.UIAutomationClient import *

start_time = (strftime("%H:%M", localtime()))
failure = []  # 保存安装失败的软件名称
os.system('netsh advfirewall set allprofiles state off')  # 关闭防火墙
os.system(
    'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /d 1 /t REG_DWORD /f')  # 关闭微软def杀毒
os.system('netsh interface ip set dns name="以太网" source=static addr=114.114.114.114')  # 修改DNS
os.system('netsh interface ip set dns name="WLAN" source=static addr=114.114.114.114')


def running_time(start, end):
    """计算程序运行多少时间"""
    start = datetime.strptime(start, "%H:%M")  # 将字符串格式的开始时间实例化为datetime对象
    end = datetime.strptime(end, "%H:%M")
    return int((end - start).seconds / 60)  # 计算结束时间与开始时间之间相差多少秒并将秒换算成分钟


def new_window_ready_path(backend, path, title):
    """通过路径连接新的窗口"""
    while True:
        try:
            application = Application(backend=backend).connect(path=path)
        except:
            continue
        application.window(title=title).wait("ready", timeout=300)
        return application


def connect_progaram(path):
    """通过路径连接运行的程序"""
    while True:
        try:
            Application().connect(path=path)
        except:
            continue
        else:
            return True


def new_window_ready_title(title1, title2):
    """通过title名判断新的窗口是否连接成功"""
    while True:
        try:
            application = Application().connect(title=title1)
            if application.top_window().child_window(title=title2).exists():
                return application
            else:
                sleep(3)
                continue
        except:
            continue


def control_check(application, control, edit_info="", wait_time=100):
    """根据控件类型自动编辑内容或者点击按钮
    按钮：自动点击
    编辑框：填写内容"""
    if "Button" in control or "CheckBox" in control or "ListBox" in control:
        application.top_window()[control].wait("ready", timeout=wait_time)
        application.top_window()[control].click_input()
    elif "Edit" in control:
        application.top_window()[control].wait("ready", timeout=wait_time)
        application.top_window()[control].set_text(edit_info)


def desk_top():
    """显示桌面"""
    x, y = size()
    rightClick(x // 2, y - 2)
    press('s')
    sleep(1)


def load_menu():
    """
    读取本目录菜单文件
    :return: 表示各文件名的列表
    """
    with open(os.path.join(os.getcwd(), "menu.txt")) as file:
        return file.readline().split('、')


def menu_format(choice_list):
    """将英文选单格式为中文名"""

    menu_dir = {'Wechat': '微信', 'NF3': 'Net Farmework3', '360drv': '360驱动大师', 'Chrome': '谷歌浏览器', 'TXvideo': '腾讯视频',
                'IQIYI': '爱奇艺', 'DX': 'DirectX9', '163music': '网易云音乐', 'SougouPY': '搜狗输入法', 'QQmusic': 'QQ音乐',
                'Dtalk': '钉钉'}

    menu_temp = choice_list.copy()
    for item in menu_temp:
        if item in menu_dir:
            menu_temp[menu_temp.index(item)] = menu_dir[item]
    return menu_temp


if __name__ == '__main__':
    step_menu = {"QQ": [["自定义选项", "Button"],  # 第四步：程序执行过程
                        ["添加到快速启动栏", "Button"],
                        ["开机自动启动", "Button"],
                        ["程序安装目录Edit", ""],
                        ["立即安装", "Button"],
                        ["完成安装", "Button"]],
                 "Wechat": [["更多选项", "Button"],
                            ["程序安装目录", "Edit"],
                            ["安装微信", "Button"],
                            ["开始使用", "Button"]],
                 "Winrar": [["目标文件夹(&D)Edit", ""],
                            ["安装", "Button"]],
                 "VCRedist": [["确定", "Button"]],
                 "NF3": [["确定", "Button"]],
                 "DX": [["确定", "Button"]],
                 "OFFICE2013": [["Edit8", ""]],
                 "CAD2007": [["确定", "Button"]],
                 "360drv": [["已经阅读并同意", "Button"],
                            ["立即安装", "Button"]],
                 "TXvideo": [["自定义安装Button", ""],
                             ["安装位置：Edit", ""],
                             ["立即安装", "Button"],
                             ["立即体验", "Button"]],
                 "IQIYI": [["阅读并同意", "Button"],
                           ["Edit", ""],
                           ["立即安装", "Button"],
                           ["CheckBox", ""],
                           ["CheckBox2", ""],
                           ["CheckBox3", ""],
                           ["CheckBox4", ""],
                           ["立即体验", "Button"]]
                 }

    type_menu = {"QQ": "win32",  # 第三步：程序类型
                 "Wechat": "uia",
                 "Winrar": "win32",
                 "VCRedist": "win32",
                 "NF3": "win32",
                 "OFFICE2013": "win32",
                 "CAD2007": "win32",
                 "360drv": "win32",
                 "Chrome": "win32",
                 "TXvideo": "win32",
                 "IQIYI": "win32",
                 "DX": "win32",
                 "PS CS3": "win32",
                 "163music": "uia",
                 "SougouPY": "win32",
                 "WPS": "win32",
                 "QQmusic": "win32",
                 "Dtalk": "win32"
                 }

    main_window_name = {"QQ": "腾讯QQ安装向导",  # 第二步：主窗口名称
                        "Wechat": "微信安装向导",
                        "Winrar": "WinRAR 5.91",
                        "VCRedist": "VC++运行库 一键安装 - IT天空出品",
                        "NF3": ".Net框架 3.5 一键安装 - IT天空出品",
                        "OFFICE2013": "Microsoft Office Professional Plus 2013",
                        "CAD2007": "Autodesk 安装程序",
                        "360drv": "欢迎使用 360驱动大师",
                        "Chrome": "",
                        "TXvideo": "腾讯视频 2020 安装程序 ",
                        "IQIYI": "执行的操作 安装向导",
                        "DX": "DirectX 9.0c 一键安装 - IT天空出品",
                        "PS CS3": "安装 - Adobe Photoshop CS3 Extended",
                        "163music": "",
                        "SougouPY": "",
                        "Dtalk": "钉钉 安装"
                        }

    menu = load_menu()

    for each in menu:

        if each == "QQmusic":
            desk_top()
            temp = Application(backend=type_menu[each]).start(
                os.path.join(os.getcwd(), "app_pkg", each, "QQMusic_YQQFullStack"))
            sleep(2)
            check = gui.gui_run(each, 2, 0.6)
            if check:
                if connect_progaram(r"D:\Program Files (x86)\Tencent\QQMusic\QQMusic.exe"):
                    sleep(2)
                    os.system('taskkill /IM QQmusic.exe /F')
                    continue
            else:
                failure.append("QQ音乐")
                continue

        if each == "WPS":
            desk_top()
            temp = Application(backend=type_menu[each]).start(
                os.path.join(os.getcwd(), "app_pkg", each, "W.P.S.10132.12012.2019"))
            sleep(2)
            check = gui.gui_run(each, 2, 0.6, sleep_time=10)
            if check:
                if connect_progaram(r"D:\Users\admin\AppData\Local\Kingsoft\WPS Office\11.1.0.10132\office6\wps.exe"):
                    sleep(2)
                    os.system('taskkill /IM wps.exe /F')
                    continue
            else:
                failure.append("WPS")
                continue

        if each == "163music":
            desk_top()
            temp = Application(backend=type_menu[each]).start(os.path.join(os.getcwd(), "app_pkg", each, each))
            sleep(2)
            check = gui.gui_run(each, 3, 0.6)
            if check:
                if connect_progaram(r"D:\Program Files (x86)\Netease\CloudMusic\cloudmusic.exe"):
                    sleep(2)
                    os.system('taskkill /IM cloudmusic.exe /F')
                    continue
            else:
                failure.append("网易云音乐")
                continue

        if each == "SougouPY":
            desk_top()
            temp = Application(backend=type_menu[each]).start(os.path.join(os.getcwd(), "app_pkg", each, each))
            sleep(.5)
            check = gui.gui_run(each, 3, 0.6)
            if check:
                while not temp.is_process_running():
                    break
                continue
            else:
                failure.append("搜狗输入法")
                continue

        if each == "PS CS3":
            desk_top()
            temp = Application(backend=type_menu[each]).start(os.path.join(os.getcwd(), "app_pkg", each, each))
            sleep(2)
            check = gui.gui_run(each, 1, 0.8)
            if check:
                continue
            else:
                failure.append("PS CS3")
                continue

        if each == "Chrome":  # 谷歌浏览器打开自动安装不需要任何按钮
            temp = Application(backend=type_menu[each]).start(os.path.join(os.getcwd(), "app_pkg", each, each))
            sleep(5)
            while True:
                sleep(5)
                if not temp.is_process_running():
                    break
            os.system('taskkill /IM chrome.exe /F')
            continue

        if each == "CAD2014":
            app = Application().start(
                os.path.join(os.getcwd(), "app_pkg", each, "setup.exe")).top_window().wait("ready", timeout=20)
            cad2014_app = new_window_ready_title("Autodesk® AutoCAD® 2014", "退出")
            for i in ['ListBox3', '我接受Button', '下一步Button']:
                control_check(application=cad2014_app, control=i)
                sleep(1)
            control_check(application=cad2014_app, control="序列号:Edit", edit_info="666")
            control_check(application=cad2014_app, control="Edit2", edit_info="69696969")
            control_check(application=cad2014_app, control="产品密钥:Edit", edit_info="001F1")
            for i in ['下一步Button', '安装路径:Edit', '安装Button']:
                if "Edit" not in i:
                    control_check(application=cad2014_app, control=i)
                    sleep(1)
                elif "Edit" in i:
                    control_check(application=cad2014_app, control=i, edit_info=r"D:\Program Files\Autodesk")
            sleep(120)
            while True:
                if cad2014_app.top_window().child_window(title="完成").exists():
                    cad2014_app.top_window()['完成'].click_input()
                    break
                else:
                    sleep(3)
            continue

        p = Program(os.getcwd(), each, type_menu[each], main_window_name[each])

        if each == "Dtalk":
            for i in ['Button', 'Edit', 'Button2', 'CheckBox', 'Button2']:
                if "Edit" not in i:
                    control_check(application=p.app, control=i)
                elif "Edit" in i:
                    control_check(application=p.app, control=i, edit_info=r"D:\Program Files (x86)\DingDing")
            continue

        if each == "OFFICE2013":  # office2013获取不到按钮用快捷键实现安装
            if p.app.top_window().wait("ready", timeout=300):
                p.app.top_window().type_keys("%a")
                sleep(.5)
                p.app.top_window().type_keys("%c")
                p.app.top_window().wait("ready", timeout=300)
                p.app.top_window().type_keys("%u")
                p.app.top_window().wait("ready", timeout=300)
                p.app.top_window().set_focus()
                check = offce_select.choose_menu()
                if check:
                    p.app.top_window().type_keys("%f")
                else:
                    failure.append("OFFICE2013")
                    continue

        step_len = len(step_menu[each])
        for i in range(step_len):
            class_name = step_menu[each][i][1]
            title_name = step_menu[each][i][0]
            if "Edit" in class_name or "Edit" in title_name:
                p.check_window(title_name, class_name)
                p.main_edit()
            elif class_name == "Button" or class_name == "":
                p.check_window(title_name, class_name)
                p.button_click()

        if each == "QQ":
            sleep(3)
            os.system('taskkill /IM QQ.exe /F')  # 关闭自动打开的QQ程序
        if each == "Wechat":
            sleep(3)
            os.system('taskkill /IM WeChat.exe /F')  # 关闭自动打开的微信程序
        if each == "Winrar":
            app = new_window_ready_path("win32", r"D:\Program Files\Winrar\Uninstall", "WinRAR 简体中文版安装")
            window = app["WinRAR 简体中文版安装"]
            window.child_window(title="确定", class_name="Button").click()
            app = new_window_ready_path("win32", r"D:\Program Files\Winrar\Uninstall", "WinRAR 简体中文版安装")
            window = app["WinRAR 简体中文版安装"]
            window.child_window(title="完成", class_name="Button").click_input()
        if each == "VCRedist":
            app = new_window_ready_path("win32", os.path.join(os.getcwd(), "app_pkg", "VCRedist", "VCRedist"), "信息")
            window = app["信息"]
            window.child_window(title="是(&Y)", class_name="Button").click_input()
            app = new_window_ready_path("win32", os.path.join(os.getcwd(), "app_pkg", "VCRedist", "VCRedist"), "信息")
            window = app["信息"]
            window.child_window(title="确定", class_name="Button").click_input()
        if each == "NF3":
            app = new_window_ready_path("win32", os.path.join(os.getcwd(), "app_pkg", "NF3", "NF3"), "信息")
            window = app["信息"]
            window.child_window(title="是(&Y)", class_name="Button").click_input()
            app = new_window_ready_path("win32", os.path.join(os.getcwd(), "app_pkg", "NF3", "NF3"), "信息")
            window = app["信息"]
            window.child_window(title="确定", class_name="Button").click_input()
        if each == "DX":
            app = new_window_ready_path("win32", os.path.join(os.getcwd(), "app_pkg", "DX", "DX"), "信息")
            window = app["信息"]
            window.child_window(title="是(&Y)", class_name="Button").click_input()
            app = new_window_ready_path("win32", os.path.join(os.getcwd(), "app_pkg", "DX", "DX"), "信息")
            window = app["信息"]
            window.child_window(title="确定", class_name="Button").click_input()
        if each == "OFFICE2013":
            p.app.top_window().wait("ready", timeout=300)
            p.app.top_window().type_keys("%i")
            sleep(3)
            while True:
                try:
                    p.app.top_window().type_keys("%c")
                    sleep(10)
                except RuntimeError:
                    break
            office_crack = os.path.join(os.getcwd(), "app_pkg", "OFFICE2013", "office13.bat")
            os.system(office_crack)

        if each == "CAD2007":
            app = new_window_ready_title("AutoCAD 2007 安装", "下一步(&N)>")
            for i in ['Button2', 'RadioButton2', 'Button0']:
                control_check(application=app, control=i)
                sleep(1)

            control_check(application=app, control='Edit1', edit_info="000")
            sleep(0.5)
            control_check(application=app, control='Edit2', edit_info="00000000")
            sleep(0.5)
            control_check(application=app, control='Button1')

            for i in range(1, 6):
                control_check(application=app, control="Edit" + str(i), edit_info="asd")
                sleep(0.5)

            for i in ['Button1', 'Button1', 'Button1']:
                control_check(application=app, control=i)
                sleep(2)

            control_check(application=app, control='Edit', edit_info=r"D:\Program Files\CAD2007")
            for i in ['Button1', 'Button1', 'Button1']:
                control_check(application=app, control=i)
                sleep(3)
            app = new_window_ready_title("AutoCAD 2007 安装程序", "完成(&F)")
            for i in ['CheckBox', 'Button1']:
                control_check(application=app, control=i)
            crack_path = os.path.join(os.getcwd(), "app_pkg", "CAD2007", "crack", "adlmdll.dll")
            os.system(f'xcopy "{crack_path}" "D:\\Program Files\CAD2007\\adlmdll.dll" /Y')
            sleep(1)
            crack_path = os.path.join(os.getcwd(), "app_pkg", "CAD2007", "crack", "lacadp.dll")
            os.system(f'xcopy "{crack_path}" "D:\\Program Files\CAD2007\\lacadp.dll" /Y')

        if each == "360drv":
            sleep(3)
            os.system('taskkill /IM 360DrvMgr.exe /F')
        if each == "TXvideo":
            sleep(3)
            os.system('taskkill /IM QQLive.exe /F')
        if each == "IQIYI":
            sleep(3)
            os.system('taskkill /IM QyClient.exe /F')

    end_time = (strftime("%H:%M", localtime()))
    menu = menu_format(menu)
    textbox('', '程序安装完毕',
            f"程序安装完毕，用时{running_time(start_time, end_time)}分钟，共选择了{len(menu)}个软件，分别为：{','.join(menu)}，安装失败的软件为：{','.join(failure)}")
