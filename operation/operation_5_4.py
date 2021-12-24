"""
        案例一百一十六 取整函数

"""
print(f'{"案例一百一十六 取整函数" :^30s}' + "\n")
import math
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