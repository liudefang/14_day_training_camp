# -*- encoding: utf-8 -*-
# @Time    : 18-9-7 下午5:45
# @Author  : mike.liu
# @File    : converters.py

class FourDigitYearConverter:
    regex = '[0-9]{4}'
    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value