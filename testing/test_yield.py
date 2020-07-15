# -*- coding: utf-8 -*-
# @Time : 2020/7/14 21:15
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : test_yield.py
# @Software: PyCharm
# yield 生成器

def fun():
    for i in range(3):
        print(f'i = {i}')
        yield  # return 同时相当于暂停并且记住上次执行的位置


next(f)
