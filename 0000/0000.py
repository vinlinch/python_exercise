#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 0000 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
# 步骤：
# 1.image获取底层头像图片
# 2.使用imagedraw在image对象上画出数字，数值位置按照image个size标记在右边

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def draw_photo(font, text, pic):
    # open my handsome photo
    img = Image.open(pic)
    # point = (100,100)
    # print(img.size)
    text_sz = img.size[0] / 4

    # draw a text
    dg = ImageDraw.Draw(img)
    dg.text([img.size[0] - text_sz, text_sz], text, "red", font=font)
    # print pic
    # img.show()
    return img

if __name__ =="__main__":
    font = ImageFont.truetype("simsun.ttc", 72)
    text = "4"
    pic = "linjie.jpg"
    img = draw_photo(font, text, pic)
    img.show()