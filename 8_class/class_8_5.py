"""
        对象复制

"""

"""
        案例二百一十七 id()函数

"""
from abc import ABC
print(f'{"案例二百一十七 id()函数" :^30s}' + "\n")
#id()返回对象的唯一标识,用整数表示
#CPython()中,id()返回对象的内存地址
# id(a) == id(b) or a is b  判断是否引用同一个对象
a = 888
b = 888
print(f' 变量a对象标识: {hex(id(a))}')
print(f' 变量b对象标识: {hex(id(b))}')
print(f' a与b是否引用同一个对象: {"是" if id(a) == id(b) else "不是"}')

c = 'port'
d = 'port'
print(f' 变量c的对象标识: {hex(id(c))}')
print(f' 变量d的对象标识: {hex(id(d))}')
print(f' c与d是否引用同一个对象: {"是" if id(c)==id(d) else "不是"}')

s = ABC()
t = ABC()
m = t
print(f' 变量c的对象标识: {hex(id(s))}')
print(f' 变量t的对象标识: {hex(id(t))}')
print(f' s与d是不是引用同一个对象: {"是" if id(s)==id(t) else "不是"}')
print(f' m与t是不是引用同一个对象: {"是" if id(m)==id(t) else "不是"}')

print("="*36)

"""
        案例二百一十八 浅拷贝与深拷贝

"""
from copy import copy,deepcopy

print(f'{"案例二百一十八 浅拷贝与深拷贝" :^30s}' + "\n")
#浅拷贝仅复制对象本身
#深拷贝不仅复制对象本身,次对象中引用的其他对象也会递归式复制
#copy():浅拷贝 deepcopy():深拷贝
class addressInfo:
    def __init__(self,provice,city) -> None:
        self.provice = provice
        self.city = city
class person:
    def __init__(self,name,age,address) -> None:
        self.name = name
        self.age =age
        self.address = address
p0 = person('小米',18,addressInfo('广东','珠海'))
p1 = copy(p0)
print(f'''
------浅拷贝------
拷贝前:
    原person对象标识: {id(p0)}
    原person对象address属性所引用的对象标识: {id(p0.address)}
拷贝后:
    新person对象标识: {id(p1)}
    新person对象address属性所引用的对象标识: {id(p1.address)}
''')

p2 = deepcopy(p0)
print(f'''
------深拷贝------
拷贝前:
    原person对象标识: {id(p0)}
    原person对象address属性所引用的对象标识: {id(p0.address)}
拷贝后:
    新person对象标识: {id(p2)}
    新person对象address属性所引用的对象标识: {id(p2.address)}
''')

print("="*36)