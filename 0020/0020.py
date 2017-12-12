#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
# 就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
# 步骤
# 1.使用xlrd读取excel文件内容到json类型对象
# 2.使用 xlm minidom创建xlmnode,常规文件write保存

import xlrd
import time

def cal_call_time(file):
    time_call = 0
    time_called = 0

    with xlrd.open_workbook(file) as f:
        sheet = f.sheet_by_index(0)
        row_n = sheet.nrows
        for i in range(5,row_n):
            rowvalue = sheet.row_values(i)
            if rowvalue[2] == '被叫':
                calltime = time.strptime(rowvalue[4], "%H:%M:%S")
                time_called += calltime.tm_hour * 3600 + calltime.tm_min * 60 + calltime.tm_sec
            elif rowvalue[2] == '主叫':
                calltime = time.strptime(rowvalue[4], "%H:%M:%S")
                time_call += calltime.tm_hour * 3600 + calltime.tm_min * 60 + calltime.tm_sec
    print("主叫时长:{0} seconds".format(time_call))
    print("被叫时长:{0} seconds".format(time_called))
    print("全部通话时长:{0} seconds".format(time_called+time_call))


if __name__ == "__main__":
    excel_path = "tellist.xlsx"
    cal_call_time(excel_path)







