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
                    if excel[name][row + str(n2)].value.replace('\r', '').split("\n")[1] in person_name:
                        info = teacher_info.copy()  # 教师信息备份
                        subject_name = excel[name][row + str(n2)].value.replace('\r', '').split("\n")[0]  # 科目名
                        grade = name[:3]  # 年级
                        info = filter_1(subject_name, info)
                        print(info)


def filter_1(subject, info):
    """删除教师信息中科目不相关人员"""
    if subject == '校本-英语':
        subject = '英语'
    cache = list()
    for each in info:
        check = 0
        for each2 in info[each][1].split('、'):
            if each2 == subject:
                check = 1
        if check == 0:
            cache.append(each)
    for each in cache:
        info.pop(each)
    return info


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


def remove_person(info, name):
    """删除字典中存在的person信息"""
    for each in name:
        try:
            info.pop(each)
        except KeyError:
            print(f"{each}不存在老师信息中")
            choose = input("是否继续执行程序？ y/n")
            if choose.lower() == "n":
                raise KeyError
    return info


if __name__ == '__main__':
    teacher_info = load_pickle("teacher_info.pickle")

    with open("without.txt", mode='r') as temp:
        person_name = temp.readline().split('、')

    teacher_info = remove_person(teacher_info, person_name)

    easygui.msgbox("请选择班级课表所在位置")
    teacher_schedule = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx",
                                           filetypes=["*.xlsx"])
    teacher_schedule_work = openpyxl.load_workbook(teacher_schedule)
    main(teacher_schedule_work)
