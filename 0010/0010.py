#!python3.6.1
# -*- coding: utf-8 -*-
# author: https://github.com/vinlinch
# 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
# 步骤：
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
# from py0001 import gene_active_code
import string
import random

color_range = 200
text_color_start, text_color_end = 50, 150
def generatechar():
    """generate char"""
    return random.choice(string.ascii_letters + string.digits)

def generatecolor():
    """generate color"""
    return (random.randint(text_color_start, text_color_end), random.randint(text_color_start, text_color_end), random.randint( text_color_start, text_color_end))

def draw_photo(font):
    """draw a photo with randam char"""
    # create a photo
    width, height = 400, 60
    img = Image.new('RGB',(width, height),(color_range,color_range,color_range))

    dg = ImageDraw.Draw(img)
    # draw a text
    codes_number = 4
    point_distance = width/codes_number
    for i in range(codes_number):
        dg.text((point_distance * i + 10, 10), generatechar(), generatecolor(), font=font)
    # 填充噪点
    for i in range(random.randint(1000, 2000)):
        dg.point((random.randint(0, width), random.randint(0, height)), fill=generatecolor())
    # 模糊处理
    img = img.filter(ImageFilter.BLUR)
    file_name = ''.join(random.choices(string.ascii_letters+string.digits,weights=None,k=12)) + ".jpg"
    img.save('img/' + file_name)
    return img

if __name__ =="__main__":
    font = ImageFont.truetype("simsun.ttc", 48)
    img = draw_photo(font)
    img.show()