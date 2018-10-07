# -*- encoding: utf-8 -*-
# @Time    : 2018-10-03 11:24
# @Author  : mike.liu
# @File    : validCode.py
import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def getRandomColor():
    '''获取一个随机颜色(r,g,b)格式的'''
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return c1, c2, c3


def getRandomStr():
    '''获取一个随机字符串，每个字符串的颜色也是随机的'''
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
    return random_char


def getValidCodeImg(request):
    # 获取一个Image对象，参数分别是rgb模式。宽150，高40，随机颜色
    image = Image.new('RGB', (150, 40), color=getRandomColor())

    # 获取一个画笔对象，将图片对象传过去
    draw = ImageDraw.Draw(image)

    # 获取一个font字体对象参数时ttf的字体文件的目录，以及字体的大小
    font = ImageFont.truetype("static/font/KumoFont.ttf", size=32)

    temp = []
    for i in range(5):
        # 循环5次，获取5个随机字符串
        random_char = getRandomStr()

        # 在图片上一次写入得到的随机字符串，参数是：定位，字符串，颜色，字体
        draw.text((10+i*30, -2), random_char, getRandomColor(), font=font)

        # 保存随机字符，以供验证用户输入的验证码是否正确使用
        temp.append(random_char)

    valid_code_str = "".join(temp)

    # 噪点噪线
    # 划线
    for i in range(3):
        x1 = random.randint(0, 150)
        x2 = random.randint(0, 150)
        y1 = random.randint(0, 40)
        y2 = random.randint(0, 40)
        draw.line((x1, y1, x2, y2), fill=getRandomColor())

    # 画点
    for i in range(20):
        draw.point([random.randint(0, 150), random.randint(0, 30)], fill=getRandomColor())
        x = random.randint(0, 150)
        y = random.randint(0, 30)
        draw.arc((x, y, x+4, y+4), 0, 90, fill=getRandomColor())

    request.session["valid_code_str"] = valid_code_str
    # 在内存生成图片
    f = BytesIO()
    image.save(f, 'png')
    data = f.getvalue()

    return data
