"""
        ------ 模块 ------

"""
"""
        案例三十八 独立运行模块

"""
print(f'{"案例三十八 独立运行模块" :^30s}' + "\n")
#python -m<模块名称>
#模块运行后，在代码文件同级目录下创建名为__pycache__的目录，目录下包含扩展名为.pyc的文件
#该文件是代码编译后生成的二进制文件
print("="*36)

"""
        案例三十九 导入模块

"""
print(f'{"案例三十九 导入模块" :^30s}' + "\n")
#improt<模块名称>[as<别名>]
print("="*36)

"""
        案例四十 使用from...improt语句导入模块

"""
print(f'{"案例四十 使用from...improt语句导入模块" :^30s}' + "\n")
print(f' 从某个模块中导入指定成员.\n')
print(f' 模块的相对路径一般用于包的导入.\n')
print(f' 路径使用点(.)来分割,只有一个点(.)表示导入当前包下的模块.\n')
print(f' 两个点(..)表示导入当前包的父级目录下的模块,以此类推.\n')
print(f'import *:把模块中的所有成员导入.\n')
print(f'命名中不以下划线(_)开头的,或者在__all__变量中声明的成员会被导入.\n')
print(f'------下面是模块调用!\n')

from model_2_1_40.mod_1 import work,MAX_MESSAGES
work()
print(f'{MAX_MESSAGES}\n')

from model_2_1_40.mod_2 import person as student, address as cityInfo
stu = student()
stu.name = "Jack"
city = cityInfo()
city.city = "北京"
print(f'{stu.name}来自于:{city.city}.\n')

from model_2_1_40.mod_3 import *
#globads函数:返回当前代码模块中所有全局变量,以字典的形式呈现.
#以下划线(_)开头的方法不会导入
dic = globals().copy()
keys = dic.keys()
for key in keys:
        print(key)
print("="*36)

"""
        案例四十一 __all__变量的使用

"""
print(f'{"案例四十一 __all__变量的使用" :^30s}' + "\n")
print(f'模块未定义__all__变量,from...improt * 不会导入以下划线(_)开头的成员.\n')
print(f'模块中定义__all__变量,from...import * 只导入__all__中列出的成员.\n')
print(f'__all__变量是字符串序列,如:列表、元祖.\n')

from model_2_1_41.demo_mod import *
keys = globals().copy().keys()
for key in keys:
        print(key)
print("="*36)

"""
        案例四十二 以编程方式生成__all__变量

"""
print(f'{"案例四十二 以编程方式生成__all__变量" :^30s}' + "\n")

from model_2_1_42.demo import *
dic = globals().copy()
keys = [k for k in dic.keys() if not k.startswith('_')]
for key in keys:
        print(key)
print("="*36)

"""
        案例四十三 为模块编写帮助文档

"""
print(f'{"案例四十三 为模块编写帮助文档" :^30s}' + "\n")

import model_2_1_43.test
print("以下是test模块的帮助文档:\n")
print(model_2_1_43.test.__doc__)
print("="*36)

"""
        案例四十四 特殊的模块名称 --- __main__

"""
print(f'{"特殊的模块名称 --- __main__" :^30s}' + "\n")
import model_2_1_44.demo
print("="*36)

"""
        案例四十五 __file__与__cached__属性

"""
print(f'{"案例四十五 __file__与__cached__属性" :^30s}' + "\n")
import model_2_1_45.demo
model_2_1_45.demo.demo_address()
print("="*36)