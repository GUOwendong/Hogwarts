# -*- coding: utf-8 -*-
# @Time : 2020/7/15 0:24
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : test_cart.py
# @Software: PyCharm
import pytest


def test_cart1(login):
    print('购物车测试用例1')


def test_cart2(login):
    print('购物车测试用例2')


# 参数化结合fixture使用
# 情况一：传入值 和数据
# 情况二：传入一个fixture的方法，将数据传入到fixture方法中，fixture方法使用request参数来接收这组数据，在方法体里面使用'''request.param'''来使用这个数据

@pytest.fixture()
def fun():
    print('这是另一个fixture')


@pytest.fixture()
def fun1():
    print('这是另一个fixture1')


@pytest.mark.parametrize('login', [
    ('username', 'password'),
    ('username1', 'password1')
], indirect=True)
@pytest.mark.parametrize('a,b', [
    (1, 3),
    (2, 3)
])
def test_cart3(login, fun, fun1, a, b):
    print('购物车测试用例3')
    print(login)


@pytest.mark.parametrize('x', [1, 2, 3])
@pytest.mark.parametrize('y', [2, 3, 4])
def test_data(x, y):
    print(x, y)
