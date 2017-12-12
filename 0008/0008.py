#!python2.7.14
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0008 题： 一个HTML文件，找出里面的正文。
# 步骤：
# 1. 参考了解gits上的goose项目，安装后, 获取cleaned_text网页正文

import sys
from goose import Goose
from goose.text import StopWordsChinese
reload(sys)
sys.setdefaultencoding("utf-8")

def get_url_extract_body_text(url, config=None):
    # url ="https://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2"
    if config:
        g = Goose(config)
    else:
        g = Goose()
    article = g.extract(url=url)
    return article.cleaned_text

if __name__ == "__main__":
    # url = 'http://www.ruanyifeng.com/blog/2015/05/thunk.html'
    url = 'http://blog.csdn.net/tina_ttl/article/details/51830845'
    print get_url_extract_body_text(url)







