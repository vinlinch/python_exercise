#!python2.7.14
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0009 题： 一个HTML文件，找出里面的链接。
# 步骤：
# 1. 参考0008的项目

import sys
from goose import Goose
# from goose.text import StopWordsChinese
reload(sys)
sys.setdefaultencoding("utf-8")

def get_url_extract_links(url, config=None):
    # url ="https://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2"
    if config:
        g = Goose(config)
    else:
        g = Goose()
    article = g.extract(url=url)
    # print('title is ', article.title)
    # print('cleaned_text is ', article.cleaned_text)
    # print('meta is ', article.meta_description)
    # print('link is', article.canonical_link)
    print('link is:')
    for link in article.links:
        print(link)

    # return article.links


if __name__ == "__main__":
    # url = 'http://www.ruanyifeng.com/blog/2015/05/thunk.html'
    url = 'https://github.com/grangier/python-goose'
    get_url_extract_links(url)







