"""
        自定义的属性访问

"""

"""
        案例一百七十九 属性协议

"""
print(f'{"案例一百七十九 属性协议" :^30s}' + "\n")
#__getattribute__: 对象属性被访问时调用
#__getattr__: 只有当被访问的属性不存在时才调用.
#若类中同时定义__getattribute__和__getattr__,前者调用后不再调用后者,除非前者引发AttributeError异常
#__setattr__: 属性被赋值时调用
#__delattr__: 删除属性时调用

class test0:
    def __getattribute__(self, __name: str):
        print(f' {__name}属性被访问  __getattribute__')
        if __name.startswith('__'):
            raise AttributeError
        return object.__getattribute__(self,__name)
    def __getattr__(self,name):
        print(f' {name}属性被访问   __getattr__ 方法')
        return '其他属性值'
    def __setattr__(self, __name: str, __value) -> None:
        print(f' 设置属性: {__name} = {__value}  __setattr__ 方法')
        object.__setattr__(self,__name,__value)
    def __delattr__(self, __name: str) -> None:
        print(f' {__name}属性被删除  delattr 方法')
        object.__delattr__(self,__name)

p = test0()
p.content = 'abcde'
xa = p.content
p.__pipe = 1
xb = p.__pipe
del p.content

print("="*36)

"""
        案例一百八十 禁止访问模块中的特定成员

"""
print(f'{"案例一百八十 禁止访问模块中的特定成员" :^30s}' + "\n")
import sys
import types

class MemberAccessError(Exception):
    pass

class MyModule(types.ModuleType):
    def __getattribute__(self, __name):
        if __name.endswith('__prv'):
            raise MemberAccessError(f' {__name} 成员不允许访问')
        return super().__getattribute__(__name)
    def theFirst():
        pass
    def theTest__prv():
        pass
    min__prv = 0
    minimum = 0
    max__prv = 100
    maximum = 100

sys.modules[__name__].__class__ = MyModule

v = MyModule('v')
c = MyModule.minimum
print(f' c : {c}')

try:
   v.theTest__prv()
except Exception as ex:
    print(f' 错误: {ex}')

print("="*36)