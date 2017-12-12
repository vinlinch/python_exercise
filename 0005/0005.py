#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0005 题: 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
##
# .返回指定目录下的所有文件和目录名:os.listdir()
# .返回一个路径的目录名和文件名:os.path.split()     eg os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt')
# .分离扩展名：os.path.splitext()

# 步骤：
# 1.使用image操作图片,按照iPhone5 分辨率等比压缩 resize。
# 2.遍历所有图片，改变分别率后存入新的路径；非图片文件跳过

import os
import re
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True # 解决图片save时候提示的truncate错误


def reshape_image(img ,ppi):
    w, h = img.size
    # 等比压缩
    if w > ppi["width"]:
        h_new = ppi["width"] * h / w
        if h_new > ppi["height"]:
            h_new = ppi["height"]
            w_new = h_new * w / h
        else:
            w_new = ppi["width"]
    elif h > ppi["height"]:
        w_new = ppi["height"] * w / h
        if w_new > ppi["width"]:
            w_new = ppi["width"]
            h_new = w_new * h / w
        else:
            h_new = ppi["height"]
    else:
        w_new, h_new = w, h
    return img.resize((w_new,h_new),Image.ANTIALIAS)


def reshape_file(src, dst, ppi):
    """
    把src路径下的图片按照ppi压缩后转储到dst路径下
    :param src:
    :param dst:
    :return:
    """
    for file in os.listdir(src):
        try:
            img = Image.open(os.path.join(src,file))
            dst_name = os.path.join(dst, file )
        except:
            # print("{0} is not a picture.".format(file) )
            continue
        img_resize = reshape_image(img, ppi)
        img_resize.save(dst_name)
        print("{0} is success.".format(file))

if __name__ == "__main__":
    src = "image/src/"
    dst = "image/image_reshape/"
    iphone5_ppi = {"width": 1136, "height": 640}
    reshape_file(src, dst, iphone5_ppi)


