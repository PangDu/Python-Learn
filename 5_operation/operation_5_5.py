"""
        ------ 三角函数 ------

"""

"""
        案例一百二十八 弧度制与角度制之间的转换

"""
import math
from typing import Iterable

print(f'{"案例一百二十八 弧度制与角度制之间的转换" :^30s}' + "\n")
print(f' 30° - > {math.radians(30):.4f} rad')
print(f' 45° - > {math.radians(45):.4f} rad')
print(f' 130° - > {math.radians(130):.4f} rad')

print(f' 2.5 rad - > {math.degrees(2.5):.4f}°')
print(f' 0.77 rad - > {math.degrees(0.77):.4f}°')
print(f' 4.5 rad - > {math.degrees(4.5):.4f}°')

print("="*36)

"""
        案例一百二十九 常用的三角函数

"""
print(f'{"案例一百二十九 常用的三角函数" :^30s}' + "\n")

#正割
def sec(x):
    return 1 / math.cos(x)
#余割
def csc(x):
    return 1 / math.sin(x)
#余切
def cot(x):
    return 1/ math.tan(x)

#正弦值
a = 90
rad = math.radians(a)
res = math.sin(rad)
print(f' sin {a}° = {res}')
#余弦值
a = 45
rad = math.radians(a)
res = math.cos(rad)
print(f' cos {a}° = {res}')
#正切值
a = 60
rad = math.radians(a)
res = math.tan(rad)
print(f' tan {a}° = {res}')
#余切值
a = 15
rad = math.radians(a)
res = cot(rad)
print(f' cot {a}° = {res}')
#正割值
a = 120
rad = math.radians(a)
res = sec(rad)
print(f' sec {a}° = {res}')
#余割值
a = 75
rad = math.radians(a)
res = csc(rad)
print(f' csc {a}° = {res}')

print("="*36)

"""
        案例一百三十 反三角函数

"""
print(f'{"案例一百三十 反三角函数" :^30s}' + "\n")
#反余切函数
def acot(x):
    return math.pi / 2 - math.atan(x)
#反正割函数
def asec(x):
    return math.acos(1 / x)
#反余割函数
def acsc(x):
    return math.asin(1 / x)
#反正弦值
n = 0.5
a = math.asin(n)
d = math.degrees(a)
print(f' arcsin {n} = {d}°')
#反余弦值
n = 1
a = math.acos(n)
d = math.degrees(a)
print(f' arccos {n} = {d}°')
#反正切值
n = 12.5
a = math.atan(n)
d = math.degrees(a)
print(f' arctan {n} = {d}°')
#反余切值
n = -15.21
a = acot(n)
d = math.degrees(a)
print(f' arccot {n} = {d}°')
#反正割值
n = 4.5
a = asec(n)
d = math.degrees(a)
print(f' arcsec {n} = {d}°')
#反余割值
n = -20.6
a = acsc(n)
d = math.degrees(a)
print(f' arccsc {n} = {d}°')
#求经过坐标原点(0,0)和坐标点(15,-8)的直线与x轴的夹角,使用atan2函数
x = 15
y = -8
a = math.atan2(y,x)
d = math.degrees(a)
print(f' arctan2 ({x},{y}) = {d}°')

print("="*36)

"""
        案例一百三十一 欧氏距离

"""
print(f'{"案例一百三十 反三角函数" :^30s}' + "\n")
#平面中两个坐标间距离
x1,y1 = 16,-20
x2,y2 = 25,16
d = math.hypot(x2-x1,y2-y1)
print(f' 点({x1},{y1}) 与 点({x2},{y2}) 间直线距离是: {d:.6f}')
#坐标点与原点间距离
x,y = -100,-60
d = math.hypot(x,y)
print(f' 点({x},{y}) 到 原点的距离是: {d:.6f}')

print("="*36)

"""
        案例一百三十二 闵式距离公式

"""
print(f'{"案例一百三十二 闵式距离公式" :^30s}' + "\n")
def minkowski_distance(x: Iterable,y:Iterable,p:float):
    """
    求闵式距离的函数
    当p=1时为曼哈顿距离
    当p=2时为欧几里何距离
    当p趋于无穷大时为契比雪夫距离
    """
    # 如果两个坐标的维度不同,抛出异常
    if len(x) != len(y):
        raise Exception('两个坐标的维度不相等!')
    # 合并两个坐标序列
    cb = zip(x,y)
    # 求和
    s = sum([abs(xu - yu) ** p for xu,yu in cb])
    # 开p次方，即指数为 1/p的幂
    return s ** (1/p)

#三维空间中两个点间的欧氏距离
p1 = (15,7,24)
p2 = (-30,15,-9)
de = minkowski_distance(p1,p2,2.0)
print(f' 三维坐标 {p1} 与 {p2} 之间的欧式距离:\n {de:.6f}\n')
#二维空间中两个点间的曼哈顿距离
p1 = 1,5
p2 = 3,-2
dm = minkowski_distance(p1,p2,1.0)
print(f' 二维坐标 {p1} 与 {p2} 间的曼哈顿距离为: \n {dm:.6f}')
print("="*36)