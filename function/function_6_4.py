"""
        装饰器

"""

"""
        案例一百五十九 将函数对象作为参数传递

"""
from sys import version_info


print(f'{"案例一百五十九 将函数对象作为参数传递" :^30s}' + "\n")

def demo_fun_7(s):
    print(s)
def other_fun(func):
    print(f' 参数对象: {func}')

other_fun(demo_fun_7)

print("="*36)

"""
        案例一百六十 嵌套的函数定义

"""
print(f'{"案例一百六十 嵌套的函数定义" :^30s}' + "\n")

def first_demo():
    def second_demo():
        return 88
    def third():
        return 999
    return second_demo() + third()

x = first_demo()
print(f' x = {x}\n')

def outer():
    print('{}函数被调用'.format(outer.__name__))
    def inner():
        print('{}函数被调用'.format(inner.__name__))
    return inner

the_fun = outer()
the_fun()

print("="*36)

"""
        案例一百六十一 实现简单的装饰器

"""
print(f'{"案例一百六十一 实现简单的装饰器" :^30s}' + "\n")
#存在一个可用接收其他函数引用的参数
def my_decor(fun):
    print(' 装饰器被应用,目标对象: {}'.format(fun))
    return fun
@my_decor
def demo_decor():
        print(' {}函数被调用'.format(demo_decor.__name__))
print(f' demo_decor : {demo_decor}')
demo_decor()

print("="*36)

"""
        案例一百六十二 限制调用函数的Python版本

"""
print(f'{"案例一百六十二 限制调用函数的Python版本" :^30s}' + "\n")

class versionError(Exception):
    pass
def py_vers_limited(major=3,minor=5):
    def _inner(func):
        def __infunc(*args,**kwargs):
            import sys
            vs = sys.version_info
            if vs.major <major:
                raise versionError('版本过低')
            elif vs.major == major and vs.minor < minor:
                raise versionError('版本过低')
            func(*args,**kwargs)
        return __infunc
    return _inner
@py_vers_limited(major=3,minor=6)
def demo_1():
    print(' {}函数被调用'.format(demo_1.__name__))
@py_vers_limited(major=3,minor=8)
def demo_2(x,y,z):
    print(' {}函数被调用'.format(demo_2.__name__))
    print(f'参数: x= {x}, y= {y}, z= {z}\n')

try:
    demo_1()
except Exception as ex:
    print(f'错误信息: {ex}')

try:
    demo_2(-1,-2,-3)
except  Exception as ex:
    print(f'错误信息: {ex}')

print("="*36)

"""
        案例一百六十三 实现只能使用三次的装饰器

"""
print(f'{"案例一百六十三 实现只能使用三次的装饰器" :^30s}' + "\n")

class limited_decorator:
    _count = 0
    def __new__(cls,func):
        cls._count += 1
        if cls._count > 3:
            raise Exception('装饰器已被使用过三次')
        self = object.__new__(cls)
        self._func = func
        return self
    def __call__(self, *args, **kwds):
        if self._func is not None:
            return self._func(*args,**kwds)

@limited_decorator
def add(a,b):
    return a+b
@limited_decorator
def sub(a,b):
    return a-b
@limited_decorator
def mul(a,b):
    return a * b
@limited_decorator
def div(a,b):
    return a / b
print("="*36)
