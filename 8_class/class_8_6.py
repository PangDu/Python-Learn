"""
        特殊成员

"""

"""
        案例二百一十九 __str__方法与__repr__方法

"""
print(f'{"案例二百一十九 __str__方法与__repr__方法" :^30s}' + "\n")
#__str__: 返回字符串较短,仅描述对象的数据内容
#__repr__: 返回字符串可最为Python代码执行
class contact:
        def __init__(self,name,email,phone,city):
                self.name = name
                self.email = email
                self.phone = phone
                self.city = city
        def __str__(self) -> str:
            return f' 姓名:{self.name},邮箱:{self.email},手机号:{self.phone},所在城市:{self.city}'
        def __repr__(self) -> str:
            className = type(self).__name__
            prms = f'name={self.name!r},email={self.email!r},phone={self.phone!r},city={self.city!r}'
            return f'{className}({prms})'
a = contact('小米','about@163.com','8888888','北京')
gls = str(a)
print(f' str: {gls}')
rps = repr(a)
print(f' repr: {rps}')
newobj = eval(rps)
print(f' name: {newobj.name}\n email: {newobj.email}\n phone: {newobj.phone}\n city: {newobj.city}')

print("="*36)

"""
        案例二百二十 模拟函数调用

"""
print(f'{"案例二百二十 模拟函数调用" :^30s}' + "\n")

class Test0:
        def __call__(self,a,b):
            return a * b
v = Test0()
a = v(8,9)
b = v(7,8)
print(f' a: {a}, b: {b}')

print("="*36)

"""
        案例二百二十一 自定义对象目录

"""
print(f'{"案例二百二十一 自定义对象目录" :^30s}' + "\n")

class Rect:
        def __init__(self,width=0,height=0) -> None:
            self.width = width
            self.height = height
        def __dir__(self):
            _dir = super().__dir__()
            if not '__area__' in _dir:
                    _dir = list(_dir)
                    _dir.append('__area__')
                    return _dir
        def __getattr__(self,name):
                if name == '__area__':
                        return self.width * self.height
                return None
r = Rect(15,3)
mb_list = dir(r)
print(f' rect 对象的成员列表:\n {", ".join(mb_list)}')
print(f'__area__: {r.__area__}')

print("="*36)

"""
        案例二百二十二 获取对象所占内存大小

"""
print(f'{"案例二百二十二 获取对象所占内存大小" :^30s}' + "\n")

a = 0.0009
print(f' float数值: {a.__sizeof__()}')
b = 8888
print(f' int数值: {b.__sizeof__()}')

class Pet:
        def __init__(self,name,age):
            self.name = name
            self.age = age
e = Pet('小明',18)
print(f' Pet对象: {e.__sizeof__()}')

print("="*36)