#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
#
# {
# 	"1":["张三",150,120,100],
# 	"2":["李四",90,99,95],
# 	"3":["王五",60,66,68]
# }
# 请将上述内容写到 student.xls 文件中，如下图所示：
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
        for key,value in jsondict.items():
            j = 0
            ws.write(i,j,key)
            for v in value:
                j += 1
                ws.write(i, j, v)
            i += 1

def write_txt_to_excel(txt, excel):
    json_dict = load_json_file(txt)
    write_json_to_excel(json_dict, excel)

if __name__ == "__main__":
    excel_file = "student.xlsx"
    txt_file = "student.txt"
    write_txt_to_excel(txt_file, excel_file)





