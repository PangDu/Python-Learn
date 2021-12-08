"""
        案例四十六 普通目录变成包

"""
print(f'{"案例四十六 普通目录变成包" :^30s}' + "\n")
import packages.demo
packages.demo.show()
print("="*36)

"""
        案例四十七 __init__.py文件

"""
print(f'{"案例四十七 __init__.py文件" :^30s}' + "\n")
import packages_my
packages_my.test_f1()
packages_my.test_f2()
print("="*36)

"""
        案例四十八 合并子模块的成员列表

"""
print(f'{"案例四十八 合并子模块的成员列表" :^30s}' + "\n")

from model_2_1_48 import *
numOne = add(23,9)
numTwo = sub(32,4)
numThree = mult(45,8)
numFour = div(345,9)
print(f'one = {numOne},two = {numTwo},three = {numThree}, four = {numFour}')
print("="*36)

"""
        案例四十九 合并多个__init__.py文件中的__all__属性

"""
print(f'{"案例四十九 合并多个__init__.py文件中的__all__属性" :^30s}' + "\n")
from model_2_1_49 import *
dic = globals().copy()
membs = [k for k in dic.keys()]
for name in membs:
        print(name)
print("="*36)
