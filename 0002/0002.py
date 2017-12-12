#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）
# 保存到 MySQL 关系型数据库中。
# import sys
# sys.path.append("..")
# from 0001 import gene_active_code
# 步骤：
# 1.使用0001定义的函数生成激活码
# 2.使用pymysql模块插入数据到数据库

import pymysql
from py0001 import gene_active_code

#连接配置信息
# get connection of mysql
def inserrt_mysql(config):
    conn = pymysql.connect(**config)

    # insert data
    try:
        codes = gene_active_code(200, 16)
        with conn.cursor() as cursor:
            sql = "INSERT INTO activate_code (code) VALUES (%s)"
            cursor.executemany(sql, codes)
        conn.commit()

    finally:
        conn.close()

if __name__ == "__main__":
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'linjie',
        'password': 'linjie',
        'db': 'test_python',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    inserrt_mysql(config)
