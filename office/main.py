import datetime
import easygui
import openpyxl
from myapp.office.setting import Setting

if __name__ == '__main__':
    easygui.msgbox("请选择考勤文件所在位置")
    file = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
    excel_work = openpyxl.load_workbook(file)
    sheet_work = excel_work["考勤记录"]

    easygui.msgbox("请选择汇总所在位置")
    file2 = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
    excel_trunk = openpyxl.load_workbook(file2)
    sheet_trunk = excel_trunk[str(datetime.datetime.now().month - 1) + '月考勤详情']
