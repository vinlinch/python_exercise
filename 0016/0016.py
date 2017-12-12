#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
#
# [
# 	[1, 82, 65535],
# 	[20, 90, 13],
# 	[26, 809, 1024]
# ]
# 请将上述内容写到 numbers.xls 文件中，如下图所示：
# 步骤
# 1.使用json读取txt文件内容到json类型对象
# 2.使用 xlsxwriter来写数据到excel

import xlwt
import xlsxwriter
import json

def load_json_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json_to_excel(jsondict, excel):
    # student.xls
    with xlsxwriter.Workbook(excel) as wb:
        ws = wb.add_worksheet("student")
        i = 0
        for lists in jsondict:
            j = 0
            for value in lists:
                ws.write(i,j,value)
                j += 1
            i += 1

def write_txt_to_excel(txt, excel):
    json_dict = load_json_file(txt)
    write_json_to_excel(json_dict, excel)

if __name__ == "__main__":
    excel_file = "number.xlsx"
    txt_file = "number.txt"
    write_txt_to_excel(txt_file, excel_file)





