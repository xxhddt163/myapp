import openpyxl
import easygui
import re
from openpyxl import styles
from os.path import basename


class Remark:
    """遍历统计总表，通过手工写好的统计总表自动填入相应课表"""

    def __init__(self):
        easygui.msgbox("请选择已统计完的表格")
        self.open_path = easygui.fileopenbox(default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
        easygui.msgbox("请选择汇总文件保存位置")
        self.save_path = easygui.filesavebox(default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
        self.file = openpyxl.load_workbook(self.open_path)  # excel文件对象
        self.main()

    def main(self):
        count = 1
        while self.file["统计总表"]["A" + str(count)].value is not None:
            comment = self.file["统计总表"]["A" + str(count)].comment
            if comment is not None:
                self.filter_object_teacher(count)
            else:
                self.update_hyperlink(count)
            count += 1
        self.file.save(self.save_path)

    def filter_object_teacher(self, line):
        """筛选出科目名与代课教师名"""
        info = self.file["统计总表"]["A" + str(line)].value
        temp = re.search(r"班级：.*科目：(.*)\s任课老师：.*代课老师：(.*)", info)
        sub = temp.group(1).strip()  # 科目
        teacher = temp.group(2).strip()  # 代课老师
        sheet_name = self.file["统计总表"]["A" + str(line)].hyperlink.location.replace('\'', '').split('!')[0]  # 表单名
        cell = self.file["统计总表"]["A" + str(line)].hyperlink.location.replace('\'', '').split('!')[1]  # 单元格坐标
        self.update_hyperlink(line)
        self.format_cell(sheet_name, cell, sub, teacher)

    def format_cell(self, sheet_name, cell, sub, teacher):
        """修改对应数据并填充颜色"""
        self.file[sheet_name][cell].value = sub + "\n" + teacher
        self.file[sheet_name][cell].font = styles.Font(color='0099CC00')

    def update_hyperlink(self, count):
        """刷新超链接"""
        sheet_name = self.file["统计总表"]["A" + str(count)].hyperlink.location.replace('\'', '').split('!')[0]  # 表单名
        cell = self.file["统计总表"]["A" + str(count)].hyperlink.location.replace('\'', '').split('!')[1]  # 单元格坐标
        self.file["统计总表"]["A" + str(count)].hyperlink = f"{basename(self.save_path)}#'{sheet_name}'!{cell}"


if __name__ == '__main__':
    remark = Remark()
