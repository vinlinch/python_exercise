#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 0001 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？
import string
import random



def gene_active_code(number_of_code, str_len):
    # generate a str list with 26 upper alphabeta and  10 digits
    choose_str = string.ascii_uppercase + string.digits

    # re shuffle the string, is this necessary?
    seq = list(choose_str)
    random.shuffle(seq)
    # f_seq = ''.join(seq)
    # print(f_seq

    # use random to generate random str
    # random.choices(population, weights=None, *, cum_weights=None, k=1) 3.6版本新增。从population集群中随机抽取K个元素（可重复）。
    # random.sample(population, k)   从population样本或集合中随机抽取K个不重复的元素形成新的序列。常用于不重复的随机抽样。

    # use set for distinct code
    # use len to check number of code
    code_set = set()
    while len(code_set) < number_of_code:
        # random.choices(f_seq, str_len)
        code_set.add(''.join(random.choices(seq, weights=None, k=str_len)))

    # print("%d active code were generated. " % len(code_set))
    return list(code_set)

if __name__ == "__main__":
    # defing 200 active code
    number_of_code = 200
    # define 16 length string
    str_len = 16
    # print (string.ascii_uppercase,string.digits)
    codes = gene_active_code(number_of_code,str_len)
    print(codes)