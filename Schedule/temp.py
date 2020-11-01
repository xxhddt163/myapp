import openpyxl
import easygui
import re


def main(excel):
    for sheet_name in excel.sheetnames:  # 遍历课表
        info = excel[sheet_name]["A2"].value
        temp = re.search(r".* 班主任：(.*)", info)
        name = temp.group(1)
        excel[sheet_name]["B10"].value = "班会\n" + name
        excel.save("kcb.xlsx")


if __name__ == '__main__':
    easygui.msgbox("请选择班级课表所在位置")
    teacher_schedule = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx",
                                           filetypes=["*.xlsx"])
    teacher_schedule_work = openpyxl.load_workbook(teacher_schedule)
    main(teacher_schedule_work)
