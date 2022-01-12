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

print("=" * 36)