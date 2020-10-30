import easygui
import openpyxl
import pickle


def main(excel):
    name_to_subject = {}  # 教师名字:科目
    name_to_class = {}  # 教师名字:年级
    for name in excel.sheetnames:  # 遍历课表人名
        sheet_work = excel[name]
        name_to_subject[name] = sheet_work['G3'].value
        name_to_class[name] = sheet_work['G4'].value
    with open('high_name_to_subject.pickle', mode='wb') as temp:
        pickle.dump(name_to_subject, temp)
    with open('high_name_to_class.pickle', mode='wb') as temp:
        pickle.dump(name_to_class, temp)
    print(name_to_class)
    print(name_to_subject)


if __name__ == '__main__':
    easygui.msgbox("请选择教师课表所在位置")
    file = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx",
                               filetypes=["*.xlsx"])
    file_work = openpyxl.load_workbook(file)
    main(file_work)
