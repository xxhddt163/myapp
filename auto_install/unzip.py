import zipfile
from easygui import diropenbox, multchoicebox


def unzip(menu):
    """
    解压制定软件安装包到指定目录
    :param menu: 选择安装的文件菜单
    :return: 软件解压目录
    """
    extract_dir = diropenbox("选择加压文件保存的位置")
    zip_file = zipfile.ZipFile("auto_install.zip", "r")
    for program in menu:
        for name in zip_file.namelist():
            if program in name:
                zip_file.extract(name, extract_dir)
    zip_file.extract('auto_install.exe', extract_dir)
    zip_file.close()
    return extract_dir

def menu_format(choice_list):
    """将中文选单格式为英文名"""

    menu_dir = {"微信": "Wechat",
                "Net Farmework3": "NF3",
                "360驱动大师": "360drv",
                "谷歌浏览器": "Chrome",
                "腾讯视频": "TXvideo",
                "爱奇艺": "IQIYI",
                "DirectX9": "DX",
                "网易云音乐": "163music",
                "搜狗输入法": "SougouPY",
                "QQ音乐": "QQmusic",
                "钉钉": "Dtalk"}

    menu_temp = choice_list.copy()
    for item in menu_temp:
        if item in menu_dir:
            menu_temp[menu_temp.index(item)] = menu_dir[item]
    return menu_temp


if __name__ == '__main__':
    choice = multchoicebox(msg="请选择安装的程序", title="选择程序",
                           choices=["QQ", "微信", "钉钉", "Winrar", "VCRedist", "Net Farmework3", "DirectX9", "OFFICE2013",
                                    "CAD2007", "360驱动大师", "谷歌浏览器", "腾讯视频", "爱奇艺", "PS CS3", "网易云音乐",
                                    "QQ音乐", "搜狗输入法", "WPS"])
    menu = menu_format(choice)
    extract_dir = unzip(menu)
