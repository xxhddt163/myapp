import datetime
import easygui
import openpyxl
from myapp.office.setting import Setting
from openpyxl.comments import Comment  # 批注相关的模块
from openpyxl import styles

time_set = Setting()  # 设置部门上下班时间


def main():
    """主函数，遍历考勤表的所有部门及考勤"""
    for number in range(5, 999, 2):
        if sheet_work['U' + str(number)].value is not None:
            trunk_line = find_line(sheet_work['K' + str(number)].value)  # 名字在汇总表中的行
            print(f"正在统计{sheet_work['K' + str(number)].value}的考勤")
            if trunk_line is None:  # 考勤表中出现的人名未出现在统计表中
                print(f"{sheet_work['K' + str(number)].value}未出现在考勤统计表中")
                choose = input("是否继续统计？(y/n)")
                if choose.lower() == "y":
                    continue
                else:
                    raise TypeError

            for row in range(1, 32):  # 遍历1-31号考勤
                if sheet_work[convert2title(row) + str(number + 1)].value is not None:  # 当日是否无打卡记录
                    up_time, down_time = crow_time(row, number)  # 上、下班时间
                    if sheet_work['U' + str(number)].value != "招商运营部":
                        check_time(up_time, down_time, trunk_line, row, number)
                    elif sheet_work['U' + str(number)].value == "招商运营部":
                        check_time_bus(up_time, down_time, trunk_line, row, number)
                else:
                    continue
        else:
            break
    save_file()


def find_line(name):
    """在汇总表找到名字对应的行"""
    for line in range(4, 100):
        if sheet_trunk['D' + str(line)].value is not None and sheet_trunk['D' + str(line)].value == name:
            return line


def crow_time(row, number):
    """遍历考勤"""
    up_time = sheet_work[convert2title(row) + str(number + 1)].value[:5]  # 最早的上班时间
    up_time = datetime.time(int(up_time.split(":")[0]), int(up_time.split(":")[1]))  # 将字符串的时间转换成datetime对象
    down_time = sheet_work[convert2title(row) + str(number + 1)].value[-5:]  # 最晚的下班时间
    down_time = datetime.time(int(down_time.split(":")[0]), int(down_time.split(":")[1]))
    return up_time, down_time


def check_time(up_time, down_time, trunk_line, row, number):
    """其他部门检查考勤"""
    # 获取规定的上下班时间并转换成datetime对象
    set_up_time = datetime.time(int(time_set.uptime.split(":")[0]), int(time_set.uptime.split(":")[1]))
    set_down_time = datetime.time(int(time_set.downtime.split(":")[0]), int(time_set.downtime.split(":")[1]))

    if up_time <= set_up_time:  # 判定上班时间
        if down_time >= set_down_time:  # 判定下班时间
            sheet_trunk[convert2title(row + 4) + str(trunk_line)].value = "√"  # 正常考勤打钩
        else:
            sheet_trunk[convert2title(row + 4) + str(trunk_line)].value = \
                sheet_work[convert2title(row) + str(number + 1)].value
    else:
        if (up_time != down_time) and (down_time.hour - up_time.hour >= 8):
            sheet_trunk[convert2title(row + 4) + str(trunk_line)].value = \
                sheet_work[convert2title(row) + str(number + 1)].value
            up_cell_format(row, trunk_line)  # 上班异常字体颜色改红
            up_comment(row, trunk_line, up_time, down_time, set_up_time)  # 统计迟到时间并加入批注
        else:
            sheet_trunk[convert2title(row + 4) + str(trunk_line)].value = \
                sheet_work[convert2title(row) + str(number + 1)].value  # 异常记录直接复制进统计表中


def check_time_bus(up_time, down_time, trunk_line, row, number):
    """招商运营部统计考勤"""
    set_up_time1 = datetime.time(int(time_set.uptime_bus.split(":")[0]), int(time_set.uptime_bus.split(":")[1]))
    set_down_time1 = datetime.time(int(time_set.downtime_bus.split(":")[0]), int(time_set.downtime_bus.split(":")[1]))
    set_up_time2 = datetime.time(int(time_set.uptime_bus2.split(":")[0]), int(time_set.uptime_bus2.split(":")[1]))
    set_down_time2 = datetime.time(int(time_set.downtime_bus2.split(":")[0]), int(time_set.downtime_bus2.split(":")[1]))

    if up_time <= set_up_time1:  # 上班时间符合第一个上班时间
        if down_time >= set_down_time1:  # 上班时间符合第一个设置且下班时间也符合第一个设置
            sheet_trunk[convert2title(row + 4) + str(trunk_line)].value = "√"  # 正常考勤打钩
        else:  # 上班时间符合第一个设置，下班时间不符合
            sheet_trunk[convert2title(row + 4) + str(trunk_line)].value = \
                sheet_work[convert2title(row) + str(number + 1)].value
    elif set_up_time1 < up_time <= set_up_time2 and down_time >= set_down_time2:  # 如果上班时间大于第一个上班时间且小于第二个上班时间
        sheet_trunk[convert2title(row + 4) + str(trunk_line)].value = "√"  # 正常考勤打钩
    else:  # 如果以上条件都不符合肯定就是迟到了
        sheet_trunk[convert2title(row + 4) + str(trunk_line)].value = \
            sheet_work[convert2title(row) + str(number + 1)].value
        up_cell_format(row, trunk_line)  # 设置字体颜色
        up_comment_bus(row, trunk_line, up_time, down_time, set_up_time1, set_up_time2)  # 招商部填写批注


def up_comment(row, trunk_line, up_time, down_time, set_up_time):
    """非招商部门上班考勤异常自动填批注"""
    comment = Comment(f"考勤异常,上班打卡时间为{up_time.__format__('%H:%M')},下班打卡时间为{down_time.__format__('%H:%M')},"
                      f"迟到{up_time.hour - set_up_time.hour}小时{up_time.minute - set_up_time.minute}分钟", "")
    comment.width, comment.height = 120, 120
    sheet_trunk[convert2title(row + 4) + str(trunk_line)].comment = comment


def up_comment_bus(row, trunk_line, up_time, down_time, set_up_time1, set_up_time2):
    """招商部门上班考勤异常自动填批注"""
    if (up_time.hour == set_up_time1.hour) and (down_time.hour - up_time.hour >= 8):  # 如果上下班小时数不超过8小时可能只有一个记录
        comment = Comment(f"考勤异常,上班打卡时间{up_time.__format__('%H:%M')},下班打卡时间{down_time.__format__('%H:%M')},"
                          f"迟到{up_time.hour - set_up_time1.hour}小时{up_time.minute - set_up_time1.minute}分钟", "")
        comment.width, comment.height = 120, 120
        sheet_trunk[convert2title(row + 4) + str(trunk_line)].comment = comment
    elif (up_time.hour == set_up_time2.hour) and (down_time.hour - up_time.hour >= 8):
        comment = Comment(f"考勤异常,上班打卡时间{up_time.__format__('%H:%M')},下班打卡时间{down_time.__format__('%H:%M')},"
                          f"迟到{up_time.hour - set_up_time2.hour}小时{up_time.minute - set_up_time2.minute}分钟", "")
        comment.width, comment.height = 120, 120
        sheet_trunk[convert2title(row + 4) + str(trunk_line)].comment = comment


def up_cell_format(row, trunk_line):
    """设置上班异常考勤单元格文字颜色"""
    sheet_trunk[convert2title(row + 4) + str(trunk_line)].font = \
        styles.Font(name='Aria', size=8, color='00FF0000')  # 不正常上班考勤填充红色


def save_file():
    """保存文件"""
    easygui.msgbox("考勤统计完成，请选择汇总文件保存位置")
    file_save = easygui.filesavebox(default=r"C:\Users\Administrator\Desktop\*.xlsx",
                                    filetypes=["*.xlsx"])
    excel_trunk.save(file_save)


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
    easygui.msgbox("请选择考勤文件所在位置")
    file = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
    excel_work = openpyxl.load_workbook(file)
    sheet_work = excel_work["考勤记录"]

    easygui.msgbox("请选择汇总所在位置")
    file2 = easygui.fileopenbox("选择文件路径", default=r"C:\Users\Administrator\Desktop\*.xlsx", filetypes=["*.xlsx"])
    excel_trunk = openpyxl.load_workbook(file2)
    sheet_trunk = excel_trunk[str(datetime.datetime.now().month - 1) + '月考勤详情']
    main()
