"""
        元祖

"""
"""
        案例二百三十六 初始化方法

"""
print(f'{"案例二百三十六 初始化方法" :^30s}' + "\n")
a = 'abc','xyz'
b = (0.008,-888,999)
c = 0,
d = tuple((999,'hello'))
print(f' a: {a}')
print(f' b: {b}')
print(f' c: {c}')
print(f' d: {d}')
print("="*36)
"""
        案例二百三十七 带命名字段的元祖

"""
print(f'{"案例二百三十七 带命名字段的元祖" :^30s}' + "\n")
from collections import namedtuple
data = namedtuple('data',['id','size','parts'])
x = data(id=1,size=8888,parts=9)
for n in range(len(x)):
    print(f' {n} : {x[n]}')
print(f' id:{x.id}\n size:{x.size}\n parts:{x.parts}')
print("="*36)
"""
        案例二百三十八 将带命名字段的元祖转换为字典

"""
print(f'{"案例二百三十八 将带命名字段的元祖转换为字典" :^30s}' + "\n")
from collections import namedtuple
dic = x._asdict()
for k,v in dic.items():
    print(f' {k} : {v}')
print("="*36)