# -*- coding: utf-8 -*-
# @Time : 2020/7/14 20:06
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : test_login.py
# @Software: PyCharm

# 在执行test_case1前，执行login这个函数；这就是fixture的优势所在

def test_case1(login):
    print(f'case1 login = {login}')


def test_case2():
    print('case2')


def test_case3():
    print('case3')
