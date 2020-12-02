from setup_class import Program
import os
import time
from pywinauto import Application
import easygui


def new_window_ready(backend, path, title):
    """安装程序后检测并连接新的窗口"""
    while True:
        application = Application(backend=backend).connect(path=path)
        if application.window(title=title).wait("ready", timeout=300):
            return application


if __name__ == '__main__':
    step_menu = {"QQ": [["自定义选项", "Button"],  # 第四步：程序执行过程
                        ["添加到快速启动栏", "Button"],
                        ["开机自动启动", "Button"],
                        [r"C:\Program Files (x86)\Tencent\QQ", "Edit"],
                        ["立即安装", "Button"],
                        ["完成安装", "Button"]],
                 "Wechat": [["更多选项", "Button"],
                            ["程序安装目录", "Edit"],
                            ["安装微信", "Button"],
                            ["开始使用", "Button"]],
                 "Winrar": [[r"C:\Program Files\WinRAR", "Edit"],
                            ["安装", "Button"]],
                 "VCRedist": [["确定", "Button"]],
                 "NF3": [["确定", "Button"]],
                 "OFFICE2013": [[r"C:\Program Files\Microsoft Office", "RichEdit20W"]],
                 "CAD2007": [["确定", "Button"]],
                 "360drv": [["已经阅读并同意", "Button"],
                            ["立即安装", "Button"], ],
                 "TXvideo": [["自定义安装Button", ""],
                             [r"C:\Program Files (x86)\Tencent\QQLive", "Edit"],
                             ["立即安装", "Button"],
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
                 "TXvideo": "win32"}

    main_window_name = {"QQ": "腾讯QQ安装向导",  # 第二步：主窗口名称
                        "Wechat": "微信安装向导",
                        "Winrar": "WinRAR 5.91",
                        "VCRedist": "VC++运行库 一键安装 - IT天空出品",
                        "NF3": ".Net框架 3.5 一键安装 - IT天空出品",
                        "OFFICE2013": "Microsoft Office Professional Plus 2013",
                        "CAD2007": "Autodesk 安装程序",
                        "360drv": "欢迎使用 360驱动大师",
                        "Chrome": "",
                        "TXvideo": "腾讯视频 2020 安装程序 "}

    setup_menu = easygui.multchoicebox(msg="请选择安装的程序", title="选择程序",
                                       choices=["QQ", "Wechat", "Winrar", "VCRedist", "NF3", "OFFICE2013", "CAD2007",
                                                "360drv", "Chrome", "TXvideo"])
    for each in setup_menu:
        if each == "Chrome":  # 谷歌浏览器打开自动安装不需要任何按钮
            temp = Application(backend=type_menu[each]).start(os.getcwd() + "\\" + each + "\\" + each)
            time.sleep(5)
            while True:
                time.sleep(5)
                if not temp.is_process_running():
                    break
            os.system('taskkill /IM chrome.exe /F')
            continue

        p = Program(os.getcwd(), each, type_menu[each], main_window_name[each])

        if each == "OFFICE2013":  # office2013获取不到按钮用快捷键实现安装
            if p.app.top_window().wait("ready", timeout=300):
                p.app.top_window().type_keys("%a")
                time.sleep(.5)
                p.app.top_window().type_keys("%c")
                p.app.top_window().wait("ready", timeout=300)
                p.app.top_window().type_keys("%u")
                p.app.top_window().wait("ready", timeout=300)
                p.app.top_window().type_keys("%f")

        step_len = len(step_menu[each])
        for i in range(step_len):
            class_name = step_menu[each][i][1]
            title_name = step_menu[each][i][0]
            if "Edit" in class_name:
                p.check_window(title_name, class_name)
                p.main_edit()
            elif class_name == "Button" or class_name == "":
                p.check_window(title_name, class_name)
                p.button_click()
        if each == "QQ":
            time.sleep(3)
            os.system('taskkill /IM QQ.exe /F')  # 关闭自动打开的QQ程序
        if each == "Wechat":
            time.sleep(3)
            os.system('taskkill /IM WeChat.exe /F')  # 关闭自动打开的微信程序
        if each == "Winrar":
            app = new_window_ready("win32", r"D:\Program Files\Winrar\Uninstall", "WinRAR 简体中文版安装")
            window = app["WinRAR 简体中文版安装"]
            window.child_window(title="确定", class_name="Button").click()
            app = new_window_ready("win32", r"D:\Program Files\Winrar\Uninstall", "WinRAR 简体中文版安装")
            window = app["WinRAR 简体中文版安装"]
            window.child_window(title="完成", class_name="Button").click_input()
        if each == "VCRedist":
            app = new_window_ready("win32", os.getcwd() + "\\" + "VCRedist" + "\\" + "VCRedist", "信息")
            window = app["信息"]
            window.child_window(title="是(&Y)", class_name="Button").click_input()
            app = new_window_ready("win32", os.getcwd() + "\\" + "VCRedist" + "\\" + "VCRedist", "信息")
            window = app["信息"]
            window.child_window(title="确定", class_name="Button").click_input()
        if each == "NF3":
            app = new_window_ready("win32", os.getcwd() + "\\" + "NF3" + "\\" + "NF3", "信息")
            window = app["信息"]
            window.child_window(title="是(&Y)", class_name="Button").click_input()
            app = new_window_ready("win32", os.getcwd() + "\\" + "NF3" + "\\" + "NF3", "信息")
            window = app["信息"]
            window.child_window(title="确定", class_name="Button").click_input()
        if each == "OFFICE2013":
            p.app.top_window().wait("ready", timeout=300)
            p.app.top_window().type_keys("%i")
            time.sleep(3)
            while True:
                try:
                    p.app.top_window().type_keys("%c")
                    time.sleep(10)
                except RuntimeError:
                    break
            office_crack = os.getcwd() + "\\" + "OFFICE2013" + "\\" + "office13.bat"
            os.system(office_crack)
        if each == "CAD2007":
            time.sleep(3)
            while True:
                app = Application().connect(title="AutoCAD 2007 安装")
                if app.top_window().child_window(title="下一步(&N)>", class_name="Button").exists():
                    break
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").wait("ready", timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="我接受(&A)", class_name="Button").wait("ready", timeout=300)
            app.top_window().child_window(title="我接受(&A)", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").wait("ready", timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="序列号(&S)", class_name="Static").wait("ready", timeout=300)
            app.top_window().type_keys("%s")
            app.top_window().type_keys("00000000000")
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").wait("ready", timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="用户信息", class_name="Static").wait("ready", timeout=300)
            app.top_window().type_keys("%f")
            app.top_window().type_keys("asd")
            app.top_window().type_keys("%l")
            app.top_window().type_keys("asd")
            app.top_window().type_keys("%o")
            app.top_window().type_keys("asd")
            app.top_window().type_keys("%d")
            app.top_window().type_keys("asd")
            app.top_window().type_keys("%p")
            app.top_window().type_keys("asd")
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").wait("ready", timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="选择安装类型", class_name="Static").wait("ready", timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").wait("ready", timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").wait("ready", timeout=300)
            app.top_window().child_window(title="C:\\Program Files (x86)\\AutoCAD 2007\\", class_name="Edit").set_text(
                r"D:\Program Files\CAD2007")
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").wait("ready", timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="选择用于编辑文本文件的默认文字编辑器(&E):", class_name="Static").wait("ready",
                                                                                                     timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="开始安装", class_name="Static").wait("ready", timeout=300)
            app.top_window().child_window(title="下一步(&N)>", class_name="Button").click_input()
            time.sleep(30)
            while True:
                app = Application().connect(title="AutoCAD 2007 安装程序")
                if app.top_window().child_window(title="完成(&F)", class_name="Button").exists():
                    break
                else:
                    time.sleep(5)
            time.sleep(3)
            app.top_window().child_window(title="完成(&F)", class_name="Button").wait("ready", timeout=100)
            app.top_window().child_window(title="是，我想现在阅读自述文件的内容(&Y)", class_name="Button").click_input()
            time.sleep(1)
            app.top_window().child_window(title="完成(&F)", class_name="Button").wait("ready", timeout=100)
            app.top_window().child_window(title="完成(&F)", class_name="Button").click_input()
            time.sleep(1)
            crack_path = os.getcwd() + "\\" + "CAD2007" + "\\" + "crack" + "\\" + "adlmdll.dll"
            os.system(f'xcopy "{crack_path}" "D:\\Program Files\CAD2007\\adlmdll.dll" /Y')
            time.sleep(.5)
            crack_path = os.getcwd() + "\\" + "CAD2007" + "\\" + "crack" + "\\" + "lacadp.dll"
            os.system(f'xcopy "{crack_path}" "D:\\Program Files\CAD2007\\lacadp.dll" /Y')
        if each == "360drv":
            time.sleep(3)
            os.system('taskkill /IM 360DrvMgr.exe /F')
        if each == "TXvideo":
            time.sleep(3)
            os.system('taskkill /IM QQLive.exe /F')
