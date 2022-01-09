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
        print(f' 此为{type(self).__name__} speak')
class Dog(Animal):
    def speak(self):
        print(f' 此为{type(self).__name__} speak')
class Cat(Animal):
    def speak(self):
        print(f' 此为{type(self).__name__} speak')

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

print("="*36)