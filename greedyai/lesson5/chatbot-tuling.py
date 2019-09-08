# -*- encoding: utf-8 -*-
# @Time    : 2019/9/4 22:38
# @Author  : mike.liu
# @File    : chatbot-tuling.py

from flask import Flask
import requests


app = Flask(__name__)
# 装饰器里面写的是访问的路径
@app.route("/greedyai/<data>")
def hello_world(data):

    if "帅" in data:
        return "mike.liu"
    elif "线上" in data:
        return "线上课程为主"
    elif "助教" in data or "服务" in data:
        return "为提高服务质量，课程配有专业的助教老师"
    elif "优势" in data:
        return "这你都问，mike.liu就是优势"
    elif "有效期" in data:
        return "只要你想学,我一直在你身边"
    else:
        return "你问的问题太难了，需要学习一下"
    return data


if __name__ == "__main__":
    app.run()
