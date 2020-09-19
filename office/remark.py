import openpyxl
import datetime
from openpyxl import styles
import easygui
import re


class Remark:
    """根据批注自动填写迟到次数并填写备注"""

    def __init__(self, file, sh_name):
        self.file = file
        self.sh_name = sh_name
        self.open_file()
        self.iter_row()
        self.delete_rstrip()
        self.save_file()

    def open_file(self):
        """打开excel文件"""
        self.excel = openpyxl.load_workbook(file)
        self.sheet = self.excel[self.sh_name]

    def iter_row(self):
        """遍历列"""
        for number in range(4, 100):
            if self.sheet['D' + str(number)].value is not None:
                self.iter_line(number)
            else:
                break

    def iter_line(self, number):
        """遍历Dnumber有内容的行"""
        for line in range(5, 36):
            row = self.converttotitle(line)
            if self.sheet[row + str(number)].comment is not None:
                self.remark(number, line, row)

    def remark(self, number, line, row):
        """填写备注"""
        info = self.sheet[row + str(number)].comment
        temp = re.search(r"考勤异常,上班打卡时间.*,下班打卡时间.*,迟到(\d+)小时(\d+)分钟", info.content)  # 提取迟到时间的正则
        hour = temp.group(1)  # 提取迟到小时
        min = temp.group(2)  # 提取迟到分钟
        if int(hour) == 0:
            if self.sheet['BI' + str(number)].value is not None:
                self.sheet['BI' + str(number)].value = self.sheet['BI' + str(number)].value + \
                                                       str(datetime.datetime.now().month - 1) + \
                                                       "月" + str(line - 4) + "日" \
                                                       + "迟到" + str(min) + "分钟,"
                self.check_time(number, hour, min)
            else:
                self.sheet['BI' + str(number)].value = str(datetime.datetime.now().month - 1) + \
                                                       "月" + str(line - 4) + "日" \
                                                       + "迟到" + str(min) + "分钟,"
                self.check_time(number, hour, min)
        else:
            if self.sheet['BI' + str(number)].value is not None:
                self.sheet['BI' + str(number)].value = self.sheet['BI' + str(number)].value + \
                                                       str(datetime.datetime.now().month - 1) + \
                                                       "月" + str(line - 4) + "日" \
                                                       + "迟到" + str(hour) + "小时" + str(min) + "分钟,"
                self.check_time(number, hour, min)
            else:
                self.sheet['BI' + str(number)].value = str(datetime.datetime.now().month - 1) + \
                                                       "月" + str(line - 4) + "日" \
                                                       + "迟到" + str(hour) + "小时" + str(min) + "分钟,"
                self.check_time(number, hour, min)
        self.sheet['BI' + str(number)].font = styles.Font(name='宋体', size=6, bold=True)

    def save_file(self):
        easygui.msgbox("备注填写完毕，请选择保存路径")
        file_save = easygui.filesavebox(default=r"C:\Users\Administrator\Desktop\*.xlsx",
                                        filetypes=["*.xlsx"])
        self.excel.save(file_save)

    def check_time(self, number, hour, min):
        """统计迟到次数"""
        if int(hour) >= 1:  # 大于一个小时的迟到时间
            letter = "BB"
            self.check_time2(number, letter)
        elif int(hour) == 0:
            if int(min) < 10:  # 迟到10分钟以内
                letter = "AY"
                self.check_time2(number, letter)
            elif 10 <= int(min) < 30:
                letter = "AZ"
                self.check_time2(number, letter)
            elif 30 <= int(min) < 60:
                letter = "BA"
                self.check_time2(number, letter)

    def check_time2(self, number, letter):
        """在对应迟到的表格内填上迟到次数"""
        if self.sheet[letter + str(number)].value is None:
            self.sheet[letter + str(number)].value = 1
        else:
            self.sheet[letter + str(number)].value = int(self.sheet[letter + str(number)].value) + 1
        self.sheet[letter + str(number)].font = styles.Font(name='宋体', size=6, bold=True)

    def delete_rstrip(self):
        """删除每一行备注的最后一个逗号"""
        for number in range(4, 91):
            if self.sheet['BI' + str(number)].value is not None:
                self.sheet['BI' + str(number)].value = self.sheet['BI' + str(number)].value.rstrip(',')

    @staticmethod
    def converttotitle(n):
        """将数字转换成EXCEL列"""
        rStr = ""
        while n != 0:
            res = n % 26
            if res == 0:
                res = 26
                n -= 26
            rStr = chr(ord('A') + res - 1) + rStr
            n = n // 26
        return rStr


if __name__ == '__main__':
    easygui.msgbox("请选择统计好的考勤汇总文件")
    file = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
    sh_name = easygui.enterbox(msg='请输入工作表名字', default=str(datetime.datetime.now().month - 1) + '月考勤详情')
    r = Remark(file, sh_name)
