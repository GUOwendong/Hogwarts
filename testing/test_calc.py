# -*- coding: utf-8 -*-
# @Time : 2020/7/12 13:22
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : test_calc.py
# @Software: PyCharm
# 测试文件
import sys

import pytest

print(sys.path.append('..'))

from pythoncode.calc import Calculator


def setup_module():  # 首先执行的是模块级别的setup
    print('模块级别setup')


def teardown_module():
    print('模块级别的teardown')


def setup_function():
    print('函数级别 setup')


def teardown_function():  # 类外面的叫函数
    print('函数级别 teardown')


def test_case1():
    print('testcase1')


class TestCalc:
    # setup_class,teardown_class每个类开始和结束分别执行
    def setup_class(self):  # 类里面的叫方法,进行大型的数据初始化
        print('类级别 setup')

    def teardown_class(self):
        print('类级别 teardown')

    # setup和teardown在每个方法前后都会被执行
    def setup(self):  # 只是对某个方法进行初始化
        self.cal = Calculator()
        print('setup')

    def teardown(self):
        print('teardown')

    @pytest.mark.important  # 为我们的测试用例做个标记，因为有限测试用例比较重要
    @pytest.mark.parametrize('a,b,result', [  # 进行参数化，传参，切记给参数加单引号
        (1, 1, 2),
        (2, 2, 4),
        (100, 100, 200),
        (0.1, 0.1, 0.2),
        (-1, -1, -2),
        (99, 99, 198)
    ]
        , ids=['guowendong', 'liuxiaoying', 'shengshuangyan', 'wuzhengyun', 'luzhixiang', 'huangcanling'])
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    @pytest.mark.important
    def test_add1(self):
        # cal = Calculator()
        assert 5 == self.cal.add(3, 2)

    @pytest.mark.easy
    def test_div(self):
        # cal = Calculator()
        assert 1 == self.cal.div(1, 1)
