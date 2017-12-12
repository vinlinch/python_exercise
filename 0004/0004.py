#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0004 题: 任一个英文的纯文本文件，统计其中的单词出现的个数。
#
# 按所有空白字符来切割：\s（[\t\n\r\f\v]）\S（任意非空白字符[ ^\t\n\r\f\v]
#
# re.split(r'[\s]', line)
# ['abc', 'aa;bb,cc', '|', 'dd(xx).xxx', "12.12'", 'xxxx']
#
# 多字符匹配
# re.split(r'[;,]', line)
# 步骤：
# 1.统计每个文件中每个单词的频率，输出 word:count字典;把所有英文单词都转换成小写。
# 2.排除常用介词，冠词，代词后，找出最个频率的词和频率
# 3.遍历所有文件，输出每个文件的最高频率单词

from collections import Counter
import os
import re


def count_words(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        # r'[.:"\s]'
        str_list = re.split(r'[,.:"\s]',f.read().lower())
        # print(f.read())
        # str_list = f.read().split(" ")
        # trim space from list
        str_trimspace = [s for s in str_list if s]

    return Counter(str_trimspace)


if __name__ == "__main__":
    file_name = "words.txt"
    a = count_words(file_name)
    # [(key,a[key]) for key in sorted(a.keys())]
    for key in sorted(a.keys()):
        print(key,a[key])
    print(len(a),sum(a.values()))
    # for key ,value in a.items():
    #     print (key,value)
    # print(a)

