"""
        枚举

"""
"""
        案例二百五十二 定义枚举类

"""
print(f'{"案例二百五十二 定义枚举类" :^30s}' + "\n")
from enum import Enum
import enum
class Shapes(Enum):
        CIRCLE = 0
        RECTANGLE = 1
        TRIANGLE = 2
        RHOMBUS = 3
# 枚举类型转化为列表对象
mems = list(Shapes)
for m in Shapes:
        print(f' m: {m}')
x = Shapes['CIRCLE']
y = Shapes(2)
print(f' x: {Shapes.CIRCLE}')
print(f' y: {Shapes.TRIANGLE}')
print("="*36)
"""
        案例二百五十三 只能使用int值得枚举

"""
print(f'{"案例二百五十三 只能使用int值得枚举" :^30s}' + "\n")
from enum import IntEnum
class em1(IntEnum):
        Q = 1
        R = 2
class em2(IntEnum):
        U = 1
        W = 2
b1 = em1.Q
b2 = em2.U
print(f' b1{"等于"if b1==b2 else "不等于"}b2')
print(f' em1的成员:')
for m in em1:
        print(f' {m.name} : {m.value}')
print("="*36)
"""
        案例二百五十四 带标志位的枚举

"""
print(f'{"案例二百五十四 带标志位的枚举" :^30s}' + "\n")
from enum import IntFlag
class MyFlags(IntFlag):
        item1 = 1
        item2 = 2
        item3 = 4
        item4 = 8
        item5 = 16
        All = item1|item2|item3|item4|item5
s1 = MyFlags.item1 | MyFlags.item2
print(f' s1 : {s1}')
s2 = MyFlags.item3 | MyFlags.item4 | MyFlags.item5
print(f' s2 : {s2}')
b = MyFlags.item3 in s2
print(f' b : {b}')
print("="*36)
"""
        案例二百五十五 禁止使用重复的成员值

"""
print(f'{"案例二百五十五 禁止使用重复的成员值" :^30s}' + "\n")
from enum import unique
@unique
class DemoEn2(Enum):
        LABEL_A = 10
        LABEL_B = 20
        LABEL_C = 30
for m in DemoEn2:
        print(f' {m.name} : {m.value}')
print("="*36)