"""
        列表

"""

"""
        案例二百二十七 初始化列表对象

"""
print(f'{"案例二百二十七 初始化列表对象" :^30s}' + "\n")

a = ['flow','year','day']
b = [0.009,0.999]
c = ['picture',999,b'5a23']
d = list([2,'f'])
print(f' a: {a}\n b: {b}\n c: {c}\n d: {d}\n')

print("="*36)

"""
        案例二百二十八 添加元素

"""
print(f'{"案例二百二十八 添加元素" :^30s}' + "\n")

x = []
x.append(99)
x.append('a')
x.extend([55,'flow',0.999])
x.insert(2,'blow')
print(f' 最终列表:\n {x}')

print("="*36)

"""
        案例二百二十九 删除元素

"""
print(f'{"案例二百二十九 删除元素" :^30s}' + "\n")

x = list(range(20))
print(f' 列表 x:\n {x}')
del x[10]
print(f' 列表 x: \n {x}')
x.remove(19)
print(f' 列表 x:\n {x}')
x.clear()
print(f' 列表 x: {x}')

print("="*36)

"""
        案例二百三十 自定义排序

"""
print(f'{"案例二百三十 自定义排序" :^30s}' + "\n")

class shooter:
    def __init__(self,nick=None,hits=0) -> None:
        self.nickName = nick
        self.hits = hits
    def __str__(self) -> str:
        return f' {self.nickName} - {self.hits}'

shooters = [
    shooter('小张',39),
    shooter('小崔',59),
    shooter('小海',38),
    shooter('小刘',25),
    shooter('小马',35),
    shooter('小胡',19),
    shooter('小李',29),
    shooter('小度',31),
    shooter('小吴',56),
    shooter('小米',30),
    shooter('小王',41)
]
print(' 排序前:')
for e in shooters:
    print(f' {e!s}')
shooters.sort(key=lambda o:o.hits)
print(' 排序后:')
for e in shooters:
    print(f' {e!s}')

print("="*36)

"""
        案例二百三十一 反转列表

"""
print(f'{"案例二百三十一 反转列表" :^30s}' + "\n")
# reversed类
# list类reverse()方法
a = [120,23,9,'low',999,"反转"]
r = reversed(a)
print(f' 反转前:\n a: {a}')
print(f' 反转后:')
print(','.join(str(y) for y in r))

b = ['123',999,'hello','正则表达式',0.9999]
print(f' 原列表:\n {b}')
b.reverse()
print(f' 反转后:')
print(','.join(str(y) for y in b))

print("="*36)

"""
        案例二百三十二 统计某个元素出现次数

"""
print(f'{"案例二百三十二 统计某个元素出现次数" :^30s}' + "\n")
x = [2,6,6,5,3,2,9,9,7]
print(f' 列表: {x}')
print(f' 元素6出现{x.count(6)}次')
print(f' 元素2出现{x.count(2)}次')
print(f' 元素8出现{x.count(8)}次')
print("="*36)

"""
        案例二百三十三 将列表对象作为栈结构使用

"""
print(f'{"案例二百三十三 将列表对象作为栈结构使用" :^30s}' + "\n")
m = [12,15,999,888,40,88,45]
n = m.copy()
print(f' 原列表: {m}')
print(f' 列表出栈:')
while True:
    try:
        print(f' {m.pop()}',end='')
    except IndexError:
        break
print(' \n 列表顺序输出:')

while True:
    try:
        print(f' {n.pop(0)}',end='')
    except IndexError:
        break
print('\n')
print("="*36)

"""
        案例二百三十四 合并列表

"""
print(f'{"案例二百三十四 合并列表" :^30s}' + "\n")
a = [12,45,67]
b = ['a','b','c']
print(f' a + b = {a + b}')
print("="*36)

"""
        案例二百三十五 重复列表中的元素

"""
print(f'{"案例二百三十五 重复列表中的元素" :^30s}' + "\n")
x = [100,200,300]
print(f' 重复三次: {x * 3}')
m = [['a','b'],['c','d']]
n = m * 3
print(f' 重复三次: {n}')
n[0][1]= 888
print(f' 修改运算结果: {n}')
print(f' 原列表: {m}')
print("="*36)