# -*- coding: utf-8 -*-
# @Time : 2020/7/15 0:05
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : conftest.py
# @Software: PyCharm
import pytest


@pytest.fixture()
# autouse=True,params=['guowendong','luzhixiang','huangcanling'])#scope=session,module这里决定了这个文件执行作用域！
# autouse代表在每个方法（函数都会被调用到！
def login(request):
    print('登录方法')
    print(request.param)
    # yield 会激活fixture 的teardown
    yield ['username', 'password']
    print('GUOwendong')
