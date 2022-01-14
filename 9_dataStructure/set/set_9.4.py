"""
        集合

"""
"""
        案例二百四十五 集合实例化

"""
print(f'{"案例二百四十五 集合实例化" :^30s}' + "\n")
# set类: 初始化后可通过add()和remove()修改元素
# frozenset类: 初始化后元素不可修改
# 使用大括号初始化{}
s1 = set(['88','99',666,0.9999])
s2 = {'abc',999,0.8888,'集合'}
s3 = frozenset(['hello',321,0.3333])
print(f' s1: {s1}\n s2: {s2}\n s3: {s3}')
print("="*36)
"""
        案例二百四十六 合并集合

"""
print(f'{"案例二百四十六 合并集合" :^30s}' + "\n")
# 使用union()或 |运算符
s1 = {'abc','def'}
s2 = {'hij','klm'}
s = s1.union(s2)
print(f' 合并后: {s}')
s3 = {1,2,3}
s4 = {4,5,6}
s = s3|s4
print(f' 合并后: {s}')
print("="*36)
"""
        案例二百四十七 集合的包含关系

"""
print(f'{"案例二百四十七 集合的包含关系" :^30s}' + "\n")
# issuperset(): 判断当前集合是否是另一个集合的父集合或两个集合元素完全相同
# issubset(): 判断当前集合是否是另一个集合的子集合或两个集合元素完全相同
set1 = {1,2,3,4,5,6}
set2 = {4,5,6}
a = set1.issuperset(set2)
b = set2.issubset(set1)
print(f' set1{"是" if a else "不是" }set2的父集合')
print(f' set2{"是" if b else "不是"}set1的子集')
set3 = {2,3,4,5}
set4 = {3,2,5,4}
c = set3.issuperset(set4)
print(f' set3{"是" if c else "不是"}set4的父集合')
print("="*36)
"""
        案例二百四十八 交集与差集

"""
print(f'{"案例二百四十八 交集与差集" :^30s}' + "\n")
# intersection()和&:用于获取两个集合的交集
# symmetric_difference类似于^异或,不在两个集合内的元素
# A.intersection_update(B) == A = A & B
# A.difference_update(B) == A = A - B
# A.symmetric_difference_update(B) == A = A ^ B
# 不带"_update"结尾的方法会将计算结果存放到新的集合对象中,并返回给调用方
# 带"_update"结尾的方法会更新当前集合,以存储计算结果
s1 = {1,2,3,4,5,6,7}
s2 = {8,9,10,11,1,2}
s3 = {1,8,3,9,12}
r1 = s1.intersection(s2,s3)
print(f' 三个集合交集: {r1}')
print(f' 三个集合差集: {s1-s2-s3}')
print(f' s1与s2的对称差集: {s1 ^ s2}')
print(f' s2与s3的对称差集: {s2.symmetric_difference(s3)}')
# print("="*36)