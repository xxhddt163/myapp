import openpyxl
import easygui
import re


def main(excel):
    name_to_subject = {}  # 教师名字:[[年级],[科目]]
    for name in excel.sheetnames:  # 遍历课表人名
        sheet_work = excel[name]
        name_to_subject = subject(sheet_work, name_to_subject, name)


def subject(sheet, name_to_subject, name):
    """遍历教师课表每个单元格得到名字与对应的年级及科目"""
    for n1 in range(2, 7):
        crow = convert2title(n1)
        for n2 in range(4, 13):
            if sheet[crow + str(n2)].value is not None:
                name_to_subject[name] =


def convert2title(n):
    """将数字转换成EXCEL对应的字母列"""
    title = ""
    while n != 0:
        res = n % 26
        if res == 0:
            res = 26
            n -= 26
        title = chr(ord('A') + res - 1) + title
        n = n // 26
    return title


if __name__ == '__main__':
    easygui.msgbox("请选择教师课表所在位置")
    teacher_schedule = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx",
                                           filetypes=["*.xlsx"])
    teacher_schedule_work = openpyxl.load_workbook(teacher_schedule)
    main(teacher_schedule_work)
