#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0003 题: 将 0001 题生成的 200 个激活码（或者优惠券）
# 保存到 Redis 非关系型数据库中。
# import sys
# sys.path.append("..")
# from 0001 import gene_active_code
# 步骤：
# 1.使用0001定义的函数生成激活码
# 2.使用 redis 模块插入数据到数据库

from py0001 import gene_active_code
import redis

#连接配置信息
# get connection of mysql
def inserrt_redis(config):
    r = redis.Redis(**config)

    # insert data

    codes = gene_active_code(200, 16)
    r.set("code",codes)


if __name__ == "__main__":
    config = {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0
    }
    inserrt_redis(config)
