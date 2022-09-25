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

"""
        案例五十 __main__.py文件的用途

"""
print(f'{"案例五十 __main__.py文件的用途" :^30s}' + "\n")
print(f' 命令终端运行:python3 -m demo')
print("="*36)

"""
        案例五十一 基于名称空间的包

"""
print(f'{"案例五十一 基于名称空间的包" :^30s}' + "\n")
from model_2_1_51 import mod_1,mod_2
mod_1.test_fun_a()
mod_2.test_fun_b()
print("="*36)

"""
        案例五十二 __package__属性

"""
print(f'{"案例五十二 __package__属性" :^30s}' + "\n")
from model_2_1_52 import pack1,pack2
print(f' pack1的__page__属性:{pack1.__name__}')
print(f' pack2的__page__属性:{pack2.__package__}')
print("="*36)

"""
        案例五十三 自定义包或模块的搜索路径

"""
print(f'{"案例五十二 __package__属性" :^30s}' + "\n")
print(" 将demo目录移动任意地方,通过模块.path.insert(0,r地址)添加自定义查找路径")
print("="*36)

"""
        案例五十四 从.zip文件中导入包

"""
print(f'{"案例五十四 从.zip文件中导入包" :^30s}' + "\n")
import sys
sys.path.append("model_2_1_54.zip")
from model_2_1_54 import func
func()
print("="*36)

"""
        案例五十五 检查是否能够导入某个模块

"""
print(f'{"案例五十五 检查是否能够导入某个模块" :^30s}' + "\n")
#find_spec('A','B') A包里面存在B模块,通过绝对路径查找
#find_spec('.B','A') 通过相对路径查找
from importlib.util import find_spec
result = find_spec('sys')
print(f' 模块sys{"能"if result else "不能"}被导入')
result = find_spec('js_test')
print(f' 模块js_test{"能"if result else "不能"}被导入')
print("="*36)

"""
        案例五十六 使用import_module函数导入模块

"""
print(f'{"案例五十六 使用import_module函数导入模块" :^30s}' + "\n")
import importlib
dm = importlib.import_module('model_2_1_56.demo')
dm.happy()
print("="*36)

"""
        案例五十七 重新载入模块

"""
print(f'{"案例五十七 重新载入模块" :^30s}' + "\n")
print("="*36)