import openpyxl
import easygui
import pickle


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


easygui.msgbox("请选择已统计完的表格")
open_path = easygui.fileopenbox(default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
sheet = openpyxl.load_workbook(open_path)
teacher = {}
for sheet_name in sheet.sheetnames:
    line_start = 4
    while sheet[sheet_name]["A" + str(line_start)].value is not None:
        class_number = sheet[sheet_name]["A" + str(line_start)].value[2]  # 班级
        low_start = 2
        while sheet[sheet_name][convert2title(low_start) + str(line_start)].value is not None:
            name = sheet[sheet_name][convert2title(low_start) + str(line_start)].value.strip()
            if teacher.get(name) is not None:
                if str(class_number) + "班" not in teacher[name]:
                    teacher[name] = teacher[name] + "、" + str(class_number) + "班"
            else:
                teacher[name] = str(class_number) + "班"
            low_start += 1
        line_start += 1

with open("new_teacher_info.pickle", mode="wb") as file:
    pickle.dump(teacher, file)
