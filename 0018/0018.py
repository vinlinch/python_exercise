#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：
#
# <?xmlversion="1.0" encoding="UTF-8"?>
# <root>
#     { "1" : "上海", "2" : "北京", "3" : "成都" }
# 步骤
# 1.使用xlrd读取excel文件内容到json类型对象
# 2.使用 xlm minidom创建xlmnode,常规文件write保存

import xlrd
from collections import OrderedDict
from xml.dom import minidom
import json
# import HTMLParser
import html

def readtojson(file):
    with xlrd.open_workbook(file) as f:
        sheet = f.sheet_by_index(0)
        row_n = sheet.nrows
        col_n = sheet.ncols
        d = OrderedDict()
        for i in range(row_n):
            rowvalue = sheet.row_values(i)
            # print(rowvalue)
            d[rowvalue[0]] = rowvalue[1]
        return d

class makexml():
    def __init__(self,xml_path):
        self.xml_path = xml_path
        self.dom = minidom.DOMImplementation().createDocument(None,'root',None)
        self.root = self.dom.documentElement

    def create_node(self,node_name, node_text='', comment=''):
        newtextnode = self.dom.createTextNode(comment + node_text)
        new_node = self.dom.createElement(node_name)
        new_node.appendChild(newtextnode)
        self.root.appendChild(new_node)


    def add_child(self,json_obj, comment='', node_name='citys'):
        text = json.dumps(json_obj, ensure_ascii=False,indent=4)
        # print(text)
        self.create_node(node_name, text, comment)

    def save_xml(self):
        with open(self.xml_path, 'w', encoding="utf-8") as f:
            f.write( html.unescape( self.dom.toxml()))

if __name__ == "__main__":
    excel_path = "city.xlsx"
    xml_path = "city.xlm"
    comment = ''

    newxml = makexml(xml_path)
    newxml.add_child(readtojson(excel_path), comment)
    newxml.save_xml()
    # print(readtojson(excel_path))






