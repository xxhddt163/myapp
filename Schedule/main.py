import openpyxl
import easygui
import re
import pickle


def main(excel):
    for name in excel.sheetnames:  # 遍历课表
        for n1 in range(2, 7):
            for n2 in range(4, 12):
                row = convert2title(n1)
                if excel[name][row + str(n2)].value is not None:
                    if excel[name][row + str(n2)].value.split("\n")[1] in person_name:
                        subject_name = excel[name][row + str(n2)].value.split("\n")[0]




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


def load_pickle(file):
    """加载pickle文件"""
    with open(file=file, mode='rb') as temp:
        return pickle.load(temp)


if __name__ == '__main__':
    high_class = load_pickle("high_name_to_class.pickle")
    high_subject = load_pickle("high_name_to_subject.pickle")
    low_class = load_pickle("low_name_to_class.pickle")
    low_subject = load_pickle("low_name_to_subject.pickle")

    with open("without.txt", mode='r') as temp:
        person_name = temp.readline().split('、')

    easygui.msgbox("请选择班级课表所在位置")
    teacher_schedule = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx",
                                           filetypes=["*.xlsx"])
    teacher_schedule_work = openpyxl.load_workbook(teacher_schedule)
    main(teacher_schedule_work)
