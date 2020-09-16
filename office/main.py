import datetime
import easygui
import openpyxl
from myapp.office.setting import Setting

department = {}


def find_name():
    """遍历考勤表内员工名字,将名字与对应的部门写入字典"""
    for number in range(5, 999, 2):
        if sheet_work['U' + str(number)].value is not None:
            department[sheet_work['K' + str(number)].value] = sheet_work['U' + str(number)].value  # 存放名字与对应部门
            trunk_line = find_line(sheet_work['K' + str(number)].value)  # 名字在汇总表中的行
            up_time, down_time = crow_time(number)  # 上、下班时间
            check_time(up_time, down_time, trunk_line, sheet_work['K' + str(number)].value)
        else:
            break


def check_time(up_time, down_time, trunk_line, name):
    """检查考勤"""
    time_set = Setting()
    if department[name] != "招商运营部":


def crow_time(number):
    """遍历考勤"""
    for row in range(2, 32):
        return sheet_work[converttotitle(row) + number + 1].value[:5], \
               sheet_work[converttotitle(row) + number + 1].value[-5:]


def find_line(name):
    """在汇总表找到名字对应的行"""
    for line in range(2, 100):
        if not sheet_trunk['C' + str(line)].value is None and sheet_trunk['C' + str(line)].value == name:
            return line


def converttotitle(n):
    """将数字转换成EXCEL对应的字母列"""
    rstr = ""
    while n != 0:
        res = n % 26
        if res == 0:
            res = 26
            n -= 26
        rstr = chr(ord('A') + res - 1) + rstr
        n = n // 26
    return rstr


if __name__ == '__main__':
    easygui.msgbox("请选择考勤文件所在位置")
    file = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
    excel_work = openpyxl.load_workbook(file)
    sheet_work = excel_work["考勤记录"]

    easygui.msgbox("请选择汇总所在位置")
    file2 = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
    excel_trunk = openpyxl.load_workbook(file2)
    sheet_trunk = excel_trunk[str(datetime.datetime.now().month - 1) + '月考勤详情']
    find_name()
