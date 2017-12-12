#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
#
# 步骤：参考0006题的遍历，主要是判断空行和注释行
# 1.这里我的空行标记为\r\n, windoes环境 ；注释行只统计了单行带有#的注释；其它为代码行
# 2.先统计每个文件的行数，存储在字典
# 3.遍历文件所有文件，行数和文件数求和
from collections import Counter
import os
import re



def count_lines(file_name):
    script_line = 0
    comment_line = 0
    space_line = 0
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            if line.strip():
                space_line = space_line + 1
                continue

            if line == '\r\n':
                space_line = space_line +1
            elif line.strip().find( '#') >=0:
                comment_line = comment_line +1
            else:
                script_line = script_line + 1

    return dict({'script_line':script_line,
                 'comment_line': comment_line,
                 'space_line': space_line, })



def count_program_lines(src):
    script_line = 0
    comment_line = 0
    space_line = 0

    for file in os.listdir(src):
        file_path = os.path.join(src, file)
        lines = count_lines(file_path)
        script_line = lines['script_line'] + script_line
        comment_line = lines['comment_line'] + comment_line
        space_line = lines['space_line'] + space_line
    return dict({'script_line':script_line,
                 'comment_line': comment_line,
                 'space_line': space_line, })

if __name__ == "__main__":
    src = 'scripts/'
    print(src)
    a = count_program_lines(src)
    for key, value in a.items():
        print('{0}: {1}\n'.format(key, str(value)))


