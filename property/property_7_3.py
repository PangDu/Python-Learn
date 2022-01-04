"""
        __slots__成员

"""

"""
        案例一百七十四 禁止创建__dict__成员

"""
print(f'{"案例一百七十四 禁止创建__dict__成员" :^30s}' + "\n")

class person1:
    __slots__ ='name','age','city'

x = person1()
x.name = 'lin'
x.age  = 18
x.city = 'bei jing'

try:
    x.email = 'ddd@163.com'
except Exception as ex:
    print(f' 错误: {ex}')

try:
    person1.email = '9999@163.com'
    print(f' 类属性设置成功')
except Exception as ex:
    print(f' 属性设置错误: {ex}')

print("="*36)

"""
        案例一百七十五 派生类需重新定义__slots__成员

"""
print(f'{"案例一百七十五 派生类需重新定义__slots__成员" :^30s}' + "\n")

class demoA:
    __slots__ = ['name','age']

class demoB(demoA):
    pass
class demoC(demoA):
    __slots__ = demoA.__slots__

a = demoB()
a.email = '678@163.com'
a.city = 'bei jing'
print(f' {demoB.__name__}对象属性: {vars(a)}')

try:
    b = demoC()
    b.emial = '4345@163.com'
    b.city = 'bei jing'
except Exception as ex:
    print(f' {demoC.__name__}设置动态属性失败')

print("="*36)

"""
        案例一百七十六 对象属性设置为只读

"""
print(f'{"案例一百七十六 对象属性设置为只读" :^30s}' + "\n")

class demoD:
    __slots__ = ['name','age']
demoD.name = 'lin'
demoD.age  = 18

a = demoD()
try:
    a.name = 'wang'
    a.age  = 20
except Exception as ex:
    print(f' 修改对象属性值失败')

print("="*36)