"""
        字典

"""
"""
        案例二百三十九 字典的实例化

"""
print(f'{"案例二百三十九 字典的实例化" :^30s}' + "\n")
d0 = dict()
d0['type'] = 'token'
d0['issuer'] = 'kabbie'
d0['hash'] = 'HMAC-SHA256'
d2 = {1:'green',2:'red',3:'black'}
d3 = dict((('id',100000),('company','抖音'),('date','now')))
print(f' d0: {d0}')
print(f' d2: {d2}')
print(f' d3: {d3}')
print("="*36)

"""
        案例二百四十 字典与for循环

"""
print(f'{"案例二百四十 字典与for循环" :^30s}' + "\n")
the_dic = {
        'title' : 'about something',
        'body' : 'work with something',
        'group' : 'R-1'
}
print(f' {"key":^20s} {"value":^20s}')
print('-' * 40)
for k,v in the_dic.items():
        print(f' {k:<20s}{v:20s}')
print("=" * 36)
"""
        案例二百四十一 从其他数据来更新字典

"""
print(f'{"案例二百四十一 从其他数据来更新字典" :^30s}' + "\n")
mydict = {
        'item1' : 0x25,
        'item2' : 0x8910,
        'item3' : 0xb7c2,
        'item4' : 0x10a6
}
print(f' 原字典: {mydict}')
mydict.update((('item5',0xa89),('item6',0x3012)))
print(f' 更新字典: {mydict}')
mydict.update({'item7' : 0x765b})
print(f' 更新字典: {mydict}')
mydict.update(item8=0xab123)
print(f' 字典为:')
for k,v in mydict.items():
        print(f' {k:<12s}{"0x"+"{0:>04x}".format(v)}')
print("=" * 36)
"""
        案例二百四十二 可以调整元素次序的字典

"""
print(f'{"案例二百四十二 可以调整元素次序的字典" :^30s}' + "\n")
from collections import OrderedDict
mydict = OrderedDict(task1=1,task2=2,task3=3,task4=4)
print(f' 原字典: {mydict}')
mydict.move_to_end('task3',last=False)
print(f' 更新后字典: {mydict}')
mydict.move_to_end('task2')
print(f' 更新后字典: {mydict}')
print("=" * 36)
"""
        案例二百四十三 合并字典

"""
print(f'{"案例二百四十三 合并字典" :^30s}' + "\n")
from collections import ChainMap
a = {
        'item1':12,
        'item2':'hello'
}
b = {
        'progress1':1,
        'progress2':2,
        'progress3':3
}
c = {
        'rid' : '005',
        'title' : 'demo',
        'var' : '1.0.1'
}
m = ChainMap(a,b,c)
print('合并字典后的数据:')
for k,v in m.items():
        print(f' {k} : {v}')
print("=" * 36)
"""
        案例二百四十四 计算器

"""
print(f'{"案例二百四十四 计算器" :^30s}' + "\n")
from collections import Counter
ns = 23,67,89,12,34,54,37,78,54
c = Counter(ns)
print(f' 23出现了{c[23]}次')
x = c.most_common(2)
a = x[0]
print(f' x: {x} a: {a}')
print(f' 出现次数最多的元素:{a[0]},出现了{a[1]}次')
c = Counter({100: 3,888: 6,999: 8})
t = c.elements()
for e in t:
        print(e,end=' ')
print('\n')
print("=" * 36)