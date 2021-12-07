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
import packages.demo
packages.demo.show()
print("="*36)