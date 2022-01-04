"""
        ------ 运算符 ------

"""

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
x,y = 12, 9
print(f'{x:b} & {y:b} = {x & y :04b}')
print(f'{x:b} | {y:b} = {x | y :04b}')
print(f'{x:b} ^ {y:b} = {x ^ y :04b}')
print("="*36)

"""
        案例九十七 移动二进制位

"""
print(f'{"案例九十七 移动二进制位" :^30s}' + "\n")
n = int('01011011',base=2)
c1 = n << 4
c2 = n >> 3
print(f' 原数值:{n :08b}')
#左边0忽略
print(f' 二进制位向左移动4位后:{c1:08b}')
#右边0忽略
print(f' 二进制向右移动3位后:{c2:08b}')
print("="*36)

"""
        案例九十八 查找同时包含a、e两个字母的单词

"""
print(f'{"案例九十八 查找同时包含a、e两个字母的单词" :^30s}' + "\n")
words = ('amount','wisdom','perfect','learn','daedal')
results = []
for n in words:
    if n.count('a') and n.count('e'):
        results.append(n)
print(f'results: {results}')
print("="*36)

"""
        案例九十九 or运算符

"""
print(f'{"案例九十九 or运算符" :^30s}' + "\n")
results = []
for num in range(1,200):
    if (num % 12 == 0) or (num % 15 == 0):
        results.append(num)
print(f'results: {results}')
print("="*36)

"""
        案例一百 自定义布尔运算

"""
#检测对象是否存在__bool__方法,若找到调用该方法运算结果
#若__bool__方法找不到,查找__len__方法,该方法返回非0值视为True、返回0视为False
#以上二个方法都找不到则布尔运算结果总是True
#bool类从int类派生,对于整数值非0即为Ture;浮点型数值也是,因为float类实现了__bool__方法
print(f'{"案例一百 自定义布尔运算" :^30s}' + "\n")
class Demo100:
    def __bool__(self):
        if len(self.__dict__):
            return True
        return False

x = Demo100()
if x:
    print(' x中设置了动态属性!')
else:
    print(' x中未设置动态属性!')

y = Demo100()
y.test1 = 5
y.test2 = 10
if y:
    print(' y中设置了动态属性!')
else:
    print(' y中未设置动态属性!')
print("="*36)

"""
        案例一百零一 对象标识的比较运算

"""
print(f'{"案例一百零一 对象标识的比较运算" :^30s}' + "\n")
x,y = "word","hello"
print(f' x 与 y 是同一个对象吗? {x is y}')
z,k = "word","word"
print(f' z 与 k 是同一个对象吗? {z is k}')
a = 7
b = 7
print(f' a 与 b 是同一个对象吗? {a is b}')
c = float
d = float
print(f' c 与 d 是同一个对象吗? {c is d}')
print("="*36)

"""
        案例一百零二 not运算符

"""
print(f'{"案例一百零二 not运算符" :^30s}' + "\n")
print(f' not 5 is: {not 5}')
print(f' not 10 < 6 is: {not 10 < 6}')
print(not 1 > 0 or len('abc') == 3)
print("="*36)

"""
        案例一百零三 检查类型成员的存在性

"""
print(f'{"案例一百零三 检查类型成员的存在性" :^30s}' + "\n")
class test103:
        def __init__(self,count):
            self.count = count
        
        def __contains__(self,item):
                if item in self.__class__.__dict__:
                        return True
                if item in self.__dict__:
                        return True
                return False
        def work(self):
                pass

v = test103(3)
v.label = "test"

if 'work' in v:
        print(f'此对象存在次方法')
else:
        print(f'未找到次方法')

if 'label' in v:
        print(f'存在此属性')
else:
        print(f'不存在此属性')

if 'count' in v:
        print(f'存在此属性')
else:
        print(f'不存在此属性')
print("="*36)

"""
        案例一百零四 复合赋值运算符

"""
print(f'{"案例一百零四 复合赋值运算符" :^30s}' + "\n")
m = 200
print(f'复合赋值前: {id(m)}')
m *= 9
print(f'复合赋值后: {id(m)}')
print("="*36)

"""
        案例一百零五 三目运算符

"""
print(f'{"案例一百零五 三目运算符" :^30s}' + "\n")
x = 888
msg = "{0} {1} 被5整除".format(x,'能' if x %5 == 0 else '不能')
print(msg)
print("="*36)