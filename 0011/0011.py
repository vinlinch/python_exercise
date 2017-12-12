#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0011 题：  敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
#
# 北京
# 程序员
# 公务员
# 领导
# 牛比
# 牛逼
# 你娘
# 你妈
# love
# sex
# jiangge

from collections import Counter
import os
import re

def get_filter_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()

if __name__ == "__main__":
    filter_file = "filtered_words.txt"
    filter_words = get_filter_words(filter_file)

    while True:
        iw = input("please input a word: ")
        if iw in filter_words:
            print("Freedom\n")

        else:
            print("Human Rights.\n")

        end_flag = input("want end?(Y/N): ")
        if end_flag.lower() == 'y':
            break





