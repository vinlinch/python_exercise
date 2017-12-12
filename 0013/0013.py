#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)


#urllib模块提供了读取Web页面数据的接口
import urllib
import urllib.request
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
def getHtml(url):
    page = urllib.request.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html):
    html = html.decode('utf-8')  # python3
    reg = r'src="(.+?\.jpg)" pic_ext'    #正则表达式，得到图片地址
    # imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(reg, html)
    # imglist = imgre.findall(html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    return  imglist

def save_pic(pics, path):
    x=0
    for pic in pics:
        urllib.request.urlretrieve(pic, '%s/%s.jpg' % (path,x))
        x += 1

if __name__ == "__main__":
    path = 'pic/'
    html = getHtml("http://tieba.baidu.com/p/2166231880")
    save_pic(getImg(html), path)