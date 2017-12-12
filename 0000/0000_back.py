from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
font = ImageFont.truetype("simsun.ttc",36)
text ="4"
pic = "linjie.jpg"
linjie = Image.open(pic)

a = Image.new("RGB",[1024,768],"white")
b = Image.new("RGB",[1024,768],"white")
p1 =(100,100)
p2 =(600,600)
p3 =(600,100)
p4 =(100,600)
g1 =(600,400)
# a.show()
dg = ImageDraw.Draw(a)
dg.line([p1,p4],fill=10)
dg.line([p1,p3],fill=60)
dg.line((p3,p2),"black")
dg.line((p4,p2), "red")
#画一个60度蓝色圆弧
dg.arc((p1,p2),0,90,fill="blue")
#画一个上半圆弧
dg.arc((p1,p2),180,360,fill="red")
#画一个右半椭圆，只需改区域大小为长方形
dg.arc((p1,g1),0,360,fill="green")
# 用法同arc，用于画圆（或者椭圆
dg.ellipse((p1,p2),outline=128)
# dg.ellipse((100,250,600,450),fill="pink")

# 画一个圆，并在园内画弦示例如下：
#画一条弦
dg.chord((p1,p2),0,90,outline="red")
dg.chord((p1,p2),90,180,fill="red")

#在上一行画出的园内画180度到210度的扇形区域轮廓
dg.pieslice((p1,p2),60,90,fill="blue")

# ，python会根据第一个参量中的xy坐标对，连接出整个图形
x1, x2, x3  = (200,200),(600,300),(300,600)
y1,y2,y3,y4 = (300,300),(500,300),(300,500),(500,500)
dg2 = ImageDraw.Draw(b)
dg2.polygon((x1, x2, x3),outline="red")
dg2.polygon((y1,y2,y3,y4),fill="red")

#画矩形
dg2.rectangle((250,300,450,400),fill="red")
dg2.rectangle((200,200,500,500),outline=128)
# a.show()
text = "4"
dg2.text((300,350),text,"blue")
print (dg2.textsize(text))
b.show()