"""
        ------ 数学函数 ------

"""

"""
        案例一百一十六 取整函数

"""
print(f'{"案例一百一十六 取整函数" :^30s}' + "\n")
import math
from os import name
a,b,c = 16.888,5.09,-11.64
print('向上舍入:')
print(f' {a} --> {math.ceil(a)}')
print(f' {b} --> {math.ceil(b)}')
print(f' {c} --> {math.ceil(c)}')
print('向下舍入: \n')
print(f' {a} --> {math.floor(a)}')
print(f' {b} --> {math.floor(b)}')
print(f' {c} --> {math.floor(c)}')
print("="*36)

"""
        案例一百一十七 四舍六入五留双算法

"""
print(f'{"案例一百一十七 四舍六入五留双算法" :^30s}' + "\n")
x = 1.227
#尾数7 大于6 舍去位数后前进一位
print(f' {x} --> {round(x,2)}')
x = 12.3928
#尾数2 小于4 可直接舍去
print(f' {x} --> {round(x,2)}')
x = 7.015
#尾数5,5之后都是0,舍去尾数后,前一位为1是奇数,结果实际为7.02,二进制与浮点数误差输出为7.01
print(f' {x} --> {round(x,2)}')
x = 24.865009
#尾数5，5之后出现有效数字,
print(f' {x} --> {round(x,2)}') 
print("="*36)

"""
        案例一百一十八 求绝对值

"""
print(f'{"案例一百一十八 求绝对值" :^30s}' + "\n")
x1 = -3.33
a1 = abs(x1)
x2 = 76.36
a2 = abs(x2)
print(f' {x1} --> {a1}')
print(f' {x2} --> {a2}')

x3 = 9.006
a3 = math.fabs(x3)
x4 = -14.105
a4 = math.fabs(x4)
print(f' {x3} --> {a3}')
print(f' {x4} --> {a4}')

import decimal
ctx = decimal.Context(prec=5)
x5 = ctx.create_decimal(-26.2617)
a5 = ctx.abs(x5)
x6 = ctx.create_decimal(0.123456789)
a6 = ctx.abs(x6)
print(f' {x5} --> {a5}')
print(f' {x6} --> {a6}')
print("="*36)

"""
        案例一百一十九 最大值与最小值

"""
print(f'{"案例一百一十九 最大值与最小值" :^30s}' + "\n")
print(f'最小值: {min([78,76,9,888])}')
print(f'最大值: {max([72,999,8888,23])}')
print("="*36)

"""
        案例一百二十 排序函数---sorted

"""
print(f'{"案例一百二十 排序函数---sorted" :^30s}' + "\n")
org = ['时','升','非','张','余']
r1 = sorted(org)
r2 = sorted(org, reverse=True)
print(f' 原列表: {org}\n')
print(f' 排序后: {r1}\n')
print(f' 排序后反转后: {r2}\n')
print("="*36)

"""
        案例一百二十一 按字符串长度排序

"""
print(f'{"案例一百二十一 按字符串长度排序" :^30s}' + "\n")
src_list = ['abc','cake','xy','rw13de23ed','x']
result = sorted(src_list,key=len)
print(f'原序列: {src_list}\n')
print(f'按字符串长度排序后: {result}\n')
print("="*36)

"""
        案例一百二十二 依据员工的年龄排序

"""
print(f'{"案例一百二十二 依据员工的年龄排序" :^30s}' + "\n")
class Employee:
        name : str
        age : int
        # 构造函数
        def __init__(self,name ='',age = 0) -> None:
            self.name = name
            self.age = age
        # 自定义输出文本
        def __repr__(self) -> str:
            return f' name: {self.name}, age: {self.age}'
        # 自定义 大于 比较运算
        def __gt__(self,other):
                return self.age > other.age
e1 = Employee(name = '小王', age = 38)
e2 = Employee(name = '小红', age = 29)
e3 = Employee(name = '小张', age = 20)
e4 = Employee(name = '小刘', age = 32)

e_list = [e1,e2,e3,e4]

result = sorted(e_list)
print('排序前:')
for x in e_list:
        print(x)
print('\n排序后:')
for x in result:
        print(x)
print("="*36)

"""
        案例一百二十三 以自然常数为底的指数运算

"""
print(f'{"案例一百二十三 以自然常数为底的指数运算" :^30s}' + "\n")
r1 = math.exp(0)
print(f' e的0次方: {r1}')
r2 = math.exp(-1.5)
print(f' e的-1.5次方: {r2}')
r3 = math.exp(100)
print(f' e的100次方: {r3}')
r4 = math.exp(0.5)
print(f' e的0.5次方: {r4}')
r5 = math.exp(math.pi)
print(f' e的π次方: {r5}')
print("="*36)

"""
        案例一百二十四 求以10为底数的对数

"""
print(f'{"案例一百二十四 求以10为底数的对数" :^30s}' + "\n")
a = math.log10(100)
b = math.log10(100000)
c = math.log10(7000)
d = math.log10(15.5)
e = math.log10(8.3)
print(f'log10 100 -- > {a}')
print(f'log10 100000 -- > {b}')
print(f'log10 7000 -- > {c}')
print(f'log10 15.5 -- > {d}')
print(f'log10 8.3 -- > {e}')
print("="*36)

"""
        案例一百二十五 获取浮点数的分数与整数部分

"""
print(f'{"案例一百二十五 获取浮点数的分数与整数部分" :^30s}' + "\n")
numbers = [12.035,-9.00021,4.25,68,21.902]
for n in numbers:
        f,i = math.modf(n)
        print(f' {n} 拆分后\n 分数: {f:.8f}\n 整数: {i}\n')
print("="*36)

"""
        案例一百二十六 计算最大公约数

"""
print(f'{"案例一百二十六 计算最大公约数" :^30s}' + "\n")
def gcdMethod(a,b):
        if(isinstance(a,int))and(isinstance(b,int)):
                print(f' {a}与{b}的最大公约数: {math.gcd(a,b)}')       
        else:
                a0 = isinstance(a,int)
                a1 = isinstance(b,int)
                if a0 == False:
                        print(f' a: {a} 不是整数')
                if a1 == False:
                        print(f' b: {b} 不是整数')
gcdMethod(15,150)
gcdMethod(72,60)
gcdMethod(135,250)
gcdMethod(45.6,59)
gcdMethod(990.6,878.89)
print("="*36)

"""
        案例一百二十七 阶乘运算

"""
print(f'{"案例一百二十七 阶乘运算" :^30s}' + "\n")
nums = [6,4,9,16,10]
for n in nums:
        r = math.factorial(n)
        print(' {0} != {1}'.format(n,r))
print("="*36)