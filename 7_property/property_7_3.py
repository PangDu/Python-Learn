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

"""
        案例一百七十七 以编程方式生成__slots__成员

"""
print(f'{"案例一百七十七 以编程方式生成__slots__成员" :^30s}' + "\n")
#首先通过type类或其派生类的对象创建类，再用类创建对象

#第一种:直接使用type类创建新类型,在名称空间字典加入__slots__成员
prps = ['item_{}'.format(i) for i in range(1,4)]
ns = {'__slots__' : prps}
demoF = type('demoF',(),ns)
x = demoF()
x.item_1 = 1
x.item_2 = 2
x.item_3 = 3
try:
    x.item_4 = 4
except Exception as ex:
    print(f' 错误: {ex}')
#第二种:使用元类(Meta Class)
class _my_meta(type):
    def __new__(cls,new_type,bases,ns):
        props = ('first','second','next')
        ns['__slots__'] = props
        return super().__new__(cls,new_type,bases,ns)
class demoG(metaclass=_my_meta):
    pass
k = demoG()
k.first = 0
k.next = 'next'
try:
    k.begin = 100
except Exception as ex:
    print(f' 错误: {ex}')

print("="*36)

"""
        案例一百七十八 类变量与__slots__之间的冲突

"""
print(f'{"案例一百七十八 类变量与__slots__之间的冲突" :^30s}' + "\n")
#类在构建时会根据__slots__成员所列出的内容来生成新成员,成员值由member_descriptor类封装
#若在类中继续声明与__slots__成员相同名称的成员,会将前面生成的成员替换掉,破坏原有数据结构
import datetime
class order:
    __slots__ = 'id','date','company'
    def __init__(self) -> None:
        self.id = 1
        self.date = datetime.date.today()
        self.company = '抖音'
od = order()
print(f' 订单: {od.id},\n 时间: {od.date},\n 公司: {od.company}')

print("="*36)