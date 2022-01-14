"""
        案例五十八 声明变量

"""
print(f'{"案例五十八 声明变量" :^30s}' + "\n")
v1 = True
v2 = "start"
v3 = 3.1415
v4 = [1,2,3]
if hasattr(v1.__class__,'__name__'):
    print(f' v1的数据类型: {v1.__class__.__name__}')
print(f' v2的数据类型: {v2.__class__.__name__}')
print(f' v3的数据类型: {v3.__class__.__name__}')
print(f' v4的数据类型: {v4.__class__.__name__}')
print("="*36)

"""
        案例五十九 类型批注

"""
print(f'{"案例五十九 类型批注" :^30s}' + "\n")
xa:str = "ewqw"
st:int = (3,5,8)
print(f' xa的实际类型: {xa.__class__.__name__}')
print(f' st变量的实际类型: {st.__class__.__name__}')
print(f'变量的批注类型:{__annotations__}')
print("="*36)

"""
        案例六十 声明语句也是变量赋值

"""
print(f'{"案例六十 声明语句也是变量赋值" :^30s}' + "\n")
def num_sqr(x,n):
    return x ** n
sqr_num = num_sqr
print(f' num_sqr引用的对象:\n{num_sqr}')
print(f' sqr_num引用的对象:\n{sqr_num}')
d = {k:v for k,v in globals().items() if v is num_sqr}
print(" 全局名称空间中,引用num_sqr函数的变量有:")
for var,func in d.items():
    print(f' {var} : {func}')
print("="*36)

"""
        案例六十一 as关键字与赋值

"""
print(f'{"案例六十一 as关键字与赋值" :^30s}' + "\n")
from variable_61.test_mod import trunc_str as truncateStr
print(truncateStr(" 一二三四五六七八九十".strip(),7))
print(truncateStr(" 曾经沧海难为水,除却巫山不是云!".strip(),10))
print("="*36)

"""
        案例六十二 组合赋值法

"""
print(f'{"案例六十二 组合赋值法" :^30s}' + "\n")
a,*b = 1,2,3
print(f'a = {a},b = {b}')
v1,v2 = 0.003, 8.897
m1,m2 = b'\x6e',888
s1,s2,*s3 = 'ade',123,'大地方','^&*'
print(f'v1 = {v1},v2 = {v2}')
print(f'm1 = {m1},m2 = {m2}')
print(f's1 = {s1},s2 = {s2},s3 = {s3}')
print("="*36)

"""
        案例六十三 组合赋值与表达式列表

"""
print(f'{"案例六十三 组合赋值与表达式列表" :^30s}' + "\n")
v1,v2,v3 = 'a','b','c'
(v1,v2,v3) = ('a','b','c')
*v1,v2,v3, = 'a','b','c','d','e','f'
print(f'v1 = {v1}')
[*a,b,c] = ('a','b','c','d','e','f')
num = [a,b,c]
print(f'num = {num}')
n1,n2,n3 = 100,101,102
m1,*m2,m3 = 0.1,0.2,0.3,0.4,0.5
[*q] = 'abcedfg'
print(f'm2 = {m2}')
print(f'q = {q}')
print("="*36)