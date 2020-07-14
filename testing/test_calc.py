# -*- coding: utf-8 -*-
# @Time : 2020/7/12 13:22
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : test_calc.py
# @Software: PyCharm
# 测试文件

from pythoncode.calc import Calculator


def test_add():
    cal = Calculator()
    assert 2 == cal.add(1, 1)
