"""
        案例八十七 四则运算

"""
print(f'{"案例八十七 四则运算" :^30s}' + "\n")
a = 14
b = 8
print(f' a+b = {a + b}')
print(f' a - b = {a - b}')
print(f' a ✖️ b = {a * b}')
print(f' a / b = {a / b}')
print("="*36)

"""
        案例八十八 指数运算符

"""
print(f'{"案例八十八 指数运算符" :^30s}' + "\n")
a = 2 **10
print(f' 2的10次方: {a}')
b = 8 ** -2
print(f' 8的-2次方: {b}')
c = 512 **(1/3)
print(f' 512的立方根: {c}')
d = -23 ** 3
print(f' -23的立方: {d}')
print("="*36)

"""
        案例八十九 分解整数位

"""
print(f'{"案例八十九 分解整数位" :^30s}' + "\n")
w = []
i = 1234897
while i > 0:
        t = i % 10
        w.append(t)
        i = i // 10
w.reverse()
print(w)
print("="*36)

"""
        案例九十 连接字符串

"""
print(f'{"案例九十 连接字符串" :^30s}' + "\n")
h = '亭'
i = '玉'
j = '立'
print(f'" {h}、{i}、{j}" 组成一个成语:{h+h+i+j}')
print("="*36)

"""
        案例九十一 当字符串遇上乘法运算符

"""
print(f'{"案例九十一 当字符串遇上乘法运算符" :^30s}' + "\n")
print('f' * 10)
print(7 *'&')
print('@' * 8 + 9 * '->')
print('^_^' * (-6))
print("="*36)

"""
        案例九十二 运算优先级

"""
print(f'{"案例九十二 运算优先级" :^30s}' + "\n")
a = (3 + 7) / 5
print(f' (3 + 7)/5 = {a}')
b = 10 * 5 / 25
print(f' 10 * 5 / 25 = {b}')
c = 10 *(5 / 25)
print(f' 10 * (5 / 25) = {c}')
d = 8 * (12 + 6)
print(f' 8 * (12 + 6) = {d}')
print("="*36)

"""
        案例九十三 自定义的相等比较

"""
print(f'{"案例九十三 自定义的相等比较" :^30s}' + "\n")
class zdyClass:
        def __init__(self,itemOne,itemTwo) -> None:
            self.itemOne = itemOne
            self.itemTwo = itemTwo
        def __eq__(self, other) -> bool:
            s1 = self.itemOne + self.itemTwo
            s2 = other.itemOne + other.itemTwo
            return s1 == s2
        def __ne__(self, other: object) -> bool:
            s1 = self.itemOne + self.itemTwo
            s2 = other.itemOne + other.itemTwo
            return s1 != s2

x = zdyClass(18,8)
y = zdyClass(6,20)
print(f' x 和 y 相等吗? {x == y}')
print(f' x 和 y 不相等吗? {x != y}')
print("="*36)

"""
        案例九十四 比较对象的大小

"""
print(f'{"案例九十四 比较对象的大小" :^30s}' + "\n")
array = (4,-3,89,0)
for i in array:
        print(f' {i}大于或等于0吗? {i >= 0}')
print("="*36)

"""
        案例九十五 自定义的大小比较

"""
print(f'{"案例九十五 自定义的大小比较" :^30s}' + "\n")
class Person:
        def __init__(self,name,age) -> None:
            self.name = name
            self.age = age
        def __gt__(self,other):
                return self.age > other.age
        def __ge__(self,other):
                return self.age >= other.age
        def __lt__(self,other):
                return self.age < other.age
        def __le__(self,other):
                return self.age <= other.age
        def __eq__(self, other: object) -> bool:
                return self.age == other.age
        def __ne__(self, other: object) -> bool:
                return self.age != other.age

p1 = Person('Jack', 28)
p2 = Person('Tom',31)
print(f' {p1.name}比{p2.name}小吗? {p1 < p2}')
print("="*36)

"""
        案例九十六 二进制的逻辑运算

"""
print(f'{"案例九十六 二进制的逻辑运算" :^30s}' + "\n")
print("="*36)