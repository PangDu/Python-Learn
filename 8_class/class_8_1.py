"""
        类的定义与实例化

"""

"""
        案例一百八十九 class关键字

"""
print(f'{"案例一百八十九 class关键字" :^30s}' + "\n")

class test1(object):
    pass

class test2:
    pass

class test3:
    id = -1
    kind = 'member'

class test4:
    def bind(self):
        pass

class test5:
    a = 1
    b = 'hello'
    def bind(self):
        pass
print(test5)

print("="*36)

"""
        案例一百九十 类的实例化

"""
print(f'{"案例一百九十 类的实例化" :^30s}' + "\n")

class task:
    def run(self):
        pass

r = task()
r.run()
r.tid = 88888
print(r)

print("="*36)

"""
        案例一百九十一 __new__方法与__init__方法

"""
print(f'{"案例一百九十一 __new__方法与__init__方法" :^30s}' + "\n")

class keybase:
    def __new__(cls):
        print(f' __new__方法被调用')
        print(f' cls参数: {cls}')
        return object.__new__(cls)
    def __init__(self) -> None:
        print('__init__方法被调用')
        print(f' self 参数: {self}')
kb = keybase()

print("="*36)

"""
        案例一百九十二 带参数的构造函数

"""
print(f'{"案例一百九十二 带参数的构造函数" :^30s}' + "\n")

class employee:
    def __new__(cls,*ps,**kw):
        print(f' 正在创建{cls.__name__}实例')
        prs = (*ps,*kw.items())
        print(f' 参数: {prs}\n')
        return object.__new__(cls)
    def __init__(self,eid,ename,eage,ecity) -> None:
        print(f' 正在初始化 {type(self).__name__}实例')
        print(f' 参数: eid:{eid},ename:{ename},eage:{eage},ecity:{ecity}\n')
        self.id = eid
        self.name = ename
        self.age = eage
        self.city = ecity

ek = employee(1,'Dick',eage=32,ecity='北京')
dx = vars(ek)
for k,v in dx.items():
    print(f' {k} : {v}')

print("="*36)

"""
        案例一百九十三 实现__del__方法

"""
print(f'{"案例一百九十三 实现__del__方法" :^30s}' + "\n")

class demo0:
    def __del__(self):
        print('对象引用计数为0')
a = demo0()
b = a
c = b
d = c

del d
del c
del b
del a

print("="*36)