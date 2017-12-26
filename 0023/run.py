#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0023 题： 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。
from flask import Flask, request, render_template, url_for
import pymongo
import datetime

#连接配置信息
# get connection of mysql
app = Flask(__name__)

mongoClient = pymongo.MongoClient('localhost',27017)
db = mongoClient['msgboard']

# conn = pymongo.Connection('localhost',27017)
# msgboard = conn.msgboard
# msgboard.create_collection('msg')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', msglist=db['msg'].find())
    else:
        msg_collection = db['msg']
        time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        msg_collection.insert({
            'msg': request.form['msg'],
            'time': time
        })
        return render_template('index.html', msglist=db['msg'].find())

if __name__ == '__main__':
    app.run(debug=True)