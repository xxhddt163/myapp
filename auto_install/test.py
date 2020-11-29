from pywinauto import Application

app = Application(backend='uia').start(r"C:\Users\admin\Desktop\soft\Wechat.exe")
if app.window(title="微信安装向导").wait('ready', timeout=300):  # 等待界面出现才执行
    main_window = app["微信安装向导"]
    if main_window.window(title="安装微信").wait('ready', timeout=300):
        cache = main_window.child_window(title="安装微信")
        cache.click_input()
        if main_window.window(title="开始使用").wait('ready', timeout=300):
            cache = main_window.child_window(title="开始使用")
            cache.click_input()
