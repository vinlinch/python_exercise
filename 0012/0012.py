#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
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
        return f.read().split('\n')

def replace_words(sentence, filter_word):
    for word in filter_word:

        if sentence.find(word) > -1:
            sentence = sentence.replace(word,'**')

    return sentence

if __name__ == "__main__":
    filter_file = "filtered_words.txt"
    filter_words = get_filter_words(filter_file)
    print(filter_words)

    while True:
        iw = input("please input a word: ")
        print(replace_words(iw,filter_words))

        end_flag = input("want end?(Y/N): ")
        if end_flag.lower() == 'y':
            break





