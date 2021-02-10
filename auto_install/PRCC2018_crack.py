from pywinauto import Application
from time import sleep
from os import getcwd
from os.path import join
from os import system


def control_check(application, control, edit_info="", wait_time=100):
    """根据控件类型自动编辑内容或者点击按钮
    按钮：自动点击
    编辑框：填写内容"""
    if "Button" in control or "CheckBox" in control or "ListBox" in control:
        if application.top_window()[control].wait("ready", timeout=wait_time) and application.top_window()[
            control].exists():
            application.top_window()[control].click_input()
            sleep(1)
    elif "Edit" in control:
        if application.top_window()[control].wait("ready", timeout=wait_time) and application.top_window()[
            control].exists():
            application.top_window()[control].set_text(edit_info)
            sleep(1)


def crack_pr():
    ps_cra = Application().start(join(getcwd(), "app_pkg", 'PRCC2018', 'crack'))
    ps_cra.top_window().wait('ready', timeout=50)

    edit_temp = {'Create config based from dropdown listEdit3': 'Adobe Prelude CC 2015',
                 'Create config based from dropdown listEdit2': 'V7{}Prelude-4-Win-GM',
                 'Create config based from dropdown listEdit': '4.0.0',
                 'Button2': '',
                 'Edit': r'C:\Program Files\Adobe\Adobe Premiere Pro CC 2018\amtlib.dll',
                 '打开(&O)Button': ''
                 }

    for each in ['Create config based from dropdown listEdit3',
                 'Create config based from dropdown listEdit2',
                 'Create config based from dropdown listEdit',
                 'Button2',
                 'Edit',
                 '打开(&O)Button']:
        control_check(application=ps_cra, control=each, edit_info=edit_temp[each], wait_time=5)
    sleep(2)
    ps_cra.kill()
    sleep(1)
    system('taskkill /IM PDapp.exe /F')
