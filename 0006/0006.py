#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
#
# 按所有空白字符来切割：\s（[\t\n\r\f\v]）\S（任意非空白字符[ ^\t\n\r\f\v]
# 步骤：
# 1.统计每个文件中每个单词的频率，输出 word:count字典;把所有英文单词都转换成小写。
# 2.排除常用介词，冠词，代词后，找出最个频率的词和频率
# 3.遍历所有文件，输出每个文件的最高频率单词

from collections import Counter
import os
import re

filter_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that',
             'this', 's', 'is', 'are', 'a', 'with', 'as', 'an','it','i','on','at']


def count_words(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        pat = r"[a-z']+"
        str_list = re.findall(pat, f.read().lower())
        str_trimspace = [s for s in str_list if s and s not in filter_word]

    return Counter(str_trimspace)

def get_important_word(file_name):
    word_dicts = count_words(file_name)
    max_value = max(word_dicts.values())
    important_words = dict(
        [(key, value) for key, value in word_dicts.items()
         if value == max_value]
    )

    return important_words

def list_dairy_important_words(src):
    file_dicts = {}
    for file in os.listdir(src):
        try:
            file_path = os.path.join(src, file)
            file_dicts[file] = get_important_word(file_path)
        except:
            continue
    return file_dicts

def format_dict(dict):
    sum = 0
    for key, value in dict.items():
        print("file {0}'s important:".format(key))
        sum = sum + len(value)
        for key, value in value.items():
            print("     {0}: {1}".format(key,value))

    print('Total {0} files, total {1} important words.'.format( len(dict),sum))


if __name__ == "__main__":
    result_file = "filtered_words.txt"
    # dirpath = os.path.abspath(os.path.dirname(__name__))
    # src = dirpath + '/dairy/'
    src = 'dairy/'
    print(src)
    a = list_dairy_important_words(src)
    format_dict(a)
    with open(result_file, 'w') as f:
        for key, value in a.items():
            f.write('{0}: {1}\n'.format(key, str(value)))


