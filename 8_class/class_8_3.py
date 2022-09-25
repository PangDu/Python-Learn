"""
        元类

"""

"""
        案例一百九十七 使用type类创建新类型

"""
print(f'{"案例一百九十七 使用type类创建新类型" :^30s}' + "\n")

def _run(self):
    print(f' self: {self}')

members = {
    'one' : 1,
    'two' : 2,
    'run' : _run
}
G = type('G',(),members)
v = G()
print(f' 对象类型: {v.__class__}')
print(f' 对象成员: {dir(v)}')
v.run()

print("="*36)

"""
        案例一百九十八 元类的实现过程

"""
print(f'{"案例一百九十八 元类的实现过程" :^30s}' + "\n")

class my_meta(type):
        def __new__(cls,newType,bases,members):
                print(f' 元类: {cls.__name__}')
                print(f' 新类: {newType}')
                print(f' 基类: {bases}')
                print(f' 新类成员:')
                for k,v in members.items():
                        print(f' {k} : {v}')
                obj = type.__new__(cls,newType,bases,members)
                print(f'\n 元类的实例对象: {obj}')
                return obj
class Data(metaclass=my_meta):
        def get_init_count(slef):
                return 0
        default_pos = -1

Port = my_meta('Port',(Data,),{'x':888,'y':'999'})
print(Port)

print("="*36)

"""
        案例一百九十九 向元类传递参数

"""
print(f'{"案例一百九十九 向元类传递参数" :^30s}' + "\n")

class cust_meta(type):
        def __new__(cls,ntype,bases,members,flag=0):
                print(' 元类实例化')
                print(f' flag参数的值: {flag}')
                return type.__new__(cls,ntype,bases,members)
class demo(metaclass=cust_meta,flag=999):
        pass

print("="*36)

"""
        案例二百 元类与继承

"""
print(f'{"案例二百 元类与继承" :^30s}' + "\n")

class my_meta(type):
        def __new__(cls,newType,bases,members):
                print(f' 元类对象: {cls.__name__}')
                print(f' 正在创建 {newType}类,基类为: {bases}')
                return type.__new__(cls,newType,bases,members)
class Ball(metaclass=my_meta):
        pass
class FootBall(Ball):
        pass
class BasketBall(Ball):
        pass

print("="*36)

"""
        案例二百一 __prepare__方法

"""
print(f'{"案例二百一 __prepare__方法" :^30s}' + "\n")

class sorted_dict(dict):
        #获取排序后的键列表
        def keys(self):
                _keys =super().keys()
                _s = sorted(_keys,key=lambda k: str(k))
                return tuple(_s)
        #返回排序后的列表,其中每个元素皆有key,value组成
        def items(self):
                _keys = self.keys()
                _items = [(x,self[x]) for x in _keys]
                return tuple(_items)
        #取出并删除字典中最后一项
        def popitem(self):
                _keys = self.keys()
                #获取排序后最后一个键
                _lastkey = _keys[len(_keys) - 1]
                _val = super().pop(_lastkey)
                return _lastkey,_val
        #自定义字符串标识形式
        def __str__(self):
                _keys = self.keys()
                #拼接字符串
                _prts = [f'{k!r}:{self[k]!r}' for k in _keys]
                _str = ','.join(_prts)
                return f'{{{_str}}}'
        def __repr__(self) -> str:
            return f'{type(self).__name__}({str(self)})'
        #自定义迭代行为
        def __iter__(self):
            return iter(self.keys())
        def __del__(self):
                print(f' {type(self).__name__}字典对象被释放\n')

class my_meta(type):
        def __new__(cls,newType,bases,members):
                print(f' 正在创建: {newType} 类\n')
                return type.__new__(cls,newType,bases,members)
        @classmethod
        def __prepare__(cls,newType,bases):
            return sorted_dict()

class demo0:
        def q4(self):
                pass
        def z9(self):
                pass
        w = 'it'
        g = 99
        a = 8888
class demo1(metaclass=my_meta):
        def q4(self):
                pass
        def z9(self):
                pass
        w = 'it'
        g = 99
        a = 8888
print(' demo0类的成员列表:')
dxl = vars(demo0)
for k,v in dxl.items():
        if not k.startswith('__'):
                print(f' {k} : {v}')
print('\n demo1类的成员列表:')                
dx2 = vars(demo1)
for k,v in dx2.items():
        if not k.startswith('__'):
                print(f' {k} : {v}')

print("="*36)