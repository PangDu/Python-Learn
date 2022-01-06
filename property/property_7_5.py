"""
        描述符

"""

"""
        案例一百八十一 描述符的协议方法

"""
print(f'{"案例一百八十一 描述符的协议方法" :^30s}' + "\n")
class my_descr:
    def __init__(self,default = None):
        self._value = default
    #以下为描述符协议方法
    def __get__(self,obj,type):
        print(' gettting value ......')
        if obj is None:
            return self
        return self._value
    def __set__(self,obj,value):
        print(' setting value ......')
        self._value = value
class demoZ:
    a = my_descr(0)
    b = my_descr(0)
d = demoZ()
d.a = 100
d.b = 999
print(f' d.a = {d.a}\n d.b = {d.b}')

print("="*36)

"""
        案例一百八十二 作用于类级别的描述符

"""
print(f'{"案例一百八十二 作用于类级别的描述符" :^30s}' + "\n")

print("="*36)