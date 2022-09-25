"""
        描述符

"""

"""
        案例一百八十一 描述符的协议方法

"""
from asyncio import exceptions


print(f'{"案例一百八十一 描述符的协议方法" :^30s}' + "\n")
# 存在以下方法的类别称为描述符
# __get__(): 获取属性值时调用
# __set__(): 设置属性值时调用
# __delete__(): 删除属性时调用
# __set_name__(): 当描述符被实例化并赋值给某个属性时调用
# 使用描述符时,描述符的对象要存储在当前对象的父级对象的变量字典中
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
class my_property:
    def __get__(self,obj,type):
        print(' getting value......')
        if obj is None:
            return self
        if not hasattr(self,'_val'):
            return None
        return self._val
    def __set__(self,obj,value):
        print(' setting value......')
        self._val = value
class cust_meta(type):
    max_count = my_property()
    min_count = my_property()
class demo(metaclass=cust_meta):
    pass
demo.max_count = 999
demo.min_count = 1
print(f' max_count: {demo.max_count} min_count: {demo.min_count}')
print("="*36)
"""
        案例一百八十三 防止描述符被替换

"""
print(f'{"案例一百八十三 防止描述符被替换" :^30s}' + "\n")
class my_descriptor:
    def __init__(self,default=None) -> None:
        self.val = default
    def __get__(self,obj,type):
        print(' getting value......')
        if obj is None:
            return self
        return self.val
    def __set__(self,obj,value):
        print(' setting value......')
        self.val = value
class meta_sam(type):
    def __setattr__(self,name,value):
        if hasattr(self,name):
            p = getattr(self,name)
            if hasattr(p,'__get__') or hasattr(p,'__set__'):
                if type(p) == type(value):
                    super().__setattr__(name,value)
        else:
            super().__setattr__(name,value)
class demo(metaclass=meta_sam):
    x = my_descriptor(-1)
    y = my_descriptor(-1)
demo.x = 'abc'
demo.y = 0.009
demo.z = 2
print(f' x:{type(demo.x)} x = {demo.x.val} y:{type(demo.y)} z:{type(demo.z)}')
demo.x = my_descriptor(1)
print(f' x:{type(demo.x)}, x = {demo.x.val}')
print("="*36)
"""
        案例一百八十四 实现基于特定类型的描述符

"""
print(f'{"案例一百八十四 实现基于特定类型的描述符" :^30s}' + "\n")
class typed_descr:
    def __init__(self,valType,default):
        if not isinstance(valType,type):
            raise TypeError(' valType参数必须是类型')
        if not isinstance(default,valType):
            raise TypeError(' 默认值的类型与valType参数提供的类型不匹配')
        self._type = valType
        self.val = default
    def __get__(self,obj,otype):
        if obj is None:
            return self
        return self.val
    def __set__(self,obj,value):
        if not isinstance(value,self._type):
            raise TypeError('所提供的值不符合类型要求')
        self.val = value
class test0:
    p1 = typed_descr(float,0.0)
    p2 = typed_descr(str,'...')
v = test0()
try:
    v.p1 = b'abc'
except Exception as ex:
    print(f' 错误:{ex}')
v.p2 = 'hello'
print(f' p2: {v.p2}')
print("="*36)
"""
        案例一百八十五 如何让对象属性存储独立的值

"""
print(f'{"案例一百八十五 如何让对象属性存储独立的值" :^30s}' + "\n")
class my_descr0:
    def __set_name__(self,owner,name):
        self.fd_name = f'_{owner.__name__}_{name}'
    def __get__(self,obj,objType):
        if obj is None:
            return self
        if not hasattr(obj,self.fd_name):
            return None
        return getattr(obj,self.fd_name)
    def __set__(self,obj,value):
        if obj is not None:
            setattr(obj,self.fd_name,value)
class demo0:
    x = my_descr0()
d1 = demo0()
d2 = demo0()
d1.x = 999
d2.x = 888
print(f' d1.x: {d1.x} d2.x: {d2.x}')
print(f' d1.__dict__: {vars(d1)}')
print(f' d2.__dict__: {vars(d2)}')
print("="*36)
"""
        案例一百八十六 使用property类封装属性值

"""
print(f'{"案例一百八十六 使用property类封装属性值" :^30s}' + "\n")
class pet:
    def __init__(self) -> None:
        self._name = ''
        self._age = 0
        self._owner = ''
    # name
    def _get_name_(self):
        return self._name
    def _set_name_(self,value):
        self._name = value
    def _del_name_(self):
        del self._name
    name = property(fget=_get_name_,fset=_set_name_,fdel=_del_name_,doc='宠物名称')
    # age
    def _get_age_(self):
        return self._age
    def _set_age_(self,value):
        self._age = value
    def _del_age_(self):
        del self._age
    age = property(fget=_get_age_,fset=_set_age_,fdel=_del_age_,doc='宠物年龄')
    # owner
    def _get_owner_(self):
        return self._owner
    def _set_owner_(self,value):
        self._owner = value
    def _del_owner_(self):
        del self._owner
    owner = property(fget=_get_owner_,fset=_set_owner_,fdel=_del_owner_,doc='宠物主人')
p = pet()
p.name = 'Tom'
p.age = 2
p.owner = 'Jirry'
print(f' name:{p.name}, age:{p.age},owner:{p.owner}')
print("="*36)
"""
        案例一百八十七 将property类作为装饰器使用

"""
print(f'{"案例一百八十七 将property类作为装饰器使用" :^30s}' + "\n")
class report:
    # id
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        self._id = value
    # caption
    @property
    def caption(self):
        return self._caption
    @caption.setter
    def caption(self,value):
        self._caption = value
    # voltage
    @property
    def voltage(self):
        return self._voltage
    @voltage.setter
    def voltage(self,value):
        self._voltage = value
p = report()
p.id = 99999
p.caption = 'some data'
p.voltage = 100.8
print(f' id:{p.id},caption:{p.caption},voltage:{p.voltage}')
print("="*36)
"""
        案例一百八十八 在模块中使用描述符

"""
print(f'{"案例一百八十八 在模块中使用描述符" :^30s}' + "\n")
import test_mode
test_mode.remark = '备注信息'
print(f' remark:{test_mode.remark}')
print("="*36)