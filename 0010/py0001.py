#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片


import string
import random

def gene_active_code(number_of_code, str_len):
    # generate a str list with 26 upper alphabeta and  10 digits
    choose_str = string.ascii_uppercase + string.digits

    # re shuffle the string, is this necessary?
    seq = list(choose_str)
    random.shuffle(seq)

    code_set = set()
    while len(code_set) < number_of_code:
        code_set.add(''.join(random.choices(seq, weights=None, k=str_len)))

    # print("%d active code were generated. " % len(code_set))
    return list(code_set)

if __name__ == "__main__":
    # defing 200 active code
    number_of_code = 200
    # define 16 length string
    str_len = 16
    # print (string.ascii_uppercase,string.digits)
    codes = gene_active_code(number_of_code, str_len)
    print(codes)