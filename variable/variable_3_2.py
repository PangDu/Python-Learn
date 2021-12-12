"""
        案例六十四 获取全局名称空间的字典

"""
print(f'{"案例六十四 获取全局名称空间的字典" :^30s}' + "\n")
#不管在模块调用globals()还是函数(或类)内部调用,始终返回全局名称空间的字典
other_dic = globals().copy()
for name,value in other_dic.items():
    print(f'{name} : {value}')

other_dic = {k:v for k,v in globals().items()}
for name,value in other_dic.items():
    print(f'{name} : {value}')

other_dic = {** globals()}
for name, value in other_dic.items():
    print(f'{name} : {value}')

var1 = 'label'
var2 = None
var3 = 3456
var4 = True

def func_1():
    pass

def func_2():
    pass

class members:
    pass

gdic = globals()

__dic = {key:value for key,value in gdic.items() if not key.startswith('_')}
for name in __dic:
    print(f'{name} : {__dic[name]}')
print("="*36)

"""
        案例六十五 获取局部名称空间的字典

"""
print(f'{"案例六十五 获取局部名称空间的字典" :^30s}' + "\n")
def test():
    item1 = b'f36e03'
    item2 = 'daerw'
    item3 = 3.2322
    item4 = 98

    def inner():
        pass
    _dic = {**locals()}
    print("test 函数中局部变量:")
    for key in _dic:
        print(f'{key} : {_dic[key]}')

test()

class demo:
    m_1 = 1
    m_2 = 2
    def do_something(self):
        pass
    dic = {**locals()}

v = demo()
v.a = 0.98
v.b = 1.67

for k,v in v.dic.items():
    print(f'{k} : {v}')
print("="*36)

"""
        案例六十六 直接更新名称空间字典

"""
print(f'{"案例六十六 直接更新名称空间字典" :^30s}' + "\n")
g_dic = globals()
g_dic['var_x'] = 'coding'
g_dic['var_y'] = 8888
g_dic['var_z'] = b'af7c32'

__dic = {key:value for key,value in gdic.items() if not key.startswith('_')}
for name in __dic:
    print(f'{name} : {__dic[name]}')
print("="*36)

"""
        案例六十七 使用global关键字声明变量

"""
print(f'{"案例六十七 使用global关键字声明变量" :^30s}' + "\n")
number = 10
def add_20():
    global number
    number += 20
def add_30():
    global number
    number += 30
add_20()
add_30()
print(f'number : {number}')
print("="*36)

"""
        案例六十八 使用nonlocal关键字声明变量

"""
print(f'{"案例六十八 使用nonlocal关键字声明变量" :^30s}' + "\n")
def somework():
    a = 'a'
    def inner1():
        nonlocal a
        a = 'b - ' + a
    def inner2():
        nonlocal a
        a = 'c - ' + a
    inner1()
    inner2()
    return a
print(somework())
print("="*36)