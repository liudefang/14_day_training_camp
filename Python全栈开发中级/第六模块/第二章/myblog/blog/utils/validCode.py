# -*- encoding: utf-8 -*-
# @Time    : 2018-09-24 20:52
# @Author  : mike.liu
# @File    : validCode.py
import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_valid_code_img(request):
    # 方式1:
    # with open("lufei.jpg", "rb") as f:
    #     data = f.read()

    # 方式2: # pip install pillow

    # from PIL import Image
    # img = Image.new("RGB", (270, 40),color=get_random_color())
    #
    # with open("validCode.png", "wb") as f:
    #     img.save(f,"png")
    #
    # with open("validCode.png", "rb") as f:
    #     data = f.read()

    # 方式3:

    # from PIL import Image
    # from io import BytesIO
    #
    # img = Image.new("RGB", (270, 40), color=get_random_color())
    # f = BytesIO()
    # img.save(f, "png")
    # data=f.getvalue()

    # 方式4:

    img = Image.new("RGB", (270, 40), color=get_random_color())

    draw = ImageDraw.Draw(img)

    kumo_font = ImageFont.truetype("static/font/KumoFont.ttf", size=20)

    valid_code_str = ""
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(95, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((20 + i * 50, 15), random_char, get_random_color(), font=kumo_font)

        # 保存验证码字符串
        valid_code_str += random_char

    # width = 270
    # height = 40
    # for i in range(5):
    #     x1 = random.randint(0, width)
    #     x2 = random.randint(0, width)
    #     y1 = random.randint(0, height)
    #     y2 = random.randint(0, height)
    #     draw.line((x1, y1, x2, y2), fill=get_random_color())
    #
    # for i in range(10):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x+4, y+4), 0, 90, fill=get_random_color())

    print("valid_code_str", valid_code_str)
    request.session["valid_code_str"] = valid_code_str

    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()

    return data
