"""
        继承与多态

"""

"""
        案例二百零二 类型派生

"""
print(f'{"案例二百零二 类型派生" :^30s}' + "\n")

class C1:
    def open(self):
        print(' 打开文件')
class C2:
    def close(self):
        print(' 关闭文件')
class C3:
    def read(self):
        print(' 阅读文件')
class D(C1,C2,C3):
    def write(self):
        print(' 写入文件')
print(' D类的成员:')
print(','.join([x for x in dir(D) if not x.startswith('__')]))
v = D()
v.open()
v.read()
v.write()
v.close()

print("="*36)

"""
        案例二百零三 类型继承中的多态

"""
print(f'{"案例二百零一 类型继承中的多态" :^30s}' + "\n")

class Animal:
    def speak(self):
        print(f' 此为 {type(self).__name__} speak')
class Dog(Animal):
        pass
class Cat(Animal):
        pass

c = Animal()
c.speak()
a = Dog()
a.speak()
b = Cat()
b.speak()

print("="*36)

"""
        案例二百零四 覆盖基类的成员

"""
print(f'{"案例二百零四 覆盖基类的成员" :^30s}' + "\n")

class Base:
    def Work(self):
        print(" Base's Work")
class Derive(Base):
    def Work(self):
        print(" Derive's Work")
print(' Base.Work: {}'.format(Base.Work))
print(' Derive.Work: {}'.format(Derive.Work))
k = Base()
k.Work()
n = Derive()
n.Work()

print("="*36)

"""
        案例二百零五 访问基类的成员

"""
print(f'{"案例二百零五 访问基类的成员" :^30s}' + "\n")

class the_base:
    def play(self):
        print(f' the_base.play')
    def change(self):
        print(f' the_base.change')

class test0(the_base):
    def change(self):
        print(f' {type(self).__name__}.change')
        the_base.change(self)
        self.play()   
var = test0()
var.change()

print("="*36)

"""
        案例二百零六 使用super访问基类的成员

"""
print(f'{"案例二百零六 使用super访问基类的成员" :^30s}' + "\n")

class A:
    def foo(self):
        print(' A实例对象的foo方法被调用')
class B(A):
    def foo(self):
        super().foo()
        print(' B实例对象的foo方法被调用')
vk = B()
vk.foo()

print("="*36)

"""
        案例二百零七 使用基类的类方法

"""
print(f'{"案例二百零七 使用基类的类方法" :^30s}' + "\n")

class X:
    @classmethod
    def go(cls):
        print(' 调用X的类方法 go')
class Y(X):
    @classmethod
    def go(cls):
        super(Y,Y).go()
        print(' 调用Y的类方法 go')
Y.go()

print("="*36)

"""
        案例二百零八 super类的非绑定用法

"""
print(f'{"案例二百零八 super类的非绑定用法" :^30s}' + "\n")
#super类构造函数:super([type[,object - or - type]]),若实例化是仅提供type参数,则super对象被视为非绑定对象
#super(type(self),self).eat() or super(type(self)).__get__(self,type(self)).eat()
class track:
        def play(self):
                print(' track play')
class stereo_track(track):
        def __new__(cls):
                cls.__base = super(cls)
                return object.__new__(cls)
        def play(self):
            self.__base.play()
            print(' stereo_track.play')
a = stereo_track()
a.play()

print("="*36)

"""
        案例二百零九 方法解析顺序(MRO)

"""
print(f'{"案例二百零九 方法解析顺序(MRO)" :^30s}' + "\n")
#MRO是元组对象,存储在类的__mro__成员中,列出了在基类中查找成员的顺序
#MRO列表第一个元素是当前类,最后一个是object类,从子类开始查找,自下向上最后在object类中查找
#多继承查找顺序是以当前类为起点,沿着类的派生线路向上递归搜索，遇到object类为止.object类是最后查找。

class base1:
        def work(self):
                print(' base1 work')
class base2:
        def work(self):
                print(' base2 work')
class workboard(base1,base2):
        def work(self):
            super(base1,self).work()
a = workboard()
a.work()

print("="*36)

"""
        案例二百一十 鸭子类型

"""
print(f'{"案例二百一十 鸭子类型" :^30s}' + "\n")
#动态语言的函数可以接收任意类型的参数,只需检查参数所引用的对象是否窜在要访问的成员即可
#不关心是否实现接口或是否存在继承关系
def play_a_game(game):
        if not hasattr(game,'get_name'):
                raise RuntimeError(' game参数不存在 get_name() 方法')
        method = getattr(game,'get_name')
        if not callable(method):
                raise RuntimeError(' 此成员不可调用')
        game.get_name()

class game1:
        @classmethod
        def get_name(cls):
                print(' game1 方法')
class game2:
        @classmethod
        def get_name(cls):
                print(' game2 方法')
class game3:
        @classmethod
        def get_name(cls):
                print(' game3 方法')
play_a_game(game1)
play_a_game(game2)
play_a_game(game3)

print("="*36)

"""
        案例二百一十一 issubclass()函数与派生类检查

"""
print(f'{"案例二百一十一 issubclass()函数与派生类检查" :^30s}' + "\n")

class A0:
        pass
class B0:
        pass
class M(B0):
        pass
class N(A0,B0):
        pass
print(f' issubclass(M,A0): {issubclass(M,A0)}')
print(f' issubclass(N,(A0,B0)): {issubclass(N,(A0,B0))}')

print("="*36)

"""
        案例二百一十二 自定义派生类的检查逻辑

"""
print(f'{"案例二百一十二 自定义派生类的检查逻辑" :^30s}' + "\n")
#由于鸭子类型,不存在派生关系的两个类,issubclass()函数返回True
#__subclasscheck__只能在元类中定义,不能直接在类中定义
class meta(type):
        def __subclasscheck__(self, subclass: type) -> bool:
            method_name = 'create'
            if hasattr(self,method_name) and hasattr(subclass,method_name):
                    m1 = type(getattr(self,method_name))
                    m2 = type(getattr(subclass,method_name))
                    if m1.__name__ == 'method' and m2.__name__ == 'method':
                            return True
            return False
class T(metaclass=meta):
        @classmethod
        def create(cls):
                return cls()
class A1(metaclass=meta):
        @classmethod
        def create(cls):
                return cls()
class B1(metaclass=meta):
        @classmethod
        def copy(cls):
                return cls()
class C1(metaclass=meta):
        def create(self):
                return type(self)()
b = issubclass(A1,T)
print(f' A1{"是"if b else "不是"}T的派生类')
b = issubclass(C1,A1)
print(f' C1{"是"if b else "不是"}A1的派生类')
b = issubclass(C1,T)
print(f' C1{"是"if b else "不是"}T的派生类')

print("="*36)

"""
        案例二百一十三 初始化派生类型

"""
print(f'{"案例二百一十三 初始化派生类型" :^30s}' + "\n")

class person:
        def __init_subclass__(cls, **prpe):
            if prpe:
                    for key,value in prpe.items():
                            setattr(cls,key,value)
class student(person,name='小米',age=18,major='C语言'):
        pass
class employee(person,name='王敏',age=25,city='北京',partm='IT部门'):
        pass
print(f' {student.__name__}类的属性列表:')
for key,value in vars(student).items():
        if not key.startswith('__'):
                print(f' {key} : {value}')
print(f'\n {employee.__name__}类的属性列表:')
for key,value in vars(employee).items():
        if not key.startswith('__'):
                print(f' {key} : {value}')

print("="*36)

"""
        案例二百一十四 抽象类

"""
print(f'{"案例二百一十四 抽象类" :^30s}' + "\n")
#定义的类需将ABCMeta类作为元类或ABC类派生(Abstract Base Class)
#类成员使用abstractmethod装饰器
#抽象类不能实例化,必须派生出子类并实现所有抽象成员;若部分抽象成员未实现,派生类不能实例化
from abc import ABC,abstractmethod
class Ball(ABC):
        @abstractmethod
        def play(self):
                pass
        @classmethod
        @abstractmethod
        def count(cls):
                pass
        @staticmethod
        @abstractmethod
        def teamMember():
                pass

class FootBall(Ball):
        @classmethod
        def count(cls):
            print(' 梅西射进一球')
        @staticmethod
        def teamMember():
            print(' 踢足球需要22个人')
        def play(self):
            print(' 踢足球')

class BasetBall(Ball):
        @classmethod
        def count(cls):
            print(' 科比上篮得分')
        @staticmethod
        def teamMember():
            print(' 打篮球需要10个人')
        def play(self):
            print(' 打篮球')

a = FootBall()
a.play()
a.count()
FootBall.teamMember()

b = BasetBall()
b.play()
b.count()
BasetBall.teamMember()

print("="*36)

"""
        案例二百一十五 虚拟子类

"""
print(f'{"案例二百一十五 虚拟子类" :^30s}' + "\n")
#register()方法设置类的虚拟子类
#虚拟子类并非从抽象类继承,只是实现了抽象类的抽象成员
class Person(ABC):
        @property
        @abstractmethod
        def ID(self):
                return None
        @ID.setter
        @abstractmethod
        def ID(self,id):
                pass
        @property
        @abstractmethod
        def Name(self):
                return None
        @Name.setter
        @abstractmethod
        def Name(self,name):
                pass

@Person.register
class Sales:
        def __init__(self,id = None,name = None):
            self._id = id
            self._name = name
        @property
        def ID(self):
                return self._id
        @ID.setter
        def ID(self,id):
                self._id = id
        @property
        def Name(self):
                return self._name
        @Name.setter
        def Name(self,name):
                self._name = name
b = issubclass(Sales,Person)
print(f' {Sales.__name__} {"是" if b else "不是"} {Person.__name__} 的子类')

print("="*36)

"""
        案例二百一十六 获取类的直接子类

"""
print(f'{"案例二百一十六 获取类的直接子类" :^30s}' + "\n")

class G:
        pass
class M(G):
        pass
class N(G):
        pass
class S(N):
        pass

subs = G.__subclasses__()
print(' G类的直接子类:')
for i in subs:
        print(f' {i.__name__}')

print("="*36)