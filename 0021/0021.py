#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
#  步骤： copy from https://www.pythoncentral.io/hashing-strings-with-python/
# 1. 使用hashlib.sha256做不可逆加密
# 2.使用uuid生成随机种子，作为salt 加密；存储hash后的密文和salt
# 3.验证时候，使用输入密码+salt再做一次hashlib.sha256加密，比较存储的密文是否相同

import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    print(salt)
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()



if __name__ =="__main__":
    new_pass = input('Please enter a password: ')
    hashed_password = hash_password(new_pass)
    print('The string to store in the db is: ' + hashed_password)
    old_pass = input('Now please enter the password again to check: ')
    if check_password(hashed_password, old_pass):
        print('You entered the right password')
    else:
        print('I am sorry but the password does not match')